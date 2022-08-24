# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_gui_projects_constraints.py
* Description:  Unittests for `app` module on the `GET /gui/projects/{project_id}/constraints` route.
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
    Test the `GET /gui/projects/{project_id}/constraints` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /gui/projects/{project_id}/constraints` works.
    response_get = await async_client.get(url="/gui/projects/UNKNOWN_PROJECT/constraints")
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
    Test the `GET /gui/projects/{project_id}/constraints` route.

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

    # Get constraints before test.
    response_get_constraints = await async_client.get(
        url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/constraints?without_hidden_constraints=true"
    )
    assert response_get_constraints.status_code == 200
    assert response_get_constraints.json()["constraints"] == {}  # noqa: WPS520

    # Assert route `GET /gui/projects/{project_id}/constraints` works.
    response_get = await async_client.get(url="/gui/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/constraints")
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - TITLE -->" in parsed_response_get
    assert "Iteration (0): Constraints synthesis" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - INFORMATIONS - PROJECT ID -->" in parsed_response_get
    assert "0a_INITIALIZATION_WITHOUT_MODELIZATION" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - INFORMATIONS - TEXTS -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - INFORMATIONS - CONSTRAINTS -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - INFORMATIONS - MODELIZATION -->" not in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - ACTIONS -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS LIST -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS LIST - TITLE -->" in parsed_response_get
    assert "List of constraints" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS LIST - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS LIST - CONSTRAINT TABLE -->" in parsed_response_get
    assert "<!-- CONSTRAINT " not in parsed_response_get


# ==============================================================================
# test_ok_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_2(async_client, tmp_path):
    """
    Test the `GET /gui/projects/{project_id}/constraints` route.

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
            "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        ],
    )

    # Get constraints before test.
    response_get_constraints = await async_client.get(
        url="/api/projects/1l_ANNOTATION_WITH_UPTODATE_MODELIZATION/constraints?without_hidden_constraints=true"
    )
    assert response_get_constraints.status_code == 200

    # Assert route `GET /gui/projects/{project_id}/constraints` works.
    response_get = await async_client.get(url="/gui/projects/1l_ANNOTATION_WITH_UPTODATE_MODELIZATION/constraints")
    parsed_response_get = html.unescape(bytes.decode(response_get.content, encoding="utf-8"))
    assert response_get.status_code == 200
    assert response_get.headers["content-type"] == "text/html; charset=utf-8"
    assert "<!-- HEAD -->" in parsed_response_get
    assert "<title>Interactive Clustering</title>" in parsed_response_get
    assert "<!-- BODY -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - TITLE -->" in parsed_response_get
    assert "Iteration (1): Constraints synthesis" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - INFORMATIONS - PROJECT ID -->" in parsed_response_get
    assert "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - INFORMATIONS - TEXTS -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - INFORMATIONS - CONSTRAINTS -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - INFORMATIONS - MODELIZATION -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS - ACTIONS -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS LIST -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS LIST - TITLE -->" in parsed_response_get
    assert "List of constraints" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS LIST - CONTENT -->" in parsed_response_get
    assert "<!-- CONTAINER CONSTRAINTS LIST - CONSTRAINT TABLE -->" in parsed_response_get
    assert parsed_response_get.count("<!-- CONSTRAINT ") == len(response_get_constraints.json()["constraints"].keys())
    for constraint_id in response_get_constraints.json()["constraints"].keys():
        assert "<!-- CONSTRAINT " + constraint_id + " -->" in parsed_response_get
        assert 'id="' + constraint_id + '">' in parsed_response_get
