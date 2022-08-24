# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_put_api_projects_texts_rename.py
* Description:  Unittests for `app` module on the `PUT /api/projects/{project_id}/texts/{text_id}/rename` route.
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
# test_ko_not_found
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found_1(async_client):
    """
    Test the `PUT /api/projects/{project_id}/texts/{text_id}/rename` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects/{project_id}/texts/{text_id}/rename` works.
    response_put = await async_client.put(
        url="/api/projects/UNKNOWN_PROJECT/texts/UNKNOWN_TEXT/rename?"
        + urlencode(
            {"text_value": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
    assert response_put.status_code == 404
    assert response_put.json() == {
        "detail": "The project with id 'UNKNOWN_PROJECT' doesn't exist.",
    }


# ==============================================================================
# test_ko_not_found
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found_2(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/texts/{text_id}/rename` route with not existing project.

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

    # Assert route `PUT /api/projects/{project_id}/texts/{text_id}/rename` works.
    response_put = await async_client.put(
        url="/api/projects/1a_SAMPLING_TODO/texts/UNKNOWN_TEXT/rename?"
        + urlencode(
            {"text_value": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
    assert response_put.status_code == 404
    assert response_put.json() == {
        "detail": "In project with id '1a_SAMPLING_TODO', the text with id 'UNKNOWN_TEXT' to rename doesn't exist.",
    }


# ==============================================================================
# test_ko_bad_state_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_state_1(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/texts/{text_id}/rename` route with bad state.

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

    # Get texts before test.
    response_get_texts_before = await async_client.get(
        url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/texts?without_deleted_texts=false"
    )
    assert response_get_texts_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/texts/{text_id}/rename` works.
    response_put = await async_client.put(
        url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/texts/0/rename?"
        + urlencode(
            {"text_value": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
    assert response_put.status_code == 403
    assert response_put.json() == {
        "detail": "The project with id '0a_INITIALIZATION_WITHOUT_MODELIZATION' doesn't allow modification during this state (state='INITIALIZATION_WITHOUT_MODELIZATION').",
    }

    # Assert route `GET /api/projects/{project_id}/texts` is still the same.
    response_get_texts_after = await async_client.get(
        url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/texts?without_deleted_texts=false"
    )
    assert response_get_texts_after.status_code == 200
    assert response_get_texts_after.json() == response_get_texts_before.json()


# ==============================================================================
# test_ko_bad_state_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_state_2(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/texts/{text_id}/rename` route with bad state.

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
    response_get_texts_before = await async_client.get(
        url="/api/projects/1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS/texts?without_deleted_texts=false"
    )
    assert response_get_texts_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/texts/{text_id}/rename` works.
    response_put = await async_client.put(
        url="/api/projects/1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS/texts/0/rename?"
        + urlencode(
            {"text_value": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
    assert response_put.status_code == 403
    assert response_put.json() == {
        "detail": "The project with id '1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS' doesn't allow modification during this state (state='ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS').",
    }

    # Assert route `GET /api/projects/{project_id}/texts` is still the same.
    response_get_texts_after = await async_client.get(
        url="/api/projects/1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS/texts?without_deleted_texts=false"
    )
    assert response_get_texts_after.status_code == 200
    assert response_get_texts_after.json() == response_get_texts_before.json()


# ==============================================================================
# test_ok_good_state_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_good_state_1(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/texts/{text_id}/rename` route with good state.

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
    response_get_texts_before = await async_client.get(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts?without_deleted_texts=false"
    )
    assert response_get_texts_before.status_code == 200
    assert response_get_texts_before.json()["texts"]["0"]["text"] != "Changement de valeur !"

    # Assert route `PUT /api/projects/{project_id}/texts/{text_id}/rename` works.
    response_put = await async_client.put(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts/0/rename?"
        + urlencode(
            {"text_value": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
    assert response_put.status_code == 202
    assert response_put.json() == {
        "project_id": "1d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "text_id": "0",
        "text_value": "Changement de valeur !",
        "detail": "In project with id '1d_ANNOTATION_WITH_UPTODATE_MODELIZATION', the text with id '0' has been renamed.",
    }

    # Assert route `GET /api/projects/{project_id}/texts` is updated.
    response_get_texts_after = await async_client.get(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts?without_deleted_texts=false"
    )
    assert response_get_texts_after.status_code == 200
    assert response_get_texts_after.json()["texts"]["0"]["text"] == "Changement de valeur !"

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS"


# ==============================================================================
# test_ok_good_state_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_good_state_2(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/texts/{text_id}/rename` route with good state.

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
    response_get_texts_before = await async_client.get(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/texts?without_deleted_texts=false"
    )
    assert response_get_texts_before.status_code == 200
    assert response_get_texts_before.json()["texts"]["0"]["text"] != "Changement de valeur !"

    # Assert route `PUT /api/projects/{project_id}/texts/{text_id}/rename` works.
    response_put = await async_client.put(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/texts/0/rename?"
        + urlencode(
            {"text_value": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
    assert response_put.status_code == 202
    assert response_put.json() == {
        "project_id": "1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS",
        "text_id": "0",
        "text_value": "Changement de valeur !",
        "detail": "In project with id '1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS', the text with id '0' has been renamed.",
    }

    # Assert route `GET /api/projects/{project_id}/texts` is updated.
    response_get_texts_after = await async_client.get(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/texts?without_deleted_texts=false"
    )
    assert response_get_texts_after.status_code == 200
    assert response_get_texts_after.json()["texts"]["0"]["text"] == "Changement de valeur !"

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/status"
    )
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS"


# ==============================================================================
# test_ok_good_state_3
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_good_state_3(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/texts/{text_id}/rename` route with good state.

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
    response_get_texts_before = await async_client.get(
        url="/api/projects/1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/texts?without_deleted_texts=false"
    )
    assert response_get_texts_before.status_code == 200
    assert response_get_texts_before.json()["texts"]["0"]["text"] != "Changement de valeur !"

    # Assert route `PUT /api/projects/{project_id}/texts/{text_id}/rename` works.
    response_put = await async_client.put(
        url="/api/projects/1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/texts/0/rename?"
        + urlencode(
            {"text_value": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
    assert response_put.status_code == 202
    assert response_put.json() == {
        "project_id": "1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
        "text_id": "0",
        "text_value": "Changement de valeur !",
        "detail": "In project with id '1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS', the text with id '0' has been renamed.",
    }

    # Assert route `GET /api/projects/{project_id}/texts` is updated.
    response_get_texts_after = await async_client.get(
        url="/api/projects/1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/texts?without_deleted_texts=false"
    )
    assert response_get_texts_after.status_code == 200
    assert response_get_texts_after.json()["texts"]["0"]["text"] == "Changement de valeur !"

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
    Test the `PUT /api/projects/{project_id}/texts/{text_id}/rename` route with double request.

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
    response_get_texts_before = await async_client.get(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts?without_deleted_texts=false"
    )
    assert response_get_texts_before.status_code == 200
    assert response_get_texts_before.json()["texts"]["0"]["text"] != "Changement de valeur !"

    # Assert route `PUT /api/projects/{project_id}/texts/{text_id}/rename` works.
    response_put1 = await async_client.put(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts/0/rename?"
        + urlencode(
            {"text_value": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
    assert response_put1.status_code == 202
    assert response_put1.json() == {
        "project_id": "1d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "text_id": "0",
        "text_value": "Changement de valeur !",
        "detail": "In project with id '1d_ANNOTATION_WITH_UPTODATE_MODELIZATION', the text with id '0' has been renamed.",
    }

    # Assert route `PUT /api/projects/{project_id}/texts/{text_id}/rename` works.
    response_put2 = await async_client.put(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts/0/rename?"
        + urlencode(
            {"text_value": "Changement de valeur !"},
            quote_via=quote_plus,
        )
    )
    assert response_put2.status_code == 202
    assert response_put2.json() == {
        "project_id": "1d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "text_id": "0",
        "text_value": "Changement de valeur !",
        "detail": "In project with id '1d_ANNOTATION_WITH_UPTODATE_MODELIZATION', the text with id '0' has been renamed.",
    }

    # Assert route `GET /api/projects/{project_id}/texts` is updated.
    response_get_texts_after = await async_client.get(
        url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts?without_deleted_texts=false"
    )
    assert response_get_texts_after.status_code == 200
    assert response_get_texts_after.json()["texts"]["0"]["text"] == "Changement de valeur !"

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")

    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS"
