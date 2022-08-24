# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_post_api_projects_clustering.py
* Description:  Unittests for `app` module on the `POST /api/projects/{project_id}/clustering` route.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

import pytest

from tests.dummies_utils import create_dummy_projects

# ==============================================================================
# test_ko_not_found
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found(async_client):
    """
    Test the `POST /api/projects/{project_id}/clustering` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `POST /api/projects/{project_id}/clustering` works.
    response_post = await async_client.post(url="/api/projects/UNKNOWN_PROJECT/clustering")
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
    Test the `POST /api/projects/{project_id}/clustering` route with bad state.

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

    # Assert route `POST /api/projects/{project_id}/clustering` works.
    response_post = await async_client.post(url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/clustering")
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '0a_INITIALIZATION_WITHOUT_MODELIZATION' doesn't allow the preparation of constrained clustering task during this state (state='INITIALIZATION_WITHOUT_MODELIZATION')."
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
    Test the `POST /api/projects/{project_id}/clustering` route with bad state.

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

    # Assert route `POST /api/projects/{project_id}/clustering` works.
    response_post = await async_client.post(url="/api/projects/1b_SAMPLING_PENDING/clustering")
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '1b_SAMPLING_PENDING' doesn't allow the preparation of constrained clustering task during this state (state='SAMPLING_PENDING')."
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
    Test the `POST /api/projects/{project_id}/clustering` route with bad state.

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

    # Assert route `POST /api/projects/{project_id}/clustering` works.
    response_post = await async_client.post(url="/api/projects/1o_CLUSTERING_WORKING/clustering")
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '1o_CLUSTERING_WORKING' doesn't allow the preparation of constrained clustering task during this state (state='CLUSTERING_WORKING')."
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/1o_CLUSTERING_WORKING/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "CLUSTERING_WORKING"


# ==============================================================================
# test_ok_1_200
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_1_200(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/clustering` route with good state.

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
            "0d_CLUSTERING_TODO",
        ],
    )

    # Assert route `POST /api/projects/{project_id}/clustering` works.
    response_post = await async_client.post(url="/api/projects/0d_CLUSTERING_TODO/clustering")
    assert response_post.status_code == 202
    assert response_post.json() == {
        "project_id": "0d_CLUSTERING_TODO",
        "detail": "In project with id '0d_CLUSTERING_TODO', the constrained clustering task has been requested and is waiting for a background task.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is update.
    response_get = await async_client.get(url="/api/projects/0d_CLUSTERING_TODO/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 0
    assert response_get.json()["status"]["state"] in {"CLUSTERING_PENDING", "CLUSTERING_WORKING", "ITERATION_END"}
    if response_get.json()["status"]["state"] in {"CLUSTERING_PENDING", "CLUSTERING_WORKING"}:  # pragma: nocover
        assert response_get.json()["status"]["task"] is not None
    else:  # pragma: nocover
        assert response_get.json()["status"]["task"] is None


# ==============================================================================
# test_ok_2_200
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_2_200(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/clustering` route with good state.

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
            "1m_CLUSTERING_TODO",
        ],
    )

    # Assert route `POST /api/projects/{project_id}/clustering` works.
    response_post = await async_client.post(url="/api/projects/1m_CLUSTERING_TODO/clustering")
    assert response_post.status_code == 202
    assert response_post.json() == {
        "project_id": "1m_CLUSTERING_TODO",
        "detail": "In project with id '1m_CLUSTERING_TODO', the constrained clustering task has been requested and is waiting for a background task.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is update.
    response_get = await async_client.get(url="/api/projects/1m_CLUSTERING_TODO/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] in {"CLUSTERING_PENDING", "CLUSTERING_WORKING", "ITERATION_END"}
    if response_get.json()["status"]["state"] in {"CLUSTERING_PENDING", "CLUSTERING_WORKING"}:  # pragma: nocover
        assert response_get.json()["status"]["task"] is not None
    else:  # pragma: nocover
        assert response_get.json()["status"]["task"] is None
