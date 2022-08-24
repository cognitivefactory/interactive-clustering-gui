# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_api_projects_modelization.py
* Description:  Unittests for `app` module on the `GET /api/projects/{project_id}/modelization` route.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import json

import pytest

from tests.dummies_utils import create_dummy_projects

# ==============================================================================
# test_ko_not_found
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found(async_client):
    """
    Test the `GET /api/projects/{project_id}/modelization` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /api/projects/{project_id}/modelization` works.
    response_get = await async_client.get(url="/api/projects/UNKNOWN_PROJECT/modelization")
    assert response_get.status_code == 404
    assert response_get.json() == {
        "detail": "The project with id 'UNKNOWN_PROJECT' doesn't exist.",
    }


# ==============================================================================
# test_ok_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_1(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/modelization` route with some projects.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
        tmp_path: The temporary path given for this test, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "0a_INITIALIZATION_WITHOUT_MODELIZATION",
        ],
    )

    # Assert route `GET /api/projects/{project_id}/modelization` works.
    response_get = await async_client.get(url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/modelization")
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "modelization"]
    assert response_get.json() == {
        "project_id": "0a_INITIALIZATION_WITHOUT_MODELIZATION",
        "modelization": {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        },
    }

    # Assert file content is the same.
    with open(
        tmp_path / "0a_INITIALIZATION_WITHOUT_MODELIZATION" / "modelization.json", "r"
    ) as modelization_fileobject:
        assert response_get.json()["modelization"] == json.load(modelization_fileobject)


# ==============================================================================
# test_ok_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_2(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/modelization` route with some projects.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
        tmp_path: The temporary path given for this test, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        ],
    )

    # Assert route `GET /api/projects/{project_id}/modelization` works.
    response_get = await async_client.get(url="/api/projects/1l_ANNOTATION_WITH_UPTODATE_MODELIZATION/modelization")
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "modelization"]
    assert response_get.json() == {
        "project_id": "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "modelization": {
            "0": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "1": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "2": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "3": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "4": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 1},
            "6": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "7": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "8": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "9": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "10": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "11": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "12": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": ["16"], "COMPONENT": 3},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": ["16"], "COMPONENT": 4},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": ["15", "13"], "COMPONENT": 5},
            "17": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 6,
            },
            "18": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 6,
            },
            "19": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 6,
            },
            "20": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 6,
            },
            "21": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 6,
            },
            "22": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 6,
            },
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 7},
        },
    }

    # Assert file content is the same.
    with open(
        tmp_path / "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION" / "modelization.json", "r"
    ) as modelization_fileobject:
        assert response_get.json()["modelization"] == json.load(modelization_fileobject)
