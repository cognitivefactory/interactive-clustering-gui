# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_api_projects.py
* Description:  Unittests for `app` module on the `GET /api/projects` route.
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
# test_ok_empty
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_empty(async_client):
    """
    Test the `GET /api/projects` route with no projects.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /api/projects` works.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ok_not_empty
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_not_empty(async_client, tmp_path):
    """
    Test the `GET /api/projects` route with some projects.

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
            "1a_SAMPLING_TODO",
            "1k_ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS",
            "archive-1d_ANNOTATION_WITH_UPTODATE_MODELIZATION.zip",
        ],
    )

    # Assert route `GET /api/projects` works.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert sorted(response_get.json()) == [
        "0a_INITIALIZATION_WITHOUT_MODELIZATION",
        "0e_CLUSTERING_PENDING",
        "1a_SAMPLING_TODO",
        "1k_ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS",
    ]
