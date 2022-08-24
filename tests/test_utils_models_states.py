# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_utils_models_states.py
* Description:  Unittests for `app` states models on the `ICGUIStates.contains()` method.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

from cognitivefactory.interactive_clustering_gui.models.states import ICGUIStates

# ==============================================================================
# test_icguitasks_contains
# ==============================================================================


async def test_icguistates_contains():
    """
    Test the `ICGUIStates.contains()` method.
    """
    assert ICGUIStates.contains("INITIALIZATION_WITHOUT_MODELIZATION") is True
    assert ICGUIStates.contains("SAMPLING_TODO") is True
    assert ICGUIStates.contains("CLUSTERING_PENDING") is True
    assert ICGUIStates.contains("IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION") is True
    assert ICGUIStates.contains("UNKNOWN") is False
