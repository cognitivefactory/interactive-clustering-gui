# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_api_projects_status.py
* Description:  Unittests for `app` module on the `GET /api/projects/{project_id}/status` route.
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
    Test the `GET /api/projects/{project_id}/status` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /api/projects/{project_id}/status` works.
    response_get = await async_client.get(url="/api/projects/UNKNOWN_PROJECT/status")
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
    Test the `GET /api/projects/{project_id}/status` route.

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

    # Assert route `GET /api/projects/{project_id}/status` works.
    response_get = await async_client.get(url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/status")
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "status"]
    assert response_get.json() == {
        "project_id": "0a_INITIALIZATION_WITHOUT_MODELIZATION",
        "status": {
            "iteration_id": 0,
            "state": "INITIALIZATION_WITHOUT_MODELIZATION",
            "task": None,
            "state_details": {
                "step": "CLUSTERING",
                "step_status": "LOCKED",
                "modelization_status": "TODO",
                "conflict_status": "UNKNOWN",
            },
        },
    }

    # Assert file content is the same.
    with open(tmp_path / "0a_INITIALIZATION_WITHOUT_MODELIZATION" / "status.json", "r") as status_fileobject:
        project_status = json.load(status_fileobject)
        assert response_get.json()["status"]["iteration_id"] == project_status["iteration_id"]
        assert response_get.json()["status"]["state"] == project_status["state"]
        assert response_get.json()["status"]["task"] == project_status["task"]


# ==============================================================================
# test_ok_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_2(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/status` route.

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

    # Assert route `GET /api/projects/{project_id}/status` works.
    response_get = await async_client.get(url="/api/projects/1b_SAMPLING_PENDING/status")
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "status"]
    assert response_get.json() == {
        "project_id": "1b_SAMPLING_PENDING",
        "status": {
            "iteration_id": 1,
            "state": "SAMPLING_PENDING",
            "task": {
                "progression": 1,
                "detail": "Waiting for background task allocation...",
            },
            "state_details": {
                "step": "SAMPLING",
                "step_status": "PENDING",
                "modelization_status": "UPTODATE",
                "conflict_status": "FALSE",
            },
        },
    }

    # Assert file content is the same.
    with open(tmp_path / "1b_SAMPLING_PENDING" / "status.json", "r") as status_fileobject:
        project_status = json.load(status_fileobject)
        assert response_get.json()["status"]["iteration_id"] == project_status["iteration_id"]
        assert response_get.json()["status"]["state"] == project_status["state"]
        assert response_get.json()["status"]["task"] == project_status["task"]
