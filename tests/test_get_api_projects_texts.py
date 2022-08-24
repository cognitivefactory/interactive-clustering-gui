# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_get_api_texts.py
* Description:  Unittests for `app` module on the `GET /api/projects/{project_id}/texts` route.
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
    Test the `GET /api/projects/{project_id}/texts` route with not existing project.

    Arguments:
        async_client: Fixture providing an HTTP client, declared in `conftest.py`.
    """
    # Assert HTTP client is created.
    assert async_client

    # Assert route `GET /api/projects/{project_id}/texts` works.
    response_get = await async_client.get(url="/api/projects/UNKNOWN_PROJECT/texts")
    assert response_get.status_code == 404
    assert response_get.json() == {
        "detail": "The project with id 'UNKNOWN_PROJECT' doesn't exist.",
    }


# ==============================================================================
# test_ok_default
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_default(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/texts` route.

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

    # Assert route `GET /api/projects/{project_id}/texts` works.
    response_get = await async_client.get(url="/api/projects/1l_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts")
    assert response_get.status_code == 200
    list_of_deletion_marks = [text_value["is_deleted"] for text_value in response_get.json()["texts"].values()]
    assert True not in list_of_deletion_marks
    assert response_get.json() == {
        "project_id": "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "texts": {
            "1": {
                "text_original": "activer les numéros de carte virtuelle",
                "text": "activer les numéros de carte virtuelle",
                "text_preprocessed": "activer les numeros de carte virtuelle",
                "is_deleted": False,
            },
            "16": {
                "text_original": "carte bancaire avalée",
                "text": "carte bancaire avalée",
                "text_preprocessed": "carte bancaire avalee",
                "is_deleted": False,
            },
            "8": {
                "text_original": "Combien d'argent me reste-t-il sur mon compte ?",
                "text": "Combien d'argent me reste-t-il sur mon compte ?",
                "text_preprocessed": "combien d argent me reste t il sur mon compte",
                "is_deleted": False,
            },
            "2": {
                "text_original": "Comment utiliser un numéro de carte virtuelle ?",
                "text": "Comment utiliser un numéro de carte virtuelle ?",
                "text_preprocessed": "comment utiliser un numero de carte virtuelle",
                "is_deleted": False,
            },
            "0": {
                "text_original": "créer un numéro virtuel",
                "text": "créer un numéro virtuel",
                "text_preprocessed": "creer un numero virtuel",
                "is_deleted": False,
            },
            "3": {
                "text_original": "débloquer le paiement avec carte virtuelle",
                "text": "débloquer le paiement avec carte virtuelle",
                "text_preprocessed": "debloquer le paiement avec carte virtuelle",
                "is_deleted": False,
            },
            "18": {
                "text_original": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text_preprocessed": "j ai voulu retirer de l argent et le gab a garde ma carte bancaire",
                "is_deleted": False,
            },
            "9": {
                "text_original": "Je souhaite connaître le solde de mon compte.",
                "text": "Je souhaite connaître le solde de mon compte.",
                "text_preprocessed": "je souhaite connaitre le solde de mon compte",
                "is_deleted": False,
            },
            "11": {
                "text_original": "Je voudrai connaître le solde de mes comptes.",
                "text": "Je voudrai connaître le solde de mes comptes.",
                "text_preprocessed": "je voudrai connaitre le solde de mes comptes",
                "is_deleted": False,
            },
            "19": {
                "text_original": "Le distributeur a confisqué ma carte de paiement...",
                "text": "Le distributeur a confisqué ma carte de paiement...",
                "text_preprocessed": "le distributeur a confisque ma carte de paiement",
                "is_deleted": False,
            },
            "17": {
                "text_original": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text_preprocessed": "le distributeur ne m a pas rendu ma carte bleue",
                "is_deleted": False,
            },
            "20": {
                "text_original": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text_preprocessed": "le gab a garde ma carte de credit que faire",
                "is_deleted": False,
            },
            "10": {
                "text_original": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text_preprocessed": "le solde de mon compte en banque est il dans le rouge",
                "is_deleted": False,
            },
            "15": {
                "text_original": "Mon solde bancaire est-il toujours positif ?",
                "text": "Mon solde bancaire est-il toujours positif ?",
                "text_preprocessed": "mon solde bancaire est il toujours positif",
                "is_deleted": False,
            },
            "4": {
                "text_original": "obtenir un numéro virtuel pour mes achats en ligne",
                "text": "obtenir un numéro virtuel pour mes achats en ligne",
                "text_preprocessed": "obtenir un numero virtuel pour mes achats en ligne",
                "is_deleted": False,
            },
            "5": {
                "text_original": "Où puis-je gérer mes numéros virtuels ?",
                "text": "Où puis-je gérer mes numéros virtuels ?",
                "text_preprocessed": "ou puis je gerer mes numeros virtuels",
                "is_deleted": False,
            },
            "21": {
                "text_original": "Pourquoi ma carte a-t-elle été avalée ?",
                "text": "Pourquoi ma carte a-t-elle été avalée ?",
                "text_preprocessed": "pourquoi ma carte a t elle ete avalee",
                "is_deleted": False,
            },
            "6": {
                "text_original": "Que faire pour activer une carte bancaire virtuelle ?",
                "text": "Que faire pour activer une carte bancaire virtuelle ?",
                "text_preprocessed": "que faire pour activer une carte bancaire virtuelle",
                "is_deleted": False,
            },
            "22": {
                "text_original": "Que faire si je me suis fait avaler ma carte ?",
                "text": "Que faire si je me suis fait avaler ma carte ?",
                "text_preprocessed": "que faire si je me suis fait avaler ma carte",
                "is_deleted": False,
            },
            "12": {
                "text_original": "Quel est le solde de mon compte courant ?",
                "text": "Quel est le solde de mon compte courant ?",
                "text_preprocessed": "quel est le solde de mon compte courant",
                "is_deleted": False,
            },
            "13": {
                "text_original": "Quel est mon solde bancaire ?",
                "text": "Quel est mon solde bancaire ?",
                "text_preprocessed": "quel est mon solde bancaire",
                "is_deleted": False,
            },
            "23": {
                "text_original": "récupérer carte bleue avalée par distributeur",
                "text": "récupérer carte bleue avalée par distributeur",
                "text_preprocessed": "recuperer carte bleue avalee par distributeur",
                "is_deleted": False,
            },
            "7": {
                "text_original": "supprimer un numéro de carte virtuel",
                "text": "supprimer un numéro de carte virtuel",
                "text_preprocessed": "supprimer un numero de carte virtuel",
                "is_deleted": False,
            },
        },
        "parameters": {
            "without_deleted_texts": True,
            "sorted_by": "alphabetical",
            "sorted_reverse": False,
        },
    }


# ==============================================================================
# test_ok_with_deleted
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_with_deleted(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/texts` route.

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

    # Assert route `GET /api/projects/{project_id}/texts` works.
    response_get = await async_client.get(
        url="/api/projects/1l_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts?without_deleted_texts=false"
    )
    assert response_get.status_code == 200
    assert "14" in response_get.json()["texts"].keys()
    assert response_get.json() == {
        "project_id": "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "texts": {
            "1": {
                "text_original": "activer les numéros de carte virtuelle",
                "text": "activer les numéros de carte virtuelle",
                "text_preprocessed": "activer les numeros de carte virtuelle",
                "is_deleted": False,
            },
            "16": {
                "text_original": "carte bancaire avalée",
                "text": "carte bancaire avalée",
                "text_preprocessed": "carte bancaire avalee",
                "is_deleted": False,
            },
            "8": {
                "text_original": "Combien d'argent me reste-t-il sur mon compte ?",
                "text": "Combien d'argent me reste-t-il sur mon compte ?",
                "text_preprocessed": "combien d argent me reste t il sur mon compte",
                "is_deleted": False,
            },
            "2": {
                "text_original": "Comment utiliser un numéro de carte virtuelle ?",
                "text": "Comment utiliser un numéro de carte virtuelle ?",
                "text_preprocessed": "comment utiliser un numero de carte virtuelle",
                "is_deleted": False,
            },
            "0": {
                "text_original": "créer un numéro virtuel",
                "text": "créer un numéro virtuel",
                "text_preprocessed": "creer un numero virtuel",
                "is_deleted": False,
            },
            "3": {
                "text_original": "débloquer le paiement avec carte virtuelle",
                "text": "débloquer le paiement avec carte virtuelle",
                "text_preprocessed": "debloquer le paiement avec carte virtuelle",
                "is_deleted": False,
            },
            "18": {
                "text_original": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text_preprocessed": "j ai voulu retirer de l argent et le gab a garde ma carte bancaire",
                "is_deleted": False,
            },
            "9": {
                "text_original": "Je souhaite connaître le solde de mon compte.",
                "text": "Je souhaite connaître le solde de mon compte.",
                "text_preprocessed": "je souhaite connaitre le solde de mon compte",
                "is_deleted": False,
            },
            "11": {
                "text_original": "Je voudrai connaître le solde de mes comptes.",
                "text": "Je voudrai connaître le solde de mes comptes.",
                "text_preprocessed": "je voudrai connaitre le solde de mes comptes",
                "is_deleted": False,
            },
            "19": {
                "text_original": "Le distributeur a confisqué ma carte de paiement...",
                "text": "Le distributeur a confisqué ma carte de paiement...",
                "text_preprocessed": "le distributeur a confisque ma carte de paiement",
                "is_deleted": False,
            },
            "17": {
                "text_original": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text_preprocessed": "le distributeur ne m a pas rendu ma carte bleue",
                "is_deleted": False,
            },
            "20": {
                "text_original": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text_preprocessed": "le gab a garde ma carte de credit que faire",
                "is_deleted": False,
            },
            "10": {
                "text_original": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text_preprocessed": "le solde de mon compte en banque est il dans le rouge",
                "is_deleted": False,
            },
            "15": {
                "text_original": "Mon solde bancaire est-il toujours positif ?",
                "text": "Mon solde bancaire est-il toujours positif ?",
                "text_preprocessed": "mon solde bancaire est il toujours positif",
                "is_deleted": False,
            },
            "4": {
                "text_original": "obtenir un numéro virtuel pour mes achats en ligne",
                "text": "obtenir un numéro virtuel pour mes achats en ligne",
                "text_preprocessed": "obtenir un numero virtuel pour mes achats en ligne",
                "is_deleted": False,
            },
            "5": {
                "text_original": "Où puis-je gérer mes numéros virtuels ?",
                "text": "Où puis-je gérer mes numéros virtuels ?",
                "text_preprocessed": "ou puis je gerer mes numeros virtuels",
                "is_deleted": False,
            },
            "21": {
                "text_original": "Pourquoi ma carte a-t-elle été avalée ?",
                "text": "Pourquoi ma carte a-t-elle été avalée ?",
                "text_preprocessed": "pourquoi ma carte a t elle ete avalee",
                "is_deleted": False,
            },
            "6": {
                "text_original": "Que faire pour activer une carte bancaire virtuelle ?",
                "text": "Que faire pour activer une carte bancaire virtuelle ?",
                "text_preprocessed": "que faire pour activer une carte bancaire virtuelle",
                "is_deleted": False,
            },
            "22": {
                "text_original": "Que faire si je me suis fait avaler ma carte ?",
                "text": "Que faire si je me suis fait avaler ma carte ?",
                "text_preprocessed": "que faire si je me suis fait avaler ma carte",
                "is_deleted": False,
            },
            "12": {
                "text_original": "Quel est le solde de mon compte courant ?",
                "text": "Quel est le solde de mon compte courant ?",
                "text_preprocessed": "quel est le solde de mon compte courant",
                "is_deleted": False,
            },
            "13": {
                "text_original": "Quel est mon solde bancaire ?",
                "text": "Quel est mon solde bancaire ?",
                "text_preprocessed": "quel est mon solde bancaire",
                "is_deleted": False,
            },
            "23": {
                "text_original": "récupérer carte bleue avalée par distributeur",
                "text": "récupérer carte bleue avalée par distributeur",
                "text_preprocessed": "recuperer carte bleue avalee par distributeur",
                "is_deleted": False,
            },
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
                "is_deleted": True,
            },
            "7": {
                "text_original": "supprimer un numéro de carte virtuel",
                "text": "supprimer un numéro de carte virtuel",
                "text_preprocessed": "supprimer un numero de carte virtuel",
                "is_deleted": False,
            },
        },
        "parameters": {
            "without_deleted_texts": False,
            "sorted_by": "alphabetical",
            "sorted_reverse": False,
        },
    }


# ==============================================================================
# test_ok_by_id
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_by_id(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/texts` route.

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

    # Assert route `GET /api/projects/{project_id}/texts` works.
    response_get = await async_client.get(
        url="/api/projects/1l_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts?sorted_by=id"
    )
    assert response_get.status_code == 200
    list_of_texts_id = list(response_get.json()["texts"].keys())
    assert list_of_texts_id == sorted(list_of_texts_id)
    assert response_get.json() == {
        "project_id": "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "texts": {
            "0": {
                "text_original": "créer un numéro virtuel",
                "text": "créer un numéro virtuel",
                "text_preprocessed": "creer un numero virtuel",
                "is_deleted": False,
            },
            "1": {
                "text_original": "activer les numéros de carte virtuelle",
                "text": "activer les numéros de carte virtuelle",
                "text_preprocessed": "activer les numeros de carte virtuelle",
                "is_deleted": False,
            },
            "10": {
                "text_original": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text_preprocessed": "le solde de mon compte en banque est il dans le rouge",
                "is_deleted": False,
            },
            "11": {
                "text_original": "Je voudrai connaître le solde de mes comptes.",
                "text": "Je voudrai connaître le solde de mes comptes.",
                "text_preprocessed": "je voudrai connaitre le solde de mes comptes",
                "is_deleted": False,
            },
            "12": {
                "text_original": "Quel est le solde de mon compte courant ?",
                "text": "Quel est le solde de mon compte courant ?",
                "text_preprocessed": "quel est le solde de mon compte courant",
                "is_deleted": False,
            },
            "13": {
                "text_original": "Quel est mon solde bancaire ?",
                "text": "Quel est mon solde bancaire ?",
                "text_preprocessed": "quel est mon solde bancaire",
                "is_deleted": False,
            },
            "15": {
                "text_original": "Mon solde bancaire est-il toujours positif ?",
                "text": "Mon solde bancaire est-il toujours positif ?",
                "text_preprocessed": "mon solde bancaire est il toujours positif",
                "is_deleted": False,
            },
            "16": {
                "text_original": "carte bancaire avalée",
                "text": "carte bancaire avalée",
                "text_preprocessed": "carte bancaire avalee",
                "is_deleted": False,
            },
            "17": {
                "text_original": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text_preprocessed": "le distributeur ne m a pas rendu ma carte bleue",
                "is_deleted": False,
            },
            "18": {
                "text_original": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text_preprocessed": "j ai voulu retirer de l argent et le gab a garde ma carte bancaire",
                "is_deleted": False,
            },
            "19": {
                "text_original": "Le distributeur a confisqué ma carte de paiement...",
                "text": "Le distributeur a confisqué ma carte de paiement...",
                "text_preprocessed": "le distributeur a confisque ma carte de paiement",
                "is_deleted": False,
            },
            "2": {
                "text_original": "Comment utiliser un numéro de carte virtuelle ?",
                "text": "Comment utiliser un numéro de carte virtuelle ?",
                "text_preprocessed": "comment utiliser un numero de carte virtuelle",
                "is_deleted": False,
            },
            "20": {
                "text_original": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text_preprocessed": "le gab a garde ma carte de credit que faire",
                "is_deleted": False,
            },
            "21": {
                "text_original": "Pourquoi ma carte a-t-elle été avalée ?",
                "text": "Pourquoi ma carte a-t-elle été avalée ?",
                "text_preprocessed": "pourquoi ma carte a t elle ete avalee",
                "is_deleted": False,
            },
            "22": {
                "text_original": "Que faire si je me suis fait avaler ma carte ?",
                "text": "Que faire si je me suis fait avaler ma carte ?",
                "text_preprocessed": "que faire si je me suis fait avaler ma carte",
                "is_deleted": False,
            },
            "23": {
                "text_original": "récupérer carte bleue avalée par distributeur",
                "text": "récupérer carte bleue avalée par distributeur",
                "text_preprocessed": "recuperer carte bleue avalee par distributeur",
                "is_deleted": False,
            },
            "3": {
                "text_original": "débloquer le paiement avec carte virtuelle",
                "text": "débloquer le paiement avec carte virtuelle",
                "text_preprocessed": "debloquer le paiement avec carte virtuelle",
                "is_deleted": False,
            },
            "4": {
                "text_original": "obtenir un numéro virtuel pour mes achats en ligne",
                "text": "obtenir un numéro virtuel pour mes achats en ligne",
                "text_preprocessed": "obtenir un numero virtuel pour mes achats en ligne",
                "is_deleted": False,
            },
            "5": {
                "text_original": "Où puis-je gérer mes numéros virtuels ?",
                "text": "Où puis-je gérer mes numéros virtuels ?",
                "text_preprocessed": "ou puis je gerer mes numeros virtuels",
                "is_deleted": False,
            },
            "6": {
                "text_original": "Que faire pour activer une carte bancaire virtuelle ?",
                "text": "Que faire pour activer une carte bancaire virtuelle ?",
                "text_preprocessed": "que faire pour activer une carte bancaire virtuelle",
                "is_deleted": False,
            },
            "7": {
                "text_original": "supprimer un numéro de carte virtuel",
                "text": "supprimer un numéro de carte virtuel",
                "text_preprocessed": "supprimer un numero de carte virtuel",
                "is_deleted": False,
            },
            "8": {
                "text_original": "Combien d'argent me reste-t-il sur mon compte ?",
                "text": "Combien d'argent me reste-t-il sur mon compte ?",
                "text_preprocessed": "combien d argent me reste t il sur mon compte",
                "is_deleted": False,
            },
            "9": {
                "text_original": "Je souhaite connaître le solde de mon compte.",
                "text": "Je souhaite connaître le solde de mon compte.",
                "text_preprocessed": "je souhaite connaitre le solde de mon compte",
                "is_deleted": False,
            },
        },
        "parameters": {
            "without_deleted_texts": True,
            "sorted_by": "id",
            "sorted_reverse": False,
        },
    }


# ==============================================================================
# test_ok_by_alphabetical
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_by_alphabetical(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/texts` route.

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

    # Assert route `GET /api/projects/{project_id}/texts` works.
    response_get = await async_client.get(
        url="/api/projects/1l_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts?sorted_by=alphabetical"
    )
    assert response_get.status_code == 200
    list_of_preprocessed_texts = [
        text_values["text_preprocessed"] for text_values in response_get.json()["texts"].values()
    ]
    assert list_of_preprocessed_texts == sorted(list_of_preprocessed_texts)
    assert response_get.json() == {
        "project_id": "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "texts": {
            "1": {
                "text_original": "activer les numéros de carte virtuelle",
                "text": "activer les numéros de carte virtuelle",
                "text_preprocessed": "activer les numeros de carte virtuelle",
                "is_deleted": False,
            },
            "16": {
                "text_original": "carte bancaire avalée",
                "text": "carte bancaire avalée",
                "text_preprocessed": "carte bancaire avalee",
                "is_deleted": False,
            },
            "8": {
                "text_original": "Combien d'argent me reste-t-il sur mon compte ?",
                "text": "Combien d'argent me reste-t-il sur mon compte ?",
                "text_preprocessed": "combien d argent me reste t il sur mon compte",
                "is_deleted": False,
            },
            "2": {
                "text_original": "Comment utiliser un numéro de carte virtuelle ?",
                "text": "Comment utiliser un numéro de carte virtuelle ?",
                "text_preprocessed": "comment utiliser un numero de carte virtuelle",
                "is_deleted": False,
            },
            "0": {
                "text_original": "créer un numéro virtuel",
                "text": "créer un numéro virtuel",
                "text_preprocessed": "creer un numero virtuel",
                "is_deleted": False,
            },
            "3": {
                "text_original": "débloquer le paiement avec carte virtuelle",
                "text": "débloquer le paiement avec carte virtuelle",
                "text_preprocessed": "debloquer le paiement avec carte virtuelle",
                "is_deleted": False,
            },
            "18": {
                "text_original": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text_preprocessed": "j ai voulu retirer de l argent et le gab a garde ma carte bancaire",
                "is_deleted": False,
            },
            "9": {
                "text_original": "Je souhaite connaître le solde de mon compte.",
                "text": "Je souhaite connaître le solde de mon compte.",
                "text_preprocessed": "je souhaite connaitre le solde de mon compte",
                "is_deleted": False,
            },
            "11": {
                "text_original": "Je voudrai connaître le solde de mes comptes.",
                "text": "Je voudrai connaître le solde de mes comptes.",
                "text_preprocessed": "je voudrai connaitre le solde de mes comptes",
                "is_deleted": False,
            },
            "19": {
                "text_original": "Le distributeur a confisqué ma carte de paiement...",
                "text": "Le distributeur a confisqué ma carte de paiement...",
                "text_preprocessed": "le distributeur a confisque ma carte de paiement",
                "is_deleted": False,
            },
            "17": {
                "text_original": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text_preprocessed": "le distributeur ne m a pas rendu ma carte bleue",
                "is_deleted": False,
            },
            "20": {
                "text_original": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text_preprocessed": "le gab a garde ma carte de credit que faire",
                "is_deleted": False,
            },
            "10": {
                "text_original": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text_preprocessed": "le solde de mon compte en banque est il dans le rouge",
                "is_deleted": False,
            },
            "15": {
                "text_original": "Mon solde bancaire est-il toujours positif ?",
                "text": "Mon solde bancaire est-il toujours positif ?",
                "text_preprocessed": "mon solde bancaire est il toujours positif",
                "is_deleted": False,
            },
            "4": {
                "text_original": "obtenir un numéro virtuel pour mes achats en ligne",
                "text": "obtenir un numéro virtuel pour mes achats en ligne",
                "text_preprocessed": "obtenir un numero virtuel pour mes achats en ligne",
                "is_deleted": False,
            },
            "5": {
                "text_original": "Où puis-je gérer mes numéros virtuels ?",
                "text": "Où puis-je gérer mes numéros virtuels ?",
                "text_preprocessed": "ou puis je gerer mes numeros virtuels",
                "is_deleted": False,
            },
            "21": {
                "text_original": "Pourquoi ma carte a-t-elle été avalée ?",
                "text": "Pourquoi ma carte a-t-elle été avalée ?",
                "text_preprocessed": "pourquoi ma carte a t elle ete avalee",
                "is_deleted": False,
            },
            "6": {
                "text_original": "Que faire pour activer une carte bancaire virtuelle ?",
                "text": "Que faire pour activer une carte bancaire virtuelle ?",
                "text_preprocessed": "que faire pour activer une carte bancaire virtuelle",
                "is_deleted": False,
            },
            "22": {
                "text_original": "Que faire si je me suis fait avaler ma carte ?",
                "text": "Que faire si je me suis fait avaler ma carte ?",
                "text_preprocessed": "que faire si je me suis fait avaler ma carte",
                "is_deleted": False,
            },
            "12": {
                "text_original": "Quel est le solde de mon compte courant ?",
                "text": "Quel est le solde de mon compte courant ?",
                "text_preprocessed": "quel est le solde de mon compte courant",
                "is_deleted": False,
            },
            "13": {
                "text_original": "Quel est mon solde bancaire ?",
                "text": "Quel est mon solde bancaire ?",
                "text_preprocessed": "quel est mon solde bancaire",
                "is_deleted": False,
            },
            "23": {
                "text_original": "récupérer carte bleue avalée par distributeur",
                "text": "récupérer carte bleue avalée par distributeur",
                "text_preprocessed": "recuperer carte bleue avalee par distributeur",
                "is_deleted": False,
            },
            "7": {
                "text_original": "supprimer un numéro de carte virtuel",
                "text": "supprimer un numéro de carte virtuel",
                "text_preprocessed": "supprimer un numero de carte virtuel",
                "is_deleted": False,
            },
        },
        "parameters": {
            "without_deleted_texts": True,
            "sorted_by": "alphabetical",
            "sorted_reverse": False,
        },
    }


# ==============================================================================
# test_ok_by_is_deleted
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_by_is_deleted(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/texts` route.

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

    # Assert route `GET /api/projects/{project_id}/texts` works.
    response_get = await async_client.get(
        url="/api/projects/1l_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts?without_deleted_texts=false&sorted_by=is_deleted"
    )
    assert response_get.status_code == 200
    list_of_deletion_marks = [text_values["is_deleted"] for text_values in response_get.json()["texts"].values()]
    assert list_of_deletion_marks == sorted(list_of_deletion_marks)
    assert response_get.json() == {
        "project_id": "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "texts": {
            "0": {
                "text_original": "créer un numéro virtuel",
                "text": "créer un numéro virtuel",
                "text_preprocessed": "creer un numero virtuel",
                "is_deleted": False,
            },
            "1": {
                "text_original": "activer les numéros de carte virtuelle",
                "text": "activer les numéros de carte virtuelle",
                "text_preprocessed": "activer les numeros de carte virtuelle",
                "is_deleted": False,
            },
            "2": {
                "text_original": "Comment utiliser un numéro de carte virtuelle ?",
                "text": "Comment utiliser un numéro de carte virtuelle ?",
                "text_preprocessed": "comment utiliser un numero de carte virtuelle",
                "is_deleted": False,
            },
            "3": {
                "text_original": "débloquer le paiement avec carte virtuelle",
                "text": "débloquer le paiement avec carte virtuelle",
                "text_preprocessed": "debloquer le paiement avec carte virtuelle",
                "is_deleted": False,
            },
            "4": {
                "text_original": "obtenir un numéro virtuel pour mes achats en ligne",
                "text": "obtenir un numéro virtuel pour mes achats en ligne",
                "text_preprocessed": "obtenir un numero virtuel pour mes achats en ligne",
                "is_deleted": False,
            },
            "5": {
                "text_original": "Où puis-je gérer mes numéros virtuels ?",
                "text": "Où puis-je gérer mes numéros virtuels ?",
                "text_preprocessed": "ou puis je gerer mes numeros virtuels",
                "is_deleted": False,
            },
            "6": {
                "text_original": "Que faire pour activer une carte bancaire virtuelle ?",
                "text": "Que faire pour activer une carte bancaire virtuelle ?",
                "text_preprocessed": "que faire pour activer une carte bancaire virtuelle",
                "is_deleted": False,
            },
            "7": {
                "text_original": "supprimer un numéro de carte virtuel",
                "text": "supprimer un numéro de carte virtuel",
                "text_preprocessed": "supprimer un numero de carte virtuel",
                "is_deleted": False,
            },
            "8": {
                "text_original": "Combien d'argent me reste-t-il sur mon compte ?",
                "text": "Combien d'argent me reste-t-il sur mon compte ?",
                "text_preprocessed": "combien d argent me reste t il sur mon compte",
                "is_deleted": False,
            },
            "9": {
                "text_original": "Je souhaite connaître le solde de mon compte.",
                "text": "Je souhaite connaître le solde de mon compte.",
                "text_preprocessed": "je souhaite connaitre le solde de mon compte",
                "is_deleted": False,
            },
            "10": {
                "text_original": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text_preprocessed": "le solde de mon compte en banque est il dans le rouge",
                "is_deleted": False,
            },
            "11": {
                "text_original": "Je voudrai connaître le solde de mes comptes.",
                "text": "Je voudrai connaître le solde de mes comptes.",
                "text_preprocessed": "je voudrai connaitre le solde de mes comptes",
                "is_deleted": False,
            },
            "12": {
                "text_original": "Quel est le solde de mon compte courant ?",
                "text": "Quel est le solde de mon compte courant ?",
                "text_preprocessed": "quel est le solde de mon compte courant",
                "is_deleted": False,
            },
            "13": {
                "text_original": "Quel est mon solde bancaire ?",
                "text": "Quel est mon solde bancaire ?",
                "text_preprocessed": "quel est mon solde bancaire",
                "is_deleted": False,
            },
            "15": {
                "text_original": "Mon solde bancaire est-il toujours positif ?",
                "text": "Mon solde bancaire est-il toujours positif ?",
                "text_preprocessed": "mon solde bancaire est il toujours positif",
                "is_deleted": False,
            },
            "16": {
                "text_original": "carte bancaire avalée",
                "text": "carte bancaire avalée",
                "text_preprocessed": "carte bancaire avalee",
                "is_deleted": False,
            },
            "17": {
                "text_original": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text_preprocessed": "le distributeur ne m a pas rendu ma carte bleue",
                "is_deleted": False,
            },
            "18": {
                "text_original": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text_preprocessed": "j ai voulu retirer de l argent et le gab a garde ma carte bancaire",
                "is_deleted": False,
            },
            "19": {
                "text_original": "Le distributeur a confisqué ma carte de paiement...",
                "text": "Le distributeur a confisqué ma carte de paiement...",
                "text_preprocessed": "le distributeur a confisque ma carte de paiement",
                "is_deleted": False,
            },
            "20": {
                "text_original": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text_preprocessed": "le gab a garde ma carte de credit que faire",
                "is_deleted": False,
            },
            "21": {
                "text_original": "Pourquoi ma carte a-t-elle été avalée ?",
                "text": "Pourquoi ma carte a-t-elle été avalée ?",
                "text_preprocessed": "pourquoi ma carte a t elle ete avalee",
                "is_deleted": False,
            },
            "22": {
                "text_original": "Que faire si je me suis fait avaler ma carte ?",
                "text": "Que faire si je me suis fait avaler ma carte ?",
                "text_preprocessed": "que faire si je me suis fait avaler ma carte",
                "is_deleted": False,
            },
            "23": {
                "text_original": "récupérer carte bleue avalée par distributeur",
                "text": "récupérer carte bleue avalée par distributeur",
                "text_preprocessed": "recuperer carte bleue avalee par distributeur",
                "is_deleted": False,
            },
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
                "is_deleted": True,
            },
        },
        "parameters": {
            "without_deleted_texts": False,
            "sorted_by": "is_deleted",
            "sorted_reverse": False,
        },
    }


# ==============================================================================
# test_ok_sorted_reverse
# ==============================================================================


@pytest.mark.asyncio()
async def test_ok_sorted_reverse(async_client, tmp_path):
    """
    Test the `GET /api/projects/{project_id}/texts` route.

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

    # Assert route `GET /api/projects/{project_id}/texts` works.
    response_get = await async_client.get(
        url="/api/projects/1l_ANNOTATION_WITH_UPTODATE_MODELIZATION/texts?sorted_reverse=true"
    )
    assert response_get.status_code == 200
    list_of_preprocessed_texts = [
        text_values["text_preprocessed"] for text_values in response_get.json()["texts"].values()
    ]
    assert list_of_preprocessed_texts == sorted(list_of_preprocessed_texts, reverse=True)
    assert response_get.json() == {
        "project_id": "1l_ANNOTATION_WITH_UPTODATE_MODELIZATION",
        "texts": {
            "7": {
                "text_original": "supprimer un numéro de carte virtuel",
                "text": "supprimer un numéro de carte virtuel",
                "text_preprocessed": "supprimer un numero de carte virtuel",
                "is_deleted": False,
            },
            "23": {
                "text_original": "récupérer carte bleue avalée par distributeur",
                "text": "récupérer carte bleue avalée par distributeur",
                "text_preprocessed": "recuperer carte bleue avalee par distributeur",
                "is_deleted": False,
            },
            "13": {
                "text_original": "Quel est mon solde bancaire ?",
                "text": "Quel est mon solde bancaire ?",
                "text_preprocessed": "quel est mon solde bancaire",
                "is_deleted": False,
            },
            "12": {
                "text_original": "Quel est le solde de mon compte courant ?",
                "text": "Quel est le solde de mon compte courant ?",
                "text_preprocessed": "quel est le solde de mon compte courant",
                "is_deleted": False,
            },
            "22": {
                "text_original": "Que faire si je me suis fait avaler ma carte ?",
                "text": "Que faire si je me suis fait avaler ma carte ?",
                "text_preprocessed": "que faire si je me suis fait avaler ma carte",
                "is_deleted": False,
            },
            "6": {
                "text_original": "Que faire pour activer une carte bancaire virtuelle ?",
                "text": "Que faire pour activer une carte bancaire virtuelle ?",
                "text_preprocessed": "que faire pour activer une carte bancaire virtuelle",
                "is_deleted": False,
            },
            "21": {
                "text_original": "Pourquoi ma carte a-t-elle été avalée ?",
                "text": "Pourquoi ma carte a-t-elle été avalée ?",
                "text_preprocessed": "pourquoi ma carte a t elle ete avalee",
                "is_deleted": False,
            },
            "5": {
                "text_original": "Où puis-je gérer mes numéros virtuels ?",
                "text": "Où puis-je gérer mes numéros virtuels ?",
                "text_preprocessed": "ou puis je gerer mes numeros virtuels",
                "is_deleted": False,
            },
            "4": {
                "text_original": "obtenir un numéro virtuel pour mes achats en ligne",
                "text": "obtenir un numéro virtuel pour mes achats en ligne",
                "text_preprocessed": "obtenir un numero virtuel pour mes achats en ligne",
                "is_deleted": False,
            },
            "15": {
                "text_original": "Mon solde bancaire est-il toujours positif ?",
                "text": "Mon solde bancaire est-il toujours positif ?",
                "text_preprocessed": "mon solde bancaire est il toujours positif",
                "is_deleted": False,
            },
            "10": {
                "text_original": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text_preprocessed": "le solde de mon compte en banque est il dans le rouge",
                "is_deleted": False,
            },
            "20": {
                "text_original": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text_preprocessed": "le gab a garde ma carte de credit que faire",
                "is_deleted": False,
            },
            "17": {
                "text_original": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text_preprocessed": "le distributeur ne m a pas rendu ma carte bleue",
                "is_deleted": False,
            },
            "19": {
                "text_original": "Le distributeur a confisqué ma carte de paiement...",
                "text": "Le distributeur a confisqué ma carte de paiement...",
                "text_preprocessed": "le distributeur a confisque ma carte de paiement",
                "is_deleted": False,
            },
            "11": {
                "text_original": "Je voudrai connaître le solde de mes comptes.",
                "text": "Je voudrai connaître le solde de mes comptes.",
                "text_preprocessed": "je voudrai connaitre le solde de mes comptes",
                "is_deleted": False,
            },
            "9": {
                "text_original": "Je souhaite connaître le solde de mon compte.",
                "text": "Je souhaite connaître le solde de mon compte.",
                "text_preprocessed": "je souhaite connaitre le solde de mon compte",
                "is_deleted": False,
            },
            "18": {
                "text_original": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text_preprocessed": "j ai voulu retirer de l argent et le gab a garde ma carte bancaire",
                "is_deleted": False,
            },
            "3": {
                "text_original": "débloquer le paiement avec carte virtuelle",
                "text": "débloquer le paiement avec carte virtuelle",
                "text_preprocessed": "debloquer le paiement avec carte virtuelle",
                "is_deleted": False,
            },
            "0": {
                "text_original": "créer un numéro virtuel",
                "text": "créer un numéro virtuel",
                "text_preprocessed": "creer un numero virtuel",
                "is_deleted": False,
            },
            "2": {
                "text_original": "Comment utiliser un numéro de carte virtuelle ?",
                "text": "Comment utiliser un numéro de carte virtuelle ?",
                "text_preprocessed": "comment utiliser un numero de carte virtuelle",
                "is_deleted": False,
            },
            "8": {
                "text_original": "Combien d'argent me reste-t-il sur mon compte ?",
                "text": "Combien d'argent me reste-t-il sur mon compte ?",
                "text_preprocessed": "combien d argent me reste t il sur mon compte",
                "is_deleted": False,
            },
            "16": {
                "text_original": "carte bancaire avalée",
                "text": "carte bancaire avalée",
                "text_preprocessed": "carte bancaire avalee",
                "is_deleted": False,
            },
            "1": {
                "text_original": "activer les numéros de carte virtuelle",
                "text": "activer les numéros de carte virtuelle",
                "text_preprocessed": "activer les numeros de carte virtuelle",
                "is_deleted": False,
            },
        },
        "parameters": {
            "without_deleted_texts": True,
            "sorted_by": "alphabetical",
            "sorted_reverse": True,
        },
    }
