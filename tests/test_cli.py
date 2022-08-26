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

from cognitivefactory.interactive_clustering_gui import cli

# ==============================================================================
# test_show_help
# ==============================================================================


def test_show_help(capsys):
    """
    Test the CLI help display.

    Arguments:
        capsys: Pytest fixture to capture output.
    """
    with pytest.raises(SystemExit):
        cli.main(["-h"])
    captured = capsys.readouterr()
    assert "cognitivefactory-interactive-clustering-gui" in captured.out


# ==============================================================================
# test_launch_web_app
# ==============================================================================


def test_launch_web_app(capsys):
    """
    Test the CLI web app launch.

    Arguments:
        capsys: Pytest fixture to capture output.
    """
    with pytest.raises(SystemExit):
        cli.main([])
    captured = capsys.readouterr()
    assert "cognitivefactory-interactive-clustering-gui" in captured.out
