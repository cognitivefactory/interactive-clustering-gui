# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_gui_projects_home.py
* Description:  Unittests for `app` module on the `GET /gui/projects/{project_id}` route.
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
# test_ko_not_found
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found(async_client):
    """
    Test the `GET /gui/projects/{project_id}` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /gui/projects` works.
    response_get = await async_client.get(url="/gui/projects/UNKNOWN_PROJECT")
    assert response_get.status_code == 404
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert b"<!-- HEAD -->" in response_get.content
    assert b"<title>Interactive Clustering</title>" in response_get.content
    assert b"<!-- BODY -->" in response_get.content
    assert b"<!-- CONTAINER ERROR -->" in response_get.content
    assert b"Error: 404" in response_get.content
    assert b"The project with id &#39;UNKNOWN_PROJECT&#39; doesn&#39;t exist." in response_get.content


# ==============================================================================
# test_ok_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_1(async_client, tmp_path):
    """
    Test the `GET /gui/projects` route.

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
    response_get = await async_client.get(url="/gui/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION")
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert b"<!-- HEAD -->" in response_get.content
    assert b"<title>Interactive Clustering</title>" in response_get.content
    assert b"<!-- BODY -->" in response_get.content
    assert b"<!-- CONTAINER PROJECT DESCRIPTION -->" in response_get.content
    assert b"Description and Settings" in response_get.content
    assert b"0a_INITIALIZATION_WITHOUT_MODELIZATION" in response_get.content
    assert b"Iteration (0): Main steps" in response_get.content
    assert b"<!-- CONTAINER ITERATION MAIN STEPS -->" in response_get.content
    assert b"<!-- INITIALIZE MODELIZATION -->" in response_get.content
    assert b"<!-- CONSTRAINTS SAMPLING -->" in response_get.content
    assert b"<!-- CONSTRAINTS ANNOTATION AND MODELIZATION -->" in response_get.content
    assert b"<!-- CONSTRAINED CLUSTERING -->" in response_get.content
    assert b"<!-- NEXT ITERATION CREATION -->" in response_get.content


# ==============================================================================
# test_ok_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_2(async_client, tmp_path):
    """
    Test the `GET /gui/projects` route.

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
            "0e_CLUSTERING_PENDING",
        ],
    )

    # Assert route `GET /gui/projects` works.
    response_get = await async_client.get(url="/gui/projects/0e_CLUSTERING_PENDING")
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert b"<!-- HEAD -->" in response_get.content
    assert b"<title>Interactive Clustering</title>" in response_get.content
    assert b"<!-- BODY -->" in response_get.content
    assert b"<!-- CONTAINER PROJECT DESCRIPTION -->" in response_get.content
    assert b"Description and Settings" in response_get.content
    assert b"0e_CLUSTERING_PENDING" in response_get.content
    assert b"Iteration (0): Main steps" in response_get.content
    assert b"<!-- CONTAINER ITERATION MAIN STEPS -->" in response_get.content
    assert b"<!-- INITIALIZE MODELIZATION -->" in response_get.content
    assert b"<!-- CONSTRAINTS SAMPLING -->" in response_get.content
    assert b"<!-- CONSTRAINTS ANNOTATION AND MODELIZATION -->" in response_get.content
    assert b"<!-- CONSTRAINED CLUSTERING -->" in response_get.content
    assert b"<!-- NEXT ITERATION CREATION -->" in response_get.content


# ==============================================================================
# test_ok_3
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_3(async_client, tmp_path):
    """
    Test the `GET /gui/projects` route.

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

    # Assert route `GET /gui/projects` works.
    response_get = await async_client.get(url="/gui/projects/1a_SAMPLING_TODO")
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert b"<!-- HEAD -->" in response_get.content
    assert b"<title>Interactive Clustering</title>" in response_get.content
    assert b"<!-- BODY -->" in response_get.content
    assert b"<!-- CONTAINER PROJECT DESCRIPTION -->" in response_get.content
    assert b"Description and Settings" in response_get.content
    assert b"1a_SAMPLING_TODO" in response_get.content
    assert b"Iteration (1): Main steps" in response_get.content
    assert b"<!-- CONTAINER ITERATION MAIN STEPS -->" in response_get.content
    assert b"<!-- INITIALIZE MODELIZATION -->" in response_get.content
    assert b"<!-- CONSTRAINTS SAMPLING -->" in response_get.content
    assert b"<!-- CONSTRAINTS ANNOTATION AND MODELIZATION -->" in response_get.content
    assert b"<!-- CONSTRAINED CLUSTERING -->" in response_get.content
    assert b"<!-- NEXT ITERATION CREATION -->" in response_get.content


# ==============================================================================
# test_ok_4
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_4(async_client, tmp_path):
    """
    Test the `GET /gui/projects` route.

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
            "1k_ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS",
        ],
    )

    # Assert route `GET /gui/projects` works.
    response_get = await async_client.get(url="/gui/projects/1k_ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS")
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert b"<!-- HEAD -->" in response_get.content
    assert b"<title>Interactive Clustering</title>" in response_get.content
    assert b"<!-- BODY -->" in response_get.content
    assert b"<!-- CONTAINER PROJECT DESCRIPTION -->" in response_get.content
    assert b"Description and Settings" in response_get.content
    assert b"1k_ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS" in response_get.content
    assert b"Iteration (1): Main steps" in response_get.content
    assert b"<!-- CONTAINER ITERATION MAIN STEPS -->" in response_get.content
    assert b"<!-- INITIALIZE MODELIZATION -->" in response_get.content
    assert b"<!-- CONSTRAINTS SAMPLING -->" in response_get.content
    assert b"<!-- CONSTRAINTS ANNOTATION AND MODELIZATION -->" in response_get.content
    assert b"<!-- CONSTRAINED CLUSTERING -->" in response_get.content
    assert b"<!-- NEXT ITERATION CREATION -->" in response_get.content
