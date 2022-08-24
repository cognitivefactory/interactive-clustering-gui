# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_post_api_projects_iterations.py
* Description:  Unittests for `app` module on the `POST /api/projects/{project_id}/iterations` route.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import json
from typing import Any, Dict

import pytest

from tests.dummies_utils import create_dummy_projects

# ==============================================================================
# test_ko_not_found
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found(async_client):
    """
    Test the `POST /api/projects/{project_id}/iterations` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `POST /api/projects/{project_id}/iterations` works.
    response_post = await async_client.post(url="/api/projects/UNKNOWN_PROJECT/iterations")
    assert response_post.status_code == 404
    assert response_post.json() == {
        "detail": "The project with id 'UNKNOWN_PROJECT' doesn't exist.",
    }


# ==============================================================================
# test_ko_bad_state_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_state_1(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/iterations` route with bad state.

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

    # Assert route `POST /api/projects/{project_id}/iterations` works.
    response_post = await async_client.post(url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/iterations")
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '0a_INITIALIZATION_WITHOUT_MODELIZATION' hasn't completed its clustering step on iteration '0'.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 0
    assert response_get.json()["status"]["state"] == "INITIALIZATION_WITHOUT_MODELIZATION"


# ==============================================================================
# test_ko_bad_state_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_state_2(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/iterations` route with bad state.

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
            "1b_SAMPLING_PENDING",
        ],
    )

    # Assert route `POST /api/projects/{project_id}/iterations` works.
    response_post = await async_client.post(url="/api/projects/1b_SAMPLING_PENDING/iterations")
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '1b_SAMPLING_PENDING' hasn't completed its clustering step on iteration '1'.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/1b_SAMPLING_PENDING/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "SAMPLING_PENDING"


# ==============================================================================
# test_ko_bad_state_3
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_state_3(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/iterations` route with bad state.

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
            "1o_CLUSTERING_WORKING",
        ],
    )

    # Assert route `POST /api/projects/{project_id}/iterations` works.
    response_post = await async_client.post(url="/api/projects/1o_CLUSTERING_WORKING/iterations")
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '1o_CLUSTERING_WORKING' hasn't completed its clustering step on iteration '1'.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/1o_CLUSTERING_WORKING/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "CLUSTERING_WORKING"


# ==============================================================================
# test_ok_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_1(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/iterations` route with good state.

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
            "0g_ITERATION_END",
        ],
    )

    # Assert route `POST /api/projects/{project_id}/iterations` works.
    response_post = await async_client.post(url="/api/projects/0g_ITERATION_END/iterations")
    assert response_post.status_code == 201
    assert response_post.json() == {
        "project_id": "0g_ITERATION_END",
        "iteration_id": 1,
        "detail": "The project with id '0g_ITERATION_END' is now on iteration with id '1'.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/0g_ITERATION_END/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "SAMPLING_TODO"

    # Case of `settings.json`.
    with open(tmp_path / "0g_ITERATION_END" / "settings.json", "r") as settings_fileobject:
        project_settings: Dict[str, Any] = json.load(settings_fileobject)
        assert list(project_settings.keys()) == [
            "0",
            "1",
        ]
        assert list(project_settings["1"].keys()) == [
            "sampling",
            "preprocessing",
            "vectorization",
            "clustering",
        ]
        assert project_settings["1"]["preprocessing"] == project_settings["0"]["preprocessing"]
        assert project_settings["1"]["vectorization"] == project_settings["0"]["vectorization"]
        assert project_settings["1"]["clustering"] == project_settings["0"]["clustering"]


# ==============================================================================
# test_ok_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_2(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/iterations` route with good state.

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

    # Assert route `POST /api/projects/{project_id}/iterations` works.
    response_post = await async_client.post(url="/api/projects/1p_ITERATION_END/iterations")
    assert response_post.status_code == 201
    assert response_post.json() == {
        "project_id": "1p_ITERATION_END",
        "iteration_id": 2,
        "detail": "The project with id '1p_ITERATION_END' is now on iteration with id '2'.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/1p_ITERATION_END/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 2
    assert response_get.json()["status"]["state"] == "SAMPLING_TODO"

    # Case of `settings.json`.
    with open(tmp_path / "1p_ITERATION_END" / "settings.json", "r") as settings_fileobject:
        project_settings: Dict[str, Any] = json.load(settings_fileobject)
        assert list(project_settings.keys()) == [
            "0",
            "1",
            "2",
        ]
        assert list(project_settings["2"].keys()) == [
            "sampling",
            "preprocessing",
            "vectorization",
            "clustering",
        ]
        assert project_settings["2"] == project_settings["1"]
