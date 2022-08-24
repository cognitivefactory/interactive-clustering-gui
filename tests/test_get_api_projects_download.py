# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_api_projects_download.py
* Description:  Unittests for `app` module on the `GET /api/projects/{project_id}/download` route.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import pytest

from tests.dummies_utils import create_dummy_projects

# from zipp import zipfile


# ==============================================================================
# test_ko_not_found
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found(async_client):
    """
    Test the `GET /api/projects/{project_id}/download` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /api/projects/{project_id}/download` works.
    response_get = await async_client.get(url="/api/projects/UNKNOWN_PROJECT/download")
    assert response_get.status_code == 404
    assert response_get.json() == {
        "detail": "The project with id 'UNKNOWN_PROJECT' doesn't exist.",
    }


# ==============================================================================
# test_ok_without_modelization
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_without_modelization(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/download` route.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
        tmp_path: The temporary path given for this test, declared in `conftest.py`.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "0a_INITIALIZATION_WITHOUT_MODELIZATION",
        ],
    )

    # Assert route `GET /api/projects/{project_id}/download` works.
    response_get = await async_client.get(url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/download")
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "application/x-zip-compressed"
    assert (
        response_get.headers["content-disposition"]
        == 'attachment; filename="archive-0a_INITIALIZATION_WITHOUT_MODELIZATION.zip"'
    )

    # TODO: explore content
    # with zipfile.ZipFile(import_archive_path, "r") as import_archive_file:
    # import_archive_file.namelist()


# ==============================================================================
# test_ok_with_modelization
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_with_modelization(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/download` route.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
        tmp_path: The temporary path given for this test, declared in `conftest.py`.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "1c_SAMPLING_WORKING",
        ],
    )

    # Assert route `GET /api/projects/{project_id}/download` works.
    response_get = await async_client.get(url="/api/projects/1c_SAMPLING_WORKING/download")
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "application/x-zip-compressed"
    assert response_get.headers["content-disposition"] == 'attachment; filename="archive-1c_SAMPLING_WORKING.zip"'

    # TODO: explore content
    # with zipfile.ZipFile(import_archive_path, "r") as import_archive_file:
    # import_archive_file.namelist()
