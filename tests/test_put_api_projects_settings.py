# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_put_api_projects_settings.py
* Description:  Unittests for `app` module on the `PUT /api/projects/{project_id}/settings` route.
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
    Test the `PUT /api/projects/{project_id}/settings` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/UNKNOWN_PROJECT/settings",
    )
    assert response_put.status_code == 404
    assert response_put.json() == {
        "detail": "The project with id 'UNKNOWN_PROJECT' doesn't exist.",
    }


# ==============================================================================
# test_ko_preprocessing_bad_state
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_preprocessing_bad_state(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route with bad state.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(url="/api/projects/1a_SAMPLING_TODO/settings")
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/1a_SAMPLING_TODO/settings",
        json={
            "preprocessing": {
                "apply_stopwords_deletion": True,
                "apply_parsing_filter": True,
                "apply_lemmatization": True,
                "spacy_language_model": "fr_core_news_md",
            }
        },
    )
    assert response_put.status_code == 403
    assert response_put.json() == {
        "detail": "The 'preprocessing' settings of project with id '1a_SAMPLING_TODO' cant't be modified during this state (state='SAMPLING_TODO'). No changes have been taken into account.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/1a_SAMPLING_TODO/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "SAMPLING_TODO"
    # Assert route `GET /api/projects/{project_id}/settings` is still the same.
    response_get_settings_after = await async_client.get(url="/api/projects/1a_SAMPLING_TODO/settings")
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json() == response_get_settings_before.json()


# ==============================================================================
# test_ko_vectorization_bad_state
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_vectorization_bad_state(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route with bad state.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(url="/api/projects/1a_SAMPLING_TODO/settings")
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/1a_SAMPLING_TODO/settings",
        json={
            "vectorization": {"vectorizer_type": "spacy", "spacy_language_model": "fr_core_news_md", "random_seed": 88}
        },
    )
    assert response_put.status_code == 403
    assert response_put.json() == {
        "detail": "The 'vectorization' settings of project with id '1a_SAMPLING_TODO' cant't be modified during this state (state='SAMPLING_TODO'). No changes have been taken into account.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/1a_SAMPLING_TODO/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "SAMPLING_TODO"
    # Assert route `GET /api/projects/{project_id}/settings` is still the same.
    response_get_settings_after = await async_client.get(url="/api/projects/1a_SAMPLING_TODO/settings")
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json() == response_get_settings_before.json()


# ==============================================================================
# test_ko_sampling_bad_state
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_sampling_bad_state(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route with bad state.

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
            "1b_SAMPLING_PENDING",
        ],
    )

    # Get settings before test.
    response_get_settings_before = await async_client.get(url="/api/projects/1b_SAMPLING_PENDING/settings")
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/1b_SAMPLING_PENDING/settings",
        json={"sampling": {"algorithm": "random", "random_seed": 88, "nb_to_select": 10}},
    )
    assert response_put.status_code == 403
    assert response_put.json() == {
        "detail": "The 'sampling' settings of project with id '1b_SAMPLING_PENDING' cant't be modified during this state (state='SAMPLING_PENDING'). No changes have been taken into account.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/1b_SAMPLING_PENDING/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "SAMPLING_PENDING"
    # Assert route `GET /api/projects/{project_id}/settings` is still the same.
    response_get_settings_after = await async_client.get(url="/api/projects/1b_SAMPLING_PENDING/settings")
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json() == response_get_settings_before.json()


# ==============================================================================
# test_ko_clustering_bad_state
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_clustering_bad_state(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route with bad state.

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
            "1n_CLUSTERING_PENDING",
        ],
    )

    # Get settings before test.
    response_get_settings_before = await async_client.get(url="/api/projects/1n_CLUSTERING_PENDING/settings")
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/1n_CLUSTERING_PENDING/settings",
        json={
            "clustering": {
                "algorithm": "hierarchical",
                "random_seed": 41,
                "nb_clusters": 3,
                "init_kargs": {"linkage": "complete"},
            }
        },
    )
    assert response_put.status_code == 403
    assert response_put.json() == {
        "detail": "The 'clustering' settings of project with id '1n_CLUSTERING_PENDING' cant't be modified during this state (state='CLUSTERING_PENDING'). No changes have been taken into account.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/1n_CLUSTERING_PENDING/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 1
    assert response_get.json()["status"]["state"] == "CLUSTERING_PENDING"
    # Assert route `GET /api/projects/{project_id}/settings` is still the same.
    response_get_settings_after = await async_client.get(url="/api/projects/1n_CLUSTERING_PENDING/settings")
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json() == response_get_settings_before.json()


# ==============================================================================
# test_ko_preprocessing_bad_value
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_preprocessing_bad_value(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route with bad value.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_1 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "preprocessing": {
                "apply_stopwords_deletion": "UNKNOWN",
                "apply_parsing_filter": True,
                "apply_lemmatization": True,
                "spacy_language_model": "fr_core_news_md",
            }
        },
    )
    assert response_put_1.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_2 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "preprocessing": {
                "apply_stopwords_deletion": True,
                "apply_parsing_filter": "UNKNOWN",
                "apply_lemmatization": True,
                "spacy_language_model": "fr_core_news_md",
            }
        },
    )
    assert response_put_2.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_3 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "preprocessing": {
                "apply_stopwords_deletion": True,
                "apply_parsing_filter": True,
                "apply_lemmatization": "UNKNOWN",
                "spacy_language_model": "fr_core_news_md",
            }
        },
    )
    assert response_put_3.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_4 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "preprocessing": {
                "apply_stopwords_deletion": True,
                "apply_parsing_filter": True,
                "apply_lemmatization": True,
                "spacy_language_model": "UNKNOWN",
            }
        },
    )
    assert response_put_4.status_code == 422
    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 2
    assert response_get.json()["status"]["state"] == "ANNOTATION_WITH_UPTODATE_MODELIZATION"
    # Assert route `GET /api/projects/{project_id}/settings` is still the same.
    response_get_settings_after = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json() == response_get_settings_before.json()


