# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_post_api_projects.py
* Description:  Unittests for `app` module on the `POST /api/projects` route.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import json
import os
from pathlib import Path
from typing import Any, Dict

import pytest

from cognitivefactory.interactive_clustering_gui.models.states import ICGUIStates

# ==============================================================================
# test_ko_empty_project_name
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_empty_project_name(async_client):
    """
    Test the `POST /api/projects` route with empty project_name.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `POST /api/projects` works.
    with open(Path(__file__).parent / "dummies" / "dummy_24.csv", "rb") as dataset_fileobject:
        response_post = await async_client.post(
            url="/api/projects",
            params={
                "project_name": "   \n  ",
            },
            files={
                "dataset_file": (
                    "dummy_24.csv",
                    dataset_fileobject,
                    "text/csv",
                ),
            },
        )
    assert response_post.status_code == 400
    assert response_post.json() == {
        "detail": "The project name '   \n  ' is invalid.",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ko_bad_csv
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_csv(async_client):
    """
    Test the `POST /api/projects` route with bad .csv dataset.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `POST /api/projects` works.
    with open(Path(__file__).parent / "dummies" / "dummy_24.xlsx", "rb") as dataset_fileobject:
        response_post = await async_client.post(
            url="/api/projects",
            params={
                "project_name": "unittests ! with bad .CSV",
            },
            files={
                "dataset_file": (
                    "dummy_24.xlsx",
                    dataset_fileobject,
                    "text/csv",
                ),
            },
        )
    assert response_post.status_code == 400
    assert response_post.json() == {
        "detail": "The dataset file is invalid. `.csv` file, with `;` separator, must contain a list of texts in the first column, with no header.",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ko_bad_xlsx
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_xlsx(async_client):
    """
    Test the `POST /api/projects` route with bad .xlsx dataset.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `POST /api/projects` works.
    with open(Path(__file__).parent / "dummies" / "dummy_24.csv", "rb") as dataset_fileobject:
        response_post = await async_client.post(
            url="/api/projects",
            params={
                "project_name": "unittests ! with bad .XLSX",
            },
            files={
                "dataset_file": (
                    "dummy_24.csv",
                    dataset_fileobject,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
            },
        )
    assert response_post.status_code == 400
    assert response_post.json() == {
        "detail": "The dataset file is invalid. `.xlsx` file must contain a list of texts in the first column, with no header.",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ko_dataset_type
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_dataset_type(async_client):
    """
    Test the `POST /api/projects` route with bad dataset type.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `POST /api/projects` works.
    with open(Path(__file__).parent / "dummies" / "dummy_24.txt", "rb") as dataset_fileobject:
        response_post = await async_client.post(
            url="/api/projects",
            params={
                "project_name": "unittests ! with bad .XLSX",
            },
            files={
                "dataset_file": (
                    "dummy_24.txt",
                    dataset_fileobject,
                    "text/plain",
                ),
            },
        )
    assert response_post.status_code == 400
    assert response_post.json() == {
        "detail": "The file type 'text/plain' is not supported. Please use '.csv' (`;` separator) or '.xlsx' file.",
    }

    # Assert route `GET /api/projects` is kept empty.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert response_get.json() == []  # noqa: WPS520


# ==============================================================================
# test_ok_csv
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_csv(async_client, tmp_path):
    """
    Test the `POST /api/projects` route with .csv dataset.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
        tmp_path: The temporary path given for this test, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `POST /api/projects` works.
    with open(Path(__file__).parent / "dummies" / "dummy_24.csv", "rb") as dataset_fileobject:
        response_post = await async_client.post(
            url="/api/projects",
            params={
                "project_name": "unittests ! with .CSV",
            },
            files={
                "dataset_file": (
                    "dummy_24.csv",
                    dataset_fileobject,
                    "text/csv",
                ),
            },
        )
    assert response_post.status_code == 201
    assert list(response_post.json().keys()) == ["project_id", "detail"]
    created_project_id: str = response_post.json()["project_id"]

    # Assert route `GET /api/projects` works and contains the created project.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert created_project_id in response_get.json()

    # Assert created project has needed stored files.
    assert sorted(os.listdir(tmp_path / created_project_id)) == [
        "clustering.json",
        "constraints.json",
        "metadata.json",
        "modelization.json",
        "sampling.json",
        "settings.json",
        "status.json",
        "texts.json",
    ]

    # Case of `metadata.json`.
    with open(tmp_path / created_project_id / "metadata.json", "r") as metadata_fileobject:
        project_metadata: Dict[str, Any] = json.load(metadata_fileobject)
        assert project_metadata["project_id"] == created_project_id
        assert project_metadata["project_name"] == "unittests ! with .CSV"
        assert "creation_timestamp" in project_metadata.keys()

    # Case of `status.json`.
    with open(tmp_path / created_project_id / "status.json", "r") as status_fileobject:
        project_status: Dict[str, Any] = json.load(status_fileobject)
        assert project_status == {
            "iteration_id": 0,
            "state": ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION,
            "task": None,
        }


# ==============================================================================
# test_ok_xlsx
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_xlsx(async_client, tmp_path):
    """
    Test the `POST /api/projects` route with .xlsx dataset.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
        tmp_path: The temporary path given for this test, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `POST /api/projects` works.
    with open(Path(__file__).parent / "dummies" / "dummy_24.xlsx", "rb") as dataset_fileobject:
        response_post = await async_client.post(
            url="/api/projects",
            params={
                "project_name": "unittests ! with .XLSX",
            },
            files={
                "dataset_file": (
                    "dummy_24.xlsx",
                    dataset_fileobject,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
            },
        )
    assert response_post.status_code == 201
    assert list(response_post.json().keys()) == ["project_id", "detail"]
    created_project_id: str = response_post.json()["project_id"]

    # Assert route `GET /api/projects` works and contains the created project.
    response_get = await async_client.get(url="/api/projects")
    assert response_get.status_code == 200
    assert created_project_id in response_get.json()

    # Assert created project has needed stored files.
    assert sorted(os.listdir(tmp_path / created_project_id)) == [
        "clustering.json",
        "constraints.json",
        "metadata.json",
        "modelization.json",
        "sampling.json",
        "settings.json",
        "status.json",
        "texts.json",
    ]

    # Case of `metadata.json`.
    with open(tmp_path / created_project_id / "metadata.json", "r") as metadata_fileobject:
        project_metadata: Dict[str, Any] = json.load(metadata_fileobject)
        assert project_metadata["project_id"] == created_project_id
        assert project_metadata["project_name"] == "unittests ! with .XLSX"
        assert "creation_timestamp" in project_metadata.keys()

    # Case of `status.json`.
    with open(tmp_path / created_project_id / "status.json", "r") as status_fileobject:
        project_status: Dict[str, Any] = json.load(status_fileobject)
        assert project_status == {
            "iteration_id": 0,
            "state": ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION,
            "task": None,
        }
