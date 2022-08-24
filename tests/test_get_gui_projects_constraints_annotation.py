# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_gui_projects_constraints_annotation.py
* Description:  Unittests for `app` module on the `GET /gui/projects/{project_id}/constraints/{constraint_id}/{constraint_id}` route.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import html

import pytest

from tests.dummies_utils import create_dummy_projects

# ==============================================================================
# test_ko_not_found
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_not_found_1(async_client):
    """
    Test the `GET /gui/projects/{project_id}/constraints/{constraint_id}` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /gui/projects/{project_id}/constraints/{constraint_id}` works.
    response_get = await async_client.get(url="/gui/projects/UNKNOWN_PROJECT/constraints/UNKNOWN_CONSTRAINT")
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    # assert response_get.status_code == 404
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER ERROR -->" in parsed_response_get
    assert "Error: 404" in parsed_response_get
    assert "The project with id 'UNKNOWN_PROJECT' doesn't exist." in parsed_response_get


@pytest.mark.asyncio()
async def test_ko_not_found_2(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/constraints/{constraint_id}` route with not existing constraint.

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
            "0g_ITERATION_END",
        ],
    )

    # Assert route `GET /gui/projects/{project_id}/constraints/{constraint_id}` works.
    response_get = await async_client.get(url="/gui/projects/0g_ITERATION_END/constraints/UNKNOWN_CONSTRAINT")
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER ERROR -->" in parsed_response_get
    assert "Error: 404" in parsed_response_get
    assert (
        "In project with id '0g_ITERATION_END', the constraint with id 'UNKNOWN_CONSTRAINT' to annotate doesn't exist."
        in parsed_response_get
    )


# ==============================================================================
# test_ok_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_1(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/constraints/{constraint_id}` route.

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

    # Assert route `GET /gui/projects/{project_id}/constraints/{constraint_id}` works.
    response_get = await async_client.get(
        url="/gui/projects/1d_ANNOTATION_WITH_UPTODATE_MODELIZATION/constraints/(0,4)"
    )
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - TITLE -->" in parsed_response_get
    assert 'id="(0,4)"' in parsed_response_get
    assert "Iteration (1): Annotations" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - TEXTS -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - ACTIONS ANNOTATION -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - ACTIONS COMMENT/REVIEW -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - DETAILS -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - DETAILS CARD DESCRIPTION -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - DETAILS CARD LOCAL GRAPH -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - ACTIONS NAVIGATION -->" in parsed_response_get


# ==============================================================================
# test_ok_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_2(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/constraints/{constraint_id}` route.

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

    # Assert route `GET /gui/projects/{project_id}/constraints/{constraint_id}` works.
    response_get = await async_client.get(url="/gui/projects/1m_CLUSTERING_TODO/constraints/(14,9)")
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert 'id="(14,9)"' in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - TITLE -->" in parsed_response_get
    assert "Iteration (1): Annotations" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - TEXTS -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - ACTIONS ANNOTATION -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - ACTIONS COMMENT/REVIEW -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - DETAILS -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - DETAILS CARD DESCRIPTION -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - DETAILS CARD LOCAL GRAPH -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - ACTIONS NAVIGATION -->" in parsed_response_get


# ==============================================================================
# test_ok_3
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_3(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/constraints/{constraint_id}` route.

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
            "1p_ITERATION_END",
        ],
    )

    # Assert route `GET /gui/projects/{project_id}/constraints/{constraint_id}` works.
    response_get = await async_client.get(url="/gui/projects/1p_ITERATION_END/constraints/(18,8)")
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert 'id="(18,8)"' in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - TITLE -->" in parsed_response_get
    assert "Iteration (1): Annotations" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - TEXTS -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - ACTIONS ANNOTATION -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - ACTIONS COMMENT/REVIEW -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - DETAILS -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - DETAILS CARD DESCRIPTION -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - DETAILS CARD LOCAL GRAPH -->" in parsed_response_get
    assert "<!-- CONTAINER ANNOTATION - ACTIONS NAVIGATION -->" in parsed_response_get
