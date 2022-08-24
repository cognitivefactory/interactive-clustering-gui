# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_backgroundtasks.py
* Description:  Unittests for the `backgroundtasks` module.
* Author:       Erwan Schild
* Created:      13/12/2021
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

# None


# ==============================================================================
# test_backgroundtasks_is_importable
# ==============================================================================
def test_backgroundtasks_is_importable():
    """
    Test that the `backgroundtasks` module is importable.
    """
    from cognitivefactory.interactive_clustering_gui import (  # noqa: C0415 (not top level import, it's fine)
        backgroundtasks,
    )

    assert backgroundtasks
