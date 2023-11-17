# -*- coding: utf-8 -*-

"""
* Name:         cognitivefactory.interactive_clustering_gui.models.states
* Description:  Definition of states models required for application runs.
* Author:       Erwan Schild
* Created:      25/04/2022
* Licence:      CeCILL-C License v1.0 (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import enum
from typing import Any, Dict

# ==============================================================================
# ENUMERATION OF IC GUI STATES
# ==============================================================================


class ICGUIStates(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available States for Interactive Clustering GUI."""

    ###
    ### Case of project initialization.
    ###

    INITIALIZATION_WITHOUT_MODELIZATION: str = "INITIALIZATION_WITHOUT_MODELIZATION"
    INITIALIZATION_WITH_PENDING_MODELIZATION: str = "INITIALIZATION_WITH_PENDING_MODELIZATION"
    INITIALIZATION_WITH_WORKING_MODELIZATION: str = "INITIALIZATION_WITH_WORKING_MODELIZATION"
    INITIALIZATION_WITH_ERRORS: str = "INITIALIZATION_WITH_ERRORS"

    ###
    ### Case of constraints sampling.
    ###

    # Sampling tasks.
    SAMPLING_TODO: str = "SAMPLING_TODO"
    SAMPLING_PENDING: str = "SAMPLING_PENDING"
    SAMPLING_WORKING: str = "SAMPLING_WORKING"
    # Import on sampling step.
    IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION: str = "IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION"
    IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION: str = "IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION"
    IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION: str = "IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION"
    IMPORT_AT_SAMPLING_STEP_WITH_ERRORS: str = "IMPORT_AT_SAMPLING_STEP_WITH_ERRORS"

    ###
    ### Case of constraints annotation.
    ###

    # Modelization up to date.
    ANNOTATION_WITH_UPTODATE_MODELIZATION: str = "ANNOTATION_WITH_UPTODATE_MODELIZATION"
    # Modelization outdated, without conflicts.
    ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS: str = (
        "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS"
    )
    ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS: str = (
        "ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS"
    )
    ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS: str = (
        "ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS"
    )
    # Modelization outdated, with conflicts.
    ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS: str = "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS"
    ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS: str = "ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS"
    ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS: str = "ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS"
    # Import on annotation step.
    IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION: str = "IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION"
    IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION: str = "IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION"
    IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION: str = "IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION"
    IMPORT_AT_ANNOTATION_STEP_WITH_ERRORS: str = "IMPORT_AT_ANNOTATION_STEP_WITH_ERRORS"

    ###
    ### Case of constrained clustering.
    ###

    # Clustering tasks.
    CLUSTERING_TODO: str = "CLUSTERING_TODO"
    CLUSTERING_PENDING: str = "CLUSTERING_PENDING"
    CLUSTERING_WORKING: str = "CLUSTERING_WORKING"
    # Import on clustering step.
    IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION: str = "IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION"
    IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION: str = "IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION"
    IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION: str = "IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION"
    IMPORT_AT_CLUSTERING_STEP_WITH_ERRORS: str = "IMPORT_AT_CLUSTERING_STEP_WITH_ERRORS"

    ###
    ### Case of iteration end.
    ###

    # End of iteration.
    ITERATION_END: str = "ITERATION_END"
    # Import on iteration end.
    IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION: str = "IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION"
    IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION: str = "IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION"
    IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION: str = "IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION"
    IMPORT_AT_ITERATION_END_WITH_ERRORS: str = "IMPORT_AT_ITERATION_END_WITH_ERRORS"

    @classmethod
    def contains(cls, state: str) -> bool:
        """Test if state is in this enumeration.

        Args:
            state (str): A state.

        Returns:
            bool: `True` if the state is in the enumeration.
        """
        return state in cls._value2member_map_


# ==============================================================================
# SET ICGUI STATES DETAILS
# ==============================================================================


