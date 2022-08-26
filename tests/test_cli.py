# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_cli.py
* Description:  Unittests for `cli` module.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import pytest

from cognitivefactory.interactive_clustering_gui.cli import main

# ==============================================================================
# test_main_help
# ==============================================================================


def test_main_help(capsys):
    """
    Test the CLI help display.

    Arguments:
        capsys: Pytest fixture to capture output.
    """

    # Request the help of the CLI.
    with pytest.raises(SystemExit):
        main(["-h"])

    # Capture the output and check it.
    captured = capsys.readouterr()
    assert "cognitivefactory-interactive-clustering-gui" in captured.out
