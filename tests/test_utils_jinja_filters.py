# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_utils_jinja_filters.py
* Description:  Unittests for `app` jinja filters `timestamp_to_date`, `timestamp_to_hour`, `get_previous_key`, `get_next_key`.
* Author:       Erwan Schild
* Created:      22/02/2022
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

from cognitivefactory.interactive_clustering_gui.app import (
    get_next_key,
    get_previous_key,
    timestamp_to_date,
    timestamp_to_hour,
)

# ==============================================================================
# test_timestamp_to_date
# ==============================================================================


async def test_timestamp_to_date():
    """
    Test the `timestamp_to_hour()` method.
    """
    assert timestamp_to_date(timestamp=1658909898.219331) == "27/07/2022"


# ==============================================================================
# test_timestamp_to_hour
# ==============================================================================


async def test_timestamp_to_hour():
    """
    Test the `timestamp_to_hour()` method.
    """
    assert timestamp_to_hour(timestamp=1658909898.219331) == "10:18:18"


# ==============================================================================
# test_get_previous_key
# ==============================================================================


async def test_get_previous_key():
    """
    Test the `get_previous_key()` method.
    """
    dictionary = {"a": 0, "e": -2, "c": None, "b": 0, "d": [0, 2, 5]}
    assert get_previous_key(key="a", dictionary=dictionary) is None
    assert get_previous_key(key="e", dictionary=dictionary) == "a"
    assert get_previous_key(key="c", dictionary=dictionary) == "e"
    assert get_previous_key(key="b", dictionary=dictionary) == "c"
    assert get_previous_key(key="d", dictionary=dictionary) == "b"
    assert get_previous_key(key="UNKNOWN", dictionary=dictionary) is None


# ==============================================================================
# test_get_next_key
# ==============================================================================


async def test_get_next_key():
    """
    Test the `get_next_key()` method.
    """
    dictionary = {"a": 0, "e": -2, "c": None, "b": 0, "d": [0, 2, 5]}
    assert get_next_key(key="a", dictionary=dictionary) == "e"
    assert get_next_key(key="e", dictionary=dictionary) == "c"
    assert get_next_key(key="c", dictionary=dictionary) == "b"
    assert get_next_key(key="b", dictionary=dictionary) == "d"
    assert get_next_key(key="d", dictionary=dictionary) is None
    assert get_next_key(key="UNKNOWN", dictionary=dictionary) is None
