# -*- coding: utf-8 -*-

"""
* Name:         cognitivefactory.interactive_clustering_gui.__main__
* Description:  Entry-point module, in case you use `python -m cognitivefactory.interactive_clustering_gui`.
* Author:       Erwan Schild
* Created:      22/10/2021
* Licence:      CeCILL-C License v1.0 (https://cecill.info/licences.fr.html)

Why does this file exist, and why `__main__`? For more info, read:

- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import sys

from cognitivefactory.interactive_clustering_gui.cli import main

# ==============================================================================
# MAIN SCRIPT
# ==============================================================================


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
