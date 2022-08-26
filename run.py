"""Script used to run the program."""


# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

from uvicorn import Config, Server
from uvicorn.supervisors import ChangeReload


# ==============================================================================
# RUN APPLICATION
# ==============================================================================
def run(host: str = "127.0.0.1", port: int = 8080) -> None:  # noqa: S104
    """
    Run the Uvicorn server for debug.

    Args:
        host (str, optional): The host to bind. Defaults to `"127.0.0.1"`.
        port (int, optional): The port to use. Defaults to `8080`.
    """

    # Config the serveur.
    config = Config(
        "cognitivefactory.interactive_clustering_gui.app:app",
        host=host,
        port=port,
        log_level="debug",
        reload=True,
    )
    server = Server(config)

    # Run the web app with reload option.
    sock = config.bind_socket()
    ChangeReload(config, target=server.run, sockets=[sock]).run()
