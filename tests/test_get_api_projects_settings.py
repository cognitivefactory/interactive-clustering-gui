# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_api_projects_settings.py
* Description:  Unittests for `app` module on the `GET /api/projects/{project_id}/settings` route.
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
    Test the `GET /api/projects/{project_id}/settings` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /api/projects/{project_id}/settings` works.
    response_get = await async_client.get(url="/api/projects/UNKNOWN_PROJECT/settings")
    assert response_get.status_code == 404
    assert response_get.json() == {
        "detail": "The project with id 'UNKNOWN_PROJECT' doesn't exist.",
    }


# ==============================================================================
# test_ko_bad_iteration_id
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_iteration_id(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/settings` route with not existing iteration id.

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

    # Assert route `GET /api/projects/{project_id}/settings` works.
    response_get = await async_client.get(
        url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/settings?iteration_id=99"
    )
    assert response_get.status_code == 404
    assert response_get.json() == {
        "detail": "The project with id '0a_INITIALIZATION_WITHOUT_MODELIZATION' has no iteration with id '99'.",
    }


# ==============================================================================
# test_ko_bad_settings_name
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_settings_name(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/settings` route with bad settings name.

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

    # Assert route `GET /api/projects/{project_id}/settings` works.
    response_get = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings?settings_names=UNKNOWN_SETTINGS"
    )
    assert response_get.status_code == 422


# ==============================================================================
# test_ok_default
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_default(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/settings` route with some projects.

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

    # Assert route `GET /api/projects/{project_id}/settings` works.
    response_get = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings")
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "iteration_id", "parameters", "settings"]
    assert response_get.json() == {
        "project_id": "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "iteration_id": 2,
        "parameters": {"settings_names": ["preprocessing", "vectorization", "sampling", "clustering"]},
        "settings": {
            "sampling": {
                "algorithm": "custom",
                "random_seed": 42,
                "nb_to_select": 999,
                "init_kargs": {
                    "clusters_restriction": "same_cluster",
                    "distance_restriction": "closest_neighbors",
                    "without_inferred_constraints": True,
                },
            },
            "preprocessing": {
                "apply_stopwords_deletion": False,
                "apply_parsing_filter": False,
                "apply_lemmatization": False,
                "spacy_language_model": "fr_core_news_md",
            },
            "vectorization": {"vectorizer_type": "tfidf", "spacy_language_model": None, "random_seed": 42},
            "clustering": {
                "algorithm": "kmeans",
                "random_seed": 42,
                "nb_clusters": 3,
                "init_kargs": {"model": "COP", "max_iteration": 150, "tolerance": 0.0001},
            },
        },
    }

    # Assert file content is the same.
    with open(tmp_path / "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION" / "settings.json", "r") as settings_fileobject:
        assert response_get.json()["settings"] == json.load(settings_fileobject)["2"]


# ==============================================================================
# test_ok_with_iteration_id_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_with_iteration_id_1(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/settings` route with some projects.

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

    # Assert route `GET /api/projects/{project_id}/settings` works.
    response_get = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings?iteration_id=2"
    )
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "iteration_id", "parameters", "settings"]
    assert response_get.json() == {
        "project_id": "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "iteration_id": 2,
        "parameters": {"settings_names": ["preprocessing", "vectorization", "sampling", "clustering"]},
        "settings": {
            "sampling": {
                "algorithm": "custom",
                "random_seed": 42,
                "nb_to_select": 999,
                "init_kargs": {
                    "clusters_restriction": "same_cluster",
                    "distance_restriction": "closest_neighbors",
                    "without_inferred_constraints": True,
                },
            },
            "preprocessing": {
                "apply_stopwords_deletion": False,
                "apply_parsing_filter": False,
                "apply_lemmatization": False,
                "spacy_language_model": "fr_core_news_md",
            },
            "vectorization": {"vectorizer_type": "tfidf", "spacy_language_model": None, "random_seed": 42},
            "clustering": {
                "algorithm": "kmeans",
                "random_seed": 42,
                "nb_clusters": 3,
                "init_kargs": {"model": "COP", "max_iteration": 150, "tolerance": 0.0001},
            },
        },
    }

    # Assert file content is the same.
    with open(tmp_path / "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION" / "settings.json", "r") as settings_fileobject:
        assert response_get.json()["settings"] == json.load(settings_fileobject)["2"]


# ==============================================================================
# test_ok_with_iteration_id_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_with_iteration_id_2(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/settings` route with some projects.

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

    # Assert route `GET /api/projects/{project_id}/settings` works.
    response_get = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings?iteration_id=0"
    )
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "iteration_id", "parameters", "settings"]
    assert response_get.json() == {
        "project_id": "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "iteration_id": 0,
        "parameters": {"settings_names": ["preprocessing", "vectorization", "sampling", "clustering"]},
        "settings": {
            "preprocessing": {
                "apply_stopwords_deletion": False,
                "apply_parsing_filter": False,
                "apply_lemmatization": False,
                "spacy_language_model": "fr_core_news_md",
            },
            "vectorization": {"vectorizer_type": "tfidf", "spacy_language_model": None, "random_seed": 42},
            "clustering": {
                "algorithm": "kmeans",
                "random_seed": 42,
                "nb_clusters": 3,
                "init_kargs": {"model": "COP", "max_iteration": 150, "tolerance": 0.0001},
            },
        },
    }

    # Assert file content is the same.
    with open(tmp_path / "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION" / "settings.json", "r") as settings_fileobject:
        assert response_get.json()["settings"] == json.load(settings_fileobject)["0"]


# ==============================================================================
# test_ok_with_settings_name
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_with_settings_name(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/settings` route with some projects.

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

    # Assert route `GET /api/projects/{project_id}/settings` works.
    response_get = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings?settings_names=preprocessing&settings_names=vectorization"
    )
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "iteration_id", "parameters", "settings"]
    assert response_get.json() == {
        "project_id": "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "iteration_id": 2,
        "parameters": {"settings_names": ["preprocessing", "vectorization"]},
        "settings": {
            "preprocessing": {
                "apply_stopwords_deletion": False,
                "apply_parsing_filter": False,
                "apply_lemmatization": False,
                "spacy_language_model": "fr_core_news_md",
            },
            "vectorization": {"vectorizer_type": "tfidf", "spacy_language_model": None, "random_seed": 42},
        },
    }

    # Assert file content is the same.
    with open(tmp_path / "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION" / "settings.json", "r") as settings_fileobject:
        project_settings = json.load(settings_fileobject)["2"]
        assert response_get.json()["settings"]["preprocessing"] == project_settings["preprocessing"]
        assert response_get.json()["settings"]["vectorization"] == project_settings["vectorization"]
