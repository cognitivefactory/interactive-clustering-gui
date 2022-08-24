# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_gui_help.py
* Description:  Unittests for `app` module on the `GET /gui/help` route.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import pytest

# ==============================================================================
# test_ok
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok(async_client):
    """
    Test the `GET /gui/help` route.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /gui/help` works.
    response = await async_client.get(url="/gui/help")
    assert response.status_code == 200
