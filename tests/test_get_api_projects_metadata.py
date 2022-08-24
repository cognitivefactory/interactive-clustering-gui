# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_api_projects_metadata.py
* Description:  Unittests for `app` module on the `GET /api/projects/{project_id}/metadata` route.
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
    Test the `GET /api/projects/{project_id}/metadata` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /api/projects/{project_id}/metadata` works.
    response_get = await async_client.get(url="/api/projects/UNKNOWN_PROJECT/metadata")
    assert response_get.status_code == 404
    assert response_get.json() == {
        "detail": "The project with id 'UNKNOWN_PROJECT' doesn't exist.",
    }


# ==============================================================================
# test_ok
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/metadata` route with some projects.

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

    # Assert route `GET /api/projects/{project_id}/metadata` works.
    response_get = await async_client.get(url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/metadata")
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "metadata"]
    assert response_get.json() == {
        "project_id": "0a_INITIALIZATION_WITHOUT_MODELIZATION",
        "metadata": {
            "project_id": "0a_INITIALIZATION_WITHOUT_MODELIZATION",
            "project_name": "unittests",
            "creation_timestamp": 1657541236.556489,
        },
    }

    # Assert file content is the same.
    with open(tmp_path / "0a_INITIALIZATION_WITHOUT_MODELIZATION" / "metadata.json", "r") as metadata_fileobject:
        assert response_get.json()["metadata"] == json.load(metadata_fileobject)
