# -*- coding: utf-8 -*-

"""
* Name:         cognitivefactory.interactive_clustering_gui.backgroundtasks
* Description:  Definition of bakgroundtasks for interactive clustering graphical user interface.
* Author:       Erwan Schild
* Created:      22/10/2021
* Licence:      CeCILL-C License v1.0 (https://cecill.info/licences.fr.html)
"""


# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import json
import os
import pathlib
import pickle  # noqa: S403
from typing import Any, Dict, List, Optional, Tuple

from filelock import FileLock
from numpy import ndarray
from scipy.sparse import csr_matrix, vstack
from sklearn.manifold import TSNE

from cognitivefactory.interactive_clustering.clustering.abstract import AbstractConstrainedClustering
from cognitivefactory.interactive_clustering.clustering.factory import clustering_factory
from cognitivefactory.interactive_clustering.constraints.binary import BinaryConstraintsManager
from cognitivefactory.interactive_clustering.sampling.abstract import AbstractConstraintsSampling
from cognitivefactory.interactive_clustering.sampling.clusters_based import ClustersBasedConstraintsSampling
from cognitivefactory.interactive_clustering.sampling.factory import sampling_factory
from cognitivefactory.interactive_clustering.utils.preprocessing import preprocess
from cognitivefactory.interactive_clustering.utils.vectorization import vectorize
from cognitivefactory.interactive_clustering_gui.models.states import ICGUIStates

# ==============================================================================
# CONFIGURE FASTAPI APPLICATION
# ==============================================================================


# Define `DATA_DIRECTORY` (where data are stored).
DATA_DIRECTORY = pathlib.Path(os.environ.get("DATA_DIRECTORY", ".data"))
DATA_DIRECTORY.mkdir(parents=True, exist_ok=True)


# ==============================================================================
# DEFINE COMMON METHODS
# ==============================================================================


###
### Utils: Get the list of existing project IDs.
###
def get_projects() -> List[str]:
    """
    Get the list of existing project IDs.
    (A project is represented by a subfolder in `.data` folder.)

    Returns:
        List[str]: The list of existing project IDs.
    """

    # Return the list of project IDs.
    return [project_id for project_id in os.listdir(DATA_DIRECTORY) if os.path.isdir(DATA_DIRECTORY / project_id)]


###
### Utils: Update project status during task.
###
def update_project_status(
    project_id: str,
    task_progression: Optional[int],
    task_detail: Optional[str],
    state: Optional[ICGUIStates] = None,
) -> None:
    """
    Update project status during task.

    Args:
        project_id (str): The ID of the project.
        task_progression (Optional[int]): The progression of the updated task.
        task_detail (Optional[str]): The detail of the updated task.
        state (Optional[ICGUIStates], optional): The state of the application. Unchanged if `None`. Defaults to `None`.
    """

    # Load status file.
    with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject_r:
        project_status: Dict[str, Any] = json.load(status_fileobject_r)

    # Update status.
    project_status["task"] = (
        {
            "progression": task_progression,
            "detail": task_detail,
        }
        if (task_progression is not None)
        else None
    )
    project_status["state"] = project_status["state"] if (state is None) else state

    # Store status.
    with open(DATA_DIRECTORY / project_id / "status.json", "w") as status_fileobject_w:
        json.dump(
            project_status,
            status_fileobject_w,
            indent=4,
        )


# ==============================================================================
# DEFINE BACKGROUND TASKS FOR MODELIZATION UPDATE
# ==============================================================================


