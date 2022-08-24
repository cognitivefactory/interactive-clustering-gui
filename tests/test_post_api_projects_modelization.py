# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_post_api_projects_modelization.py
* Description:  Unittests for `app` module on the `POST /api/projects/{project_id}/modelization` route.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

from pathlib import Path

import pytest

from tests.dummies_utils import create_dummy_projects

# ==============================================================================
# test_ko_not_found
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found(async_client):
    """
    Test the `POST /api/projects/{project_id}/modelization` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `POST /api/projects/{project_id}/modelization` works.
    response_post = await async_client.post(url="/api/projects/UNKNOWN_PROJECT/modelization")
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
    Test the `POST /api/projects/{project_id}/modelization` route with bad state.

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
            "0b_INITIALIZATION_WITH_PENDING_MODELIZATION",
        ],
    )

    # Assert route `POST /api/projects/{project_id}/modelization` works.
    response_post = await async_client.post(
        url="/api/projects/0b_INITIALIZATION_WITH_PENDING_MODELIZATION/modelization"
    )
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '0b_INITIALIZATION_WITH_PENDING_MODELIZATION' doesn't allow the preparation of modelization update task during this state (state='INITIALIZATION_WITH_PENDING_MODELIZATION')."
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/0b_INITIALIZATION_WITH_PENDING_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 0
    assert response_get.json()["status"]["state"] == "INITIALIZATION_WITH_PENDING_MODELIZATION"


# ==============================================================================
# test_ko_bad_state_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_state_2(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/modelization` route with bad state.

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

    # Assert route `POST /api/projects/{project_id}/modelization` works.
    response_post = await async_client.post(url="/api/projects/1b_SAMPLING_PENDING/modelization")
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '1b_SAMPLING_PENDING' doesn't allow the preparation of modelization update task during this state (state='SAMPLING_PENDING')."
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
    Test the `POST /api/projects/{project_id}/modelization` route with bad state.

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
            "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS",
        ],
    )

    # Assert route `POST /api/projects/{project_id}/modelization` works.
    response_post = await async_client.post(
        url="/api/projects/1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS/modelization"
    )
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS' doesn't allow the preparation of modelization update task during this state (state='ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS')."
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(
        url="/api/projects/1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS/status"
    )
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS"


# ==============================================================================
# test_ko_bad_state_4
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_state_4(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/modelization` route with bad state.

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

    # Assert route `POST /api/projects/{project_id}/modelization` works.
    response_post = await async_client.post(url="/api/projects/1o_CLUSTERING_WORKING/modelization")
    assert response_post.status_code == 403
    assert response_post.json() == {
        "detail": "The project with id '1o_CLUSTERING_WORKING' doesn't allow the preparation of modelization update task during this state (state='CLUSTERING_WORKING')."
    }

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/1o_CLUSTERING_WORKING/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "CLUSTERING_WORKING"


# ==============================================================================
# test_ok_1_202
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_1_202(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/modelization` route with good state.

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

    # Assert route `POST /api/projects/{project_id}/modelization` works.
    response_post = await async_client.post(url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/modelization")
    assert response_post.status_code == 202
    assert response_post.json() == {
        "project_id": "0a_INITIALIZATION_WITHOUT_MODELIZATION",
        "detail": "In project with id '0a_INITIALIZATION_WITHOUT_MODELIZATION', the modelization update task has been requested and is waiting for a background task.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is update.
    response_get = await async_client.get(url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 0
    assert response_get.json()["status"]["state"] in {
        "INITIALIZATION_WITH_PENDING_MODELIZATION",
        "INITIALIZATION_WITH_WORKING_MODELIZATION",
        "CLUSTERING_TODO",
    }
    if response_get.json()["status"]["state"] in {
        "INITIALIZATION_WITH_PENDING_MODELIZATION",
        "INITIALIZATION_WITH_WORKING_MODELIZATION",
    }:  # pragma: nocover
        assert response_get.json()["status"]["task"] is not None
    else:  # pragma: nocover
        assert response_get.json()["status"]["task"] is None


# ==============================================================================
# test_ok_2_202
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_2_202(async_client):
    """
    Test the `POST /api/projects/{project_id}/modelization` route with good state.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Import project.
    with open(Path(__file__).parent / "dummies" / "archive-1b_SAMPLING_PENDING.zip", "rb") as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-1b_SAMPLING_PENDING.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 201
    imported_project_id: str = response_put.json()["project_id"]

    # Assert route `POST /api/projects/{project_id}/modelization` works.
    response_post = await async_client.post(url="/api/projects/" + imported_project_id + "/modelization")
    assert response_post.status_code == 202
    assert response_post.json() == {
        "project_id": imported_project_id,
        "detail": "In project with id '"
        + imported_project_id
        + "', the modelization update task has been requested and is waiting for a background task.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is update.
    response_get = await async_client.get(url="/api/projects/" + imported_project_id + "/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] in {
        "IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
        "IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION",
        "SAMPLING_TODO",
    }
    if response_get.json()["status"]["state"] in {
        "IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
        "IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION",
    }:  # pragma: nocover
        assert response_get.json()["status"]["task"] is not None
    else:  # pragma: nocover
        assert response_get.json()["status"]["task"] is None


# ==============================================================================
# test_ok_3_202
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_3_202(async_client):
    """
    Test the `POST /api/projects/{project_id}/modelization` route with good state.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Import project.
    with open(
        Path(__file__).parent / "dummies" / "archive-1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS.zip", "rb"
    ) as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-1h_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 201
    imported_project_id: str = response_put.json()["project_id"]

    # Assert route `POST /api/projects/{project_id}/modelization` works.
    response_post = await async_client.post(url="/api/projects/" + imported_project_id + "/modelization")
    assert response_post.status_code == 202
    assert response_post.json() == {
        "project_id": imported_project_id,
        "detail": "In project with id '"
        + imported_project_id
        + "', the modelization update task has been requested and is waiting for a background task.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is update.
    response_get = await async_client.get(url="/api/projects/" + imported_project_id + "/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] in {
        "IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
        "IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION",
        "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
    }
    if response_get.json()["status"]["state"] in {
        "IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
        "IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION",
    }:  # pragma: nocover
        assert response_get.json()["status"]["task"] is not None
    else:  # pragma: nocover
        assert response_get.json()["status"]["task"] is None


# ==============================================================================
# test_ok_4_202
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_4_202(async_client):
    """
    Test the `POST /api/projects/{project_id}/modelization` route with good state.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Import project.
    with open(Path(__file__).parent / "dummies" / "archive-1o_CLUSTERING_WORKING.zip", "rb") as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-1o_CLUSTERING_WORKING.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 201
    imported_project_id: str = response_put.json()["project_id"]

    # Assert route `POST /api/projects/{project_id}/modelization` works.
    response_post = await async_client.post(url="/api/projects/" + imported_project_id + "/modelization")
    assert response_post.status_code == 202
    assert response_post.json() == {
        "project_id": imported_project_id,
        "detail": "In project with id '"
        + imported_project_id
        + "', the modelization update task has been requested and is waiting for a background task.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is update.
    response_get = await async_client.get(url="/api/projects/" + imported_project_id + "/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] in {
        "IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
        "IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION",
        "CLUSTERING_TODO",
    }
    if response_get.json()["status"]["state"] in {
        "IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
        "IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION",
    }:  # pragma: nocover
        assert response_get.json()["status"]["task"] is not None
    else:  # pragma: nocover
        assert response_get.json()["status"]["task"] is None


# ==============================================================================
# test_ok_5_202
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_5_202(async_client):
    """
    Test the `POST /api/projects/{project_id}/modelization` route with good state.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Import project.
    with open(Path(__file__).parent / "dummies" / "archive-1p_ITERATION_END.zip", "rb") as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-1p_ITERATION_END.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 201
    imported_project_id: str = response_put.json()["project_id"]

    # Assert route `POST /api/projects/{project_id}/modelization` works.
    response_post = await async_client.post(url="/api/projects/" + imported_project_id + "/modelization")
    assert response_post.status_code == 202
    assert response_post.json() == {
        "project_id": imported_project_id,
        "detail": "In project with id '"
        + imported_project_id
        + "', the modelization update task has been requested and is waiting for a background task.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is update.
    response_get = await async_client.get(url="/api/projects/" + imported_project_id + "/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] in {
        "IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
        "IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION",
        "ITERATION_END",
    }
    if response_get.json()["status"]["state"] in {
        "IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
        "IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION",
    }:  # pragma: nocover
        assert response_get.json()["status"]["task"] is not None
    else:  # pragma: nocover
        assert response_get.json()["status"]["task"] is None


# ==============================================================================
# test_ok_6_202
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_6_202(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/modelization` route with good state.

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

    # Assert route `POST /api/projects/{project_id}/modelization` works.
    response_post = await async_client.post(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/modelization"
    )
    assert response_post.status_code == 202
    assert response_post.json() == {
        "project_id": "1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS",
        "detail": "In project with id '1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS', the modelization update task has been requested and is waiting for a background task.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is update.
    response_get = await async_client.get(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/status"
    )
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] in {
        "ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS",
        "ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS",
        "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
    }
    if response_get.json()["status"]["state"] in {
        "ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS",
        "ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS",
    }:  # pragma: nocover
        assert response_get.json()["status"]["task"] is not None
    else:  # pragma: nocover
        assert response_get.json()["status"]["task"] is None


# ==============================================================================
# test_ok_7_202
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_7_202(async_client, tmp_path):
    """
    Test the `POST /api/projects/{project_id}/modelization` route with good state.

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

    # Assert route `POST /api/projects/{project_id}/modelization` works.
    response_post = await async_client.post(
        url="/api/projects/1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/modelization"
    )
    assert response_post.status_code == 202
    assert response_post.json() == {
        "project_id": "1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
        "detail": "In project with id '1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS', the modelization update task has been requested and is waiting for a background task.",
    }

    # Assert route `GET /api/projects/{project_id}/status` is update.
    response_get = await async_client.get(
        url="/api/projects/1i_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS/status"
    )
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] in {
        "ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS",
        "ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS",
        "ANNOTATION_WITH_UPTODATE_MODELIZATION",
    }
    if response_get.json()["status"]["state"] in {
        "ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS",
        "ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS",
    }:  # pragma: nocover
        assert response_get.json()["status"]["task"] is not None
    else:  # pragma: nocover
        assert response_get.json()["status"]["task"] is None
