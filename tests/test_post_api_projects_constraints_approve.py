# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_post_api_projects_constraints_approve.py
* Description:  Unittests for `app` module on the `POST /api/projects/{project_id}/constraints/approve` route.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import pytest

from tests.dummies_utils import create_dummy_projects

# ==============================================================================
# test_ko_not_found
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found(async_client):
    """
    Test the `POST /api/projects/{project_id}/constraints/approve` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `POST /api/projects/{project_id}/constraints/approve` works.
    response_post = await async_client.post(url="/api/projects/UNKNOWN_PROJECT/constraints/approve")
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
    Test the `POST /api/projects/{project_id}/constraints/approve` route with bad state.

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

    # Assert route `POST /api/projects/{project_id}/constraints/approve` works.
    response_post = await async_client.post(
        url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/constraints/approve"
    )
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '0a_INITIALIZATION_WITHOUT_MODELIZATION' doesn't allow constraints approbation during this state (state='INITIALIZATION_WITHOUT_MODELIZATION').",
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
    Test the `POST /api/projects/{project_id}/constraints/approve` route with bad state.

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

    # Assert route `POST /api/projects/{project_id}/constraints/approve` works.
    response_post = await async_client.post(url="/api/projects/1b_SAMPLING_PENDING/constraints/approve")
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '1b_SAMPLING_PENDING' doesn't allow constraints approbation during this state (state='SAMPLING_PENDING').",
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
    Test the `POST /api/projects/{project_id}/constraints/approve` route with bad state.

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

    # Assert route `POST /api/projects/{project_id}/constraints/approve` works.
    response_post = await async_client.post(url="/api/projects/1o_CLUSTERING_WORKING/constraints/approve")
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '1o_CLUSTERING_WORKING' doesn't allow constraints approbation during this state (state='CLUSTERING_WORKING').",
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/1o_CLUSTERING_WORKING/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "CLUSTERING_WORKING"


# ==============================================================================
# test_ko_bad_state_4
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_state_4(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/constraints/approve` route with bad state.

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
            "1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
        ],
    )

    # Assert route `POST /api/projects/{project_id}/constraints/approve` works.
    response_post = await async_client.post(
        url="/api/projects/1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/constraints/approve"
    )
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS' doesn't allow constraints approbation during this state (state='ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS').",
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(
        url="/api/projects/1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/status"
    )
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS"


# ==============================================================================
# test_ok_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_1(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/constraints/approve` route with good state.

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
            "1d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        ],
    )

    # Assert route `POST /api/projects/{project_id}/constraints/approve` works.
    response_post = await async_client.post(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/constraints/approve"
    )
    assert response_post.status_code == 201
    assert response_post.json() == {
        "project_id": "1d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "detail": "In project with id '1d_ANNOTATION_WITH_UPTODATE_MODELIZATION', the constraints have been approved.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "CLUSTERING_TODO"


# ==============================================================================
# test_ok_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_2(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/constraints/approve` route with good state.

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

    # Assert route `POST /api/projects/{project_id}/constraints/approve` works.
    response_post = await async_client.post(
        url="/api/projects/1l_ANNOTATION_WITH_UPTODATE_MODELIZATION/constraints/approve"
    )
    assert response_post.status_code == 201
    assert response_post.json() == {
        "project_id": "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "detail": "In project with id '1l_ANNOTATION_WITH_UPTODATE_MODELIZATION', the constraints have been approved.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/1l_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "CLUSTERING_TODO"