# ==============================================================================
# test_ko_preprocessing_missing_value
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_preprocessing_missing_value(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route with missing value.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_1 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "preprocessing": {
                "apply_parsing_filter": True,
                "apply_lemmatization": True,
                "spacy_language_model": "fr_core_news_md",
            }
        },
    )
    assert response_put_1.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_2 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "preprocessing": {
                "apply_stopwords_deletion": True,
                "apply_lemmatization": True,
                "spacy_language_model": "fr_core_news_md",
            }
        },
    )
    assert response_put_2.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_3 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "preprocessing": {
                "apply_stopwords_deletion": True,
                "apply_parsing_filter": True,
                "spacy_language_model": "fr_core_news_md",
            }
        },
    )
    assert response_put_3.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_4 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "preprocessing": {
                "apply_stopwords_deletion": True,
                "apply_parsing_filter": True,
                "apply_lemmatization": True,
            }
        },
    )
    assert response_put_4.status_code == 422
    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 2
    assert response_get.json()["status"]["state"] == "ANNOTATION_WITH_UPTODATE_MODELIZATION"
    # Assert route `GET /api/projects/{project_id}/settings` is still the same.
    response_get_settings_after = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json() == response_get_settings_before.json()


# ==============================================================================
# test_ko_vectorization_bad_value
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_vectorization_bad_value(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route with bad value.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_1 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "vectorization": {
                "vectorizer_type": "UNKNOWN",
                "spacy_language_model": "fr_core_news_md",
                "random_seed": 88,
            }
        },
    )
    assert response_put_1.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_2 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"vectorization": {"vectorizer_type": "spacy", "spacy_language_model": "UNKNOWN", "random_seed": 88}},
    )
    assert response_put_2.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_3 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "vectorization": {"vectorizer_type": "tfidf", "spacy_language_model": "fr_core_news_md", "random_seed": 88}
        },
    )
    assert response_put_3.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_4 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"vectorization": {"vectorizer_type": "tfidf", "random_seed": -99}},
    )
    assert response_put_4.status_code == 422
    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 2
    assert response_get.json()["status"]["state"] == "ANNOTATION_WITH_UPTODATE_MODELIZATION"
    # Assert route `GET /api/projects/{project_id}/settings` is still the same.
    response_get_settings_after = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json() == response_get_settings_before.json()


