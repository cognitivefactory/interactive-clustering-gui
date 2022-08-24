# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_app.py
* Description:  Unittests for `app` module.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

# None


# ==============================================================================
# test_is_importable
# ==============================================================================
def test_is_importable():
    """
    Test that the `app` module is importable.
    """
    from cognitivefactory.interactive_clustering_gui import app  # noqa: C0415 (not top level import, it's fine)

    assert app