###
### BACKGROUND TASK: Run modelization update task.
###
def run_modelization_update_task(
    project_id: str,
) -> None:
    """
    Background task route for modelization update.
    It performs the following actions : texts propressing, texts vectorization, constraints manager update.
    Emit message to share progress, raise error and announce success.

    Args:
        project_id (str): The ID of the project.
    """

    ###
    ### Check parameters.
    ###

    # Check project id : Case of unknown.
    if project_id not in get_projects():
        return

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        ###
        ### Load needed data.
        ###

        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject_r:
            project_status: Dict[str, Any] = json.load(status_fileobject_r)

        ###
        ### Check parameters.
        ###

        # Check project status.
        working_state: Optional[ICGUIStates] = None
        if project_status["state"] == ICGUIStates.INITIALIZATION_WITH_PENDING_MODELIZATION:
            working_state = ICGUIStates.INITIALIZATION_WITH_WORKING_MODELIZATION
        elif project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION:
            working_state = ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION
        elif project_status["state"] == ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION:
            working_state = ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION
        elif project_status["state"] == ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION:
            working_state = ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION
        elif project_status["state"] == ICGUIStates.IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION:
            working_state = ICGUIStates.IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION
        elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS:
            working_state = ICGUIStates.ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS
        elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS:
            working_state = ICGUIStates.ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS
        else:
            return

        # Update status.
        update_project_status(
            project_id=project_id,
            task_progression=5,
            task_detail="Lock the project for modelization update step.",
            state=working_state,
        )

    # Get current iteration.
    iteration_id: int = project_status["iteration_id"]

    ###
    ### Settings loading.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=10,
            task_detail="Load settings.",
        )

    # Load settings file.
    with open(DATA_DIRECTORY / project_id / "settings.json", "r") as settings_fileobject:
        settings: Dict[str, Any] = json.load(settings_fileobject)

    ###
    ### Texts loading.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=15,
            task_detail="Load texts.",
        )

    # Load texts
    with open(DATA_DIRECTORY / project_id / "texts.json", "r") as texts_fileobject_r:
        texts: Dict[str, Any] = json.load(texts_fileobject_r)

    ###
    ### Texts preprocessing.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=20,
            task_detail="Preprocess texts.",
        )

    # Get all unpreprocessed texts.
    dict_of_unpreprocessed_texts: Dict[str, str] = {
        text_id_before_preprocessing: text_value_before_preprocessing["text"]
        for text_id_before_preprocessing, text_value_before_preprocessing in texts.items()
    }

    # Preprocess all texts (even if text is deleted).
    dict_of_preprocessed_texts: Dict[str, str] = preprocess(
        dict_of_texts=dict_of_unpreprocessed_texts,
        apply_stopwords_deletion=settings[str(iteration_id)]["preprocessing"]["apply_stopwords_deletion"],
        apply_parsing_filter=settings[str(iteration_id)]["preprocessing"]["apply_parsing_filter"],
        apply_lemmatization=settings[str(iteration_id)]["preprocessing"]["apply_lemmatization"],
        spacy_language_model=settings[str(iteration_id)]["preprocessing"]["spacy_language_model"],
    )

    # Update texts with preprocessed values.
    for text_id_with_preprocessing in texts.keys():
        texts[text_id_with_preprocessing]["text_preprocessed"] = dict_of_preprocessed_texts[text_id_with_preprocessing]

    # Store texts.
    with open(DATA_DIRECTORY / project_id / "texts.json", "w") as texts_fileobject_w:
        json.dump(
            texts,
            texts_fileobject_w,
            indent=4,
        )

    ###
    ### Texts vectorization.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=35,
            task_detail="Vectorize texts.",
        )

    # Get managed preprocessed texts.
    dict_of_managed_preprocessed_texts: Dict[str, str] = {
        text_id_before_vectorization: text_value_before_vectorization["text_preprocessed"]
        for text_id_before_vectorization, text_value_before_vectorization in texts.items()
        if text_value_before_vectorization["is_deleted"] is False
    }

    # Vectorize texts (only if text is not deleted).
    dict_of_managed_vectors: Dict[str, csr_matrix] = vectorize(
        dict_of_texts=dict_of_managed_preprocessed_texts,
        vectorizer_type=settings[str(iteration_id)]["vectorization"]["vectorizer_type"],
        spacy_language_model=settings[str(iteration_id)]["vectorization"]["spacy_language_model"],
    )

    # Store vectors.
    with open(DATA_DIRECTORY / project_id / "vectors.pkl", "wb") as vectors_fileobject:
        pickle.dump(
            dict_of_managed_vectors,
            vectors_fileobject,
            pickle.HIGHEST_PROTOCOL,
        )

    # Convert vectors into matrix.
    vectors_ND: csr_matrix = vstack(
        dict_of_managed_vectors[text_id_with_ND] for text_id_with_ND in dict_of_managed_vectors.keys()
    )

    ###
    ### Texts vectorization in 2D.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=50,
            task_detail="Reduce vectors to 2 dimensions.",
        )

    # Reduce vectors to 2 dimensions with TSNE.
    vectors_2D: ndarray = TSNE(
        n_components=2,
        # learning_rate="auto",  # Error on "scikit-learn==0.24.1" !
        init="random",
        random_state=settings[str(iteration_id)]["vectorization"]["random_seed"],
        perplexity=min(30.0, vectors_ND.shape[0] - 1),  # TSNE requirement.
    ).fit_transform(vectors_ND)

    # Store 2D vectors.
    with open(DATA_DIRECTORY / project_id / "vectors_2D.json", "w") as vectors_2D_fileobject:
        json.dump(
            {
                text_id_with_2D: {
                    "x": float(vectors_2D[i_2D][0]),
                    "y": float(vectors_2D[i_2D][1]),
                }
                for i_2D, text_id_with_2D in enumerate(dict_of_managed_vectors.keys())
            },
            vectors_2D_fileobject,
            indent=4,
        )

    ###
    ### Texts vectorization in 3D.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=65,
            task_detail="Reduce vectors to 3 dimensions.",
        )

    # Reduce vectors to 3 dimensions with TSNE.
    vectors_3D: ndarray = TSNE(
        n_components=3,
        # learning_rate="auto",  # Error on "scikit-learn==0.24.1" !
        init="random",
        random_state=settings[str(iteration_id)]["vectorization"]["random_seed"],
        perplexity=min(30.0, vectors_ND.shape[0] - 1),  # TSNE requirement.
    ).fit_transform(vectors_ND)

    # Store 3D vectors.
    with open(DATA_DIRECTORY / project_id / "vectors_3D.json", "w") as vectors_3D_fileobject:
        json.dump(
            {
                text_id_with_3D: {
                    "x": float(vectors_3D[i_3D][0]),
                    "y": float(vectors_3D[i_3D][1]),
                    "z": float(vectors_3D[i_3D][2]),
                }
                for i_3D, text_id_with_3D in enumerate(dict_of_managed_vectors.keys())
            },
            vectors_3D_fileobject,
            indent=4,
        )

    ###
    ### Constraints manager regeneration.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=80,
            task_detail="(Re)generate constraints manager.",
        )

    # Initialize constraints manager with managed texts IDs.
    new_constraints_manager: BinaryConstraintsManager = BinaryConstraintsManager(
        list_of_data_IDs=list(dict_of_managed_preprocessed_texts.keys())
    )

    # Load annotated constraints.
    with open(DATA_DIRECTORY / project_id / "constraints.json", "r") as constraints_fileobject_r:
        constraints: Dict[str, Any] = json.load(constraints_fileobject_r)

    # First, reset `to_fix_conflict` status of all constraints.
    for constraint_id in constraints.keys():
        constraints[constraint_id]["to_fix_conflict"] = False

    # Then, update constraints manager with "CANNOT_LINK" constraints.
    for _, constraint_CL in constraints.items():
        if constraint_CL["constraint_type"] == "CANNOT_LINK" and constraint_CL["is_hidden"] is False:
            new_constraints_manager.add_constraint(
                data_ID1=constraint_CL["data"]["id_1"],
                data_ID2=constraint_CL["data"]["id_2"],
                constraint_type="CANNOT_LINK",
            )  # No conflict can append, at this step the constraints manager handle only constraints of same type.

    # Initialize conflicts counter.
    number_of_conflicts: int = 0

    # Finaly, update constraints manager with "MUST_LINK" constraints.
    for constraint_ML_id, constraint_ML in constraints.items():
        if constraint_ML["constraint_type"] == "MUST_LINK" and constraint_ML["is_hidden"] is False:
            try:
                new_constraints_manager.add_constraint(
                    data_ID1=constraint_ML["data"]["id_1"],
                    data_ID2=constraint_ML["data"]["id_2"],
                    constraint_type="MUST_LINK",
                )  # Conflicts can append.
            except ValueError:
                # Update conflicts status.
                constraints[constraint_ML_id]["to_fix_conflict"] = True
                number_of_conflicts += 1

    # Store new constraints manager.
    with open(DATA_DIRECTORY / project_id / "constraints_manager.pkl", "wb") as constraints_manager_fileobject:
        pickle.dump(
            new_constraints_manager,
            constraints_manager_fileobject,
            pickle.HIGHEST_PROTOCOL,
        )

    # Store updated constraints in file.
    with open(DATA_DIRECTORY / project_id / "constraints.json", "w") as constraints_fileobject_w:
        json.dump(constraints, constraints_fileobject_w, indent=4)

    ###
    ### Store modelization inference.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=95,
            task_detail="Store modelization inference results.",
        )

    # Load modelization inference file.
    with open(DATA_DIRECTORY / project_id / "modelization.json", "r") as modelization_fileobject_r:
        modelization: Dict[str, Any] = json.load(modelization_fileobject_r)

    # Get constraints transitivity.
    constraints_transitivity: Dict[
        str, Dict[str, Dict[str, None]]
    ] = new_constraints_manager._constraints_transitivity  # noqa: WPS437

    # Update modelization inference.
    modelization = {}
    for text_id_in_manager in new_constraints_manager.get_list_of_managed_data_IDs():
        modelization[text_id_in_manager] = {
            "MUST_LINK": list(constraints_transitivity[text_id_in_manager]["MUST_LINK"].keys()),
            "CANNOT_LINK": list(constraints_transitivity[text_id_in_manager]["CANNOT_LINK"].keys()),
        }
    for component_id, component in enumerate(new_constraints_manager.get_connected_components()):
        for text_id_in_component in component:
            modelization[text_id_in_component]["COMPONENT"] = component_id

    # Store updated modelization inference in file.
    with open(DATA_DIRECTORY / project_id / "modelization.json", "w") as modelization_fileobject_w:
        json.dump(modelization, modelization_fileobject_w, indent=4)

    ###
    ### End of task.
    ###

    # Define the next state.
    end_state: Optional[ICGUIStates] = None
    if working_state == ICGUIStates.INITIALIZATION_WITH_WORKING_MODELIZATION:
        end_state = (
            ICGUIStates.CLUSTERING_TODO if (number_of_conflicts == 0) else ICGUIStates.INITIALIZATION_WITH_ERRORS
        )
    elif working_state == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION:
        end_state = (
            ICGUIStates.SAMPLING_TODO if (number_of_conflicts == 0) else ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_ERRORS
        )
    elif working_state == ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION:
        end_state = (
            ICGUIStates.CLUSTERING_TODO
            if (number_of_conflicts == 0)
            else ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITH_ERRORS
        )
    elif working_state == ICGUIStates.IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION:
        end_state = (
            ICGUIStates.ITERATION_END if (number_of_conflicts == 0) else ICGUIStates.IMPORT_AT_ITERATION_END_WITH_ERRORS
        )
    #### elif working_state in {
    ####     ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION,
    ####     ICGUIStates.ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS,
    ####     ICGUIStates.ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS,
    #### }:
    else:
        end_state = (
            ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION
            if (number_of_conflicts == 0)
            else ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
        )

    # Lock status file in order to update project status.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=None,
            task_detail=None,
            state=end_state,
        )


