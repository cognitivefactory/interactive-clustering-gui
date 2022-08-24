# -*- coding: utf-8 -*-

"""
* Name:         interactive-clustering-gui/tests/test_fake_backgroundtasks.run_modelization_update_task.py
* Description:  Unittests for the `fake_backgroundtasks.run_modelization_update_task` background task.
* Author:       Erwan Schild
* Created:      13/12/2021
* Licence:      CeCILL (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import json
import os

from tests.dummies_utils import create_dummy_projects

# ==============================================================================
# test_ko_not_found
# ==============================================================================


def test_ko_not_found(fake_backgroundtasks):
    """
    Test the `modelization update` task with project not existing.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
    """

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="UNKNOWN_PROJECT",
    )


# ==============================================================================
# test_ko_bad_state
# ==============================================================================


def test_ko_bad_state(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task with bad state.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "1a_SAMPLING_TODO",
        ],
    )

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="1a_SAMPLING_TODO",
    )


# ==============================================================================
# test_ok_1a
# ==============================================================================


def test_ok_1a(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "0b_INITIALIZATION_WITH_PENDING_MODELIZATION",
        ],
    )

    # Check texts.
    with open(tmp_path / "0b_INITIALIZATION_WITH_PENDING_MODELIZATION" / "texts.json", "r") as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
            "0": {
                "text_original": "créer un numéro virtuel",
                "text": "créer un numéro virtuel",
                "text_preprocessed": "créer un numéro virtuel",
                "is_deleted": False,
            },
            "1": {
                "text_original": "activer les numéros de carte virtuelle",
                "text": "activer les numéros de carte virtuelle",
                "text_preprocessed": "activer les numéros de carte virtuelle",
                "is_deleted": False,
            },
            "2": {
                "text_original": "Comment utiliser un numéro de carte virtuelle ?",
                "text": "Comment utiliser un numéro de carte virtuelle ?",
                "text_preprocessed": "Comment utiliser un numéro de carte virtuelle ?",
                "is_deleted": False,
            },
            "3": {
                "text_original": "débloquer le paiement avec carte virtuelle",
                "text": "débloquer le paiement avec carte virtuelle",
                "text_preprocessed": "débloquer le paiement avec carte virtuelle",
                "is_deleted": False,
            },
            "4": {
                "text_original": "obtenir un numéro virtuel pour mes achats en ligne",
                "text": "obtenir un numéro virtuel pour mes achats en ligne",
                "text_preprocessed": "obtenir un numéro virtuel pour mes achats en ligne",
                "is_deleted": False,
            },
            "5": {
                "text_original": "Où puis-je gérer mes numéros virtuels ?",
                "text": "Où puis-je gérer mes numéros virtuels ?",
                "text_preprocessed": "Où puis-je gérer mes numéros virtuels ?",
                "is_deleted": False,
            },
            "6": {
                "text_original": "Que faire pour activer une carte bancaire virtuelle ?",
                "text": "Que faire pour activer une carte bancaire virtuelle ?",
                "text_preprocessed": "Que faire pour activer une carte bancaire virtuelle ?",
                "is_deleted": False,
            },
            "7": {
                "text_original": "supprimer un numéro de carte virtuel",
                "text": "supprimer un numéro de carte virtuel",
                "text_preprocessed": "supprimer un numéro de carte virtuel",
                "is_deleted": False,
            },
            "8": {
                "text_original": "Combien d'argent me reste-t-il sur mon compte ?",
                "text": "Combien d'argent me reste-t-il sur mon compte ?",
                "text_preprocessed": "Combien d'argent me reste-t-il sur mon compte ?",
                "is_deleted": False,
            },
            "9": {
                "text_original": "Je souhaite connaître le solde de mon compte.",
                "text": "Je souhaite connaître le solde de mon compte.",
                "text_preprocessed": "Je souhaite connaître le solde de mon compte.",
                "is_deleted": False,
            },
            "10": {
                "text_original": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text_preprocessed": "Le solde de mon compte en banque est-il dans le rouge ?",
                "is_deleted": False,
            },
            "11": {
                "text_original": "Je voudrai connaître le solde de mes comptes.",
                "text": "Je voudrai connaître le solde de mes comptes.",
                "text_preprocessed": "Je voudrai connaître le solde de mes comptes.",
                "is_deleted": False,
            },
            "12": {
                "text_original": "Quel est le solde de mon compte courant ?",
                "text": "Quel est le solde de mon compte courant ?",
                "text_preprocessed": "Quel est le solde de mon compte courant ?",
                "is_deleted": False,
            },
            "13": {
                "text_original": "Quel est mon solde bancaire ?",
                "text": "Quel est mon solde bancaire ?",
                "text_preprocessed": "Quel est mon solde bancaire ?",
                "is_deleted": False,
            },
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
                "is_deleted": False,
            },
            "15": {
                "text_original": "Mon solde bancaire est-il toujours positif ?",
                "text": "Mon solde bancaire est-il toujours positif ?",
                "text_preprocessed": "Mon solde bancaire est-il toujours positif ?",
                "is_deleted": False,
            },
            "16": {
                "text_original": "carte bancaire avalée",
                "text": "carte bancaire avalée",
                "text_preprocessed": "carte bancaire avalée",
                "is_deleted": False,
            },
            "17": {
                "text_original": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text_preprocessed": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "is_deleted": False,
            },
            "18": {
                "text_original": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text_preprocessed": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "is_deleted": False,
            },
            "19": {
                "text_original": "Le distributeur a confisqué ma carte de paiement...",
                "text": "Le distributeur a confisqué ma carte de paiement...",
                "text_preprocessed": "Le distributeur a confisqué ma carte de paiement...",
                "is_deleted": False,
            },
            "20": {
                "text_original": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text_preprocessed": "Le GAB a gardé ma carte de crédit, que faire ?",
                "is_deleted": False,
            },
            "21": {
                "text_original": "Pourquoi ma carte a-t-elle été avalée ?",
                "text": "Pourquoi ma carte a-t-elle été avalée ?",
                "text_preprocessed": "Pourquoi ma carte a-t-elle été avalée ?",
                "is_deleted": False,
            },
            "22": {
                "text_original": "Que faire si je me suis fait avaler ma carte ?",
                "text": "Que faire si je me suis fait avaler ma carte ?",
                "text_preprocessed": "Que faire si je me suis fait avaler ma carte ?",
                "is_deleted": False,
            },
            "23": {
                "text_original": "récupérer carte bleue avalée par distributeur",
                "text": "récupérer carte bleue avalée par distributeur",
                "text_preprocessed": "récupérer carte bleue avalée par distributeur",
                "is_deleted": False,
            },
        }

    # Check modelization.
    assert "constraints_manager.pkl" not in os.listdir(tmp_path / "0b_INITIALIZATION_WITH_PENDING_MODELIZATION")
    assert "vectors_2D.json" not in os.listdir(tmp_path / "0b_INITIALIZATION_WITH_PENDING_MODELIZATION")
    assert "vectors_3D.json" not in os.listdir(tmp_path / "0b_INITIALIZATION_WITH_PENDING_MODELIZATION")
    with open(
        tmp_path / "0b_INITIALIZATION_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="0b_INITIALIZATION_WITH_PENDING_MODELIZATION",
    )

    # Assert status is updated.
    with open(tmp_path / "0b_INITIALIZATION_WITH_PENDING_MODELIZATION" / "status.json", "r") as status_after_fileobject:
        assert json.load(status_after_fileobject) == {"iteration_id": 0, "state": "CLUSTERING_TODO", "task": None}

    # Assert texts is updated.
    with open(tmp_path / "0b_INITIALIZATION_WITH_PENDING_MODELIZATION" / "texts.json", "r") as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(tmp_path / "0b_INITIALIZATION_WITH_PENDING_MODELIZATION")
    assert "vectors_2D.json" in os.listdir(tmp_path / "0b_INITIALIZATION_WITH_PENDING_MODELIZATION")
    assert "vectors_3D.json" in os.listdir(tmp_path / "0b_INITIALIZATION_WITH_PENDING_MODELIZATION")
    with open(
        tmp_path / "0b_INITIALIZATION_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        }


# ==============================================================================
# test_ok_1b
# ==============================================================================


def test_ok_1b(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION",
        ],
    )

    # Check texts.
    with open(
        tmp_path / "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
            "0": {
                "text_original": "créer un numéro virtuel",
                "text": "créer un numéro virtuel",
                "text_preprocessed": "créer un numéro virtuel",
                "is_deleted": False,
            },
            "1": {
                "text_original": "activer les numéros de carte virtuelle",
                "text": "activer les numéros de carte virtuelle",
                "text_preprocessed": "activer les numéros de carte virtuelle",
                "is_deleted": False,
            },
            "2": {
                "text_original": "Comment utiliser un numéro de carte virtuelle ?",
                "text": "Comment utiliser un numéro de carte virtuelle ?",
                "text_preprocessed": "Comment utiliser un numéro de carte virtuelle ?",
                "is_deleted": False,
            },
            "3": {
                "text_original": "débloquer le paiement avec carte virtuelle",
                "text": "débloquer le paiement avec carte virtuelle",
                "text_preprocessed": "débloquer le paiement avec carte virtuelle",
                "is_deleted": False,
            },
            "4": {
                "text_original": "obtenir un numéro virtuel pour mes achats en ligne",
                "text": "obtenir un numéro virtuel pour mes achats en ligne",
                "text_preprocessed": "obtenir un numéro virtuel pour mes achats en ligne",
                "is_deleted": False,
            },
            "5": {
                "text_original": "Où puis-je gérer mes numéros virtuels ?",
                "text": "Où puis-je gérer mes numéros virtuels ?",
                "text_preprocessed": "Où puis-je gérer mes numéros virtuels ?",
                "is_deleted": False,
            },
            "6": {
                "text_original": "Que faire pour activer une carte bancaire virtuelle ?",
                "text": "Que faire pour activer une carte bancaire virtuelle ?",
                "text_preprocessed": "Que faire pour activer une carte bancaire virtuelle ?",
                "is_deleted": False,
            },
            "7": {
                "text_original": "supprimer un numéro de carte virtuel",
                "text": "supprimer un numéro de carte virtuel",
                "text_preprocessed": "supprimer un numéro de carte virtuel",
                "is_deleted": False,
            },
            "8": {
                "text_original": "Combien d'argent me reste-t-il sur mon compte ?",
                "text": "Combien d'argent me reste-t-il sur mon compte ?",
                "text_preprocessed": "Combien d'argent me reste-t-il sur mon compte ?",
                "is_deleted": False,
            },
            "9": {
                "text_original": "Je souhaite connaître le solde de mon compte.",
                "text": "Je souhaite connaître le solde de mon compte.",
                "text_preprocessed": "Je souhaite connaître le solde de mon compte.",
                "is_deleted": False,
            },
            "10": {
                "text_original": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text_preprocessed": "Le solde de mon compte en banque est-il dans le rouge ?",
                "is_deleted": False,
            },
            "11": {
                "text_original": "Je voudrai connaître le solde de mes comptes.",
                "text": "Je voudrai connaître le solde de mes comptes.",
                "text_preprocessed": "Je voudrai connaître le solde de mes comptes.",
                "is_deleted": False,
            },
            "12": {
                "text_original": "Quel est le solde de mon compte courant ?",
                "text": "Quel est le solde de mon compte courant ?",
                "text_preprocessed": "Quel est le solde de mon compte courant ?",
                "is_deleted": False,
            },
            "13": {
                "text_original": "Quel est mon solde bancaire ?",
                "text": "Quel est mon solde bancaire ?",
                "text_preprocessed": "Quel est mon solde bancaire ?",
                "is_deleted": False,
            },
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
                "is_deleted": False,
            },
            "15": {
                "text_original": "Mon solde bancaire est-il toujours positif ?",
                "text": "Mon solde bancaire est-il toujours positif ?",
                "text_preprocessed": "Mon solde bancaire est-il toujours positif ?",
                "is_deleted": False,
            },
            "16": {
                "text_original": "carte bancaire avalée",
                "text": "carte bancaire avalée",
                "text_preprocessed": "carte bancaire avalée",
                "is_deleted": False,
            },
            "17": {
                "text_original": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text_preprocessed": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "is_deleted": False,
            },
            "18": {
                "text_original": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text_preprocessed": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "is_deleted": False,
            },
            "19": {
                "text_original": "Le distributeur a confisqué ma carte de paiement...",
                "text": "Le distributeur a confisqué ma carte de paiement...",
                "text_preprocessed": "Le distributeur a confisqué ma carte de paiement...",
                "is_deleted": False,
            },
            "20": {
                "text_original": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text_preprocessed": "Le GAB a gardé ma carte de crédit, que faire ?",
                "is_deleted": False,
            },
            "21": {
                "text_original": "Pourquoi ma carte a-t-elle été avalée ?",
                "text": "Pourquoi ma carte a-t-elle été avalée ?",
                "text_preprocessed": "Pourquoi ma carte a-t-elle été avalée ?",
                "is_deleted": False,
            },
            "22": {
                "text_original": "Que faire si je me suis fait avaler ma carte ?",
                "text": "Que faire si je me suis fait avaler ma carte ?",
                "text_preprocessed": "Que faire si je me suis fait avaler ma carte ?",
                "is_deleted": False,
            },
            "23": {
                "text_original": "récupérer carte bleue avalée par distributeur",
                "text": "récupérer carte bleue avalée par distributeur",
                "text_preprocessed": "récupérer carte bleue avalée par distributeur",
                "is_deleted": False,
            },
        }

    # Check modelization.
    assert "constraints_manager.pkl" not in os.listdir(tmp_path / "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION")
    assert "vectors_2D.json" not in os.listdir(tmp_path / "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION")
    assert "vectors_3D.json" not in os.listdir(tmp_path / "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION")
    with open(
        tmp_path / "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION",
    )

    # Assert status is updated.
    with open(
        tmp_path / "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION" / "status.json", "r"
    ) as status_after_fileobject:
        assert json.load(status_after_fileobject) == {"iteration_id": 0, "state": "CLUSTERING_TODO", "task": None}

    # Assert texts is updated.
    with open(
        tmp_path / "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(tmp_path / "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION")
    assert "vectors_2D.json" in os.listdir(tmp_path / "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION")
    assert "vectors_3D.json" in os.listdir(tmp_path / "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION")
    with open(
        tmp_path / "import_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        }


# ==============================================================================
# test_ok_2
# ==============================================================================


def test_ok_2(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
        ],
    )

    # Check texts.
    with open(
        tmp_path / "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Check modelization.
    assert "constraints_manager.pkl" not in os.listdir(
        tmp_path / "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" not in os.listdir(
        tmp_path / "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_3D.json" not in os.listdir(
        tmp_path / "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION"
    )
    with open(
        tmp_path / "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
    )

    # Assert status is updated.
    with open(
        tmp_path / "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION" / "status.json", "r"
    ) as status_after_fileobject:
        assert json.load(status_after_fileobject) == {"iteration_id": 1, "state": "SAMPLING_TODO", "task": None}

    # Assert texts is updated.
    with open(
        tmp_path / "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(
        tmp_path / "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" in os.listdir(tmp_path / "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION")
    assert "vectors_3D.json" in os.listdir(tmp_path / "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION")
    with open(
        tmp_path / "import_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        }


# ==============================================================================
# test_ok_3
# ==============================================================================


def test_ok_3(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
        ],
    )

    # Check texts.
    with open(
        tmp_path / "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Check modelization.
    assert "constraints_manager.pkl" not in os.listdir(
        tmp_path / "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" not in os.listdir(
        tmp_path / "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_3D.json" not in os.listdir(
        tmp_path / "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION"
    )
    with open(
        tmp_path / "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "1": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "2": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "3": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "4": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 1},
            "6": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "7": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "8": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "9": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "10": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "11": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "12": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": ["16"], "COMPONENT": 3},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 4},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": ["16"], "COMPONENT": 5},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": ["15", "13"], "COMPONENT": 6},
            "17": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "18": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "19": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "20": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "21": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "22": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 8},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
    )

    # Assert status is updated.
    with open(
        tmp_path / "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION" / "status.json", "r"
    ) as status_after_fileobject:
        assert json.load(status_after_fileobject) == {
            "iteration_id": 1,
            "state": "ANNOTATION_WITH_UPTODATE_MODELIZATION",
            "task": None,
        }

    # Assert texts is updated.
    with open(
        tmp_path / "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(
        tmp_path / "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" in os.listdir(tmp_path / "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION")
    assert "vectors_3D.json" in os.listdir(tmp_path / "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION")
    with open(
        tmp_path / "import_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "1": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "2": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "3": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "4": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 1},
            "6": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "7": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "8": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "9": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "10": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "11": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "12": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": ["16"], "COMPONENT": 3},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 4},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": ["16"], "COMPONENT": 5},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": ["15", "13"], "COMPONENT": 6},
            "17": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "18": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "19": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "20": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "21": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "22": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 8},
        }


# ==============================================================================
# test_ok_4
# ==============================================================================


def test_ok_4(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
        ],
    )

    # Check texts.
    with open(
        tmp_path / "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Check modelization.
    assert "constraints_manager.pkl" not in os.listdir(
        tmp_path / "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" not in os.listdir(
        tmp_path / "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_3D.json" not in os.listdir(
        tmp_path / "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION"
    )
    with open(
        tmp_path / "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "1": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "2": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "3": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "4": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 1},
            "6": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "7": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "8": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "9": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "10": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "11": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "12": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": ["16"], "COMPONENT": 3},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 4},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": ["16"], "COMPONENT": 5},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": ["15", "13"], "COMPONENT": 6},
            "17": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "18": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "19": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "20": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "21": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "22": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 8},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
    )

    # Assert status is updated.
    with open(
        tmp_path / "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION" / "status.json", "r"
    ) as status_after_fileobject:
        assert json.load(status_after_fileobject) == {"iteration_id": 1, "state": "CLUSTERING_TODO", "task": None}

    # Assert texts is updated.
    with open(
        tmp_path / "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(
        tmp_path / "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" in os.listdir(tmp_path / "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION")
    assert "vectors_3D.json" in os.listdir(tmp_path / "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION")
    with open(
        tmp_path / "import_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "1": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "2": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "3": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "4": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 1},
            "6": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "7": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "8": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "9": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "10": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "11": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "12": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": ["16"], "COMPONENT": 3},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 4},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": ["16"], "COMPONENT": 5},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": ["15", "13"], "COMPONENT": 6},
            "17": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "18": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "19": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "20": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "21": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "22": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 8},
        }


# ==============================================================================
# test_ok_5
# ==============================================================================


def test_ok_5(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
        ],
    )

    # Check texts.
    with open(
        tmp_path / "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Check modelization.
    assert "constraints_manager.pkl" not in os.listdir(
        tmp_path / "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" not in os.listdir(
        tmp_path / "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_3D.json" not in os.listdir(
        tmp_path / "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION"
    )
    with open(
        tmp_path / "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "1": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "2": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "3": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "4": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 1},
            "6": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "7": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "8": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "9": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "10": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "11": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "12": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": ["16"], "COMPONENT": 3},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 4},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": ["16"], "COMPONENT": 5},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": ["15", "13"], "COMPONENT": 6},
            "17": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "18": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "19": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "20": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "21": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "22": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 8},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
    )

    # Assert status is updated.
    with open(
        tmp_path / "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION" / "status.json", "r"
    ) as status_after_fileobject:
        assert json.load(status_after_fileobject) == {"iteration_id": 1, "state": "ITERATION_END", "task": None}

    # Assert texts is updated.
    with open(
        tmp_path / "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(
        tmp_path / "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" in os.listdir(tmp_path / "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION")
    assert "vectors_3D.json" in os.listdir(tmp_path / "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION")
    with open(
        tmp_path / "import_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "1": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "2": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "3": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "4": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 1},
            "6": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "7": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "8": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "9": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "10": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "11": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "12": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": ["16"], "COMPONENT": 3},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 4},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": ["16"], "COMPONENT": 5},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": ["15", "13"], "COMPONENT": 6},
            "17": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "18": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "19": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "20": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "21": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "22": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 7,
            },
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 8},
        }


# ==============================================================================
# test_ok_6
# ==============================================================================


def test_ok_6(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS",
        ],
    )

    # Check texts.
    with open(
        tmp_path / "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS" / "texts.json", "r"
    ) as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
                "is_deleted": True,
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
        }

    # Check modelization.
    assert "constraints_manager.pkl" in os.listdir(
        tmp_path / "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS"
    )
    assert "vectors_2D.json" in os.listdir(tmp_path / "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS")
    assert "vectors_3D.json" in os.listdir(tmp_path / "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS")
    with open(
        tmp_path / "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS",
    )

    # Assert status is updated.
    with open(
        tmp_path / "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS" / "status.json", "r"
    ) as status_after_fileobject:
        assert json.load(status_after_fileobject) == {
            "iteration_id": 1,
            "state": "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
            "task": None,
        }

    # Assert texts is updated.
    with open(
        tmp_path / "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS" / "texts.json", "r"
    ) as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
                "is_deleted": True,
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(
        tmp_path / "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS"
    )
    assert "vectors_2D.json" in os.listdir(tmp_path / "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS")
    assert "vectors_3D.json" in os.listdir(tmp_path / "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS")
    with open(
        tmp_path / "1f_ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4"],
                "CANNOT_LINK": ["22", "20", "21", "7", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "1": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4"],
                "CANNOT_LINK": ["22", "20", "21", "7", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "2": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4"],
                "CANNOT_LINK": ["22", "20", "21", "7", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "3": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4"],
                "CANNOT_LINK": ["22", "20", "21", "7", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "4": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4"],
                "CANNOT_LINK": ["22", "20", "21", "7", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 1},
            "6": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4"],
                "CANNOT_LINK": ["22", "20", "21", "7", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": ["4", "0", "1", "2", "3", "6"], "COMPONENT": 2},
            "8": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 3,
            },
            "9": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 3,
            },
            "10": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 3,
            },
            "11": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 3,
            },
            "12": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 3,
            },
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": ["16"], "COMPONENT": 4},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": ["16"], "COMPONENT": 5},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": ["15", "13"], "COMPONENT": 6},
            "17": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4"],
                "COMPONENT": 7,
            },
            "18": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4"],
                "COMPONENT": 7,
            },
            "19": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4"],
                "COMPONENT": 7,
            },
            "20": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4"],
                "COMPONENT": 7,
            },
            "21": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4"],
                "COMPONENT": 7,
            },
            "22": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4"],
                "COMPONENT": 7,
            },
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 8},
        }


# ==============================================================================
# test_ok_7
# ==============================================================================


def test_ok_7(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS",
        ],
    )

    # Check texts.
    with open(
        tmp_path / "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS" / "texts.json", "r"
    ) as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
                "is_deleted": True,
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
        }

    # Check modelization.
    assert "constraints_manager.pkl" in os.listdir(tmp_path / "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS")
    assert "vectors_2D.json" in os.listdir(tmp_path / "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS")
    assert "vectors_3D.json" in os.listdir(tmp_path / "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS")
    with open(
        tmp_path / "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4"],
                "CANNOT_LINK": ["22", "20", "21", "7", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "1": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4"],
                "CANNOT_LINK": ["22", "20", "21", "7", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "2": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4"],
                "CANNOT_LINK": ["22", "20", "21", "7", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "3": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4"],
                "CANNOT_LINK": ["22", "20", "21", "7", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "4": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4"],
                "CANNOT_LINK": ["22", "20", "21", "7", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 1},
            "6": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4"],
                "CANNOT_LINK": ["22", "20", "21", "7", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": ["4", "0", "1", "2", "3", "6"], "COMPONENT": 2},
            "8": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 3,
            },
            "9": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 3,
            },
            "10": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 3,
            },
            "11": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 3,
            },
            "12": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 3,
            },
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": ["16"], "COMPONENT": 4},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": ["16"], "COMPONENT": 5},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": ["15", "13"], "COMPONENT": 6},
            "17": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4"],
                "COMPONENT": 7,
            },
            "18": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4"],
                "COMPONENT": 7,
            },
            "19": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4"],
                "COMPONENT": 7,
            },
            "20": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4"],
                "COMPONENT": 7,
            },
            "21": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4"],
                "COMPONENT": 7,
            },
            "22": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4"],
                "COMPONENT": 7,
            },
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 8},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS",
    )

    # Assert status is updated.
    with open(
        tmp_path / "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS" / "status.json", "r"
    ) as status_after_fileobject:
        assert json.load(status_after_fileobject) == {
            "iteration_id": 1,
            "state": "ANNOTATION_WITH_UPTODATE_MODELIZATION",
            "task": None,
        }

    # Assert texts is updated.
    with open(
        tmp_path / "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS" / "texts.json", "r"
    ) as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
                "is_deleted": True,
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(tmp_path / "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS")
    assert "vectors_2D.json" in os.listdir(tmp_path / "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS")
    assert "vectors_3D.json" in os.listdir(tmp_path / "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS")
    with open(
        tmp_path / "1j_ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "1": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "2": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "3": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "4": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 1},
            "6": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "7": {
                "MUST_LINK": ["1", "2", "3", "6", "0", "4", "7"],
                "CANNOT_LINK": ["22", "20", "21", "17", "19", "18"],
                "COMPONENT": 0,
            },
            "8": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "9": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "10": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "11": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "12": {
                "MUST_LINK": ["8", "11", "10", "12", "9"],
                "CANNOT_LINK": ["22", "18", "20", "21", "17", "19"],
                "COMPONENT": 2,
            },
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": ["16"], "COMPONENT": 3},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": ["16"], "COMPONENT": 4},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": ["15", "13"], "COMPONENT": 5},
            "17": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 6,
            },
            "18": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 6,
            },
            "19": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 6,
            },
            "20": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 6,
            },
            "21": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 6,
            },
            "22": {
                "MUST_LINK": ["18", "19", "17", "21", "20", "22"],
                "CANNOT_LINK": ["8", "11", "10", "12", "9", "6", "1", "2", "3", "0", "4", "7"],
                "COMPONENT": 6,
            },
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 7},
        }


# ==============================================================================
# test_ok_erreur_1
# ==============================================================================


def test_ok_erreur_1(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION",
        ],
    )

    # Check texts.
    with open(
        tmp_path / "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
            "0": {
                "text_original": "créer un numéro virtuel",
                "text": "créer un numéro virtuel",
                "text_preprocessed": "créer un numéro virtuel",
                "is_deleted": False,
            },
            "1": {
                "text_original": "activer les numéros de carte virtuelle",
                "text": "activer les numéros de carte virtuelle",
                "text_preprocessed": "activer les numéros de carte virtuelle",
                "is_deleted": False,
            },
            "2": {
                "text_original": "Comment utiliser un numéro de carte virtuelle ?",
                "text": "Comment utiliser un numéro de carte virtuelle ?",
                "text_preprocessed": "Comment utiliser un numéro de carte virtuelle ?",
                "is_deleted": False,
            },
            "3": {
                "text_original": "débloquer le paiement avec carte virtuelle",
                "text": "débloquer le paiement avec carte virtuelle",
                "text_preprocessed": "débloquer le paiement avec carte virtuelle",
                "is_deleted": False,
            },
            "4": {
                "text_original": "obtenir un numéro virtuel pour mes achats en ligne",
                "text": "obtenir un numéro virtuel pour mes achats en ligne",
                "text_preprocessed": "obtenir un numéro virtuel pour mes achats en ligne",
                "is_deleted": False,
            },
            "5": {
                "text_original": "Où puis-je gérer mes numéros virtuels ?",
                "text": "Où puis-je gérer mes numéros virtuels ?",
                "text_preprocessed": "Où puis-je gérer mes numéros virtuels ?",
                "is_deleted": False,
            },
            "6": {
                "text_original": "Que faire pour activer une carte bancaire virtuelle ?",
                "text": "Que faire pour activer une carte bancaire virtuelle ?",
                "text_preprocessed": "Que faire pour activer une carte bancaire virtuelle ?",
                "is_deleted": False,
            },
            "7": {
                "text_original": "supprimer un numéro de carte virtuel",
                "text": "supprimer un numéro de carte virtuel",
                "text_preprocessed": "supprimer un numéro de carte virtuel",
                "is_deleted": False,
            },
            "8": {
                "text_original": "Combien d'argent me reste-t-il sur mon compte ?",
                "text": "Combien d'argent me reste-t-il sur mon compte ?",
                "text_preprocessed": "Combien d'argent me reste-t-il sur mon compte ?",
                "is_deleted": False,
            },
            "9": {
                "text_original": "Je souhaite connaître le solde de mon compte.",
                "text": "Je souhaite connaître le solde de mon compte.",
                "text_preprocessed": "Je souhaite connaître le solde de mon compte.",
                "is_deleted": False,
            },
            "10": {
                "text_original": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text": "Le solde de mon compte en banque est-il dans le rouge ?",
                "text_preprocessed": "Le solde de mon compte en banque est-il dans le rouge ?",
                "is_deleted": False,
            },
            "11": {
                "text_original": "Je voudrai connaître le solde de mes comptes.",
                "text": "Je voudrai connaître le solde de mes comptes.",
                "text_preprocessed": "Je voudrai connaître le solde de mes comptes.",
                "is_deleted": False,
            },
            "12": {
                "text_original": "Quel est le solde de mon compte courant ?",
                "text": "Quel est le solde de mon compte courant ?",
                "text_preprocessed": "Quel est le solde de mon compte courant ?",
                "is_deleted": False,
            },
            "13": {
                "text_original": "Quel est mon solde bancaire ?",
                "text": "Quel est mon solde bancaire ?",
                "text_preprocessed": "Quel est mon solde bancaire ?",
                "is_deleted": False,
            },
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
                "is_deleted": False,
            },
            "15": {
                "text_original": "Mon solde bancaire est-il toujours positif ?",
                "text": "Mon solde bancaire est-il toujours positif ?",
                "text_preprocessed": "Mon solde bancaire est-il toujours positif ?",
                "is_deleted": False,
            },
            "16": {
                "text_original": "carte bancaire avalée",
                "text": "carte bancaire avalée",
                "text_preprocessed": "carte bancaire avalée",
                "is_deleted": False,
            },
            "17": {
                "text_original": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "text_preprocessed": "Le distributeur ne m'a pas rendu ma carte bleue.",
                "is_deleted": False,
            },
            "18": {
                "text_original": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "text_preprocessed": "J'ai voulu retirer de l'argent, et le gab a gardé ma carte bancaire.",
                "is_deleted": False,
            },
            "19": {
                "text_original": "Le distributeur a confisqué ma carte de paiement...",
                "text": "Le distributeur a confisqué ma carte de paiement...",
                "text_preprocessed": "Le distributeur a confisqué ma carte de paiement...",
                "is_deleted": False,
            },
            "20": {
                "text_original": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text": "Le GAB a gardé ma carte de crédit, que faire ?",
                "text_preprocessed": "Le GAB a gardé ma carte de crédit, que faire ?",
                "is_deleted": False,
            },
            "21": {
                "text_original": "Pourquoi ma carte a-t-elle été avalée ?",
                "text": "Pourquoi ma carte a-t-elle été avalée ?",
                "text_preprocessed": "Pourquoi ma carte a-t-elle été avalée ?",
                "is_deleted": False,
            },
            "22": {
                "text_original": "Que faire si je me suis fait avaler ma carte ?",
                "text": "Que faire si je me suis fait avaler ma carte ?",
                "text_preprocessed": "Que faire si je me suis fait avaler ma carte ?",
                "is_deleted": False,
            },
            "23": {
                "text_original": "récupérer carte bleue avalée par distributeur",
                "text": "récupérer carte bleue avalée par distributeur",
                "text_preprocessed": "récupérer carte bleue avalée par distributeur",
                "is_deleted": False,
            },
        }

    # Check modelization.
    assert "constraints_manager.pkl" not in os.listdir(
        tmp_path / "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" not in os.listdir(tmp_path / "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION")
    assert "vectors_3D.json" not in os.listdir(tmp_path / "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION")
    with open(
        tmp_path / "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION",
    )

    # Assert status is updated.
    with open(
        tmp_path / "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION" / "status.json", "r"
    ) as status_after_fileobject:
        assert json.load(status_after_fileobject) == {
            "iteration_id": 0,
            "state": "INITIALIZATION_WITH_ERRORS",
            "task": None,
        }

    # Assert texts is updated.
    with open(
        tmp_path / "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(
        tmp_path / "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" in os.listdir(tmp_path / "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION")
    assert "vectors_3D.json" in os.listdir(tmp_path / "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION")
    with open(
        tmp_path / "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": ["7", "1", "6"], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "7": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 6},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 7},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 8},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 9},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 10},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 11},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 12},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 13},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 14},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 15},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 16},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 17},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 18},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 19},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 20},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 21},
        }
    with open(
        tmp_path / "import_error_0y1_INITIALIZATION_WITH_PENDING_MODELIZATION" / "constraints.json", "r"
    ) as constraints_after_fileobject:
        assert json.load(constraints_after_fileobject) == {
            "(4,7)": {
                "data": {"id_1": "4", "id_2": "7"},
                "constraint_type": "CANNOT_LINK",
                "constraint_type_previous": [None, "MUST_LINK"],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657545553.46324,
                "iteration_of_sampling": 0,
            },
            "(1,6)": {
                "data": {"id_1": "1", "id_2": "6"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657543490.330898,
                "iteration_of_sampling": 0,
            },
            "(1,7)": {
                "data": {"id_1": "1", "id_2": "7"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657543507.347849,
                "iteration_of_sampling": 0,
            },
            "(4,6)": {
                "data": {"id_1": "4", "id_2": "6"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": True,
                "comment": "",
                "date_of_update": 1657545344.703469,
                "iteration_of_sampling": 0,
            },
        }


# ==============================================================================
# test_ok_erreur_2
# ==============================================================================


def test_ok_erreur_2(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
        ],
    )

    # Check texts.
    with open(
        tmp_path / "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Check modelization.
    assert "constraints_manager.pkl" not in os.listdir(
        tmp_path / "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" not in os.listdir(
        tmp_path / "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_3D.json" not in os.listdir(
        tmp_path / "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION"
    )
    with open(
        tmp_path / "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
    )

    # Assert status is updated.
    with open(
        tmp_path / "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION" / "status.json", "r"
    ) as status_after_fileobject:
        assert json.load(status_after_fileobject) == {
            "iteration_id": 1,
            "state": "IMPORT_AT_SAMPLING_STEP_WITH_ERRORS",
            "task": None,
        }

    # Assert texts is updated.
    with open(
        tmp_path / "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(
        tmp_path / "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" in os.listdir(
        tmp_path / "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_3D.json" in os.listdir(
        tmp_path / "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION"
    )
    with open(
        tmp_path / "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": ["7", "1", "6"], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "7": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 6},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 7},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 8},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 9},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 10},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 11},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 12},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 13},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 14},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 15},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 16},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 17},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 18},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 19},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 20},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 21},
        }
    with open(
        tmp_path / "import_error_1w1_IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION" / "constraints.json", "r"
    ) as constraints_after_fileobject:
        assert json.load(constraints_after_fileobject) == {
            "(4,7)": {
                "data": {"id_1": "4", "id_2": "7"},
                "constraint_type": "CANNOT_LINK",
                "constraint_type_previous": [None, "MUST_LINK"],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657545553.46324,
                "iteration_of_sampling": 0,
            },
            "(1,6)": {
                "data": {"id_1": "1", "id_2": "6"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657543490.330898,
                "iteration_of_sampling": 0,
            },
            "(1,7)": {
                "data": {"id_1": "1", "id_2": "7"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657543507.347849,
                "iteration_of_sampling": 0,
            },
            "(4,6)": {
                "data": {"id_1": "4", "id_2": "6"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": True,
                "comment": "",
                "date_of_update": 1657545344.703469,
                "iteration_of_sampling": 0,
            },
        }


# ==============================================================================
# test_ok_erreur_3
# ==============================================================================


def test_ok_erreur_3(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
        ],
    )

    # Check texts.
    with open(
        tmp_path / "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Check modelization.
    assert "constraints_manager.pkl" not in os.listdir(
        tmp_path / "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" not in os.listdir(
        tmp_path / "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_3D.json" not in os.listdir(
        tmp_path / "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION"
    )
    with open(
        tmp_path / "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
    )

    # Assert status is updated.
    with open(
        tmp_path / "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION" / "status.json", "r"
    ) as status_after_fileobject:
        assert json.load(status_after_fileobject) == {
            "iteration_id": 1,
            "state": "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
            "task": None,
        }

    # Assert texts is updated.
    with open(
        tmp_path / "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(
        tmp_path / "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" in os.listdir(
        tmp_path / "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_3D.json" in os.listdir(
        tmp_path / "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION"
    )
    with open(
        tmp_path / "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": ["7", "1", "6"], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "7": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 6},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 7},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 8},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 9},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 10},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 11},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 12},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 13},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 14},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 15},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 16},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 17},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 18},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 19},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 20},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 21},
        }
    with open(
        tmp_path / "import_error_1x1_IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION" / "constraints.json", "r"
    ) as constraints_after_fileobject:
        assert json.load(constraints_after_fileobject) == {
            "(4,7)": {
                "data": {"id_1": "4", "id_2": "7"},
                "constraint_type": "CANNOT_LINK",
                "constraint_type_previous": [None, "MUST_LINK"],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657545553.46324,
                "iteration_of_sampling": 0,
            },
            "(1,6)": {
                "data": {"id_1": "1", "id_2": "6"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657543490.330898,
                "iteration_of_sampling": 0,
            },
            "(1,7)": {
                "data": {"id_1": "1", "id_2": "7"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657543507.347849,
                "iteration_of_sampling": 0,
            },
            "(4,6)": {
                "data": {"id_1": "4", "id_2": "6"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": True,
                "comment": "",
                "date_of_update": 1657545344.703469,
                "iteration_of_sampling": 0,
            },
        }


# ==============================================================================
# test_ok_erreur_4
# ==============================================================================


def test_ok_erreur_4(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
        ],
    )

    # Check texts.
    with open(
        tmp_path / "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Check modelization.
    assert "constraints_manager.pkl" not in os.listdir(
        tmp_path / "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" not in os.listdir(
        tmp_path / "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_3D.json" not in os.listdir(
        tmp_path / "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION"
    )
    with open(
        tmp_path / "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
    )

    # Assert status is updated.
    with open(
        tmp_path / "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION" / "status.json", "r"
    ) as status_after_fileobject:
        assert json.load(status_after_fileobject) == {
            "iteration_id": 1,
            "state": "IMPORT_AT_CLUSTERING_STEP_WITH_ERRORS",
            "task": None,
        }

    # Assert texts is updated.
    with open(
        tmp_path / "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(
        tmp_path / "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" in os.listdir(
        tmp_path / "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_3D.json" in os.listdir(
        tmp_path / "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION"
    )
    with open(
        tmp_path / "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": ["7", "1", "6"], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "7": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 6},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 7},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 8},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 9},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 10},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 11},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 12},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 13},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 14},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 15},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 16},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 17},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 18},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 19},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 20},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 21},
        }
    with open(
        tmp_path / "import_error_1y1_IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION" / "constraints.json", "r"
    ) as constraints_after_fileobject:
        assert json.load(constraints_after_fileobject) == {
            "(4,7)": {
                "data": {"id_1": "4", "id_2": "7"},
                "constraint_type": "CANNOT_LINK",
                "constraint_type_previous": [None, "MUST_LINK"],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657545553.46324,
                "iteration_of_sampling": 0,
            },
            "(1,6)": {
                "data": {"id_1": "1", "id_2": "6"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657543490.330898,
                "iteration_of_sampling": 0,
            },
            "(1,7)": {
                "data": {"id_1": "1", "id_2": "7"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657543507.347849,
                "iteration_of_sampling": 0,
            },
            "(4,6)": {
                "data": {"id_1": "4", "id_2": "6"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": True,
                "comment": "",
                "date_of_update": 1657545344.703469,
                "iteration_of_sampling": 0,
            },
        }


# ==============================================================================
# test_ok_erreur_5
# ==============================================================================


def test_ok_erreur_5(fake_backgroundtasks, tmp_path):
    """
    Test the `modelization update` task works.

    Args:
        fake_backgroundtasks: Fixture providing a backgroundtasks module, declared in `conftest.py`.
        tmp_path: Pytest fixture: points to a temporary directory.
    """

    # Create dummy projects.
    create_dummy_projects(
        tmp_path=tmp_path,
        list_of_dummy_project_ids=[
            "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
        ],
    )

    # Check texts.
    with open(
        tmp_path / "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_before_fileobject:
        assert json.load(texts_before_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Check modelization.
    assert "constraints_manager.pkl" not in os.listdir(
        tmp_path / "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" not in os.listdir(
        tmp_path / "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_3D.json" not in os.listdir(
        tmp_path / "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION"
    )
    with open(
        tmp_path / "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_before_fileobject:
        assert json.load(modelization_before_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1"], "CANNOT_LINK": [], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": [], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["6"], "CANNOT_LINK": [], "COMPONENT": 6},
            "7": {"MUST_LINK": ["7"], "CANNOT_LINK": [], "COMPONENT": 7},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 8},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 9},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 10},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 11},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 12},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 13},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 14},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 15},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 16},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 17},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 18},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 19},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 20},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 21},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 22},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 23},
        }

    # Run the task.
    fake_backgroundtasks.run_modelization_update_task(
        project_id="import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
    )

    # Assert status is updated.
    with open(
        tmp_path / "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION" / "status.json", "r"
    ) as status_after_fileobject:
        assert json.load(status_after_fileobject) == {
            "iteration_id": 1,
            "state": "IMPORT_AT_ITERATION_END_WITH_ERRORS",
            "task": None,
        }

    # Assert texts is updated.
    with open(
        tmp_path / "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION" / "texts.json", "r"
    ) as texts_after_fileobject:
        assert json.load(texts_after_fileobject) == {
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
            "14": {
                "text_original": "solde de mon compte en banque",
                "text": "solde de mon compte en banque",
                "text_preprocessed": "solde de mon compte en banque",
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
        }

    # Assert modelization is updated.
    assert "constraints_manager.pkl" in os.listdir(
        tmp_path / "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_2D.json" in os.listdir(
        tmp_path / "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION"
    )
    assert "vectors_3D.json" in os.listdir(
        tmp_path / "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION"
    )
    with open(
        tmp_path / "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION" / "modelization.json", "r"
    ) as modelization_after_fileobject:
        assert json.load(modelization_after_fileobject) == {
            "0": {"MUST_LINK": ["0"], "CANNOT_LINK": [], "COMPONENT": 0},
            "1": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "2": {"MUST_LINK": ["2"], "CANNOT_LINK": [], "COMPONENT": 2},
            "3": {"MUST_LINK": ["3"], "CANNOT_LINK": [], "COMPONENT": 3},
            "4": {"MUST_LINK": ["4"], "CANNOT_LINK": ["7", "1", "6"], "COMPONENT": 4},
            "5": {"MUST_LINK": ["5"], "CANNOT_LINK": [], "COMPONENT": 5},
            "6": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "7": {"MUST_LINK": ["1", "6", "7"], "CANNOT_LINK": ["4"], "COMPONENT": 1},
            "8": {"MUST_LINK": ["8"], "CANNOT_LINK": [], "COMPONENT": 6},
            "9": {"MUST_LINK": ["9"], "CANNOT_LINK": [], "COMPONENT": 7},
            "10": {"MUST_LINK": ["10"], "CANNOT_LINK": [], "COMPONENT": 8},
            "11": {"MUST_LINK": ["11"], "CANNOT_LINK": [], "COMPONENT": 9},
            "12": {"MUST_LINK": ["12"], "CANNOT_LINK": [], "COMPONENT": 10},
            "13": {"MUST_LINK": ["13"], "CANNOT_LINK": [], "COMPONENT": 11},
            "14": {"MUST_LINK": ["14"], "CANNOT_LINK": [], "COMPONENT": 12},
            "15": {"MUST_LINK": ["15"], "CANNOT_LINK": [], "COMPONENT": 13},
            "16": {"MUST_LINK": ["16"], "CANNOT_LINK": [], "COMPONENT": 14},
            "17": {"MUST_LINK": ["17"], "CANNOT_LINK": [], "COMPONENT": 15},
            "18": {"MUST_LINK": ["18"], "CANNOT_LINK": [], "COMPONENT": 16},
            "19": {"MUST_LINK": ["19"], "CANNOT_LINK": [], "COMPONENT": 17},
            "20": {"MUST_LINK": ["20"], "CANNOT_LINK": [], "COMPONENT": 18},
            "21": {"MUST_LINK": ["21"], "CANNOT_LINK": [], "COMPONENT": 19},
            "22": {"MUST_LINK": ["22"], "CANNOT_LINK": [], "COMPONENT": 20},
            "23": {"MUST_LINK": ["23"], "CANNOT_LINK": [], "COMPONENT": 21},
        }
    with open(
        tmp_path / "import_error_1z1_IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION" / "constraints.json", "r"
    ) as constraints_after_fileobject:
        assert json.load(constraints_after_fileobject) == {
            "(4,7)": {
                "data": {"id_1": "4", "id_2": "7"},
                "constraint_type": "CANNOT_LINK",
                "constraint_type_previous": [None, "MUST_LINK"],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657545553.46324,
                "iteration_of_sampling": 0,
            },
            "(1,6)": {
                "data": {"id_1": "1", "id_2": "6"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657543490.330898,
                "iteration_of_sampling": 0,
            },
            "(1,7)": {
                "data": {"id_1": "1", "id_2": "7"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": False,
                "comment": "",
                "date_of_update": 1657543507.347849,
                "iteration_of_sampling": 0,
            },
            "(4,6)": {
                "data": {"id_1": "4", "id_2": "6"},
                "constraint_type": "MUST_LINK",
                "constraint_type_previous": [None],
                "is_hidden": False,
                "to_annotate": False,
                "to_review": True,
                "to_fix_conflict": True,
                "comment": "",
                "date_of_update": 1657545344.703469,
                "iteration_of_sampling": 0,
            },
        }