# ==============================================================================
# test_ko_vectorization_missing_value
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_vectorization_missing_value(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route with missing value.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_1 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"vectorization": {"spacy_language_model": "fr_core_news_md", "random_seed": 88}},
    )
    assert response_put_1.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_2 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"vectorization": {"vectorizer_type": "spacy", "random_seed": 88}},
    )
    assert response_put_2.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_3 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"vectorization": {"vectorizer_type": "spacy", "spacy_language_model": "fr_core_news_md"}},
    )
    assert response_put_3.status_code == 422

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 2
    assert response_get.json()["status"]["state"] == "ANNOTATION_WITH_UPTODATE_MODELIZATION"
    # Assert route `GET /api/projects/{project_id}/settings` is still the same.
    response_get_settings_after = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json() == response_get_settings_before.json()


# ==============================================================================
# test_ko_sampling_bad_value
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_sampling_bad_value(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route with bad value.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_1 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"sampling": {"algorithm": "UNKNOWN", "random_seed": 88, "nb_to_select": 10}},
    )
    assert response_put_1.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_2 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"sampling": {"algorithm": "random", "random_seed": -99, "nb_to_select": 10}},
    )
    assert response_put_2.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_3 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"sampling": {"algorithm": "random", "random_seed": 88, "nb_to_select": -99}},
    )
    assert response_put_3.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_4 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "sampling": {
                "algorithm": "custom",
                "random_seed": 88,
                "nb_to_select": 10,
                "init_kargs": {
                    "clusters_restriction": "UNKNOWN1",
                    "distance_restriction": "UNKNOWN2",
                    "without_inferred_constraints": "UKNOWN3",
                },
            }
        },
    )
    assert response_put_4.status_code == 422

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 2
    assert response_get.json()["status"]["state"] == "ANNOTATION_WITH_UPTODATE_MODELIZATION"
    # Assert route `GET /api/projects/{project_id}/settings` is still the same.
    response_get_settings_after = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json() == response_get_settings_before.json()


# ==============================================================================
# test_ko_sampling_missing_value
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_sampling_missing_value(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route with missing value.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_1 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"sampling": {"random_seed": 88, "nb_to_select": 10}},
    )
    assert response_put_1.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_2 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"sampling": {"algorithm": "random", "nb_to_select": 10}},
    )
    assert response_put_2.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_3 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"sampling": {"algorithm": "random", "random_seed": 88}},
    )
    assert response_put_3.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_4 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "sampling": {
                "algorithm": "random",
                "random_seed": 88,
                "nb_to_select": 10,
                "init_kargs": {
                    "clusters_restriction": "same_cluster",
                    "distance_restriction": "closest_neighbors",
                    "without_inferred_constraints": False,
                },
            }
        },
    )
    assert response_put_4.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_5 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"sampling": {"algorithm": "custom", "random_seed": 88, "nb_to_select": 10}},
    )
    assert response_put_5.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_6 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "sampling": {
                "algorithm": "custom",
                "random_seed": 88,
                "nb_to_select": 10,
                "init_kargs": {"distance_restriction": "closest_neighbors", "without_inferred_constraints": False},
            }
        },
    )
    assert response_put_6.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_7 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "sampling": {
                "algorithm": "custom",
                "random_seed": 88,
                "nb_to_select": 10,
                "init_kargs": {"clusters_restriction": "same_cluster", "without_inferred_constraints": False},
            }
        },
    )
    assert response_put_7.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_8 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "sampling": {
                "algorithm": "custom",
                "random_seed": 88,
                "nb_to_select": 10,
                "init_kargs": {"clusters_restriction": "same_cluster", "distance_restriction": "closest_neighbors"},
            }
        },
    )
    assert response_put_8.status_code == 422

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 2
    assert response_get.json()["status"]["state"] == "ANNOTATION_WITH_UPTODATE_MODELIZATION"
    # Assert route `GET /api/projects/{project_id}/settings` is still the same.
    response_get_settings_after = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json() == response_get_settings_before.json()