def get_ICGUIStates_details(
    state: ICGUIStates,
) -> Dict[str, Any]:
    """
    Get state details.

    Args:
        state (ICGUIStates): The state.

    Returns:
        Dict[str, Any]: The state details.
    """

    map_of_ICGUIStates_details: Dict[ICGUIStates, Dict[str, Any]] = {
        ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION: {
            "step": "CLUSTERING",
            "step_status": "LOCKED",
            "modelization_status": "TODO",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.INITIALIZATION_WITH_PENDING_MODELIZATION: {
            "step": "CLUSTERING",
            "step_status": "LOCKED",
            "modelization_status": "PENDING",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.INITIALIZATION_WITH_WORKING_MODELIZATION: {
            "step": "CLUSTERING",
            "step_status": "LOCKED",
            "modelization_status": "WORKING",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.INITIALIZATION_WITH_ERRORS: {
            "step": "CLUSTERING",
            "step_status": "LOCKED",
            "modelization_status": "ERROR",
            "conflict_status": "UNKNOWN",
        },
        ###
        ### Case of constraints sampling.
        ###
        # Sampling tasks.
        ICGUIStates.SAMPLING_TODO: {
            "step": "SAMPLING",
            "step_status": "TODO",
            "modelization_status": "UPTODATE",
            "conflict_status": "FALSE",
        },
        ICGUIStates.SAMPLING_PENDING: {
            "step": "SAMPLING",
            "step_status": "PENDING",
            "modelization_status": "UPTODATE",
            "conflict_status": "FALSE",
        },
        ICGUIStates.SAMPLING_WORKING: {
            "step": "SAMPLING",
            "step_status": "WORKING",
            "modelization_status": "UPTODATE",
            "conflict_status": "FALSE",
        },
        # Import on sampling step.
        ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION: {
            "step": "SAMPLING",
            "step_status": "LOCKED",
            "modelization_status": "TODO",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION: {
            "step": "SAMPLING",
            "step_status": "LOCKED",
            "modelization_status": "PENDING",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION: {
            "step": "SAMPLING",
            "step_status": "LOCKED",
            "modelization_status": "WORKING",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_ERRORS: {
            "step": "SAMPLING",
            "step_status": "LOCKED",
            "modelization_status": "ERROR",
            "conflict_status": "UNKNOWN",
        },
        ###
        ### Case of constraints annotation.
        ###
        # Modelization up to date.
        ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION: {
            "step": "ANNOTATION",
            "step_status": "TODO",
            "modelization_status": "UPTODATE",
            "conflict_status": "FALSE",
        },
        # Modelization outdated, without conflicts.
        ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS: {
            "step": "ANNOTATION",
            "step_status": "TODO",
            "modelization_status": "OUTDATED",
            "conflict_status": "FALSE",
        },
        ICGUIStates.ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS: {
            "step": "ANNOTATION",
            "step_status": "LOCKED",
            "modelization_status": "PENDING",
            "conflict_status": "FALSE",
        },
        ICGUIStates.ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS: {
            "step": "ANNOTATION",
            "step_status": "LOCKED",
            "modelization_status": "WORKING",
            "conflict_status": "FALSE",
        },
        # Modelization outdated, with conflicts.
        ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS: {
            "step": "ANNOTATION",
            "step_status": "TODO",
            "modelization_status": "OUTDATED",
            "conflict_status": "TRUE",
        },
        ICGUIStates.ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS: {
            "step": "ANNOTATION",
            "step_status": "LOCKED",
            "modelization_status": "PENDING",
            "conflict_status": "TRUE",
        },
        ICGUIStates.ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS: {
            "step": "ANNOTATION",
            "step_status": "LOCKED",
            "modelization_status": "WORKING",
            "conflict_status": "TRUE",
        },
        # Import on annotation step.
        ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION: {
            "step": "ANNOTATION",
            "step_status": "LOCKED",
            "modelization_status": "TODO",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION: {
            "step": "ANNOTATION",
            "step_status": "LOCKED",
            "modelization_status": "PENDING",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION: {
            "step": "ANNOTATION",
            "step_status": "LOCKED",
            "modelization_status": "WORKING",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITH_ERRORS: {
            "step": "ANNOTATION",
            "step_status": "LOCKED",
            "modelization_status": "ERROR",
            "conflict_status": "UNKNOWN",
        },
        ###
        ### Case of constrained clustering.
        ###
        # Clustering tasks.
        ICGUIStates.CLUSTERING_TODO: {
            "step": "CLUSTERING",
            "step_status": "TODO",
            "modelization_status": "UPTODATE",
            "conflict_status": "FALSE",
        },
        ICGUIStates.CLUSTERING_PENDING: {
            "step": "CLUSTERING",
            "step_status": "PENDING",
            "modelization_status": "UPTODATE",
            "conflict_status": "FALSE",
        },
        ICGUIStates.CLUSTERING_WORKING: {
            "step": "CLUSTERING",
            "step_status": "WORKING",
            "modelization_status": "UPTODATE",
            "conflict_status": "FALSE",
        },
        # Import on clustering step.
        ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION: {
            "step": "CLUSTERING",
            "step_status": "LOCKED",
            "modelization_status": "TODO",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION: {
            "step": "CLUSTERING",
            "step_status": "LOCKED",
            "modelization_status": "PENDING",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION: {
            "step": "CLUSTERING",
            "step_status": "LOCKED",
            "modelization_status": "WORKING",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITH_ERRORS: {
            "step": "CLUSTERING",
            "step_status": "LOCKED",
            "modelization_status": "ERROR",
            "conflict_status": "UNKNOWN",
        },
        ###
        ### Case of iteration end.
        ###
        # End of iteration.
        ICGUIStates.ITERATION_END: {
            "step": "ITERATION_END",
            "step_status": "TODO",
            "modelization_status": "UPTODATE",
            "conflict_status": "FALSE",
        },
        # Import on iteration end.
        ICGUIStates.IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION: {
            "step": "ITERATION_END",
            "step_status": "LOCKED",
            "modelization_status": "TODO",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION: {
            "step": "ITERATION_END",
            "step_status": "LOCKED",
            "modelization_status": "PENDING",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION: {
            "step": "ITERATION_END",
            "step_status": "LOCKED",
            "modelization_status": "WORKING",
            "conflict_status": "UNKNOWN",
        },
        ICGUIStates.IMPORT_AT_ITERATION_END_WITH_ERRORS: {
            "step": "ITERATION_END",
            "step_status": "LOCKED",
            "modelization_status": "ERROR",
            "conflict_status": "UNKNOWN",
        },
    }

    return map_of_ICGUIStates_details[state]
