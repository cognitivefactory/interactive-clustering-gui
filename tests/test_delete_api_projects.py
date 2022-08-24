# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_delete_api_projects.py
* Description:  Unittests for `app` module on the `DELETE /api/projects` route.
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
# test_delete_api_projects_ok
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok(async_client, tmp_path):
    """
    Test the `DELETE /api/projects` route.

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
            "0e_CLUSTERING_PENDING",
        ],
    )

    # Assert route `DELETE /api/projects` works.
    response_delete = await async_client.delete(
        url="/api/projects/0e_CLUSTERING_PENDING",
    )
    assert response_delete.status_code == 202
    assert list(response_delete.json().keys()) == ["project_id", "detail"]
    assert response_delete.json()["project_id"] == "0e_CLUSTERING_PENDING"
    assert response_delete.json()["detail"] == "The deletion of project with id '0e_CLUSTERING_PENDING' is accepted."

    # Assert route `GET /api/projects` is now smaller.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == [
        "0a_INITIALIZATION_WITHOUT_MODELIZATION",
    ]


# ==============================================================================
# test_ok_not_existing
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_not_existing(async_client):
    """
    Test the `DELETE /api/projects` route.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `DELETE /api/projects` works.
    response_delete = await async_client.delete(
        url="/api/projects/UNKNOWN_PROJECT",
    )
    assert response_delete.status_code == 202
    assert list(response_delete.json().keys()) == ["project_id", "detail"]
    assert response_delete.json()["project_id"] == "UNKNOWN_PROJECT"
    assert response_delete.json()["detail"] == "The deletion of project with id 'UNKNOWN_PROJECT' is accepted."

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520