# ==============================================================================
# test_ko_clustering_bad_value
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_clustering_bad_value(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route with bad value.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_1 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "clustering": {
                "algorithm": "UNKNOWN",
                "random_seed": 41,
                "nb_clusters": 3,
                "init_kargs": {"linkage": "complete"},
            }
        },
    )
    assert response_put_1.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_2 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "clustering": {
                "algorithm": "hierarchical",
                "random_seed": -99,
                "nb_clusters": 3,
                "init_kargs": {"linkage": "complete"},
            }
        },
    )
    assert response_put_2.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_3 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "clustering": {
                "algorithm": "kmeans",
                "random_seed": 41,
                "nb_clusters": -99,
                "init_kargs": {"model": "COP", "max_iteration": 200, "tolerance": 0.1},
            }
        },
    )
    assert response_put_3.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_4 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "clustering": {
                "algorithm": "hierarchical",
                "random_seed": 88,
                "nb_clusters": 3,
                "init_kargs": {"linkage": "UNKNOWN"},
            }
        },
    )
    assert response_put_4.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_5 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "clustering": {
                "algorithm": "kmeans",
                "random_seed": 88,
                "nb_clusters": 3,
                "init_kargs": {"model": "UNKNOWN", "max_iteration": -99, "tolerance": -99},
            }
        },
    )
    assert response_put_5.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_6 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "clustering": {
                "algorithm": "spectral",
                "random_seed": 88,
                "nb_clusters": 3,
                "init_kargs": {"model": "UNKNOWN", "nb_components": -99},
            }
        },
    )
    assert response_put_6.status_code == 422

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 2
    assert response_get.json()["status"]["state"] == "ANNOTATION_WITH_UPTODATE_MODELIZATION"
    # Assert route `GET /api/projects/{project_id}/settings` is still the same.
    response_get_settings_after = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json() == response_get_settings_before.json()


# ==============================================================================
# test_ko_clustering_missing_value
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_clustering_missing_value(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route with missing value.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_1 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"clustering": {"random_seed": 88, "nb_clusters": 3, "init_kargs": {"linkage": "ward"}}},
    )
    assert response_put_1.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_2 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "clustering": {
                "algorithm": "spectral",
                "nb_clusters": 3,
                "init_kargs": {"model": "SPEC", "nb_components": 12},
            }
        },
    )
    assert response_put_2.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_3 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "clustering": {
                "algorithm": "spectral",
                "random_seed": 88,
                "init_kargs": {"model": "SPEC", "nb_components": None},
            }
        },
    )
    assert response_put_3.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_3 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "clustering": {
                "algorithm": "spectral",
                "nb_clusters": 3,
                "random_seed": 88,
                "init_kargs": {"linkage": "ward"},
            }
        },
    )
    assert response_put_3.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_4 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"clustering": {"algorithm": "kmeans", "random_seed": 42, "nb_clusters": 2}},
    )
    assert response_put_4.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_5 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "clustering": {
                "algorithm": "kmeans",
                "random_seed": 42,
                "nb_clusters": 2,
                "init_kargs": {"tolerance": 0.0001},
            }
        },
    )
    assert response_put_5.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_6 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "clustering": {
                "algorithm": "kmeans",
                "random_seed": 42,
                "nb_clusters": 2,
                "init_kargs": {"max_iteration": 150},
            }
        },
    )
    assert response_put_6.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_7 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"clustering": {"algorithm": "hierarchical", "random_seed": 41, "nb_clusters": 3}},
    )
    assert response_put_7.status_code == 422

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put_8 = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"clustering": {"algorithm": "hierarchical", "random_seed": 41, "nb_clusters": 3}},
    )
    assert response_put_8.status_code == 422

    # Assert route `GET /api/projects/{project_id}/status` is still the same.
    response_get = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get.status_code == 200
    assert response_get.json()["status"]["iteration_id"] == 2
    assert response_get.json()["status"]["state"] == "ANNOTATION_WITH_UPTODATE_MODELIZATION"
    # Assert route `GET /api/projects/{project_id}/settings` is still the same.
    response_get_settings_after = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json() == response_get_settings_before.json()


