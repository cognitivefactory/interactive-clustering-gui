# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_put_api_projects_constraints_comment.py
* Description:  Unittests for `app` module on the `PUT /api/projects/{project_id}/constraints/{constraint_id}/comment` route.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

from urllib.parse import quote_plus, urlencode

import pytest

from tests.dummies_utils import create_dummy_projects

# ==============================================================================
# test_ko_not_found_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found_1(async_client):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/comment` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/comment` works.
    response_put = await async_client.put(
        url="/api/projects/UNKNOWN_PROJECT/constraints/UNKNOWN_CONSTRAINT/comment?"
        + urlencode(
            {"constraint_comment": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
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
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/comment` route with not existing project.

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

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/comment` works.
    response_put = await async_client.put(
        url="/api/projects/1a_SAMPLING_TODO/constraints/UNKNOWN_CONSTRAINT/comment?"
        + urlencode(
            {"constraint_comment": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
    assert response_put.status_code == 404
    assert response_put.json() == {
        "detail": "In project with id '1a_SAMPLING_TODO', the constraint with id 'UNKNOWN_CONSTRAINT' to annotate doesn't exist.",
    }


# ==============================================================================
# test_ok_good_state_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_good_state_1(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/comment` route with good state.

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
    assert response_get_constraints_before.json()["constraints"]["(0,4)"]["comment"] == ""

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/comment` works.
    response_put = await async_client.put(
        url="/api/projects/1m_CLUSTERING_TODO/constraints/(0,4)/comment?"
        + urlencode(
            {"constraint_comment": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
    assert response_put.status_code == 202
    assert response_put.json() == {
        "project_id": "1m_CLUSTERING_TODO",
        "constraint_id": "(0,4)",
        "constraint_comment": "Changement de valeur !",
        "detail": "In project with id '1m_CLUSTERING_TODO', the constraint with id '(0,4)' has been commented.",
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
    assert response_get_constraints_after.json()["constraints"]["(0,4)"]["comment"] == "Changement de valeur !"

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/1m_CLUSTERING_TODO/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "CLUSTERING_TODO"


# ==============================================================================
# test_ok_good_state_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_good_state_2(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/comment` route with good state.

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
    assert (
        response_get_constraints_before.json()["constraints"]["(4,7)"]["comment"]
        == "Même intention (gestion carte virtuelle)."
    )

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/comment` works.
    response_put = await async_client.put(
        url="/api/projects/1p_ITERATION_END/constraints/(4,7)/comment?"
        + urlencode(
            {"constraint_comment": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
    assert response_put.status_code == 202
    assert response_put.json() == {
        "project_id": "1p_ITERATION_END",
        "constraint_id": "(4,7)",
        "constraint_comment": "Changement de valeur !",
        "detail": "In project with id '1p_ITERATION_END', the constraint with id '(4,7)' has been commented.",
    }

    # Assert route `GET /api/projects/{project_id}/constraints` is updated.
    response_get_constraints_after = await async_client.get(
        url="/api/projects/1p_ITERATION_END/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_after.status_code == 200
    for constraint_id in response_get_constraints_before.json()["constraints"].keys():
        if constraint_id != "(4,7)":
            assert (
                response_get_constraints_after.json()["constraints"][constraint_id]
                == response_get_constraints_before.json()["constraints"][constraint_id]
            )
    assert response_get_constraints_after.json()["constraints"]["(4,7)"]["comment"] == "Changement de valeur !"

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/1p_ITERATION_END/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "ITERATION_END"
