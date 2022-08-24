# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_utils_models_settings.py
* Description:  Unittests for `app` states models on the `ICGUISettings.contains()` method.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

from cognitivefactory.interactive_clustering_gui.models.settings import ICGUISettings

# ==============================================================================
# test_icguisettingstasks_contains
# ==============================================================================


async def test_icguisettingstasks_contains():
    """
    Test the `ICGUISettings.contains()` method.
    """
    assert ICGUISettings.contains("preprocessing") is True
    assert ICGUISettings.contains("vectorization") is True
    assert ICGUISettings.contains("sampling") is True
    assert ICGUISettings.contains("clustering") is True
    assert ICGUISettings.contains("UNKNOWN") is False
