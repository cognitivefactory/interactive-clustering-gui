# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_welcome.py
* Description:  Unittests for `app` module on the `GET /welcome` route.
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
    Test the `GET /welcome` route.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /welcome` works.
    response = await async_client.get(url="/welcome")
    assert response.status_code == 200
