# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_put_api_projects.py
* Description:  Unittests for `app` module on the `PUT /api/projects` route.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

from pathlib import Path

import pytest

# ==============================================================================
# test_ko_archive_type
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_archive_type(async_client):
    """
    Test the `PUT /api/projects` route with bad archive type.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
    with open(Path(__file__).parent / "dummies" / "dummy_24.xlsx", "rb") as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "dummy_24.xlsx",
                    archive_fileobject,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
            },
        )
    assert response_put.status_code == 400
    assert response_put.json() == {
        "detail": "The file type 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' is not supported. Please use '.zip' file.",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ko_bad_archive
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_archive(async_client):
    """
    Test the `PUT /api/projects` route with bad archive type.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
    with open(Path(__file__).parent / "dummies" / "archive-ERROR_bad_archive.zip", "rb") as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-ERROR_bad_archive.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 400
    assert response_put.json() == {
        "detail": "An error occurs in project import. Project archive is probably invalid.",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ko_missing_files
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_missing_files(async_client):
    """
    Test the `PUT /api/projects` route with missing file in archive.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
    with open(Path(__file__).parent / "dummies" / "archive-ERROR_missing_files.zip", "rb") as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-ERROR_missing_files.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 400
    assert response_put.json() == {
        "detail": "The project archive file doesn't contains the following files: ['metadata.json', 'status.json', 'settings.json', 'sampling.json', 'clustering.json', 'modelization.json'].",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ko_metadata_missing_project_name
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_metadata_missing_project_name(async_client):
    """
    Test the `PUT /api/projects` route with missing project name metadata in archive.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
    with open(
        Path(__file__).parent / "dummies" / "archive-ERROR_metadata_missing_project_name.zip", "rb"
    ) as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-ERROR_metadata_missing_project_name.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 400
    assert response_put.json() == {
        "detail": "The project archive file has an invalid `metadata.json` file.",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ko_metadata_bad_project_name
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_metadata_bad_project_name(async_client):
    """
    Test the `PUT /api/projects` route with bad project name metadata in archive.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
    with open(
        Path(__file__).parent / "dummies" / "archive-ERROR_metadata_bad_project_name.zip", "rb"
    ) as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-ERROR_metadata_bad_project_name.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 400
    assert response_put.json() == {
        "detail": "The project archive file has an invalid `metadata.json` file.",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ko_metadata_missing_creation_timestamp
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_metadata_missing_creation_timestamp(async_client):
    """
    Test the `PUT /api/projects` route with missing creation timestamp metadata in archive.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
    with open(
        Path(__file__).parent / "dummies" / "archive-ERROR_metadata_missing_creation_timestamp.zip", "rb"
    ) as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-ERROR_metadata_missing_creation_timestamp.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 400
    assert response_put.json() == {
        "detail": "The project archive file has an invalid `metadata.json` file.",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ko_metadata_bad_creation_timestamp
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_metadata_bad_creation_timestamp(async_client):
    """
    Test the `PUT /api/projects` route with bad creation timestamp metadata in archive.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
    with open(
        Path(__file__).parent / "dummies" / "archive-ERROR_metadata_bad_creation_timestamp.zip", "rb"
    ) as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-ERROR_metadata_bad_creation_timestamp.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 400
    assert response_put.json() == {
        "detail": "The project archive file has an invalid `metadata.json` file.",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ko_status_missing_state
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_status_missing_state(async_client):
    """
    Test the `PUT /api/projects` route with missing state status in archive.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
    with open(Path(__file__).parent / "dummies" / "archive-ERROR_status_missing_state.zip", "rb") as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-ERROR_status_missing_state.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 400
    assert response_put.json() == {
        "detail": "The project archive file has an invalid `status.json` file (see key `state`).",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ko_status_bad_state
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_status_bad_state(async_client):
    """
    Test the `PUT /api/projects` route with bad state status in archive.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
    with open(Path(__file__).parent / "dummies" / "archive-ERROR_status_bad_state.zip", "rb") as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-ERROR_status_bad_state.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 400
    assert response_put.json() == {
        "detail": "The project archive file has an invalid `status.json` file (see key `state`).",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ok_during_initialization
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_during_initialization(async_client):
    """
    Test the `PUT /api/projects` route with project during initialization step.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
    with open(
        Path(__file__).parent / "dummies" / "archive-0a_INITIALIZATION_WITHOUT_MODELIZATION.zip", "rb"
    ) as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-0a_INITIALIZATION_WITHOUT_MODELIZATION.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 201
    assert list(response_put.json().keys()) == ["project_id", "detail"]
    imported_project_id: str = response_put.json()["project_id"]
    assert response_put.json() == {
        "project_id": imported_project_id,
        "detail": "The project with name 'unittests' has been imported. It has the id '"
        + str(imported_project_id)
        + "'.",
    }

    # Assert route `GET /api/projects` works and contains the created project.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert imported_project_id in response_get.json()

    # TODO: assert content.

    # Assert route `GET /api/projects/{project_id}/status` is correct.
    response_get_status = await async_client.get(url="/api/projects/" + imported_project_id + "/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 0
    assert response_get_status.json()["status"]["state"] == "INITIALIZATION_WITHOUT_MODELIZATION"
    assert response_get_status.json()["status"]["task"] is None


# ==============================================================================
# test_ok_during_sampling
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_during_sampling(async_client):
    """
    Test the `PUT /api/projects` route with project during sampling step.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
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
    assert list(response_put.json().keys()) == ["project_id", "detail"]
    imported_project_id: str = response_put.json()["project_id"]
    assert response_put.json() == {
        "project_id": imported_project_id,
        "detail": "The project with name 'unittests' has been imported. It has the id '"
        + str(imported_project_id)
        + "'.",
    }

    # Assert route `GET /api/projects` works and contains the created project.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert imported_project_id in response_get.json()

    # TODO: assert content.

    # Assert route `GET /api/projects/{project_id}/status` is correct.
    response_get_status = await async_client.get(url="/api/projects/" + imported_project_id + "/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION"
    assert response_get_status.json()["status"]["task"] is None


# ==============================================================================
# test_ok_during_annotation
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_during_annotation(async_client):
    """
    Test the `PUT /api/projects` route with project during annotation step.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
    with open(
        Path(__file__).parent / "dummies" / "archive-1d_ANNOTATION_WITH_UPTODATE_MODELIZATION.zip", "rb"
    ) as archive_fileobject:
        response_put = await async_client.put(
            url="/api/projects",
            files={
                "project_archive": (
                    "archive-1d_ANNOTATION_WITH_UPTODATE_MODELIZATION.zip",
                    archive_fileobject,
                    "application/x-zip-compressed",
                ),
            },
        )
    assert response_put.status_code == 201
    assert list(response_put.json().keys()) == ["project_id", "detail"]
    imported_project_id: str = response_put.json()["project_id"]
    assert response_put.json() == {
        "project_id": imported_project_id,
        "detail": "The project with name 'unittests' has been imported. It has the id '"
        + str(imported_project_id)
        + "'.",
    }

    # Assert route `GET /api/projects` works and contains the created project.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert imported_project_id in response_get.json()

    # TODO: assert content.

    # Assert route `GET /api/projects/{project_id}/status` is correct.
    response_get_status = await async_client.get(url="/api/projects/" + imported_project_id + "/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION"
    assert response_get_status.json()["status"]["task"] is None


# ==============================================================================
# test_ok_during_clustering
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_during_clustering(async_client):
    """
    Test the `PUT /api/projects` route with project during clustering step.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
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
    assert list(response_put.json().keys()) == ["project_id", "detail"]
    imported_project_id: str = response_put.json()["project_id"]
    assert response_put.json() == {
        "project_id": imported_project_id,
        "detail": "The project with name 'unittests' has been imported. It has the id '"
        + str(imported_project_id)
        + "'.",
    }

    # Assert route `GET /api/projects` works and contains the created project.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert imported_project_id in response_get.json()

    # TODO: assert content.

    # Assert route `GET /api/projects/{project_id}/status` is correct.
    response_get_status = await async_client.get(url="/api/projects/" + imported_project_id + "/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION"
    assert response_get_status.json()["status"]["task"] is None


# ==============================================================================
# test_ok_during_iteration_end
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_during_iteration_end(async_client):
    """
    Test the `PUT /api/projects` route with project during iteration end step.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects` works.
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
    assert list(response_put.json().keys()) == ["project_id", "detail"]
    imported_project_id: str = response_put.json()["project_id"]
    assert response_put.json() == {
        "project_id": imported_project_id,
        "detail": "The project with name 'unittests' has been imported. It has the id '"
        + str(imported_project_id)
        + "'.",
    }

    # Assert route `GET /api/projects` works and contains the created project.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert imported_project_id in response_get.json()

    # TODO: assert content.

    # Assert route `GET /api/projects/{project_id}/status` is correct.
    response_get_status = await async_client.get(url="/api/projects/" + imported_project_id + "/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION"
    assert response_get_status.json()["status"]["task"] is None
