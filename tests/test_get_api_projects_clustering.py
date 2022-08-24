# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_api_projects_clustering.py
* Description:  Unittests for `app` module on the `GET /api/projects/{project_id}/clustering/{iteration_id}` route.
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
    Test the `GET /api/projects/{project_id}/clustering` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /api/projects/{project_id}/clustering` works.
    response_get = await async_client.get(url="/api/projects/UNKNOWN_PROJECT/clustering")
    assert response_get.status_code == 404
    assert response_get.json() == {
        "detail": "The project with id 'UNKNOWN_PROJECT' doesn't exist.",
    }


# ==============================================================================
# test_ko_bad_iteration_id_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_iteration_id_1(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/clustering` route with not existing project.

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

    # Assert route `GET /api/projects/{project_id}/clustering` works.
    response_get = await async_client.get(
        url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/clustering?iteration_id=99"
    )
    assert response_get.status_code == 404
    assert response_get.json() == {
        "detail": "The project with id '0a_INITIALIZATION_WITHOUT_MODELIZATION' has no iteration with id '99'.",
    }


# ==============================================================================
# test_ko_bad_iteration_id_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_iteration_id_2(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/clustering` route with not existing project.

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

    # Assert route `GET /api/projects/{project_id}/clustering` works.
    response_get = await async_client.get(
        url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/clustering?iteration_id=0"
    )
    assert response_get.status_code == 403
    assert response_get.json() == {
        "detail": "The project with id '0a_INITIALIZATION_WITHOUT_MODELIZATION' hasn't completed its clustering step on iteration '0'.",
    }


# ==============================================================================
# test_ok_default_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_default_1(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/clustering` route with some projects.

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
            "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        ],
    )

    # Assert route `GET /api/projects/{project_id}/clustering` works.
    response_get = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/clustering")
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "iteration_id", "clustering"]
    assert response_get.json() == {
        "project_id": "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "iteration_id": 1,
        "clustering": {
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

    # Assert file content is the same.
    with open(tmp_path / "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION" / "clustering.json", "r") as clustering_fileobject:
        assert response_get.json()["clustering"] == json.load(clustering_fileobject)["1"]


# ==============================================================================
# test_ok_default_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_default_2(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/clustering` route with some projects.

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
            "1p_ITERATION_END",
        ],
    )

    # Assert route `GET /api/projects/{project_id}/clustering` works.
    response_get = await async_client.get(url="/api/projects/1p_ITERATION_END/clustering")
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "iteration_id", "clustering"]
    assert response_get.json() == {
        "project_id": "1p_ITERATION_END",
        "iteration_id": 1,
        "clustering": {
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

    # Assert file content is the same.
    with open(tmp_path / "1p_ITERATION_END" / "clustering.json", "r") as clustering_fileobject:
        assert response_get.json()["clustering"] == json.load(clustering_fileobject)["1"]


# ==============================================================================
# test_ok_with_iteration_id
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_with_iteration_id(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/clustering` route with some projects.

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
            "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        ],
    )

    # Assert route `GET /api/projects/{project_id}/clustering` works.
    response_get = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/clustering?iteration_id=0"
    )
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "iteration_id", "clustering"]
    assert response_get.json() == {
        "project_id": "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "iteration_id": 0,
        "clustering": {
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
    }

    # Assert file content is the same.
    with open(tmp_path / "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION" / "clustering.json", "r") as clustering_fileobject:
        assert response_get.json()["clustering"] == json.load(clustering_fileobject)["0"]
