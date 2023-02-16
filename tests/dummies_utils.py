# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/dummies_utils.py
* Description:  Utils methods to create dummies projects for the pytest "app" test suite.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import os
import shutil
from pathlib import Path
from typing import List, Tuple

# ==============================================================================
# LIST OF DUMMY DATASETS
# ==============================================================================
LIST_OF_DUMMY_DATASETS: Tuple = (
    "dummy_24_err.csv",
    "dummy_24_err.xlsx",
    "dummy_24.csv",
    "dummy_24.xlsx",
)


# ==============================================================================
# LIST OF DUMMY PROJECTS
# ==============================================================================
LIST_OF_DUMMY_PROJECTS: Tuple = (
    "0a_INITIALIZATION_WITHOUT_MODELIZATION",
    "0b_INITIALIZATION_WITH_PENDING_MODELIZATION",
    "0c_INITIALIZATION_WITH_WORKING_MODELIZATION",
    "0d_CLUSTERING_TODO",
    "0e_CLUSTERING_PENDING",
    "0f_CLUSTERING_WORKING",
    "0g_ITERATION_END",
    "1a_SAMPLING_TODO",
    "1b_SAMPLING_PENDING",
    "1c_SAMPLING_WORKING",
    "1d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
    "1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS",
    "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS",
    "1g_ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS",
    "1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
    "1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
    "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS",
    "1k_ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS",
    "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION",
    "1m_CLUSTERING_TODO",
    "1n_CLUSTERING_PENDING",
    "1o_CLUSTERING_WORKING",
    "1p_ITERATION_END",
    "2a_SAMPLING_TODO",
    "2b_SAMPLING_PENDING",
    "2b2_SAMPLING_PENDING",
    "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
    "import_0y0_INITIALIZATION_WITHOUT_MODELIZATION",
    "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION",
    "import_0y2_INITIALIZATION_WITH_WORKING_MODELIZATION",
    "import_1w0_IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION",
    "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
    "import_1w2_IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION",
    "import_1x0_IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION",
    "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
    "import_1x2_IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION",
    "import_1y0_IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION",
    "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
    "import_1y2_IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION",
    "import_1z0_IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION",
    "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
    "import_1z2_IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION",
    "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION",
    "import_error_0y3_INITIALIZATION_WITH_ERRORS",
    "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
    "import_error_1w3_IMPORT_AT_SAMPLING_STEP_WITH_ERRORS",
    "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
    "import_error_1x3_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
    "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
    "import_error_1y3_IMPORT_AT_CLUSTERING_STEP_WITH_ERRORS",
    "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
    "import_error_1z3_IMPORT_AT_ITERATION_END_WITH_ERRORS",
)


# ==============================================================================
# LIST OF DUMMY EXPORTS
# ==============================================================================
LIST_OF_DUMMY_EXPORTS: Tuple = (
    "archive-0a_INITIALIZATION_WITHOUT_MODELIZATION.zip",
    "archive-1b_SAMPLING_PENDING.zip",
    "archive-1d_ANNOTATION_WITH_UPTODATE_MODELIZATION.zip",
    "archive-1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS.zip",
    "archive-1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS.zip",
    "archive-1k_ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS.zip",
    "archive-1l_ANNOTATION_WITH_UPTODATE_MODELIZATION.zip",
    "archive-1o_CLUSTERING_WORKING.zip",
    "archive-1p_ITERATION_END.zip",
    "archive-ERROR_metadata_bad_creation_timestamp.zip",
    "archive-ERROR_metadata_bad_project_name.zip",
    "archive-ERROR_metadata_missing_creation_timestamp.zip",
    "archive-ERROR_metadata_missing_project_name.zip",
    "archive-ERROR_missing_files.zip",
    "archive-ERROR_status_bad_state.zip",
    "archive-ERROR_status_missing_state.zip",
)


# ==============================================================================
# COPY DUMMY PROJECTS
# ==============================================================================
def create_dummy_projects(tmp_path: Path, list_of_dummy_project_ids: List[str]):
    """
    Create a list of dummy project (copying from "./dummies").

    Args:
        tmp_path (Path): The path to a temporary directory.
        list_of_dummy_project_ids (List[str]): A list of IDs of dummy projects to copy.
    """

    # Get path to dummy projects.
    path_to_dummy_projects: Path = Path(__file__).parent / "dummies"

    # For each request dummy project ID...
    for dummy_project_id in list_of_dummy_project_ids:
        # Copy the dummy project.
        if os.path.isdir(path_to_dummy_projects / dummy_project_id):
            shutil.copytree(
                src=(path_to_dummy_projects / dummy_project_id),
                dst=(tmp_path / dummy_project_id),
            )
        else:
            shutil.copy(
                src=(path_to_dummy_projects / dummy_project_id),
                dst=(tmp_path / dummy_project_id),
            )
