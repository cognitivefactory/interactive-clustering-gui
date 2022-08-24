# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_gui_projects_listing.py
* Description:  Unittests for `app` module on the `GET /gui/projects` route.
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
    Test the `GET /gui/projects` route with no projects.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /gui/projects` works.
    response_get = await async_client.get(url="/gui/projects")
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert b"<!-- HEAD -->" in response_get.content
    assert b"<title>Interactive Clustering</title>" in response_get.content
    assert b"<!-- BODY -->" in response_get.content
    assert b"<!-- CONTAINER PROJECTS LISTING -->" in response_get.content
    assert b"List of existing projects" in response_get.content
    assert b"(no projects)" in response_get.content
    assert b"<!-- CONTAINER PROJECTS LISTING - CONTENT -->" in response_get.content
    assert response_get.content.count(b'<div class="card" id="') == 0
    assert b"<!-- CONTAINER PROJECTS LISTING - CONTENT ACTIONS -->" in response_get.content
    assert b"Add new" in response_get.content
    assert b"Import" in response_get.content
    assert b"<!-- PROJECT CREATION POPUP -->" in response_get.content
    assert b"Create" in response_get.content
    assert b"<!-- PROJECT IMPORT POPUP -->" in response_get.content
    assert b"Import" in response_get.content


# ==============================================================================
# test_ok_one_project
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_one_project(async_client, tmp_path):
    """
    Test the `GET /gui/projects` route with one projects.

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

    # Assert route `GET /gui/projects` works.
    response_get = await async_client.get(url="/gui/projects")
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert b"<!-- HEAD -->" in response_get.content
    assert b"<title>Interactive Clustering</title>" in response_get.content
    assert b"<!-- BODY -->" in response_get.content
    assert b"<!-- CONTAINER PROJECTS LISTING -->" in response_get.content
    assert b"List of existing projects" in response_get.content
    assert b"(1 project)" in response_get.content
    assert b"<!-- CONTAINER PROJECTS LISTING - CONTENT -->" in response_get.content
    assert response_get.content.count(b'<div class="card" id="') == 1
    assert b'<div class="card" id="0a_INITIALIZATION_WITHOUT_MODELIZATION">' in response_get.content
    assert b"<!-- CONTAINER PROJECTS LISTING - CONTENT ACTIONS -->" in response_get.content
    assert b"Add new" in response_get.content
    assert b"Import" in response_get.content
    assert b"<!-- PROJECT CREATION POPUP -->" in response_get.content
    assert b"Create" in response_get.content
    assert b"<!-- PROJECT IMPORT POPUP -->" in response_get.content
    assert b"Import" in response_get.content


# ==============================================================================
# test_ok_some_projects
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_some_projects(async_client, tmp_path):
    """
    Test the `GET /gui/projects` route with some projects.

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

    # Assert route `GET /gui/projects` works.
    response_get = await async_client.get(url="/gui/projects")
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert b"<!-- HEAD -->" in response_get.content
    assert b"<title>Interactive Clustering</title>" in response_get.content
    assert b"<!-- BODY -->" in response_get.content
    assert b"<!-- CONTAINER PROJECTS LISTING -->" in response_get.content
    assert b"List of existing projects" in response_get.content
    assert b"(4 projects)" in response_get.content
    assert b"<!-- CONTAINER PROJECTS LISTING - CONTENT -->" in response_get.content
    assert response_get.content.count(b'<div class="card" id="') == 4
    assert b'<div class="card" id="0a_INITIALIZATION_WITHOUT_MODELIZATION">' in response_get.content
    assert b'<div class="card" id="0e_CLUSTERING_PENDING">' in response_get.content
    assert b'<div class="card" id="1a_SAMPLING_TODO">' in response_get.content
    assert b'<div class="card" id="1k_ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS">' in response_get.content
    assert b"<!-- CONTAINER PROJECTS LISTING - CONTENT ACTIONS -->" in response_get.content
    assert b"Add new" in response_get.content
    assert b"Import" in response_get.content
    assert b"<!-- PROJECT CREATION POPUP -->" in response_get.content
    assert b"Create" in response_get.content
    assert b"<!-- PROJECT IMPORT POPUP -->" in response_get.content
    assert b"Import" in response_get.content
