# -*- coding: utf-8 -*-

"""
* Name:         cognitivefactory.interactive_clustering_gui
* Description:  Web application for Interactive Clustering methodology.
* Author:       Erwan SCHILD
* Created:      22/10/2021
* Licence:      CeCILL (https://cecill.info/licences.fr.html)

Several modules and files are needed for this web application:

- `app`: the main application file, that defines FastAPI routes (project management, ). See [interactive_clustering_gui/app](https://cognitivefactory.github.io/interactive-clustering-gui/reference/cognitivefactory/interactive_clustering_gui/app/) documentation ;
- `backgroundtasks`: the worker file, that defines tasks to run in background (). See [interactive_clustering_gui/backgroundtasks](https://cognitivefactory.github.io/interactive-clustering-gui/reference/cognitivefactory/interactive_clustering_gui/backgroundtasks/) documentation ;
- `models`: the models file, that defines requests parameters and application states. See [interactive_clustering_gui/models](https://cognitivefactory.github.io/interactive-clustering-gui/reference/cognitivefactory/interactive_clustering_gui/models/) documentation ;
- `cli`: the command line input functionnalities, needed to launch the app. See [interactive_clustering_gui/cli](https://cognitivefactory.github.io/interactive-clustering-gui/reference/cognitivefactory/interactive_clustering_gui/cli/) documentation.
"""

from typing import List

__all__: List[str] = []  # noqa: WPS410 (the only __variable__ we use)
