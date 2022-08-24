# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_api_projects_vectors.py
* Description:  Unittests for `app` module on the `GET /api/projects/{project_id}/vectors` route.
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
    Test the `GET /api/projects/{project_id}/vectors` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /api/projects/{project_id}/vectors` works.
    response_get = await async_client.get(url="/api/projects/UNKNOWN_PROJECT/vectors")
    assert response_get.status_code == 404
    assert response_get.json() == {
        "detail": "The project with id 'UNKNOWN_PROJECT' doesn't exist.",
    }


# ==============================================================================
# test_ko_bad_state_1
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_state_1(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/vectors` route with some projects.

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

    # Assert route `GET /api/projects/{project_id}/vectors` works.
    response_get = await async_client.get(url="/api/projects/0a_INITIALIZATION_WITHOUT_MODELIZATION/vectors")
    assert response_get.status_code == 403
    assert response_get.json() == {
        "detail": "The project with id '0a_INITIALIZATION_WITHOUT_MODELIZATION' hasn't completed its modelization update step.",
    }


# ==============================================================================
# test_ko_bad_state_2
# ==============================================================================


@pytest.mark.asyncio()
async def test_ko_bad_state_2(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/vectors` route with some projects.

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
            "0c_INITIALIZATION_WITH_WORKING_MODELIZATION",
        ],
    )

    # Assert route `GET /api/projects/{project_id}/vectors` works.
    response_get = await async_client.get(url="/api/projects/0c_INITIALIZATION_WITH_WORKING_MODELIZATION/vectors")
    assert response_get.status_code == 403
    assert response_get.json() == {
        "detail": "The project with id '0c_INITIALIZATION_WITH_WORKING_MODELIZATION' hasn't completed its modelization update step.",
    }


# ==============================================================================
# test_ok
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/vectors` route with some projects.

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

    # Assert route `GET /api/projects/{project_id}/vectors` works.
    response_get = await async_client.get(url="/api/projects/1l_ANNOTATION_WITH_UPTODATE_MODELIZATION/vectors")
    assert response_get.status_code == 200
    assert list(response_get.json().keys()) == ["project_id", "vectors_2d", "vectors_3d"]
    assert response_get.json() == {
        "project_id": "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "vectors_2d": {
            "0": {"x": 91.36274719238281, "y": 21.67824935913086},
            "1": {"x": -0.9386575222015381, "y": 0.43653735518455505},
            "2": {"x": -39.60744857788086, "y": 24.44004249572754},
            "3": {"x": 88.78878021240234, "y": -33.314998626708984},
            "4": {"x": -114.78877258300781, "y": 79.15187072753906},
            "5": {"x": 49.28199005126953, "y": 123.4693374633789},
            "6": {"x": -29.51285171508789, "y": 81.52217864990234},
            "7": {"x": -2.4428157806396484, "y": -44.19341278076172},
            "8": {"x": -129.07321166992188, "y": 20.79026222229004},
            "9": {"x": -1.6523088216781616, "y": 45.01224899291992},
            "10": {"x": -9.337442398071289, "y": -93.84052276611328},
            "11": {"x": -82.09162902832031, "y": 7.956731796264648},
            "12": {"x": 22.62102699279785, "y": 82.16755676269531},
            "13": {"x": 42.19430160522461, "y": -13.67241096496582},
            "15": {"x": -70.86075592041016, "y": 57.78665542602539},
            "16": {"x": -45.6887321472168, "y": -23.74492073059082},
            "17": {"x": 43.95357131958008, "y": -68.4990234375},
            "18": {"x": -104.2291488647461, "y": -39.33942794799805},
            "19": {"x": -10.273590087890625, "y": 129.61111450195312},
            "20": {"x": 42.092933654785156, "y": 33.699771881103516},
            "21": {"x": -59.6293830871582, "y": -71.61207580566406},
            "22": {"x": -67.85298919677734, "y": 116.51306915283203},
            "23": {"x": 77.96465301513672, "y": 73.44774627685547},
        },
        "vectors_3d": {
            "0": {"x": 70.29167175292969, "y": -266.54766845703125, "z": 20.373777389526367},
            "1": {"x": 233.35336303710938, "y": -156.25953674316406, "z": -100.0744857788086},
            "2": {"x": 186.1459503173828, "y": 73.08946990966797, "z": -184.87689208984375},
            "3": {"x": -8.0564603805542, "y": 111.37313842773438, "z": -21.52240753173828},
            "4": {"x": -19.584718704223633, "y": -92.258544921875, "z": 271.7480163574219},
            "5": {"x": 199.4398193359375, "y": -137.07095336914062, "z": 221.79983520507812},
            "6": {"x": 169.81517028808594, "y": -84.50203704833984, "z": 719.15478515625},
            "7": {"x": -83.7402114868164, "y": 295.5261535644531, "z": 26.949981689453125},
            "8": {"x": -60.69163513183594, "y": 135.87303161621094, "z": 220.9168243408203},
            "9": {"x": -76.2159423828125, "y": -125.81424713134766, "z": 76.24165344238281},
            "10": {"x": -84.635009765625, "y": 176.4404296875, "z": -230.58082580566406},
            "11": {"x": -166.36639404296875, "y": -225.3141632080078, "z": -90.8826904296875},
            "12": {"x": -218.71446228027344, "y": 12.174712181091309, "z": 128.22303771972656},
            "13": {"x": 130.4368438720703, "y": -7.396134853363037, "z": 73.75303649902344},
            "15": {"x": 108.37644958496094, "y": 74.9406509399414, "z": 515.5901489257812},
            "16": {"x": -155.9998016357422, "y": -16.28353500366211, "z": -120.30685424804688},
            "17": {"x": -84.97659301757812, "y": -65.17621612548828, "z": -308.581298828125},
            "18": {"x": -238.48118591308594, "y": 152.14096069335938, "z": -19.21702003479004},
            "19": {"x": 185.66650390625, "y": 200.40057373046875, "z": 8.32783317565918},
            "20": {"x": -226.6430206298828, "y": 49.02275848388672, "z": -462.8315124511719},
            "21": {"x": 43.422847747802734, "y": -75.41294860839844, "z": -120.16666412353516},
            "22": {"x": -341.8919372558594, "y": 96.16680908203125, "z": -187.0303497314453},
            "23": {"x": 164.00942993164062, "y": 116.74947357177734, "z": 243.1012725830078},
        },
    }

    # Assert file content is the same.
    with open(tmp_path / "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION" / "vectors_2D.json", "r") as vectors_2d_fileobject:
        assert response_get.json()["vectors_2d"] == json.load(vectors_2d_fileobject)
    with open(tmp_path / "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION" / "vectors_3D.json", "r") as vectors_3d_fileobject:
        assert response_get.json()["vectors_3d"] == json.load(vectors_3d_fileobject)