# ==============================================================================
# test_ok_all_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_all_1(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/2a_SAMPLING_TODO/settings",
        json={
            "sampling": {"algorithm": "random", "random_seed": 88, "nb_to_select": 10},
            "clustering": {
                "algorithm": "hierarchical",
                "random_seed": 41,
                "nb_clusters": 3,
                "init_kargs": {"linkage": "complete"},
            },
        },
    )
    assert response_put.status_code == 201
    assert response_put.json() == {
        "project_id": "2a_SAMPLING_TODO",
        "detail": "The project with id '2a_SAMPLING_TODO' has updated the following settings: sampling, clustering.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 2
    assert response_get_status.json()["status"]["state"] == "SAMPLING_TODO"
    # Assert route `GET /api/projects/{project_id}/settings` is updated.
    response_get_settings_after = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_after.status_code == 200
    assert (
        response_get_settings_after.json()["settings"]["preprocessing"]
        == response_get_settings_before.json()["settings"]["preprocessing"]
    )
    assert (
        response_get_settings_after.json()["settings"]["vectorization"]
        == response_get_settings_before.json()["settings"]["vectorization"]
    )
    assert response_get_settings_after.json()["settings"]["sampling"] == {
        "algorithm": "random",
        "random_seed": 88,
        "nb_to_select": 10,
        "init_kargs": None,
    }
    assert response_get_settings_after.json()["settings"]["clustering"] == {
        "algorithm": "hierarchical",
        "random_seed": 41,
        "nb_clusters": 3,
        "init_kargs": {"linkage": "complete"},
    }


# ==============================================================================
# test_ok_all_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_all_2(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={
            "preprocessing": {
                "apply_stopwords_deletion": True,
                "apply_parsing_filter": True,
                "apply_lemmatization": True,
                "spacy_language_model": "fr_core_news_md",
            },
            "vectorization": {"vectorizer_type": "spacy", "spacy_language_model": "fr_core_news_md", "random_seed": 88},
            "clustering": {
                "algorithm": "hierarchical",
                "random_seed": 41,
                "nb_clusters": 3,
                "init_kargs": {"linkage": "complete"},
            },
        },
    )
    assert response_put.status_code == 201
    assert response_put.json() == {
        "project_id": "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "detail": "The project with id '2d_ANNOTATION_WITH_UPTODATE_MODELIZATION' has updated the following settings: preprocessing, vectorization, clustering.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 2
    assert response_get_status.json()["status"]["state"] == "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS"
    # Assert route `GET /api/projects/{project_id}/settings` is updated.
    response_get_settings_after = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json()["settings"]["preprocessing"] == {
        "apply_stopwords_deletion": True,
        "apply_parsing_filter": True,
        "apply_lemmatization": True,
        "spacy_language_model": "fr_core_news_md",
    }
    assert response_get_settings_after.json()["settings"]["vectorization"] == {
        "vectorizer_type": "spacy",
        "spacy_language_model": "fr_core_news_md",
        "random_seed": 88,
    }
    assert (
        response_get_settings_after.json()["settings"]["sampling"]
        == response_get_settings_before.json()["settings"]["sampling"]
    )
    assert response_get_settings_after.json()["settings"]["clustering"] == {
        "algorithm": "hierarchical",
        "random_seed": 41,
        "nb_clusters": 3,
        "init_kargs": {"linkage": "complete"},
    }


# ==============================================================================
# test_ok_preprocessing_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_preprocessing_1(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route.

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
            "1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS",
        ],
    )

    # Get settings before test.
    response_get_settings_before = await async_client.get(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/settings"
    )
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/settings",
        json={
            "preprocessing": {
                "apply_stopwords_deletion": True,
                "apply_parsing_filter": True,
                "apply_lemmatization": True,
                "spacy_language_model": "fr_core_news_md",
            },
            "vectorization": {"vectorizer_type": "tfidf", "spacy_language_model": None, "random_seed": 88},
        },
    )
    assert response_put.status_code == 201
    assert response_put.json() == {
        "project_id": "1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS",
        "detail": "The project with id '1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS' has updated the following settings: preprocessing, vectorization.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/status"
    )
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 1
    assert response_get_status.json()["status"]["state"] == "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS"
    # Assert route `GET /api/projects/{project_id}/settings` is updated.
    response_get_settings_after = await async_client.get(
        url="/api/projects/1e_ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS/settings"
    )
    assert response_get_settings_after.status_code == 200
    assert response_get_settings_after.json()["settings"]["preprocessing"] == {
        "apply_stopwords_deletion": True,
        "apply_parsing_filter": True,
        "apply_lemmatization": True,
        "spacy_language_model": "fr_core_news_md",
    }
    assert response_get_settings_after.json()["settings"]["vectorization"] == {
        "vectorizer_type": "tfidf",
        "spacy_language_model": None,
        "random_seed": 88,
    }
    assert (
        response_get_settings_after.json()["settings"]["sampling"]
        == response_get_settings_before.json()["settings"]["sampling"]
    )
    assert (
        response_get_settings_after.json()["settings"]["clustering"]
        == response_get_settings_before.json()["settings"]["clustering"]
    )


