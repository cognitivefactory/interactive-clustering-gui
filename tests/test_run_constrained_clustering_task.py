# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_run_constrained_clustering_task.py
* Description:  Unittests for the `run_constrained_clustering_task` backgroundtask.
* Author:       Erwan Schild
* Created:      13/12/2021
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================


import json

from tests.dummies_utils import create_dummy_projects

# ==============================================================================
# test_ko_not_found
# ==============================================================================


def test_ko_not_found(fake_backgroundtasks):
    """
    Test the `constrained clustering` task with project not existing.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
    """

    # Run the task.
    fake_backgroundtasks.run_constrained_clustering_task(
        project_id="UNKNOWN_PROJECT",
    )


# ==============================================================================
# test_ko_bad_state
# ==============================================================================


def test_ko_bad_state(fake_backgroundtasks, tmp_path):
    """
    Test the `constrained clustering` task with bad state.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "1m_CLUSTERING_TODO",
        ],
    )

    # Run the task.
    fake_backgroundtasks.run_constrained_clustering_task(
        project_id="1m_CLUSTERING_TODO",
    )

    # Check clustering file content.
    with open(tmp_path / "1m_CLUSTERING_TODO" / "clustering.json", "r") as clustering_before_fileobject:
        assert json.load(clustering_before_fileobject) == {
            "0": {
                "0": 0,
                "1": 1,
                "10": 2,
                "11": 1,
                "12": 2,
                "13": 2,
                "14": 2,
                "15": 2,
                "16": 0,
                "17": 0,
                "18": 0,
                "19": 0,
                "2": 0,
                "20": 0,
                "21": 0,
                "22": 1,
                "23": 0,
                "3": 0,
                "4": 1,
                "5": 1,
                "6": 0,
                "7": 0,
                "8": 2,
                "9": 1,
            }
        }

    # Assert status is still the same.
    with open(tmp_path / "1m_CLUSTERING_TODO" / "status.json", "r") as status_after_fileobject:
        assert json.load(status_after_fileobject) == {"iteration_id": 1, "state": "CLUSTERING_TODO", "task": None}

    # Assert clustering file content is still the same.
    with open(tmp_path / "1m_CLUSTERING_TODO" / "clustering.json", "r") as clustering_after_fileobject:
        assert json.load(clustering_after_fileobject) == {
            "0": {
                "0": 0,
                "1": 1,
                "10": 2,
                "11": 1,
                "12": 2,
                "13": 2,
                "14": 2,
                "15": 2,
                "16": 0,
                "17": 0,
                "18": 0,
                "19": 0,
                "2": 0,
                "20": 0,
                "21": 0,
                "22": 1,
                "23": 0,
                "3": 0,
                "4": 1,
                "5": 1,
                "6": 0,
                "7": 0,
                "8": 2,
                "9": 1,
            }
        }


# ==============================================================================
# test_ok
# ==============================================================================


def test_ok(fake_backgroundtasks, tmp_path):
    """
    Test the `constrained clustering` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "1n_CLUSTERING_PENDING",
        ],
    )

    # Check clustering file content.
    with open(tmp_path / "1n_CLUSTERING_PENDING" / "clustering.json", "r") as clustering_before_fileobject:
        assert json.load(clustering_before_fileobject) == {
            "0": {
                "0": 0,
                "1": 1,
                "10": 2,
                "11": 1,
                "12": 2,
                "13": 2,
                "14": 2,
                "15": 2,
                "16": 0,
                "17": 0,
                "18": 0,
                "19": 0,
                "2": 0,
                "20": 0,
                "21": 0,
                "22": 1,
                "23": 0,
                "3": 0,
                "4": 1,
                "5": 1,
                "6": 0,
                "7": 0,
                "8": 2,
                "9": 1,
            }
        }

    # Run the task.
    fake_backgroundtasks.run_constrained_clustering_task(project_id="1n_CLUSTERING_PENDING")

    # Assert status is updated.
    with open(tmp_path / "1n_CLUSTERING_PENDING" / "status.json", "r") as status_after_fileobject:
        assert json.load(status_after_fileobject) == {"iteration_id": 1, "state": "ITERATION_END", "task": None}

    # Assert clustering file content is updated.
    with open(tmp_path / "1n_CLUSTERING_PENDING" / "clustering.json", "r") as clustering_after_fileobject:
        assert json.load(clustering_after_fileobject) == {
            "0": {
                "0": 0,
                "1": 1,
                "10": 2,
                "11": 1,
                "12": 2,
                "13": 2,
                "14": 2,
                "15": 2,
                "16": 0,
                "17": 0,
                "18": 0,
                "19": 0,
                "2": 0,
                "20": 0,
                "21": 0,
                "22": 1,
                "23": 0,
                "3": 0,
                "4": 1,
                "5": 1,
                "6": 0,
                "7": 0,
                "8": 2,
                "9": 1,
            },
            "1": {
                "0": 0,
                "1": 0,
                "10": 0,
                "11": 0,
                "12": 0,
                "13": 0,
                "15": 0,
                "16": 1,
                "17": 2,
                "18": 2,
                "19": 2,
                "2": 0,
                "20": 2,
                "21": 2,
                "22": 2,
                "23": 2,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "7": 0,
                "8": 0,
                "9": 0,
            },
        }