# ==============================================================================
# DEFINE BACKGROUND TASKS FOR CONSTRAINTS SAMPLING
# ==============================================================================


###
### BACKGROUND TASK: Run constraints sampling task.
###
def run_constraints_sampling_task(
    project_id: str,
) -> None:
    """
    Background task route for constraints sampling task.
    It performs the following actions : constraints sampling.

    Args:
        project_id (str): The ID of the project.
    """

    ###
    ### Check parameters.
    ###

    # Check project id : Case of unknown.
    if project_id not in get_projects():
        return

    # Lock status file in order to check project iteration and project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject_r:
            project_status: Dict[str, Any] = json.load(status_fileobject_r)

        # Check project status.
        if project_status["state"] != ICGUIStates.SAMPLING_PENDING:
            return

        # Update status.
        update_project_status(
            project_id=project_id,
            task_progression=5,
            task_detail="Lock the project for constraints sampling step.",
            state=ICGUIStates.SAMPLING_WORKING,
        )

    # Get current iteration.
    iteration_id: int = project_status["iteration_id"]

    ###
    ### Settings loading.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=10,
            task_detail="Load settings.",
        )

    # Load settings file.
    with open(DATA_DIRECTORY / project_id / "settings.json", "r") as settings_fileobject:
        settings: Dict[str, Any] = json.load(settings_fileobject)

    # Get previous iteration id.
    previous_iteration_id: int = iteration_id - 1

    ###
    ### Constraints manager loading.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=20,
            task_detail="Load constraints manager.",
        )

    # Load constraints manager.
    with open(DATA_DIRECTORY / project_id / "constraints_manager.pkl", "rb") as constraints_manager_fileobject:
        constraints_manager: BinaryConstraintsManager = pickle.load(  # noqa: S301  # Usage of Pickle
            constraints_manager_fileobject
        )

    ###
    ### Clustering results loading.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=30,
            task_detail="Load previous clustering results.",
        )

    # Get previous clustering result.
    with open(DATA_DIRECTORY / project_id / "clustering.json", "r") as clustering_fileobject:
        clustering_results_for_previous_iteration: Dict[str, int] = json.load(clustering_fileobject)[
            str(previous_iteration_id)
        ]

    ###
    ### Vectors loading.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=40,
            task_detail="Load vectors.",
        )

    # Load vectors.
    with open(DATA_DIRECTORY / project_id / "vectors.pkl", "rb") as vectors_fileobject:
        dict_of_managed_vectors: Dict[str, csr_matrix] = pickle.load(  # noqa: S301  # Usage of Pickle
            vectors_fileobject
        )

    ###
    ### Constraints sampling initialization.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=50,
            task_detail="Initialize constraints sampler.",
        )

    # Initialize constraints sampler.
    kwargs_sampling_init: Dict[str, Any] = (
        settings[str(iteration_id)]["sampling"]["init_kargs"]
        if (settings[str(iteration_id)]["sampling"]["init_kargs"] is not None)
        else {}
    )
    sampler: AbstractConstraintsSampling = (
        ClustersBasedConstraintsSampling(**kwargs_sampling_init)
        if (settings[str(iteration_id)]["sampling"]["algorithm"] == "custom")
        else sampling_factory(
            algorithm=settings[str(iteration_id)]["sampling"]["algorithm"],
            random_seed=settings[str(iteration_id)]["sampling"]["random_seed"],
            **kwargs_sampling_init,
        )
    )

    ###
    ### Constraints sampling.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=60,
            task_detail="Sample {nb} pairs of texts to annotate.".format(
                nb=str(settings[str(iteration_id)]["sampling"]["nb_to_select"])
            ),
        )

    # Sample pairs of data to annotate.
    sampling_result: List[Tuple[str, str]] = sampler.sample(
        constraints_manager=constraints_manager,
        nb_to_select=settings[str(iteration_id)]["sampling"]["nb_to_select"],
        clustering_result=clustering_results_for_previous_iteration,
        vectors=dict_of_managed_vectors,
    )

    # If needed: complete with some random pairs of data IDs.
    if len(sampling_result) < settings[str(iteration_id)]["sampling"]["nb_to_select"]:
        with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
            update_project_status(
                project_id=project_id,
                task_progression=75,
                task_detail="Need to complete with {nb} random pairs of texts.".format(
                    nb=str(settings[str(iteration_id)]["sampling"]["nb_to_select"] - len(sampling_result))
                ),
            )
        sampling_result += [
            random_sample
            for random_sample in sampling_factory(
                algorithm="random",
                random_seed=settings[str(iteration_id)]["sampling"]["random_seed"],
            ).sample(
                constraints_manager=constraints_manager,
                nb_to_select=settings[str(iteration_id)]["sampling"]["nb_to_select"] - len(sampling_result),
            )
            if random_sample not in sampling_result
        ]

    ###
    ### Sampling results storage.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=90,
            task_detail="Store sampling results and prepapre annotations.",
        )

    # Load sampling results file.
    with open(DATA_DIRECTORY / project_id / "sampling.json", "r") as sampling_fileobject_r:
        sampling_results: Dict[str, List[str]] = json.load(sampling_fileobject_r)

    # Load constraints file.
    with open(DATA_DIRECTORY / project_id / "constraints.json", "r") as constraints_fileobject_r:
        constraints: Dict[str, Dict[str, Any]] = json.load(constraints_fileobject_r)

    # Initialize sampling result for this iteration.
    sampling_results[str(iteration_id)] = []

    # For all sampling to annotate...
    for data_ID1, data_ID2 in sampling_result:
        # Define sampling id.
        constraint_id: str = "({data_ID1_str},{data_ID2_str})".format(
            data_ID1_str=data_ID1,
            data_ID2_str=data_ID2,
        )

        # Add sampling id.
        sampling_results[str(iteration_id)].append(constraint_id)

        # Update constraints if not already known.
        if constraint_id not in constraints.keys():
            constraints[constraint_id] = {
                "data": {
                    "id_1": data_ID1,
                    "id_2": data_ID2,
                },
                "constraint_type": None,
                "constraint_type_previous": [],
                "is_hidden": False,  # if text is deleted.
                "to_annotate": False,
                "to_review": False,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": None,
                "iteration_of_sampling": iteration_id,
            }
        constraints[constraint_id]["to_annotate"] = True

    # Store sampling results.
    with open(DATA_DIRECTORY / project_id / "sampling.json", "w") as sampling_fileobject_w:
        json.dump(
            sampling_results,
            sampling_fileobject_w,
            indent=4,
        )

    # Store constraints results.
    with open(DATA_DIRECTORY / project_id / "constraints.json", "w") as constraints_fileobject_w:
        json.dump(
            constraints,
            constraints_fileobject_w,
            indent=4,
        )

    ###
    ### End of task.
    ###

    # Lock status file in order to update project status.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=None,
            task_detail=None,
            state=ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION,
        )


