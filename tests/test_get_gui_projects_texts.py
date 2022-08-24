# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_gui_projects_texts.py
* Description:  Unittests for `app` module on the `GET /gui/projects/{project_id}/texts` route.
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
    Test the `GET /gui/projects/{project_id}/texts` route.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /gui/projects/{project_id}/texts` works.
    response_get = await async_client.get(url="/gui/projects/UNKNOWN_PROJECT/texts")
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
# test_ok_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_1(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/texts` route.

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

    # Get texts before test.
    response_get_texts = await async_client.get(
        url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/texts?without_deleted_texts=false"
    )
    assert response_get_texts.status_code == 200

    # Assert route `GET /gui/projects/{project_id}/texts` works.
    response_get = await async_client.get(url="/gui/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/texts")
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS - TITLE -->" in parsed_response_get
    assert "Iteration (0): Texts synthesis" in parsed_response_get
    assert "<!-- CONTAINER TEXTS - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS - INFORMATIONS - PROJECT ID -->" in parsed_response_get
    assert "0a_INITIALIZATION_WITHOUT_MODELIZATION" in parsed_response_get
    assert "<!-- CONTAINER TEXTS - INFORMATIONS - TEXTS -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS - INFORMATIONS - CONSTRAINTS -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS - INFORMATIONS - MODELIZATION -->" not in parsed_response_get
    assert "<!-- CONTAINER TEXTS - ACTIONS -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS LIST -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS LIST - TITLE -->" in parsed_response_get
    assert "List of texts" in parsed_response_get
    assert "<!-- CONTAINER TEXTS LIST - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS LIST - TEXT TABLE -->" in parsed_response_get
    for text_id, text_value in response_get_texts.json()["texts"].items():
        assert "<!-- TEXT " + text_id + " -->" in parsed_response_get
        assert 'id="' + text_id + '">' in parsed_response_get
        assert text_value["text_preprocessed"] in parsed_response_get


# ==============================================================================
# test_ok_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_2(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/texts` route.

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

    # Get texts before test.
    response_get_texts = await async_client.get(
        url="/api/projects/0e_CLUSTERING_PENDING/texts?without_deleted_texts=false"
    )
    assert response_get_texts.status_code == 200

    # Assert route `GET /gui/projects/{project_id}/texts` works.
    response_get = await async_client.get(url="/gui/projects/0e_CLUSTERING_PENDING/texts")
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- CONTAINER TEXTS -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS - TITLE -->" in parsed_response_get
    assert "Iteration (0): Texts synthesis" in parsed_response_get
    assert "<!-- CONTAINER TEXTS - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS - INFORMATIONS - PROJECT ID -->" in parsed_response_get
    assert "0e_CLUSTERING_PENDING" in parsed_response_get
    assert "<!-- CONTAINER TEXTS - INFORMATIONS - TEXTS -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS - INFORMATIONS - CONSTRAINTS -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS - INFORMATIONS - MODELIZATION -->" not in parsed_response_get
    assert "<!-- CONTAINER TEXTS - ACTIONS -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS LIST -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS LIST - TITLE -->" in parsed_response_get
    assert "List of texts" in parsed_response_get
    assert "<!-- CONTAINER TEXTS LIST - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER TEXTS LIST - TEXT TABLE -->" in parsed_response_get
    assert parsed_response_get.count("<!-- TEXT ") == len(response_get_texts.json()["texts"].keys())
    for text_id, text_value in response_get_texts.json()["texts"].items():
        assert "<!-- TEXT " + text_id + " -->" in parsed_response_get
        assert 'id="' + text_id + '">' in parsed_response_get
        assert text_value["text_preprocessed"] in parsed_response_get
