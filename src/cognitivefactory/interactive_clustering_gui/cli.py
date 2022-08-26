# -*- coding: utf-8 -*-

"""
* Name:         cognitivefactory.interactive_clustering_gui.cli
* Description:  Module that contains the command line application.
* Author:       Erwan Schild
* Created:      22/10/2021
* Licence:      CeCILL-C License v1.0 (https://cecill.info/licences.fr.html)

Why does this file exist, and why not put this in `__main__`?

You might be tempted to import things from `__main__` later, but that will cause problems: the code will get executed twice:
- When you run `python -m cognitivefactory.interactive_clustering_gui` python will execute `__main__.py` as a script. That means there won't be any `cognitivefactory.interactive_clustering_gui.__main__` in `sys.modules`.
- When you import `__main__` it will get executed again (as a module) because there's no `cognitivefactory.interactive_clustering_gui.__main__` in `sys.modules`.
"""


# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import argparse
from typing import List, Optional

from uvicorn import Config, Server


# ==============================================================================
# DEFINE CLI ARGUMENTS PARSER
# ==============================================================================
def get_parser() -> argparse.ArgumentParser:
    """
    Define possible arguments of the CLI argument parser.

    Returns:
        An argparse parser.
    """
    parser = argparse.ArgumentParser(
        prog="cognitivefactory-interactive-clustering-gui",
        description="A web application designed for NLP data annotation using Interactive Clustering methodology.",
        epilog="For more details, https://cognitivefactory.github.io/interactive-clustering-gui/",
    )
    parser.add_argument(
        "--host", type=str, default="127.0.0.1", help="The host to bind. Defaults to `127.0.0.1`.",
    )
    parser.add_argument("--port", type=int, default=8080, help="The port to use. Defaults to `8080`.",)
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["critical", "error", "warning", "info", "debug", "trace"],
        default="info",
        help="The log level. Defaults to `info`.",
    )
    return parser


# ==============================================================================
# MAIN TO RUN WEB APPLICATION
# ==============================================================================


def main(args: Optional[List[str]] = None) -> None:  # noqa: S104
    """
    Run the main program.

    This function is executed when you type `cognitivefactory-interactive-clustering-gui` or `python -m cognitivefactory.interactive_clustering_gui`.

    Args:
        args: Arguments passed from the command line.
    """
    # Parse CLI arguments.
    parser = get_parser()
    opts = parser.parse_args(args=args)

    # Config the serveur.
    config = Config(
        "cognitivefactory.interactive_clustering_gui.app:app",
        host=opts.host,  # The host to bind.
        port=opts.port,  # The port to use.
        log_level=opts.log_level,  # The log level.
    )
    server = Server(config)

    # Launch the server.
    server.run()
