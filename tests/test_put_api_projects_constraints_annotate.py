# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_put_api_projects_constraints_annotate.py
* Description:  Unittests for `app` module on the `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` route.
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
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` works.
    response_put = await async_client.put(url="/api/projects/UNKNOWN_PROJECT/constraints/UNKNOWN_CONSTRAINT/annotate")
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
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` route with not existing project.

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

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` works.
    response_put = await async_client.put(url="/api/projects/1a_SAMPLING_TODO/constraints/UNKNOWN_CONSTRAINT/annotate")
    assert response_put.status_code == 404
    assert response_put.json() == {
        "detail": "In project with id '1a_SAMPLING_TODO', the constraint with id 'UNKNOWN_CONSTRAINT' to annotate doesn't exist.",
    }


# ==============================================================================
# test_ko_bad_state_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_state_1(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` route with bad state.

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
            "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS",
        ],
    )

    # Get texts before test.
    response_get_constraints_before = await async_client.get(
        url="/api/projects/1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_before.status_code == 200
    assert response_get_constraints_before.json()["constraints"]["(14,9)"]["constraint_type"] is None

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` works.
    response_put = await async_client.put(
        url="/api/projects/1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS/constraints/(14,9)/annotate?constraint_type=MUST_LINK"
    )
    assert response_put.status_code == 403
    assert response_put.json() == {
        "detail": "The project with id '1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS' doesn't allow modification during this state (state='ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS').",
    }

    # Assert route `GET /api/projects/{project_id}/constraints` is still the same.
    response_get_constraints_after = await async_client.get(
        url="/api/projects/1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_after.status_code == 200
    assert response_get_constraints_after.json() == response_get_constraints_before.json()
    assert response_get_constraints_after.json()["constraints"]["(14,9)"]["constraint_type"] is None


# ==============================================================================
# test_ko_bad_state_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_state_2(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` route with bad state.

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
    assert response_get_constraints_before.json()["constraints"]["(1,2)"]["constraint_type"] == "MUST_LINK"

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` works.
    response_put = await async_client.put(
        url="/api/projects/1m_CLUSTERING_TODO/constraints/(1,2)/annotate?constraint_type=MUST_LINK"
    )
    assert response_put.status_code == 403
    assert response_put.json() == {
        "detail": "The project with id '1m_CLUSTERING_TODO' doesn't allow modification during this state (state='CLUSTERING_TODO').",
    }

    # Assert route `GET /api/projects/{project_id}/constraints` is still the same.
    response_get_constraints_after = await async_client.get(
        url="/api/projects/1m_CLUSTERING_TODO/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_after.status_code == 200
    assert response_get_constraints_after.json() == response_get_constraints_before.json()
    assert response_get_constraints_after.json()["constraints"]["(1,2)"]["constraint_type"] == "MUST_LINK"


# ==============================================================================
# test_ko_bad_annotation
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_annotation(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` route with bad annotation.

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
    assert response_get_constraints_before.json()["constraints"]["(0,4)"]["constraint_type"] is None

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` works.
    response_put = await async_client.put(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/constraints/(0,4)/annotate?constraint_type=UNKNOWN_ANNOTATION"
    )
    assert response_put.status_code == 422

    # Assert route `GET /api/projects/{project_id}/constraints` is still the same.
    response_get_constraints_after = await async_client.get(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_after.status_code == 200
    assert response_get_constraints_after.json() == response_get_constraints_before.json()
    assert response_get_constraints_after.json()["constraints"]["(0,4)"]["constraint_type"] is None


# ==============================================================================
# test_ok_good_state_none
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_good_state_none(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` route with good state.

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

    # Get texts before test.
    response_get_constraints_before = await async_client.get(
        url="/api/projects/1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_before.status_code == 200
    assert response_get_constraints_before.json()["constraints"]["(12,9)"]["constraint_type"] == "MUST_LINK"
    assert response_get_constraints_before.json()["constraints"]["(12,9)"]["constraint_type_previous"] == [
        None,
        "CANNOT_LINK",
    ]
    assert response_get_constraints_before.json()["constraints"]["(12,9)"]["to_annotate"] is False
    assert response_get_constraints_before.json()["constraints"]["(12,9)"]["date_of_update"] is not None

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` works.
    response_put = await async_client.put(
        url="/api/projects/1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/constraints/(12,9)/annotate"
    )
    assert response_put.status_code == 202
    assert response_put.json() == {
        "project_id": "1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
        "constraint_id": "(12,9)",
        "detail": "In project with id '1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS', the constraint with id '(12,9)' has been annotated at `None`.",
    }

    # Assert route `GET /api/projects/{project_id}/constraints` is updated.
    response_get_constraints_after = await async_client.get(
        url="/api/projects/1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_after.status_code == 200
    for constraint_id in response_get_constraints_before.json()["constraints"].keys():
        if constraint_id != "(12,9)":
            assert (
                response_get_constraints_after.json()["constraints"][constraint_id]
                == response_get_constraints_before.json()["constraints"][constraint_id]
            )
    assert response_get_constraints_after.json()["constraints"]["(12,9)"]["constraint_type"] is None
    assert response_get_constraints_after.json()["constraints"]["(12,9)"]["constraint_type_previous"] == [
        None,
        "CANNOT_LINK",
        "MUST_LINK",
    ]
    assert response_get_constraints_after.json()["constraints"]["(12,9)"]["to_annotate"] is False
    assert response_get_constraints_after.json()["constraints"]["(12,9)"]["date_of_update"] is not None

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(
        url="/api/projects/1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/status"
    )
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS"


# ==============================================================================
# test_ok_good_state_must_link
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_good_state_must_link(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` route with good state.

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
    assert response_get_constraints_before.json()["constraints"]["(0,4)"]["constraint_type"] is None
    assert (
        response_get_constraints_before.json()["constraints"]["(0,4)"]["constraint_type_previous"] == []  # noqa: WPS520
    )
    assert response_get_constraints_before.json()["constraints"]["(0,4)"]["to_annotate"] is True
    assert response_get_constraints_before.json()["constraints"]["(0,4)"]["date_of_update"] is None

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` works.
    response_put = await async_client.put(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/constraints/(0,4)/annotate?constraint_type=MUST_LINK"
    )
    assert response_put.status_code == 202
    assert response_put.json() == {
        "project_id": "1d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "constraint_id": "(0,4)",
        "detail": "In project with id '1d_ANNOTATION_WITH_UPTODATE_MODELIZATION', the constraint with id '(0,4)' has been annotated at `MUST_LINK`.",
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
    assert response_get_constraints_after.json()["constraints"]["(0,4)"]["constraint_type"] == "MUST_LINK"
    assert response_get_constraints_after.json()["constraints"]["(0,4)"]["constraint_type_previous"] == [
        None,
    ]
    assert response_get_constraints_after.json()["constraints"]["(0,4)"]["to_annotate"] is False
    assert response_get_constraints_after.json()["constraints"]["(0,4)"]["date_of_update"] is not None

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS"


# ==============================================================================
# test_ok_good_state_cannot_link
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_good_state_cannot_link(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` route with good state.

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
            "1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
        ],
    )

    # Get texts before test.
    response_get_constraints_before = await async_client.get(
        url="/api/projects/1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_before.status_code == 200
    assert response_get_constraints_before.json()["constraints"]["(12,9)"]["constraint_type"] == "MUST_LINK"
    assert response_get_constraints_before.json()["constraints"]["(12,9)"]["constraint_type_previous"] == [
        None,
        "CANNOT_LINK",
    ]
    assert response_get_constraints_before.json()["constraints"]["(12,9)"]["to_annotate"] is False
    assert response_get_constraints_before.json()["constraints"]["(12,9)"]["date_of_update"] is not None

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` works.
    response_put = await async_client.put(
        url="/api/projects/1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/constraints/(12,9)/annotate?constraint_type=CANNOT_LINK"
    )
    assert response_put.status_code == 202
    assert response_put.json() == {
        "project_id": "1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
        "constraint_id": "(12,9)",
        "detail": "In project with id '1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS', the constraint with id '(12,9)' has been annotated at `CANNOT_LINK`.",
    }

    # Assert route `GET /api/projects/{project_id}/constraints` is updated.
    response_get_constraints_after = await async_client.get(
        url="/api/projects/1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_after.status_code == 200
    for constraint_id in response_get_constraints_before.json()["constraints"].keys():
        if constraint_id != "(12,9)":
            assert (
                response_get_constraints_after.json()["constraints"][constraint_id]
                == response_get_constraints_before.json()["constraints"][constraint_id]
            )
    assert response_get_constraints_after.json()["constraints"]["(12,9)"]["constraint_type"] == "CANNOT_LINK"
    assert response_get_constraints_after.json()["constraints"]["(12,9)"]["constraint_type_previous"] == [
        None,
        "CANNOT_LINK",
        "MUST_LINK",
    ]
    assert response_get_constraints_after.json()["constraints"]["(12,9)"]["to_annotate"] is False
    assert response_get_constraints_after.json()["constraints"]["(12,9)"]["date_of_update"] is not None

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(
        url="/api/projects/1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/status"
    )
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS"


# ==============================================================================
# test_ok_double_request
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_double_request(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` route with double requests.

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
            "1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS",
        ],
    )

    # Get texts before test.
    response_get_constraints_before = await async_client.get(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_before.status_code == 200
    assert response_get_constraints_before.json()["constraints"]["(11,12)"]["constraint_type"] == "MUST_LINK"
    assert response_get_constraints_before.json()["constraints"]["(11,12)"]["constraint_type_previous"] == [
        None,
    ]
    assert response_get_constraints_before.json()["constraints"]["(11,12)"]["to_annotate"] is False
    assert response_get_constraints_before.json()["constraints"]["(11,12)"]["date_of_update"] is not None

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` works.
    response_put_1 = await async_client.put(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/constraints/(11,12)/annotate?constraint_type=MUST_LINK"
    )
    assert response_put_1.status_code == 202
    assert response_put_1.json() == {
        "project_id": "1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS",
        "constraint_id": "(11,12)",
        "detail": "In project with id '1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS', the constraint with id '(11,12)' has been annotated at `MUST_LINK`.",
    }

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` works.
    response_put_2 = await async_client.put(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/constraints/(11,12)/annotate?constraint_type=CANNOT_LINK"
    )
    assert response_put_2.status_code == 202
    assert response_put_2.json() == {
        "project_id": "1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS",
        "constraint_id": "(11,12)",
        "detail": "In project with id '1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS', the constraint with id '(11,12)' has been annotated at `CANNOT_LINK`.",
    }

    # Assert route `PUT /api/projects/{project_id}/constraints/{constraint_id}/annotate` works.
    response_put_3 = await async_client.put(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/constraints/(11,12)/annotate"
    )
    assert response_put_3.status_code == 202
    assert response_put_3.json() == {
        "project_id": "1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS",
        "constraint_id": "(11,12)",
        "detail": "In project with id '1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS', the constraint with id '(11,12)' has been annotated at `None`.",
    }

    # Assert route `GET /api/projects/{project_id}/constraints` is updated.
    response_get_constraints_after = await async_client.get(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/constraints?without_hidden_constraints=false"
    )
    assert response_get_constraints_after.status_code == 200
    for constraint_id in response_get_constraints_before.json()["constraints"].keys():
        if constraint_id != "(11,12)":
            assert (
                response_get_constraints_after.json()["constraints"][constraint_id]
                == response_get_constraints_before.json()["constraints"][constraint_id]
            )
    assert response_get_constraints_after.json()["constraints"]["(11,12)"]["constraint_type"] is None
    assert response_get_constraints_after.json()["constraints"]["(11,12)"]["constraint_type_previous"] == [
        None,
        "MUST_LINK",
        "MUST_LINK",
        "CANNOT_LINK",
    ]
    assert response_get_constraints_after.json()["constraints"]["(11,12)"]["to_annotate"] is False
    assert response_get_constraints_after.json()["constraints"]["(11,12)"]["date_of_update"] is not None

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/status"
    )
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS"
