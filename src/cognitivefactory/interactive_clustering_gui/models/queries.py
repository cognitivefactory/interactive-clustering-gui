# -*- coding: utf-8 -*-

"""
* Name:         cognitivefactory.interactive_clustering_gui.models.queries
* Description:  Definition of model parameters required to define query parameters of interactive clustering.
* Author:       Erwan Schild
* Created:      07/02/2022
* Licence:      CeCILL-C License v1.0 (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import enum

# ==============================================================================
# BASE MODEL FOR CONSTRAINTS ANNOTATION
# ==============================================================================


class ConstraintsValues(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available constraints values."""

    MUST_LINK: str = "MUST_LINK"
    CANNOT_LINK: str = "CANNOT_LINK"


# ==============================================================================
# BASE MODEL FOR CONSTRAINTS
# ==============================================================================


class ConstraintsSortOptions(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available options for constraints sort."""

    ID: str = "id"
    TEXT: str = "text"
    CONSTRAINT_TYPE: str = "constraint_type"
    DATE_OF_UPDATE: str = "date_of_update"
    ITERATION_OF_SAMPLING: str = "iteration_of_sampling"
    TO_ANNOTATE: str = "to_annotate"
    TO_REVIEW: str = "to_review"
    TO_FIX_CONFLICT: str = "to_fix_conflict"


# ==============================================================================
# BASE MODEL FOR TEXTS
# ==============================================================================


class TextsSortOptions(str, enum.Enum):  # noqa: WPS600 (subclassing str)
    """The enumeration of available options for texts sort."""

    ID: str = "id"
    ALPHABETICAL: str = "alphabetical"
    IS_DELETED: str = "is_deleted"