# ==============================================================================
# test_ok_vectorization_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_vectorization_1(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings",
        json={"vectorization": {"vectorizer_type": "tfidf", "random_seed": 88}},
    )
    assert response_put.status_code == 201
    assert response_put.json() == {
        "project_id": "2d_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "detail": "The project with id '2d_ANNOTATION_WITH_UPTODATE_MODELIZATION' has updated the following settings: vectorization.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 2
    assert response_get_status.json()["status"]["state"] == "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS"
    # Assert route `GET /api/projects/{project_id}/settings` is updated.
    response_get_settings_after = await async_client.get(
        url="/api/projects/2d_ANNOTATION_WITH_UPTODATE_MODELIZATION/settings"
    )
    assert response_get_settings_after.status_code == 200
    assert (
        response_get_settings_after.json()["settings"]["preprocessing"]
        == response_get_settings_before.json()["settings"]["preprocessing"]
    )
    assert response_get_settings_after.json()["settings"]["vectorization"] == {
        "vectorizer_type": "tfidf",
        "spacy_language_model": None,
        "random_seed": 88,
    }
    assert (
        response_get_settings_after.json()["settings"]["sampling"]
        == response_get_settings_before.json()["settings"]["sampling"]
    )
    assert (
        response_get_settings_after.json()["settings"]["clustering"]
        == response_get_settings_before.json()["settings"]["clustering"]
    )


# ==============================================================================
# test_ok_sampling_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_sampling_1(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/2a_SAMPLING_TODO/settings",
        json={
            "sampling": {
                "algorithm": "custom",
                "random_seed": 88,
                "nb_to_select": 10,
                "init_kargs": {
                    "clusters_restriction": "same_cluster",
                    "distance_restriction": "closest_neighbors",
                    "without_inferred_constraints": False,
                },
            },
        },
    )
    assert response_put.status_code == 201
    assert response_put.json() == {
        "project_id": "2a_SAMPLING_TODO",
        "detail": "The project with id '2a_SAMPLING_TODO' has updated the following settings: sampling.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 2
    assert response_get_status.json()["status"]["state"] == "SAMPLING_TODO"
    # Assert route `GET /api/projects/{project_id}/settings` is updated.
    response_get_settings_after = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_after.status_code == 200
    assert (
        response_get_settings_after.json()["settings"]["preprocessing"]
        == response_get_settings_before.json()["settings"]["preprocessing"]
    )
    assert (
        response_get_settings_after.json()["settings"]["vectorization"]
        == response_get_settings_before.json()["settings"]["vectorization"]
    )
    assert response_get_settings_after.json()["settings"]["sampling"] == {
        "algorithm": "custom",
        "random_seed": 88,
        "nb_to_select": 10,
        "init_kargs": {
            "clusters_restriction": "same_cluster",
            "distance_restriction": "closest_neighbors",
            "without_inferred_constraints": False,
        },
    }
    assert (
        response_get_settings_after.json()["settings"]["clustering"]
        == response_get_settings_before.json()["settings"]["clustering"]
    )


# ==============================================================================
# test_ok_sampling_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_sampling_2(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/2a_SAMPLING_TODO/settings",
        json={
            "sampling": {"algorithm": "random", "random_seed": 88, "nb_to_select": 10, "init_kargs": None},
        },
    )
    assert response_put.status_code == 201
    assert response_put.json() == {
        "project_id": "2a_SAMPLING_TODO",
        "detail": "The project with id '2a_SAMPLING_TODO' has updated the following settings: sampling.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 2
    assert response_get_status.json()["status"]["state"] == "SAMPLING_TODO"
    # Assert route `GET /api/projects/{project_id}/settings` is updated.
    response_get_settings_after = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_after.status_code == 200
    assert (
        response_get_settings_after.json()["settings"]["preprocessing"]
        == response_get_settings_before.json()["settings"]["preprocessing"]
    )
    assert (
        response_get_settings_after.json()["settings"]["vectorization"]
        == response_get_settings_before.json()["settings"]["vectorization"]
    )
    assert response_get_settings_after.json()["settings"]["sampling"] == {
        "algorithm": "random",
        "random_seed": 88,
        "nb_to_select": 10,
        "init_kargs": None,
    }
    assert (
        response_get_settings_after.json()["settings"]["clustering"]
        == response_get_settings_before.json()["settings"]["clustering"]
    )


# ==============================================================================
# test_ok_clustering_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_clustering_1(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/2a_SAMPLING_TODO/settings",
        json={
            "clustering": {
                "algorithm": "kmeans",
                "random_seed": 88,
                "nb_clusters": 8,
                "init_kargs": {"model": "COP", "tolerance": 0.1, "max_iteration": 12},
            }
        },
    )
    assert response_put.status_code == 201
    assert response_put.json() == {
        "project_id": "2a_SAMPLING_TODO",
        "detail": "The project with id '2a_SAMPLING_TODO' has updated the following settings: clustering.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 2
    assert response_get_status.json()["status"]["state"] == "SAMPLING_TODO"
    # Assert route `GET /api/projects/{project_id}/settings` is updated.
    response_get_settings_after = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_after.status_code == 200
    assert (
        response_get_settings_after.json()["settings"]["preprocessing"]
        == response_get_settings_before.json()["settings"]["preprocessing"]
    )
    assert (
        response_get_settings_after.json()["settings"]["vectorization"]
        == response_get_settings_before.json()["settings"]["vectorization"]
    )
    assert (
        response_get_settings_after.json()["settings"]["sampling"]
        == response_get_settings_before.json()["settings"]["sampling"]
    )
    assert response_get_settings_after.json()["settings"]["clustering"] == {
        "algorithm": "kmeans",
        "random_seed": 88,
        "nb_clusters": 8,
        "init_kargs": {"model": "COP", "tolerance": 0.1, "max_iteration": 12},
    }


# ==============================================================================
# test_ok_clustering_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_clustering_2(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/2a_SAMPLING_TODO/settings",
        json={
            "clustering": {
                "algorithm": "hierarchical",
                "random_seed": 88,
                "nb_clusters": 8,
                "init_kargs": {"linkage": "average"},
            }
        },
    )
    assert response_put.status_code == 201
    assert response_put.json() == {
        "project_id": "2a_SAMPLING_TODO",
        "detail": "The project with id '2a_SAMPLING_TODO' has updated the following settings: clustering.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 2
    assert response_get_status.json()["status"]["state"] == "SAMPLING_TODO"
    # Assert route `GET /api/projects/{project_id}/settings` is updated.
    response_get_settings_after = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_after.status_code == 200
    assert (
        response_get_settings_after.json()["settings"]["preprocessing"]
        == response_get_settings_before.json()["settings"]["preprocessing"]
    )
    assert (
        response_get_settings_after.json()["settings"]["vectorization"]
        == response_get_settings_before.json()["settings"]["vectorization"]
    )
    assert (
        response_get_settings_after.json()["settings"]["sampling"]
        == response_get_settings_before.json()["settings"]["sampling"]
    )
    assert response_get_settings_after.json()["settings"]["clustering"] == {
        "algorithm": "hierarchical",
        "random_seed": 88,
        "nb_clusters": 8,
        "init_kargs": {"linkage": "average"},
    }


# ==============================================================================
# test_ok_clustering_3
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_clustering_3(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/2a_SAMPLING_TODO/settings",
        json={
            "clustering": {
                "algorithm": "spectral",
                "random_seed": 40,
                "nb_clusters": 4,
                "init_kargs": {"model": "SPEC", "nb_components": 12},
            }
        },
    )
    assert response_put.status_code == 201
    assert response_put.json() == {
        "project_id": "2a_SAMPLING_TODO",
        "detail": "The project with id '2a_SAMPLING_TODO' has updated the following settings: clustering.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 2
    assert response_get_status.json()["status"]["state"] == "SAMPLING_TODO"
    # Assert route `GET /api/projects/{project_id}/settings` is updated.
    response_get_settings_after = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_after.status_code == 200
    assert (
        response_get_settings_after.json()["settings"]["preprocessing"]
        == response_get_settings_before.json()["settings"]["preprocessing"]
    )
    assert (
        response_get_settings_after.json()["settings"]["vectorization"]
        == response_get_settings_before.json()["settings"]["vectorization"]
    )
    assert (
        response_get_settings_after.json()["settings"]["sampling"]
        == response_get_settings_before.json()["settings"]["sampling"]
    )
    assert response_get_settings_after.json()["settings"]["clustering"] == {
        "algorithm": "spectral",
        "random_seed": 40,
        "nb_clusters": 4,
        "init_kargs": {"model": "SPEC", "nb_components": 12},
    }


# ==============================================================================
# test_ok_clustering_4
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_clustering_4(async_client, tmp_path):
    """
    Test the `PUT /api/projects/{project_id}/settings` route.

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

    # Get settings before test.
    response_get_settings_before = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_before.status_code == 200

    # Assert route `PUT /api/projects/{project_id}/settings` works.
    response_put = await async_client.put(
        url="/api/projects/2a_SAMPLING_TODO/settings",
        json={
            "clustering": {
                "algorithm": "spectral",
                "random_seed": 40,
                "nb_clusters": 4,
                "init_kargs": {"model": "SPEC", "nb_components": None},
            }
        },
    )
    assert response_put.status_code == 201
    assert response_put.json() == {
        "project_id": "2a_SAMPLING_TODO",
        "detail": "The project with id '2a_SAMPLING_TODO' has updated the following settings: clustering.",
    }
    # Assert route `GET /api/projects/{project_id}/status` is updated.
    response_get_status = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/status")
    assert response_get_status.status_code == 200
    assert response_get_status.json()["status"]["iteration_id"] == 2
    assert response_get_status.json()["status"]["state"] == "SAMPLING_TODO"
    # Assert route `GET /api/projects/{project_id}/settings` is updated.
    response_get_settings_after = await async_client.get(url="/api/projects/2a_SAMPLING_TODO/settings")
    assert response_get_settings_after.status_code == 200
    assert (
        response_get_settings_after.json()["settings"]["preprocessing"]
        == response_get_settings_before.json()["settings"]["preprocessing"]
    )
    assert (
        response_get_settings_after.json()["settings"]["vectorization"]
        == response_get_settings_before.json()["settings"]["vectorization"]
    )
    assert (
        response_get_settings_after.json()["settings"]["sampling"]
        == response_get_settings_before.json()["settings"]["sampling"]
    )
    assert response_get_settings_after.json()["settings"]["clustering"] == {
        "algorithm": "spectral",
        "random_seed": 40,
        "nb_clusters": 4,
        "init_kargs": {"model": "SPEC", "nb_components": None},
    }
