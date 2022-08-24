# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_put_api_projects_constraints_review.py
* Description:  Unittests for `app` module on the `PUT /api/projects/{project_id}/constraints/{constraint_id}/review` route.
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
# test_ko_not_found_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found_1(async_client):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/review` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/review` works.
    response_put = await async_client.put(url="/api/projects/UNKNOWN_PROJECT/constraints/UNKNOWN_CONSTRAINT/review")
    assert response_put.status_code == 404
    assert response_put.json() == {
        "detail": "The project with id 'UNKNOWN_PROJECT' doesn't exist.",
    }


# ==============================================================================
# test_ko_not_found_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found_2(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/review` route with not existing project.

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
            "1a_SAMPLING_TODO",
        ],
    )

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/review` works.
    response_put = await async_client.put(url="/api/projects/1a_SAMPLING_TODO/constraints/UNKNOWN_CONSTRAINT/review")
    assert response_put.status_code == 404
    assert response_put.json() == {
        "detail": "In project with id '1a_SAMPLING_TODO', the constraint with id 'UNKNOWN_CONSTRAINT' to annotate doesn't exist.",
    }


# ==============================================================================
# test_ok_good_state_default
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_good_state_default(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/review` route with good state.

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

    # Get texts before test.
    response_get_constraints_before = await async_client.get(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_before.status_code == 200
    assert response_get_constraints_before.json()["constraints"]["(0,4)"]["to_review"] is False

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/review` works.
    response_put = await async_client.put(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/constraints/(0,4)/review"
    )
    assert response_put.status_code == 202
    assert response_put.json() == {
        "project_id": "1d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "constraint_id": "(0,4)",
        "detail": "In project with id '1d_ANNOTATION_WITH_UPTODATE_MODELIZATION', the constraint with id '(0,4)' need a review.",
    }

    # Assert route `GET /api/projects/{project_id}/constraints` is updated.
    response_get_constraints_after = await async_client.get(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_after.status_code == 200
    for constraint_id in response_get_constraints_before.json()["constraints"].keys():
        if constraint_id != "(0,4)":
            assert (
                response_get_constraints_after.json()["constraints"][constraint_id]
                == response_get_constraints_before.json()["constraints"][constraint_id]
            )
    assert response_get_constraints_after.json()["constraints"]["(0,4)"]["to_review"] is True

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "ANNOTATION_WITH_UPTODATE_MODELIZATION"


# ==============================================================================
# test_ok_good_state_review
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_good_state_review(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/review` route with good state.

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

    # Get texts before test.
    response_get_constraints_before = await async_client.get(
        url="/api/projects/1m_CLUSTERING_TODO/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_before.status_code == 200
    assert response_get_constraints_before.json()["constraints"]["(0,4)"]["to_review"] is False

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/review` works.
    response_put = await async_client.put(
        url="/api/projects/1m_CLUSTERING_TODO/constraints/(0,4)/review?to_review=true"
    )
    assert response_put.status_code == 202
    assert response_put.json() == {
        "project_id": "1m_CLUSTERING_TODO",
        "constraint_id": "(0,4)",
        "detail": "In project with id '1m_CLUSTERING_TODO', the constraint with id '(0,4)' need a review.",
    }

    # Assert route `GET /api/projects/{project_id}/constraints` is updated.
    response_get_constraints_after = await async_client.get(
        url="/api/projects/1m_CLUSTERING_TODO/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_after.status_code == 200
    for constraint_id in response_get_constraints_before.json()["constraints"].keys():
        if constraint_id != "(0,4)":
            assert (
                response_get_constraints_after.json()["constraints"][constraint_id]
                == response_get_constraints_before.json()["constraints"][constraint_id]
            )
    assert response_get_constraints_after.json()["constraints"]["(0,4)"]["to_review"] is True

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/1m_CLUSTERING_TODO/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "CLUSTERING_TODO"


# ==============================================================================
# test_ok_good_state_not_review
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_good_state_not_review(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/review` route with good state.

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

    # Get texts before test.
    response_get_constraints_before = await async_client.get(
        url="/api/projects/1p_ITERATION_END/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_before.status_code == 200
    assert response_get_constraints_before.json()["constraints"]["(4,6)"]["to_review"] is True

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/review` works.
    response_put = await async_client.put(url="/api/projects/1p_ITERATION_END/constraints/(4,6)/review?to_review=false")
    assert response_put.status_code == 202
    assert response_put.json() == {
        "project_id": "1p_ITERATION_END",
        "constraint_id": "(4,6)",
        "detail": "In project with id '1p_ITERATION_END', the constraint with id '(4,6)' has been reviewed.",
    }

    # Assert route `GET /api/projects/{project_id}/constraints` is updated.
    response_get_constraints_after = await async_client.get(
        url="/api/projects/1p_ITERATION_END/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_after.status_code == 200
    for constraint_id in response_get_constraints_before.json()["constraints"].keys():
        if constraint_id != "(4,6)":
            assert (
                response_get_constraints_after.json()["constraints"][constraint_id]
                == response_get_constraints_before.json()["constraints"][constraint_id]
            )
    assert response_get_constraints_after.json()["constraints"]["(4,6)"]["to_review"] is False

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/1p_ITERATION_END/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "ITERATION_END"