# ==============================================================================
# DEFINE BACKGROUND TASKS FOR CONSTRAINED CLUSTERING
# ==============================================================================


###
### BACKGROUND TASK: Run constraints clustering task.
###
def run_constrained_clustering_task(
    project_id: str,
) -> None:
    """
    Background task for constraints clustering task.
    It performs the following actions : constrained clustering.

    Args:
        project_id (str): The ID of the project.
    """

    ###
    ### Check parameters.
    ###

    # Check project id : Case of unknown.
    if project_id not in get_projects():
        return

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject_r:
            project_status: Dict[str, Any] = json.load(status_fileobject_r)

        # Check project status.
        if project_status["state"] != ICGUIStates.CLUSTERING_PENDING:
            return

        # Update status.
        update_project_status(
            project_id=project_id,
            task_progression=5,
            task_detail="Lock the project for constrained clustering step.",
            state=ICGUIStates.CLUSTERING_WORKING,
        )

    # Get current iteration.
    iteration_id: int = project_status["iteration_id"]

    ###
    ### Settings loading.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=10,
            task_detail="Load settings.",
        )

    # Load settings file.
    with open(DATA_DIRECTORY / project_id / "settings.json", "r") as settings_fileobject:
        settings: Dict[str, Any] = json.load(settings_fileobject)

    ###
    ### Constraints manager loading.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=20,
            task_detail="Load constraints manager.",
        )

    # Load constraints manager.
    with open(DATA_DIRECTORY / project_id / "constraints_manager.pkl", "rb") as constraints_manager_fileobject:
        constraints_manager: BinaryConstraintsManager = pickle.load(  # noqa: S301  # Usage of Pickle
            constraints_manager_fileobject
        )

    ###
    ### Vectors loading.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=30,
            task_detail="Load vectors.",
        )

    # Load vectors.
    with open(DATA_DIRECTORY / project_id / "vectors.pkl", "rb") as vectors_fileobject:
        dict_of_managed_vectors: Dict[str, csr_matrix] = pickle.load(  # noqa: S301  # Usage of Pickle
            vectors_fileobject
        )

    ###
    ### Clustering model initialization.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=40,
            task_detail="Initialize clustering model.",
        )

    # Initialize clustering model.
    kwargs_clustering_init: Dict[str, Any] = (
        settings[str(iteration_id)]["clustering"]["init_kargs"]
        if (settings[str(iteration_id)]["clustering"]["init_kargs"] is not None)
        else {}
    )
    clustering_model: AbstractConstrainedClustering = clustering_factory(
        algorithm=settings[str(iteration_id)]["clustering"]["algorithm"],
        random_seed=settings[str(iteration_id)]["clustering"]["random_seed"],
        **kwargs_clustering_init,
    )

    ###
    ### Constrained clustering.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=50,
            task_detail="Run constrained clustering.",
        )

    # Run constrained clustering.
    clustering_result: Dict[str, int] = clustering_model.cluster(
        constraints_manager=constraints_manager,
        vectors=dict_of_managed_vectors,
        nb_clusters=settings[str(iteration_id)]["clustering"]["nb_clusters"],
    )

    ###
    ### Clustering results storage.
    ###
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=90,
            task_detail="Store clustering results.",
        )

    # Load clustering results file.
    with open(DATA_DIRECTORY / project_id / "clustering.json", "r") as clustering_fileobject_r:
        history_of_clustering_results: Dict[str, Dict[str, int]] = json.load(clustering_fileobject_r)

    # Update clustering results.
    history_of_clustering_results[str(iteration_id)] = clustering_result

    # Store clustering results.
    with open(DATA_DIRECTORY / project_id / "clustering.json", "w") as clustering_fileobject_w:
        json.dump(
            history_of_clustering_results,
            clustering_fileobject_w,
            indent=4,
        )

    ###
    ### End of task.
    ###

    # Lock status file in order to update project status.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        update_project_status(
            project_id=project_id,
            task_progression=None,
            task_detail=None,
            state=ICGUIStates.ITERATION_END,
        )
