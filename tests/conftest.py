# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/conftest.py
* Description:  Configuration for the pytest "app" test suite.
* Author:       Erwan Schild
* Created:      13/12/2021
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

# from asgi_lifespan import LifespanManager  # To call startup events.
import asyncio
from pathlib import Path

import pytest
from httpx import AsyncClient

from cognitivefactory.interactive_clustering_gui import app, backgroundtasks


# ==============================================================================
# async_client
# ==============================================================================
@pytest.fixture()
async def async_client(tmp_path: Path, monkeypatch):
    """
    Provide an HTTPX asynchronous HTTP client.

    Args:
        tmp_path: Pytest fixture: points to a temporary directory.
        monkeypatch: Pytest fixture: allows to monkeypatch objects.

    Yields:
        An instance of AsyncClient using the FastAPI ASGI application.
    """
    # Replace app.DATA_DIRECTORY with a temporary directory for the test.
    monkeypatch.setattr(app, "DATA_DIRECTORY", tmp_path)
    monkeypatch.setattr(app.backgroundtasks, "DATA_DIRECTORY", tmp_path)
    print(">> PYTEST TEMPORARY PATH:", tmp_path)

    # Instanciate the application.
    # lifespan = LifespanManager(app)  # To call startup events.
    httpx_client = AsyncClient(
        app=app.app,
        base_url="http://testserver",
    )

    # Return the application.
    # async with httpx_client as client, lifespan:  # noqa: WPS316
    async with httpx_client as client:  # noqa: WPS316
        yield client


# ==============================================================================
# set_fake_backgroundtasks
# ==============================================================================
@pytest.fixture()
async def fake_backgroundtasks(tmp_path: Path, monkeypatch):
    """
    Patch the `backgroundtasks.DATA_DIRECTORY` of the worker.

    Args:
        tmp_path: Pytest fixture: points to a temporary directory.
        monkeypatch: Pytest fixture: allows to monkeypatch objects.

    Returns:
        The worker module.
    """
    # Replace backgroundtasks.DATA_DIRECTORY with a temporary directory for the test.
    monkeypatch.setattr(backgroundtasks, "DATA_DIRECTORY", tmp_path)
    print(">> PYTEST TEMPORARY PATH:", tmp_path)

    return backgroundtasks


# ==============================================================================
# event_loop
# ==============================================================================
@pytest.fixture(scope="session")
def event_loop():
    """
    Replace the fixture used by pytest asyncio marker.

    This is required because the default fixture has function scope,
    and our async client has session scope. Pytest wants both to have the same scope.
    Moreover, hypothesis asks to mark reusable fixtures as module or session scope.

    Returns:
        An event loop.
    """
    return asyncio.get_event_loop()
