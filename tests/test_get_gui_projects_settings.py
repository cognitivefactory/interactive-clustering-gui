# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_gui_projects_settings.py
* Description:  Unittests for `app` module on the `GET /gui/projects/{project_id}/settings` route.
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
async def test_ko_not_found(async_client):
    """
    Test the `GET /gui/projects/{project_id}/settings` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /gui/projects/{project_id}/settings` works.
    response_get = await async_client.get(url="/gui/projects/UNKNOWN_PROJECT/settings")
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 404
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER ERROR -->" in parsed_response_get
    assert "Error: 404" in parsed_response_get
    assert "The project with id 'UNKNOWN_PROJECT' doesn't exist." in parsed_response_get


# ==============================================================================
# test_ko_bad_iteration_id
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_iteration_id(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/settings` route with not existing iteration id.

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

    # Assert route `GET /gui/projects/{project_id}/settings` works.
    response_get = await async_client.get(
        url="/gui/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/settings?iteration_id=99"
    )
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 404
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER ERROR -->" in parsed_response_get
    assert "Error: 404" in parsed_response_get
    assert (
        "The project with id '0a_INITIALIZATION_WITHOUT_MODELIZATION' has no iteration with id '99'."
        in parsed_response_get
    )


# ==============================================================================
# test_ko_bad_settings_name
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_settings_name(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/settings` route with bad settings name.

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

    # Assert route `GET /gui/projects/{project_id}/settings` works.
    response_get = await async_client.get(
        url="/gui/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/settings?settings_names=UNKNOWN_SETTINGS"
    )
    assert response_get.status_code == 422


# ==============================================================================
# test_ok_default
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_default(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/settings` route.

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
            "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        ],
    )

    # Assert route `GET /gui/projects/{project_id}/settings` works.
    response_get = await async_client.get(url="/gui/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings")
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - TITLE -->" in parsed_response_get
    assert "Current iteration (2): Settings synthesis" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - SETTINGS -->" in parsed_response_get
    assert "<!-- CARD PREPROCESSING -->" in parsed_response_get
    assert "<!-- CARD VECTORIZATION -->" in parsed_response_get
    assert "<!-- CARD SAMPLING -->" in parsed_response_get
    assert "<!-- CARD CLUSTERING -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - ACTIONS NAVIGATION -->" in parsed_response_get


# ==============================================================================
# test_ok_with_iteration_id_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_with_iteration_id_1(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/settings` route.

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
            "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        ],
    )

    # Assert route `GET /gui/projects/{project_id}/settings` works.
    response_get = await async_client.get(
        url="/gui/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings?iteration_id=2"
    )
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - TITLE -->" in parsed_response_get
    assert "Current iteration (2): Settings synthesis" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - SETTINGS -->" in parsed_response_get
    assert "<!-- CARD PREPROCESSING -->" in parsed_response_get
    assert "<!-- CARD VECTORIZATION -->" in parsed_response_get
    assert "<!-- CARD SAMPLING -->" in parsed_response_get
    assert "<!-- CARD CLUSTERING -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - ACTIONS NAVIGATION -->" in parsed_response_get


# ==============================================================================
# test_ok_with_iteration_id_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_with_iteration_id_2(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/settings` route.

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
            "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        ],
    )

    # Assert route `GET /gui/projects/{project_id}/settings` works.
    response_get = await async_client.get(
        url="/gui/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings?iteration_id=0"
    )
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - TITLE -->" in parsed_response_get
    assert "Previous iteration (0): Settings synthesis" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - SETTINGS -->" in parsed_response_get
    assert "<!-- CARD PREPROCESSING -->" in parsed_response_get
    assert "<!-- CARD VECTORIZATION -->" in parsed_response_get
    assert "<!-- CARD SAMPLING -->" not in parsed_response_get
    assert "<!-- CARD CLUSTERING -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - ACTIONS NAVIGATION -->" in parsed_response_get


# ==============================================================================
# test_ok_with_settings_name
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_with_settings_name(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/settings` route.

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
            "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        ],
    )

    # Assert route `GET /gui/projects/{project_id}/settings` works.
    response_get = await async_client.get(
        url="/gui/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings?settings_names=preprocessing&settings_names=vectorization"
    )
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - TITLE -->" in parsed_response_get
    assert "Current iteration (2): Settings synthesis" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - SETTINGS -->" in parsed_response_get
    assert "<!-- CARD PREPROCESSING -->" in parsed_response_get
    assert "<!-- CARD VECTORIZATION -->" in parsed_response_get
    assert "<!-- CARD SAMPLING -->" not in parsed_response_get
    assert "<!-- CARD CLUSTERING -->" not in parsed_response_get
    assert "<!-- CONTAINER SETTINGS - ACTIONS NAVIGATION -->" in parsed_response_get
