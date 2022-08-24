# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_run_constraints_sampling_task.py
* Description:  Unittests for the `run_constraints_sampling_task` background task.
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
    Test the `constraints sampling` task with project not existing.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
    """

    # Run the task.
    fake_backgroundtasks.run_constraints_sampling_task(project_id="UNKNOWN_PROJECT")


# ==============================================================================
# test_ko_bad_state
# ==============================================================================


def test_ko_bad_state(fake_backgroundtasks, tmp_path):
    """
    Test the `constraints sampling` task with bad state.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "1a_SAMPLING_TODO",
        ],
    )

    # Check sampling file content.
    with open(tmp_path / "1a_SAMPLING_TODO" / "sampling.json", "r") as sampling_before_fileobject:
        assert json.load(sampling_before_fileobject) == {}  # noqa: WPS520

    # Run the task.
    fake_backgroundtasks.run_constraints_sampling_task(project_id="1a_SAMPLING_TODO")

    # Assert status is still the same.
    with open(tmp_path / "1a_SAMPLING_TODO" / "status.json", "r") as status_after_fileobject:
        assert json.load(status_after_fileobject) == {"iteration_id": 1, "state": "SAMPLING_TODO", "task": None}

    # Assert sampling file content is still the same.
    with open(tmp_path / "1a_SAMPLING_TODO" / "sampling.json", "r") as sampling_after_fileobject:
        assert json.load(sampling_after_fileobject) == {}  # noqa: WPS520


# ==============================================================================
# test_ok_1
# ==============================================================================


