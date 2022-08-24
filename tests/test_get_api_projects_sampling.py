# -*- coding: utf-8 -*-

"""
* Name:         interactive-sampling-gui/tests/test_get_api_projects_sampling.py
* Description:  Unittests for `app` module on the `GET /api/projects/{project_id}/sampling/{iteration_id}` route.
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
    Test the `GET /api/projects/{project_id}/sampling` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /api/projects/{project_id}/sampling` works.
    response_get = await async_client.get(url="/api/projects/UNKNOWN_PROJECT/sampling")
    assert response_get.status_code == 404
    assert response_get.json() == {
        "detail": "The project with id 'UNKNOWN_PROJECT' doesn't exist.",
    }


# ==============================================================================
# test_ko_bad_iteration_id_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_iteration_id_1(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/sampling` route with not existing project.

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
            "0d_CLUSTERING_TODO",
        ],
    )

    # Assert route `GET /api/projects/{project_id}/sampling` works.
    response_get = await async_client.get(url="/api/projects/0d_CLUSTERING_TODO/sampling")
    assert response_get.status_code == 403
    assert response_get.json() == {
        "detail": "The iteration `0` has no sampling step.",
    }


# ==============================================================================
# test_ko_bad_iteration_id_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_iteration_id_2(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/sampling` route with not existing project.

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

    # Assert route `GET /api/projects/{project_id}/sampling` works.
    response_get = await async_client.get(url="/api/projects/1a_SAMPLING_TODO/sampling?iteration_id=0")
    assert response_get.status_code == 403
    assert response_get.json() == {
        "detail": "The iteration `0` has no sampling step.",
    }


# ==============================================================================
# test_ko_bad_iteration_id_3
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_iteration_id_3(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/sampling` route with not existing project.

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

    # Assert route `GET /api/projects/{project_id}/sampling` works.
    response_get = await async_client.get(
        url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/sampling?iteration_id=99"
    )
    assert response_get.status_code == 404
    assert response_get.json() == {
        "detail": "The project with id '0a_INITIALIZATION_WITHOUT_MODELIZATION' has no iteration with id '99'.",
    }


# ==============================================================================
# test_ko_bad_iteration_id_4
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_iteration_id_4(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/sampling` route with not existing project.

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

    # Assert route `GET /api/projects/{project_id}/sampling` works.
    response_get = await async_client.get(url="/api/projects/1a_SAMPLING_TODO/sampling?iteration_id=1")
    assert response_get.status_code == 403
    assert response_get.json() == {
        "detail": "The project with id '1a_SAMPLING_TODO' hasn't completed its sampling step on iteration '1'.",
    }


# ==============================================================================
# test_ok_default_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_default_1(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/sampling` route with some projects.

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
            "2a_SAMPLING_TODO",
        ],
    )

    # Assert route `GET /api/projects/{project_id}/sampling` works.
    response_get = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/sampling")
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "iteration_id", "sampling"]
    assert response_get.json() == {
        "project_id": "2a_SAMPLING_TODO",
        "iteration_id": 1,
        "sampling": [
            "(0,4)",
            "(12,9)",
            "(10,9)",
            "(1,2)",
            "(14,9)",
            "(22,6)",
            "(20,22)",
            "(1,3)",
            "(4,7)",
            "(21,22)",
            "(11,12)",
            "(10,11)",
            "(1,6)",
            "(2,4)",
            "(8,9)",
            "(17,22)",
            "(19,22)",
            "(1,7)",
            "(22,8)",
            "(18,22)",
            "(11,14)",
            "(15,16)",
            "(13,16)",
            "(4,6)",
            "(18,8)",
        ],
    }

    # Assert file content is the same.
    with open(tmp_path / "2a_SAMPLING_TODO" / "sampling.json", "r") as sampling_fileobject:
        assert response_get.json()["sampling"] == json.load(sampling_fileobject)["1"]


# ==============================================================================
# test_ok_default_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_default_2(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/sampling` route with some projects.

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

    # Assert route `GET /api/projects/{project_id}/sampling` works.
    response_get = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/sampling")
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "iteration_id", "sampling"]
    assert response_get.json() == {
        "project_id": "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "iteration_id": 2,
        "sampling": [
            "(10,14)",
            "(2,7)",
            "(11,9)",
            "(18,20)",
            "(13,15)",
            "(17,23)",
            "(10,12)",
            "(17,19)",
            "(12,14)",
            "(0,7)",
            "(16,21)",
            "(12,13)",
            "(16,6)",
            "(19,20)",
            "(17,21)",
            "(21,23)",
            "(19,3)",
            "(11,5)",
            "(16,23)",
            "(19,21)",
            "(2,3)",
            "(10,15)",
            "(0,2)",
            "(16,18)",
            "(10,8)",
            "(20,6)",
            "(1,5)",
            "(18,21)",
            "(12,8)",
            "(14,8)",
            "(20,21)",
            "(15,8)",
            "(18,19)",
            "(19,23)",
            "(3,6)",
            "(17,18)",
            "(12,15)",
            "(17,20)",
            "(4,5)",
            "(22,5)",
            "(18,6)",
            "(17,3)",
            "(10,13)",
            "(5,9)",
            "(2,6)",
            "(11,4)",
            "(11,22)",
            "(14,15)",
            "(13,14)",
            "(18,3)",
            "(21,3)",
            "(20,3)",
            "(22,9)",
            "(16,3)",
            "(13,8)",
            "(19,7)",
            "(23,3)",
            "(19,2)",
            "(16,17)",
            "(21,6)",
            "(21,7)",
            "(16,19)",
            "(16,7)",
            "(18,7)",
            "(2,21)",
            "(20,7)",
            "(16,2)",
            "(18,2)",
            "(3,7)",
            "(23,6)",
            "(2,20)",
            "(23,7)",
            "(1,11)",
            "(1,22)",
            "(2,23)",
            "(16,20)",
            "(17,6)",
            "(17,7)",
            "(1,9)",
            "(19,6)",
            "(18,23)",
            "(17,2)",
            "(6,7)",
            "(20,23)",
            "(0,19)",
            "(1,4)",
            "(22,4)",
            "(0,3)",
            "(0,6)",
            "(0,16)",
            "(0,17)",
            "(0,18)",
            "(0,20)",
            "(0,21)",
            "(0,23)",
            "(4,9)",
            "(3,5)",
            "(0,13)",
            "(13,5)",
            "(12,9)",
            "(11,20)",
            "(1,23)",
            "(2,5)",
            "(11,17)",
            "(12,3)",
            "(21,9)",
            "(0,14)",
            "(11,18)",
            "(13,7)",
            "(16,8)",
            "(17,5)",
            "(1,19)",
            "(11,14)",
            "(23,4)",
            "(1,18)",
            "(16,9)",
            "(1,2)",
            "(10,23)",
            "(1,3)",
            "(10,17)",
            "(13,23)",
            "(5,6)",
            "(20,22)",
            "(0,12)",
            "(15,22)",
            "(11,23)",
            "(13,2)",
            "(1,10)",
            "(10,22)",
            "(13,6)",
            "(7,9)",
            "(14,7)",
            "(14,5)",
            "(10,18)",
            "(13,16)",
            "(15,16)",
            "(14,21)",
            "(7,8)",
            "(18,9)",
            "(14,9)",
            "(10,19)",
            "(1,20)",
            "(10,20)",
            "(10,16)",
            "(14,23)",
            "(5,7)",
            "(15,9)",
            "(15,4)",
            "(14,17)",
            "(14,2)",
            "(12,23)",
            "(12,2)",
            "(17,4)",
            "(5,8)",
            "(15,6)",
            "(3,4)",
            "(15,5)",
            "(0,15)",
            "(0,9)",
            "(10,5)",
            "(11,6)",
            "(22,8)",
            "(2,22)",
            "(14,19)",
            "(21,22)",
            "(18,22)",
            "(1,15)",
            "(19,4)",
            "(1,14)",
            "(4,6)",
            "(14,6)",
            "(13,18)",
            "(11,15)",
            "(13,22)",
            "(14,22)",
            "(15,7)",
            "(18,4)",
            "(12,17)",
            "(23,8)",
            "(1,7)",
            "(20,5)",
            "(20,8)",
            "(14,20)",
            "(11,2)",
            "(15,18)",
            "(4,7)",
            "(1,8)",
            "(20,9)",
            "(21,4)",
            "(15,3)",
            "(0,1)",
            "(12,6)",
            "(13,20)",
            "(21,8)",
            "(12,7)",
            "(1,12)",
            "(12,21)",
            "(15,23)",
            "(15,19)",
            "(17,22)",
            "(1,17)",
            "(11,13)",
            "(10,6)",
            "(11,21)",
            "(10,2)",
            "(22,6)",
            "(14,18)",
            "(15,17)",
            "(11,3)",
            "(19,5)",
            "(8,9)",
            "(15,20)",
            "(15,21)",
            "(12,20)",
            "(2,4)",
            "(18,8)",
            "(0,8)",
            "(6,8)",
            "(0,11)",
            "(10,21)",
            "(15,2)",
            "(12,18)",
            "(13,3)",
            "(13,21)",
            "(3,8)",
            "(0,22)",
            "(12,22)",
            "(14,16)",
            "(1,6)",
            "(11,12)",
            "(19,8)",
            "(2,9)",
            "(11,8)",
            "(13,17)",
            "(23,9)",
            "(22,7)",
            "(16,22)",
            "(0,5)",
            "(11,16)",
            "(1,16)",
            "(10,9)",
            "(16,4)",
            "(3,9)",
            "(0,4)",
            "(17,8)",
            "(10,4)",
            "(10,7)",
            "(13,4)",
            "(22,3)",
            "(14,4)",
            "(23,5)",
            "(1,13)",
            "(18,5)",
            "(1,21)",
            "(4,8)",
            "(19,22)",
            "(14,3)",
            "(11,7)",
            "(10,3)",
            "(6,9)",
            "(21,5)",
            "(12,16)",
            "(13,19)",
            "(12,19)",
            "(2,8)",
            "(10,11)",
            "(11,19)",
            "(13,9)",
            "(19,9)",
            "(20,4)",
            "(12,4)",
            "(0,10)",
            "(12,5)",
            "(16,5)",
            "(17,9)",
            "(22,23)",
        ],
    }

    # Assert file content is the same.
    with open(tmp_path / "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION" / "sampling.json", "r") as sampling_fileobject:
        assert response_get.json()["sampling"] == json.load(sampling_fileobject)["2"]


# ==============================================================================
# test_ok_with_iteration_id
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_with_iteration_id(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/sampling` route with some projects.

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

    # Assert route `GET /api/projects/{project_id}/sampling` works.
    response_get = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/sampling?iteration_id=1"
    )
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "iteration_id", "sampling"]
    assert response_get.json() == {
        "project_id": "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "iteration_id": 1,
        "sampling": [
            "(0,4)",
            "(12,9)",
            "(10,9)",
            "(1,2)",
            "(14,9)",
            "(22,6)",
            "(20,22)",
            "(1,3)",
            "(4,7)",
            "(21,22)",
            "(11,12)",
            "(10,11)",
            "(1,6)",
            "(2,4)",
            "(8,9)",
            "(17,22)",
            "(19,22)",
            "(1,7)",
            "(22,8)",
            "(18,22)",
            "(11,14)",
            "(15,16)",
            "(13,16)",
            "(4,6)",
            "(18,8)",
        ],
    }

    # Assert file content is the same.
    with open(tmp_path / "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION" / "sampling.json", "r") as sampling_fileobject:
        assert response_get.json()["sampling"] == json.load(sampling_fileobject)["1"]