def test_ok_1(fake_backgroundtasks, tmp_path):
    """
    Test the `constraints sampling` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "1b_SAMPLING_PENDING",
        ],
    )

    # Check sampling file content.
    with open(tmp_path / "1b_SAMPLING_PENDING" / "sampling.json", "r") as sampling_before_fileobject:
        assert json.load(sampling_before_fileobject) == {}  # noqa: WPS520

    # Run the task.
    fake_backgroundtasks.run_constraints_sampling_task(project_id="1b_SAMPLING_PENDING")

    # Assert status is updated.
    with open(tmp_path / "1b_SAMPLING_PENDING" / "status.json", "r") as status_after_fileobject:
        assert json.load(status_after_fileobject) == {
            "iteration_id": 1,
            "state": "ANNOTATION_WITH_UPTODATE_MODELIZATION",
            "task": None,
        }

    # Assert sampling file content is updated.
    with open(tmp_path / "1b_SAMPLING_PENDING" / "sampling.json", "r") as sampling_after_fileobject:
        sampling_results = json.load(sampling_after_fileobject)
        assert sampling_results == {
            "1": [
                "(0,4)",
                "(12,9)",
                "(10,9)",
                "(1,2)",
                "(14,9)",
                "(22,6)",
                "(20,22)",
                "(1,3)",
                "(4,7)",
                "(21,22)",
                "(11,12)",
                "(10,11)",
                "(1,6)",
                "(2,4)",
                "(8,9)",
                "(17,22)",
                "(19,22)",
                "(1,7)",
                "(22,8)",
                "(18,22)",
                "(11,14)",
                "(15,16)",
                "(13,16)",
                "(4,6)",
                "(18,8)",
            ]
        }

    # Assert constraints file content is updated.
    with open(tmp_path / "1b_SAMPLING_PENDING" / "constraints.json", "r") as constraints_after_fileobject:
        constraints_results = json.load(constraints_after_fileobject)
        assert sorted(constraints_results.keys()) == sorted(sampling_results["1"])


# ==============================================================================
# test_ok_2
# ==============================================================================


def test_ok_2(fake_backgroundtasks, tmp_path):
    """
    Test the `constraints sampling` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "2b_SAMPLING_PENDING",
        ],
    )

    # Check sampling file content.

    # Assert sampling file content is updated.
    with open(tmp_path / "2b_SAMPLING_PENDING" / "sampling.json", "r") as sampling_before_fileobject:
        sampling_results_before = json.load(sampling_before_fileobject)
        assert sampling_results_before == {
            "1": [
                "(0,4)",
                "(12,9)",
                "(10,9)",
                "(1,2)",
                "(14,9)",
                "(22,6)",
                "(20,22)",
                "(1,3)",
                "(4,7)",
                "(21,22)",
                "(11,12)",
                "(10,11)",
                "(1,6)",
                "(2,4)",
                "(8,9)",
                "(17,22)",
                "(19,22)",
                "(1,7)",
                "(22,8)",
                "(18,22)",
                "(11,14)",
                "(15,16)",
                "(13,16)",
                "(4,6)",
                "(18,8)",
            ]
        }

    # Assert constraints file content is updated.
    with open(tmp_path / "2b_SAMPLING_PENDING" / "constraints.json", "r") as constraints_before_fileobject:
        constraints_results_before = json.load(constraints_before_fileobject)
        assert sorted(constraints_results_before.keys()) == sorted(sampling_results_before["1"])

    # Run the task.
    fake_backgroundtasks.run_constraints_sampling_task(project_id="2b_SAMPLING_PENDING")

    # Assert status is updated.
    with open(tmp_path / "2b_SAMPLING_PENDING" / "status.json", "r") as status_after_fileobject:
        assert json.load(status_after_fileobject) == {
            "iteration_id": 2,
            "state": "ANNOTATION_WITH_UPTODATE_MODELIZATION",
            "task": None,
        }

    # Assert sampling file content is updated.
    with open(tmp_path / "2b_SAMPLING_PENDING" / "sampling.json", "r") as sampling_after_fileobject:
        sampling_results_after = json.load(sampling_after_fileobject)
        assert sampling_results_after == {
            "1": [
                "(0,4)",
                "(12,9)",
                "(10,9)",
                "(1,2)",
                "(14,9)",
                "(22,6)",
                "(20,22)",
                "(1,3)",
                "(4,7)",
                "(21,22)",
                "(11,12)",
                "(10,11)",
                "(1,6)",
                "(2,4)",
                "(8,9)",
                "(17,22)",
                "(19,22)",
                "(1,7)",
                "(22,8)",
                "(18,22)",
                "(11,14)",
                "(15,16)",
                "(13,16)",
                "(4,6)",
                "(18,8)",
            ],
            "2": [
                "(13,15)",
                "(17,23)",
                "(12,13)",
                "(10,15)",
                "(21,23)",
                "(11,5)",
                "(1,5)",
                "(15,8)",
                "(19,23)",
                "(12,15)",
                "(4,5)",
                "(10,13)",
                "(5,9)",
                "(10,3)",
                "(15,9)",
                "(13,9)",
                "(11,4)",
                "(10,4)",
                "(13,8)",
                "(15,6)",
                "(13,6)",
                "(11,3)",
                "(11,15)",
                "(11,13)",
                "(12,3)",
                "(3,9)",
                "(22,23)",
                "(1,11)",
                "(11,7)",
                "(1,12)",
                "(1,9)",
                "(11,2)",
                "(1,10)",
                "(12,7)",
                "(7,9)",
                "(18,23)",
                "(10,7)",
                "(12,2)",
                "(20,23)",
                "(2,9)",
                "(10,2)",
                "(0,11)",
                "(0,15)",
                "(1,15)",
                "(6,8)",
                "(6,9)",
                "(11,6)",
                "(12,6)",
                "(15,3)",
                "(15,7)",
                "(0,5)",
                "(0,8)",
                "(0,9)",
                "(0,10)",
                "(0,12)",
                "(0,13)",
                "(1,8)",
                "(1,13)",
                "(2,5)",
                "(2,8)",
                "(3,5)",
                "(3,8)",
                "(4,8)",
                "(4,9)",
                "(5,6)",
                "(5,7)",
                "(5,8)",
                "(7,8)",
                "(10,6)",
                "(12,4)",
                "(12,5)",
                "(13,2)",
                "(13,3)",
                "(13,4)",
                "(13,5)",
                "(13,7)",
                "(15,2)",
                "(15,4)",
                "(15,5)",
                "(10,5)",
                "(11,23)",
                "(15,19)",
                "(23,3)",
                "(17,5)",
                "(20,5)",
                "(13,17)",
                "(18,5)",
                "(13,23)",
                "(23,9)",
                "(23,5)",
                "(23,4)",
                "(15,22)",
                "(16,8)",
                "(19,5)",
                "(16,2)",
                "(1,23)",
                "(21,5)",
                "(15,18)",
                "(16,21)",
                "(22,5)",
                "(23,7)",
                "(10,16)",
                "(0,16)",
                "(13,20)",
                "(16,23)",
                "(16,3)",
                "(13,18)",
                "(16,6)",
                "(2,23)",
                "(12,16)",
                "(13,19)",
                "(23,6)",
                "(16,9)",
                "(15,20)",
                "(16,4)",
                "(13,22)",
                "(16,19)",
                "(15,17)",
                "(15,21)",
                "(16,20)",
                "(12,23)",
                "(16,18)",
                "(13,21)",
                "(23,8)",
                "(1,16)",
                "(16,5)",
                "(16,22)",
                "(11,16)",
                "(0,23)",
                "(16,7)",
                "(16,17)",
                "(10,23)",
                "(15,23)",
            ],
        }

    # Assert constraints file content is updated.
    with open(tmp_path / "2b_SAMPLING_PENDING" / "constraints.json", "r") as constraints_after_fileobject:
        constraints_results_after = json.load(constraints_after_fileobject)
        assert sorted(constraints_results_after.keys()) == sorted(
            set(sampling_results_after["1"] + sampling_results_after["2"])
        )


# ==============================================================================
# test_ok_3
# ==============================================================================


def test_ok_3(fake_backgroundtasks, tmp_path):
    """
    Test the `constraints sampling` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "2b2_SAMPLING_PENDING",
        ],
    )

    # Check sampling file content.
    with open(tmp_path / "2b2_SAMPLING_PENDING" / "sampling.json", "r") as sampling_before_fileobject:
        sampling_results_before = json.load(sampling_before_fileobject)
        assert sampling_results_before == {
            "1": [
                "(0,4)",
                "(12,9)",
                "(10,9)",
                "(1,2)",
                "(14,9)",
                "(22,6)",
                "(20,22)",
                "(1,3)",
                "(4,7)",
                "(21,22)",
                "(11,12)",
                "(10,11)",
                "(1,6)",
                "(2,4)",
                "(8,9)",
                "(17,22)",
                "(19,22)",
                "(1,7)",
                "(22,8)",
                "(18,22)",
                "(11,14)",
                "(15,16)",
                "(13,16)",
                "(4,6)",
                "(18,8)",
            ]
        }

    # Assert constraints file content is updated.
    with open(tmp_path / "2b2_SAMPLING_PENDING" / "constraints.json", "r") as constraints_before_fileobject:
        constraints_results_before = json.load(constraints_before_fileobject)
        assert sorted(constraints_results_before.keys()) == sorted(sampling_results_before["1"])

    # Run the task.
    fake_backgroundtasks.run_constraints_sampling_task(project_id="2b2_SAMPLING_PENDING")

    # Assert status is updated.
    with open(tmp_path / "2b2_SAMPLING_PENDING" / "status.json", "r") as status_after_fileobject:
        assert json.load(status_after_fileobject) == {
            "iteration_id": 2,
            "state": "ANNOTATION_WITH_UPTODATE_MODELIZATION",
            "task": None,
        }

    # Assert sampling file content is updated.
    with open(tmp_path / "2b2_SAMPLING_PENDING" / "sampling.json", "r") as sampling_after_fileobject:
        sampling_results_after = json.load(sampling_after_fileobject)
        assert sampling_results_after == {
            "1": [
                "(0,4)",
                "(12,9)",
                "(10,9)",
                "(1,2)",
                "(14,9)",
                "(22,6)",
                "(20,22)",
                "(1,3)",
                "(4,7)",
                "(21,22)",
                "(11,12)",
                "(10,11)",
                "(1,6)",
                "(2,4)",
                "(8,9)",
                "(17,22)",
                "(19,22)",
                "(1,7)",
                "(22,8)",
                "(18,22)",
                "(11,14)",
                "(15,16)",
                "(13,16)",
                "(4,6)",
                "(18,8)",
            ],
            "2": [
                "(10,14)",
                "(2,7)",
                "(11,9)",
                "(18,20)",
                "(13,15)",
                "(17,23)",
                "(10,12)",
                "(17,19)",
                "(12,14)",
                "(0,7)",
                "(16,21)",
                "(12,13)",
                "(16,6)",
                "(19,20)",
                "(17,21)",
                "(21,23)",
                "(19,3)",
                "(11,5)",
                "(16,23)",
                "(19,21)",
                "(2,3)",
                "(10,15)",
                "(0,2)",
                "(16,18)",
                "(10,8)",
                "(20,6)",
                "(1,5)",
                "(18,21)",
                "(12,8)",
                "(14,8)",
                "(20,21)",
                "(15,8)",
                "(18,19)",
                "(19,23)",
                "(3,6)",
                "(17,18)",
                "(12,15)",
                "(17,20)",
                "(4,5)",
                "(22,5)",
                "(18,6)",
                "(17,3)",
                "(10,13)",
                "(5,9)",
                "(2,6)",
                "(11,4)",
                "(11,22)",
                "(14,15)",
                "(13,14)",
                "(18,3)",
                "(21,3)",
                "(20,3)",
                "(22,9)",
                "(16,3)",
                "(13,8)",
                "(19,7)",
                "(23,3)",
                "(19,2)",
                "(16,17)",
                "(21,6)",
                "(21,7)",
                "(16,19)",
                "(16,7)",
                "(18,7)",
                "(2,21)",
                "(20,7)",
                "(16,2)",
                "(18,2)",
                "(3,7)",
                "(23,6)",
                "(2,20)",
                "(23,7)",
                "(1,11)",
                "(1,22)",
                "(2,23)",
                "(16,20)",
                "(17,6)",
                "(17,7)",
                "(1,9)",
                "(19,6)",
                "(18,23)",
                "(17,2)",
                "(6,7)",
                "(20,23)",
                "(0,19)",
                "(1,4)",
                "(22,4)",
                "(0,3)",
                "(0,6)",
                "(0,16)",
                "(0,17)",
                "(0,18)",
                "(0,20)",
                "(0,21)",
                "(0,23)",
                "(4,9)",
                "(3,5)",
                "(0,13)",
                "(13,5)",
                "(12,9)",
                "(11,20)",
                "(1,23)",
                "(2,5)",
                "(11,17)",
                "(12,3)",
                "(21,9)",
                "(0,14)",
                "(11,18)",
                "(13,7)",
                "(16,8)",
                "(17,5)",
                "(1,19)",
                "(11,14)",
                "(23,4)",
                "(1,18)",
                "(16,9)",
                "(1,2)",
                "(10,23)",
                "(1,3)",
                "(10,17)",
                "(13,23)",
                "(5,6)",
                "(20,22)",
                "(0,12)",
                "(15,22)",
                "(11,23)",
                "(13,2)",
                "(1,10)",
                "(10,22)",
                "(13,6)",
                "(7,9)",
                "(14,7)",
                "(14,5)",
                "(10,18)",
                "(13,16)",
                "(15,16)",
                "(14,21)",
                "(7,8)",
                "(18,9)",
                "(14,9)",
                "(10,19)",
                "(1,20)",
                "(10,20)",
                "(10,16)",
                "(14,23)",
                "(5,7)",
                "(15,9)",
                "(15,4)",
                "(14,17)",
                "(14,2)",
                "(12,23)",
                "(12,2)",
                "(17,4)",
                "(5,8)",
                "(15,6)",
                "(3,4)",
                "(15,5)",
                "(0,15)",
                "(0,9)",
                "(10,5)",
                "(11,6)",
                "(22,8)",
                "(2,22)",
                "(14,19)",
                "(21,22)",
                "(18,22)",
                "(1,15)",
                "(19,4)",
                "(1,14)",
                "(4,6)",
                "(14,6)",
                "(13,18)",
                "(11,15)",
                "(13,22)",
                "(14,22)",
                "(15,7)",
                "(18,4)",
                "(12,17)",
                "(23,8)",
                "(1,7)",
                "(20,5)",
                "(20,8)",
                "(14,20)",
                "(11,2)",
                "(15,18)",
                "(4,7)",
                "(1,8)",
                "(20,9)",
                "(21,4)",
                "(15,3)",
                "(0,1)",
                "(12,6)",
                "(13,20)",
                "(21,8)",
                "(12,7)",
                "(1,12)",
                "(12,21)",
                "(15,23)",
                "(15,19)",
                "(17,22)",
                "(1,17)",
                "(11,13)",
                "(10,6)",
                "(11,21)",
                "(10,2)",
                "(22,6)",
                "(14,18)",
                "(15,17)",
                "(11,3)",
                "(19,5)",
                "(8,9)",
                "(15,20)",
                "(15,21)",
                "(12,20)",
                "(2,4)",
                "(18,8)",
                "(0,8)",
                "(6,8)",
                "(0,11)",
                "(10,21)",
                "(15,2)",
                "(12,18)",
                "(13,3)",
                "(13,21)",
                "(3,8)",
                "(0,22)",
                "(12,22)",
                "(14,16)",
                "(1,6)",
                "(11,12)",
                "(19,8)",
                "(2,9)",
                "(11,8)",
                "(13,17)",
                "(23,9)",
                "(22,7)",
                "(16,22)",
                "(0,5)",
                "(11,16)",
                "(1,16)",
                "(10,9)",
                "(16,4)",
                "(3,9)",
                "(0,4)",
                "(17,8)",
                "(10,4)",
                "(10,7)",
                "(13,4)",
                "(22,3)",
                "(14,4)",
                "(23,5)",
                "(1,13)",
                "(18,5)",
                "(1,21)",
                "(4,8)",
                "(19,22)",
                "(14,3)",
                "(11,7)",
                "(10,3)",
                "(6,9)",
                "(21,5)",
                "(12,16)",
                "(13,19)",
                "(12,19)",
                "(2,8)",
                "(10,11)",
                "(11,19)",
                "(13,9)",
                "(19,9)",
                "(20,4)",
                "(12,4)",
                "(0,10)",
                "(12,5)",
                "(16,5)",
                "(17,9)",
                "(22,23)",
            ],
        }

    # Assert constraints file content is updated.
    with open(tmp_path / "2b2_SAMPLING_PENDING" / "constraints.json", "r") as constraints_after_fileobject:
        constraints_results_after = json.load(constraints_after_fileobject)
        assert sorted(constraints_results_after.keys()) == sorted(
            set(sampling_results_after["1"] + sampling_results_after["2"])
        )
