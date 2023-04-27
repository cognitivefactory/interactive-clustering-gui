# -*- coding: utf-8 -*-

"""
* Name:         cognitivefactory.interactive_clustering_gui.app
* Description:  Definition of FastAPI application and routes for interactive clustering graphical user interface.
* Author:       Erwan Schild
* Created:      22/10/2021
* Licence:      CeCILL-C License v1.0 (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import html
import json
import os
import pathlib
import shutil
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Tuple

import pandas as pd
from dateutil import tz
from fastapi import (
    BackgroundTasks,
    Body,
    FastAPI,
    File,
    HTTPException,
    Path,
    Query,
    Request,
    Response,
    UploadFile,
    status,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse  # HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from filelock import FileLock
from importlib_metadata import version
from prometheus_client import Gauge
from prometheus_fastapi_instrumentator import Instrumentator, metrics
from zipp import zipfile

from cognitivefactory.interactive_clustering_gui import backgroundtasks
from cognitivefactory.interactive_clustering_gui.models.queries import (
    ConstraintsSortOptions,
    ConstraintsValues,
    TextsSortOptions,
)
from cognitivefactory.interactive_clustering_gui.models.settings import (
    ClusteringSettingsModel,
    ICGUISettings,
    PreprocessingSettingsModel,
    SamplingSettingsModel,
    VectorizationSettingsModel,
    default_ClusteringSettingsModel,
    default_PreprocessingSettingsModel,
    default_SamplingSettingsModel,
    default_VectorizationSettingsModel,
)
from cognitivefactory.interactive_clustering_gui.models.states import ICGUIStates, get_ICGUIStates_details

# ==============================================================================
# CONFIGURE FASTAPI APPLICATION
# ==============================================================================

# Create an FastAPI instance of Interactive Clustering Graphical User Interface.
app = FastAPI(
    title="Interactive Clustering GUI",
    description="Web application for Interactive Clustering methodology",
    version=version("cognitivefactory-interactive-clustering-gui"),
)

# Add Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=[  # origins for which we allow CORS (Cross-Origin Resource Sharing).
        "http://localhost:8000",  # locally served docs.
        # "https://cognitivefactory.github.io/interactive-clustering-gui/",  # deployed docs.
        # you could add `http://your_vm_hostname:8000`.
    ],
)

# Mount `css`, `javascript` and `resources` files.
app.mount("/css", StaticFiles(directory=pathlib.Path(__file__).parent / "css"), name="css")
app.mount("/js", StaticFiles(directory=pathlib.Path(__file__).parent / "js"), name="js")
app.mount("/resources", StaticFiles(directory=pathlib.Path(__file__).parent / "resources"), name="resources")

# Define `DATA_DIRECTORY` (where data are stored).
DATA_DIRECTORY = pathlib.Path(os.environ.get("DATA_DIRECTORY", ".data"))
DATA_DIRECTORY.mkdir(parents=True, exist_ok=True)


# ==============================================================================
# CONFIGURE JINJA2 TEMPLATES
# ==============================================================================

# Define HTML templates to render.
templates = Jinja2Templates(directory=pathlib.Path(__file__).parent / "html")


# Define function to convert timestamp to date.
def timestamp_to_date(timestamp: float, timezone_str: str = "Europe/Paris") -> str:
    """
    From timestamp to date.

    Args:
        timestamp (float): The timstamp to convert.
        timezone_str (str, optional): The time zone. Defaults to `"Europe/Paris"`.

    Returns:
        str: The requested date.
    """
    timezone = tz.gettz(timezone_str)
    return datetime.fromtimestamp(timestamp, timezone).strftime("%d/%m/%Y")


templates.env.filters["timestamp_to_date"] = timestamp_to_date


# Define function to convert timestamp to hour.
def timestamp_to_hour(timestamp: float, timezone_str: str = "Europe/Paris") -> str:
    """
    From timestamp to hours.

    Args:
        timestamp (float): The timstamp to convert.
        timezone_str (str, optional): The time zone. Defaults to `"Europe/Paris"`.

    Returns:
        str: The requested hour.
    """
    timezone = tz.gettz(timezone_str)
    return datetime.fromtimestamp(timestamp, timezone).strftime("%H:%M:%S")


templates.env.filters["timestamp_to_hour"] = timestamp_to_hour


# Define function to get previous key in a dictionary.
def get_previous_key(key: str, dictionary: Dict[str, Any]) -> Optional[str]:
    """
    Get previous key in a dictionary.

    Args:
        key (str): The current key.
        dictionary (Dict[str, Any]): The dictionary.

    Returns:
        Optional[str]: The previous key.
    """
    list_of_keys: List[str] = list(dictionary.keys())
    if key in list_of_keys:
        previous_key_index: int = list_of_keys.index(key) - 1
        return list_of_keys[previous_key_index] if 0 <= previous_key_index else None
    return None


templates.env.filters["get_previous_key"] = get_previous_key


# Define function to get next key in a dictionary.
def get_next_key(key: str, dictionary: Dict[str, Any]) -> Optional[str]:
    """
    Get next key in a dictionary.

    Args:
        key (str): The current key.
        dictionary (Dict[str, Any]): The dictionary.

    Returns:
        Optional[str]: The next key.
    """
    list_of_keys: List[str] = list(dictionary.keys())
    if key in list_of_keys:
        next_key_index: int = list_of_keys.index(key) + 1
        return list_of_keys[next_key_index] if next_key_index < len(list_of_keys) else None
    return None


templates.env.filters["get_next_key"] = get_next_key


# ==============================================================================
# CONFIGURE FASTAPI METRICS
# ==============================================================================


def prometheus_disk_usage() -> Callable[[metrics.Info], None]:
    """
    Define a metric of disk usage.

    Returns:
        Callable[[metrics.Info], None]: instrumentation.
    """
    gaugemetric = Gauge(
        "disk_usage",
        "The disk usage in %",
    )

    def instrumentation(info: metrics.Info) -> None:  # noqa: WPS430 (nested function)
        total, used, _ = shutil.disk_usage(DATA_DIRECTORY)
        gaugemetric.set(used * 100 / total)

    return instrumentation


# Define application instrumentator and add metrics.
instrumentator = Instrumentator()
instrumentator.add(metrics.default())
instrumentator.add(prometheus_disk_usage())
instrumentator.instrument(app)
instrumentator.expose(app)


# ==============================================================================
# DEFINE STATE ROUTES FOR APPLICATION STATE
# ==============================================================================


###
### STATE: Startup event.
###
@app.on_event("startup")
async def startup() -> None:  # pragma: no cover
    """Startup event."""

    # Initialize ready state.
    app.state.ready = False

    # Apply database connection, long loading, etc.

    # Update ready state when done.
    app.state.ready = True


###
### STATE: Check if app is ready.
###
@app.get(
    "/ready",
    tags=["app state"],
    status_code=status.HTTP_200_OK,
)
async def ready() -> Response:  # pragma: no cover
    """
    Tell if the API is ready.

    Returns:
        An HTTP response with either 200 or 503 codes.
    """

    # Return 200_OK if ready.
    if app.state.ready:
        return Response(status_code=status.HTTP_200_OK)

    # Return 503_SERVICE_UNAVAILABLE otherwise.
    return Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)


###
### STATE: Check if app is alive.
###
@app.get(
    "/alive",
    tags=["app state"],
    status_code=status.HTTP_200_OK,
)
async def alive() -> Response:  # pragma: no cover
    """
    Tell if the API is alive/healthy.

    Returns:
        Response: An HTTP response with either 200 or 503 codes.
    """

    try:
        # Assert the volume can be reached.
        pathlib.Path(DATA_DIRECTORY / ".available").touch()
        # Or anything else asserting the API is healthy.
    except OSError:
        return Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    return Response(status_code=status.HTTP_200_OK)


# ==============================================================================
# DEFINE ROUTES FOR HOME AND DOCUMENTATION
# ==============================================================================


###
### ROUTE: Get HTML welcome page.
###
@app.get(
    "/",
    tags=["Home and Documentation"],
    response_class=Response,
    status_code=status.HTTP_200_OK,
)
async def get_html_welcome_page(
    request: Request,
) -> Response:
    """
    Define HTML welcome page.

    Args:
        request (Request): The request context.

    Returns:
        Response: The requested page.
    """

    # Return HTML welcome page.
    return templates.TemplateResponse(
        name="welcome.html",
        context={
            "request": request,
        },
        status_code=status.HTTP_200_OK,
    )


###
### ROUTE: Get HTML help page.
###
@app.get(
    "/gui/help",
    tags=["Home and Documentation"],
    response_class=Response,
    status_code=status.HTTP_200_OK,
)
async def get_html_help_page(
    request: Request,
) -> Response:
    """
    Get HTML help page.

    Args:
        request (Request): The request context.

    Returns:
        Response: The requested page.
    """

    # Return HTML help page.
    return templates.TemplateResponse(
        name="help.html",
        context={
            "request": request,
        },
        status_code=status.HTTP_200_OK,
    )


# ==============================================================================
# DEFINE ROUTES FOR PROJECT MANAGEMENT
# ==============================================================================


###
### ROUTE: Get the list of existing project IDs.
###
@app.get(
    "/api/projects",
    tags=["Projects"],
    status_code=status.HTTP_200_OK,
)
async def get_projects() -> List[str]:
    """
    Get the list of existing project IDs.
    (A project is represented by a subfolder in `.data` folder.)

    Returns:
        List[str]: The list of existing project IDs.
    """

    # Return the list of project IDs.
    return [project_id for project_id in os.listdir(DATA_DIRECTORY) if os.path.isdir(DATA_DIRECTORY / project_id)]


###
### ROUTE: Create a project.
###
@app.post(
    "/api/projects",
    tags=["Projects"],
    status_code=status.HTTP_201_CREATED,
)
async def create_project(
    project_name: str = Query(
        ...,
        description="The name of the project. Should not be an empty string.",
        min_length=3,
        max_length=64,
    ),
    dataset_file: UploadFile = File(
        ...,
        description="The dataset file to load. Use a `.csv` (`;` separator) or `.xlsx` file. Please use a list of texts in the first column, without header, with encoding 'utf-8'.",
        # TODO: max_size="8MB",
    ),
) -> Dict[str, Any]:
    """
    Create a project.

    Args:
        project_name (str): The name of the project. Should not be an empty string.
        dataset_file (UploadFile): The dataset file to load. Use a `.csv` (`;` separator) or `.xlsx` file. Please use a list of texts in the first column, without header, with encoding 'utf-8'.

    Raises:
        HTTPException: Raises `HTTP_400_BAD_REQUEST` if parameters `project_name` or `dataset_file` are invalid.

    Returns:
        Dict[str, Any]: A dictionary that contains the ID of the created project.
    """

    # Define the new project ID.
    current_timestamp: float = datetime.now().timestamp()
    current_project_id: str = str(int(current_timestamp * 10**6))

    # Check project name.
    if project_name.strip() == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The project name '{project_name_str}' is invalid.".format(
                project_name_str=str(project_name),
            ),
        )

    # Initialize variable to store loaded dataset.
    list_of_texts: List[str] = []

    # Load dataset: Case of `.csv` with `;` separator.
    if dataset_file.content_type in {"text/csv", "application/vnd.ms-excel"}:
        # "text/csv" == ".csv"
        # "application/vnd.ms-excel" == ".xls"
        try:  # noqa: WPS229  # Found too long `try` body length
            dataset_csv: pd.Dataframe = pd.read_csv(
                filepath_or_buffer=dataset_file.file,
                sep=";",
                header=None,  # No header expected in the csv file.
            )
            list_of_texts = dataset_csv[dataset_csv.columns[0]].tolist()
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The dataset file is invalid. `.csv` file, with `;` separator, must contain a list of texts in the first column, with no header.",
            )
    # Load dataset: Case of `.xlsx`.
    elif dataset_file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        # "application/vnd.ms-excel" == ".xlsx"
        try:  # noqa: WPS229  # Found too long `try` body length
            dataset_xlsx: pd.Dataframe = pd.read_excel(
                io=dataset_file.file.read(),
                engine="openpyxl",
                header=None,  # No header expected in the xlsx file.
            )
            list_of_texts = dataset_xlsx[dataset_xlsx.columns[0]].tolist()
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The dataset file is invalid. `.xlsx` file must contain a list of texts in the first column, with no header.",
            )

    # Load dataset: case of not supported type.
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The file type '{dataset_file_type}' is not supported. Please use '.csv' (`;` separator) or '.xlsx' file.".format(
                dataset_file_type=str(dataset_file.content_type),
            ),
        )

    # Create the directory and subdirectories of the new project.
    os.mkdir(DATA_DIRECTORY / current_project_id)

    # Initialize storage of metadata.
    with open(DATA_DIRECTORY / current_project_id / "metadata.json", "w") as metadata_fileobject:
        json.dump(
            {
                "project_id": current_project_id,
                "project_name": str(project_name.strip()),
                "creation_timestamp": current_timestamp,
            },
            metadata_fileobject,
            indent=4,
        )

    # Initialize storage of status.
    with open(DATA_DIRECTORY / current_project_id / "status.json", "w") as status_fileobject:
        json.dump(
            {
                "iteration_id": 0,  # Use string format for JSON serialization in dictionaries.
                "state": ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION,
                "task": None,  # "progression", "detail".
            },
            status_fileobject,
            indent=4,
        )

    # Initialize storage of texts.
    with open(DATA_DIRECTORY / current_project_id / "texts.json", "w") as texts_fileobject:
        json.dump(
            {
                str(i): {
                    "text_original": str(text),  # Will never be changed.
                    "text": str(text),  # Can be change by renaming.
                    "text_preprocessed": str(text),  # Will be preprocessed during `Modelizationpdate` task.
                    "is_deleted": False,
                }
                for i, text in enumerate(list_of_texts)
            },
            texts_fileobject,
            indent=4,
        )

    # Initialize storage of constraints.
    with open(DATA_DIRECTORY / current_project_id / "constraints.json", "w") as constraints_fileobject:
        json.dump(
            {},  # Dict[str, Any]
            constraints_fileobject,
            indent=4,
        )

    # Initialize storage of modelization inference assignations.
    with open(DATA_DIRECTORY / current_project_id / "modelization.json", "w") as modelization_fileobject:
        json.dump(
            {str(i): {"MUST_LINK": [str(i)], "CANNOT_LINK": [], "COMPONENT": i} for i in range(len(list_of_texts))},
            modelization_fileobject,
            indent=4,
        )

    # Initialize settings storage.
    with open(DATA_DIRECTORY / current_project_id / "settings.json", "w") as settings_fileobject:
        json.dump(
            {
                "0": {
                    "preprocessing": default_PreprocessingSettingsModel().to_dict(),
                    "vectorization": default_VectorizationSettingsModel().to_dict(),
                    "clustering": default_ClusteringSettingsModel().to_dict(),
                },
            },
            settings_fileobject,
            indent=4,
        )

    # Initialize storage of sampling results.
    with open(DATA_DIRECTORY / current_project_id / "sampling.json", "w") as sampling_fileobject:
        json.dump({}, sampling_fileobject, indent=4)  # Dict[str, List[str]]

    # Initialize storage of clustering results.
    with open(DATA_DIRECTORY / current_project_id / "clustering.json", "w") as clustering_fileobject:
        json.dump({}, clustering_fileobject, indent=4)  # Dict[str, Dict[str, str]]

    # Return the ID of the created project.
    return {
        "project_id": current_project_id,
        "detail": "The project with name '{project_name_str}' has been created. It has the id '{project_id_str}'.".format(
            project_name_str=str(project_name),
            project_id_str=str(current_project_id),
        ),
    }


###
### ROUTE: Delete a project.
###
@app.delete(
    "/api/projects/{project_id}",
    tags=["Projects"],
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_project(
    project_id: str = Path(
        ...,
        description="The ID of the project to delete.",
    ),
) -> Dict[str, Any]:
    """
    Delete a project.

    Args:
        project_id (str): The ID of the project to delete.

    Returns:
        Dict[str, Any]: A dictionary that contains the ID of the deleted project.
    """

    # Delete the project.
    if os.path.isdir(DATA_DIRECTORY / project_id):
        shutil.rmtree(DATA_DIRECTORY / project_id, ignore_errors=True)

    # Return the deleted project id.
    return {
        "project_id": project_id,
        "detail": "The deletion of project with id '{project_id_str}' is accepted.".format(
            project_id_str=str(project_id),
        ),
    }


###
### ROUTE: Get metadata.
###
@app.get(
    "/api/projects/{project_id}/metadata",
    tags=["Projects"],
    status_code=status.HTTP_200_OK,
)
async def get_metadata(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
) -> Dict[str, Any]:
    """
    Get metadata.

    Args:
        project_id (str): The ID of the project.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.

    Returns:
        Dict[str, Any]: A dictionary that contains metadata.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Load the project metadata.
    with open(DATA_DIRECTORY / project_id / "metadata.json", "r") as metadata_fileobject:
        # Return the project metadata.
        return {
            "project_id": project_id,
            "metadata": json.load(metadata_fileobject),
        }


###
### ROUTE: Download a project in a zip archive.
###
@app.get(
    "/api/projects/{project_id}/download",
    tags=["Projects"],
    response_class=FileResponse,
    status_code=status.HTTP_200_OK,
)
async def download_project(
    background_tasks: BackgroundTasks,
    project_id: str = Path(
        ...,
        description="The ID of the project to download.",
    ),
) -> FileResponse:
    """
    Download a project in a zip archive.

    Args:
        background_tasks (BackgroundTasks): A background task to run after the return statement.
        project_id (str): The ID of the project to download.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.

    Returns:
        FileResponse: A zip archive of the project.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Define archive name.
    archive_name: str = "archive-{project_id_str}.zip".format(project_id_str=str(project_id))
    archive_path: pathlib.Path = DATA_DIRECTORY / project_id / archive_name

    # Zip the project in an archive.
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive_filewriter:
        archive_filewriter.write(DATA_DIRECTORY / project_id / "metadata.json", arcname="metadata.json")
        archive_filewriter.write(DATA_DIRECTORY / project_id / "status.json", arcname="status.json")
        archive_filewriter.write(DATA_DIRECTORY / project_id / "texts.json", arcname="texts.json")
        archive_filewriter.write(DATA_DIRECTORY / project_id / "constraints.json", arcname="constraints.json")
        archive_filewriter.write(DATA_DIRECTORY / project_id / "settings.json", arcname="settings.json")
        archive_filewriter.write(DATA_DIRECTORY / project_id / "sampling.json", arcname="sampling.json")
        archive_filewriter.write(DATA_DIRECTORY / project_id / "clustering.json", arcname="clustering.json")
        archive_filewriter.write(DATA_DIRECTORY / project_id / "modelization.json", arcname="modelization.json")
        if "vectors_2D.json" in os.listdir(DATA_DIRECTORY / project_id):
            archive_filewriter.write(DATA_DIRECTORY / project_id / "vectors_2D.json", arcname="vectors_2D.json")
        if "vectors_3D.json" in os.listdir(DATA_DIRECTORY / project_id):
            archive_filewriter.write(DATA_DIRECTORY / project_id / "vectors_3D.json", arcname="vectors_3D.json")

    # Define a backgroundtask to clear archive after downloading.
    def clear_after_download_project():  # noqa: WPS430 (nested function)
        """
        Delete the archive file.
        """

        # Delete archive file.
        if os.path.exists(archive_path):  # pragma: no cover
            os.remove(archive_path)

    # Add the background task.
    background_tasks.add_task(
        func=clear_after_download_project,
    )

    # Return the zip archive of the project.
    return FileResponse(
        archive_path,
        media_type="application/x-zip-compressed",
        filename=archive_name,
    )


###
### ROUTE: Import a project.
###
@app.put(
    "/api/projects",
    tags=["Projects"],
    status_code=status.HTTP_201_CREATED,
)
async def import_project(
    background_tasks: BackgroundTasks,
    project_archive: UploadFile = File(
        ...,
        description="A zip archive representing a project. Use format from `download` route.",
        # TODO: max_size="8MB",
    ),
) -> Dict[str, Any]:
    """
    Import a project from a zip archive file.

    Args:
        background_tasks (BackgroundTasks): A background task to run after the return statement.
        project_archive (UploadFile, optional): A zip archive representing a project. Use format from `download` route.

    Raises:
        HTTPException: Raises `HTTP_400_NOT_FOUND` if archive is invalid.

    Returns:
        Dict[str, Any]: A dictionary that contains the ID of the imported project.
    """

    # Check archive type.
    if project_archive.content_type != "application/x-zip-compressed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The file type '{project_archive_type}' is not supported. Please use '.zip' file.".format(
                project_archive_type=str(project_archive.content_type),
            ),
        )

    # Temporarly store zip archive.
    current_timestamp: float = datetime.now().timestamp()
    new_current_project_id: str = str(int(current_timestamp * 10**6))
    import_archive_name: str = "import-{new_current_project_id_str}.zip".format(
        new_current_project_id_str=str(new_current_project_id)
    )
    import_archive_path: pathlib.Path = DATA_DIRECTORY / import_archive_name
    with open(import_archive_path, "wb") as import_archive_fileobject_w:
        shutil.copyfileobj(project_archive.file, import_archive_fileobject_w)

    # Define a backgroundtask to clear archive after importation.
    def clear_after_import_project():  # noqa: WPS430 (nested function)
        """
        Delete the archive file.
        """

        # Delete archive file.
        if os.path.exists(import_archive_path):  # pragma: no cover
            os.remove(import_archive_path)

    # Add the background task.
    background_tasks.add_task(
        func=clear_after_import_project,
    )

    # Try to open archive file.
    try:
        with zipfile.ZipFile(import_archive_path, "r") as import_archive_file:
            ###
            ### Check archive content.
            ###
            missing_files: List[str] = [
                needed_file
                for needed_file in (
                    "metadata.json",
                    "status.json",
                    "texts.json",
                    "constraints.json",
                    "settings.json",
                    "sampling.json",
                    "clustering.json",
                    "modelization.json",  # Will be recomputed during modelization step.
                    # "vectors_2D.json",  # Will be recomputed during modelization step.
                    # "vectors_3D.json",  # Will be recomputed during modelization step.
                )
                if needed_file not in import_archive_file.namelist()
            ]
            if len(missing_files) != 0:  # noqa: WPS507
                raise ValueError(
                    "The project archive file doesn't contains the following files: {missing_files_str}.".format(
                        missing_files_str=str(missing_files),
                    )
                )

            ###
            ### Check `metadata.json`.
            ###
            with import_archive_file.open("metadata.json") as metadata_fileobject_r:
                metadata: Dict[str, Any] = json.load(metadata_fileobject_r)
            metadata["project_id"] = new_current_project_id
            if (
                "project_name" not in metadata.keys()
                or not isinstance(metadata["project_name"], str)
                or "creation_timestamp" not in metadata.keys()
                or not isinstance(metadata["creation_timestamp"], float)
            ):
                raise ValueError("The project archive file has an invalid `metadata.json` file.")

            ###
            ### Check `status.json`.
            ###
            with import_archive_file.open("status.json") as status_fileobject_r:
                project_status: Dict[str, Any] = json.load(status_fileobject_r)

            # Check `status.state`.
            if "state" not in project_status.keys():
                raise ValueError("The project archive file has an invalid `status.json` file (see key `state`).")

            # Force `status.state` - Case of initialization.
            if (
                project_status["state"] == ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION  # noqa: WPS514
                or project_status["state"] == ICGUIStates.INITIALIZATION_WITH_PENDING_MODELIZATION
                or project_status["state"] == ICGUIStates.INITIALIZATION_WITH_WORKING_MODELIZATION
                or project_status["state"] == ICGUIStates.INITIALIZATION_WITH_ERRORS
            ):
                project_status["state"] = ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION
            # Force `status.state` - Case of sampling.
            elif (
                project_status["state"] == ICGUIStates.SAMPLING_TODO  # noqa: WPS514
                or project_status["state"] == ICGUIStates.SAMPLING_PENDING
                or project_status["state"] == ICGUIStates.SAMPLING_WORKING
                or project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION
                or project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION
                or project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION
                or project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_ERRORS
            ):
                project_status["state"] = ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION
            # Force `status.state` - Case of annotation.
            elif (
                project_status["state"] == ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION  # noqa: WPS514
                or project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
                or project_status["state"] == ICGUIStates.ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS
                or project_status["state"] == ICGUIStates.ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS
                or project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
                or project_status["state"] == ICGUIStates.ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS
                or project_status["state"] == ICGUIStates.ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS
                or project_status["state"] == ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION
                or project_status["state"] == ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION
                or project_status["state"] == ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION
            ):
                project_status["state"] = ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION
            # Force `status.state` - Case of clustering.
            elif (
                project_status["state"] == ICGUIStates.CLUSTERING_TODO  # noqa: WPS514
                or project_status["state"] == ICGUIStates.CLUSTERING_PENDING
                or project_status["state"] == ICGUIStates.CLUSTERING_WORKING
                or project_status["state"] == ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION
                or project_status["state"] == ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION
                or project_status["state"] == ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION
                or project_status["state"] == ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITH_ERRORS
            ):
                project_status["state"] = ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION
            # Force `status.state` - Case of iteration end.
            elif (
                project_status["state"] == ICGUIStates.ITERATION_END  # noqa: WPS514
                or project_status["state"] == ICGUIStates.IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION
                or project_status["state"] == ICGUIStates.IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION
                or project_status["state"] == ICGUIStates.IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION
                or project_status["state"] == ICGUIStates.IMPORT_AT_ITERATION_END_WITH_ERRORS
            ):
                project_status["state"] = ICGUIStates.IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION
            # Force `state` - Case of unknown state.
            else:
                raise ValueError("The project archive file has an invalid `status.json` file (see key `state`).")

            # Force `status.task`.
            project_status["task"] = None

            # TODO: Check `texts.json`.
            with import_archive_file.open("texts.json") as texts_fileobject_r:
                texts: Dict[str, Dict[str, Any]] = json.load(texts_fileobject_r)

            # TODO: Check `constraints.json`.
            with import_archive_file.open("constraints.json") as constraints_fileobject_r:
                constraints: Dict[str, Dict[str, Any]] = json.load(constraints_fileobject_r)

            # TODO: Check `settings.json`.
            with import_archive_file.open("settings.json") as settings_fileobject_r:
                settings: Dict[str, Dict[str, Any]] = json.load(settings_fileobject_r)

            # TODO: Check `sampling.json`.
            with import_archive_file.open("sampling.json") as sampling_fileobject_r:
                sampling: Dict[str, List[str]] = json.load(sampling_fileobject_r)

            # TODO: Check `clustering.json`.
            with import_archive_file.open("clustering.json") as clustering_fileobject_r:
                clustering: Dict[str, Dict[str, str]] = json.load(clustering_fileobject_r)

            # TODO: Check `modelization.json`.
            with import_archive_file.open("modelization.json") as modelization_fileobject_r:
                modelization: Dict[str, Dict[str, Any]] = json.load(modelization_fileobject_r)

    # Error: case of custom raised errors.
    except ValueError as value_error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(value_error),
        )

    # Error: other raised errors.
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An error occurs in project import. Project archive is probably invalid.",
        )

    # Create the directory and subdirectories of the new project.
    os.mkdir(DATA_DIRECTORY / metadata["project_id"])

    # Store `metadata.json`.
    with open(DATA_DIRECTORY / metadata["project_id"] / "metadata.json", "w") as metadata_fileobject_w:
        json.dump(metadata, metadata_fileobject_w, indent=4)

    # Store `status.json`.
    with open(DATA_DIRECTORY / metadata["project_id"] / "status.json", "w") as status_fileobject_w:
        json.dump(project_status, status_fileobject_w, indent=4)

    # Store `texts.json`.
    with open(DATA_DIRECTORY / metadata["project_id"] / "texts.json", "w") as texts_fileobject_w:
        json.dump(texts, texts_fileobject_w, indent=4)

    # Store `constraints.json`.
    with open(DATA_DIRECTORY / metadata["project_id"] / "constraints.json", "w") as constraints_fileobject_w:
        json.dump(constraints, constraints_fileobject_w, indent=4)

    # Store `settings.json`.
    with open(DATA_DIRECTORY / metadata["project_id"] / "settings.json", "w") as settings_fileobject_w:
        json.dump(settings, settings_fileobject_w, indent=4)

    # Store `sampling.json`.
    with open(DATA_DIRECTORY / metadata["project_id"] / "sampling.json", "w") as sampling_fileobject_w:
        json.dump(sampling, sampling_fileobject_w, indent=4)

    # Store `clustering.json`.
    with open(DATA_DIRECTORY / metadata["project_id"] / "clustering.json", "w") as clustering_fileobject_w:
        json.dump(clustering, clustering_fileobject_w, indent=4)

    # Store `modelization.json`.
    with open(DATA_DIRECTORY / metadata["project_id"] / "modelization.json", "w") as modelization_fileobject_w:
        json.dump(modelization, modelization_fileobject_w, indent=4)

    # Return the new ID of the imported project.
    return {
        "project_id": metadata["project_id"],
        "detail": "The project with name '{project_name_str}' has been imported. It has the id '{project_id_str}'.".format(
            project_name_str=str(metadata["project_name"]),
            project_id_str=str(metadata["project_id"]),
        ),
    }


###
### ROUTE: Get HTML projects listing or creation page.
###
@app.get(
    "/gui/projects",
    tags=["Projects"],
    response_class=Response,
    status_code=status.HTTP_200_OK,
)
async def get_html_projects_listing_or_creation_page(
    request: Request,
) -> Response:
    """
    Get HTML projects listing or creation page.

    Args:
        request (Request): The request context.

    Returns:
        Response: The requested page.
    """

    # Return HTML projects listing and creation page.
    return templates.TemplateResponse(
        name="projects_listing.html",
        context={
            "request": request,
            # Get projects and their description.
            "projects": {
                project_id: {
                    "metadata": (await get_metadata(project_id=project_id))["metadata"],
                    "status": (await get_status(project_id=project_id))["status"],
                }
                for project_id in (await get_projects())
            },
        },
        status_code=status.HTTP_200_OK,
    )


###
### ROUTE: Get HTML project home page.
###
@app.get(
    "/gui/projects/{project_id}",
    tags=["Projects"],
    response_class=Response,
    status_code=status.HTTP_200_OK,
)
async def get_html_project_home_page(
    request: Request,
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
) -> Response:
    """
    Get HTML project home page.

    Args:
        request (Request): The request context.
        project_id (str): The ID of the project.

    Returns:
        Response: The requested page.
    """

    # Return HTML project home page.
    try:
        return templates.TemplateResponse(
            name="project_home.html",
            context={
                "request": request,
                # Get the project ID.
                "project_id": project_id,
                # Get the project metadata (ID, name, creation date).
                "metadata": (await get_metadata(project_id=project_id))["metadata"],
                # Get the project status (iteration, step name and status, modelization state and conflict).
                "status": (await get_status(project_id=project_id))["status"],
                # Get the project constraints.
                "constraints": (
                    await get_constraints(
                        project_id=project_id,
                        without_hidden_constraints=True,
                        sorted_by=ConstraintsSortOptions.ITERATION_OF_SAMPLING,
                        sorted_reverse=False,
                    )
                )["constraints"],
            },
            status_code=status.HTTP_200_OK,
        )

    # Case of error: Return HTML error page.
    except HTTPException as error:
        # Return HTML error page.
        return templates.TemplateResponse(
            name="error.html",
            context={
                "request": request,
                "status_code": error.status_code,
                "detail": error.detail,
            },
            status_code=error.status_code,
        )


# ==============================================================================
# DEFINE ROUTES FOR STATUS
# ==============================================================================


###
### ROUTE: Get status.
###
@app.get(
    "/api/projects/{project_id}/status",
    tags=["Status"],
    status_code=status.HTTP_200_OK,
)
async def get_status(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
) -> Dict[str, Any]:
    """
    Get status.

    Args:
        project_id (str): The ID of the project.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.

    Returns:
        Dict[str, Any]: A dictionary that contains status.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Load status file.
    with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
        project_status: Dict[str, Any] = json.load(status_fileobject)
        project_status["state_details"] = get_ICGUIStates_details(state=project_status["state"])

        # Return the requested status.
        return {"project_id": project_id, "status": project_status}


###
### ROUTE: Move to next iteration after clustering step.
###
@app.post(
    "/api/projects/{project_id}/iterations",
    tags=["Status"],
    status_code=status.HTTP_201_CREATED,
)
async def move_to_next_iteration(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
) -> Dict[str, Any]:
    """
    Move to next iteration after clustering step.

    Args:
        project_id (str): The ID of the project.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the project didn't complete its clustering step.

    Returns:
        Dict[str, Any]: A dictionary that contains the ID of the new iteration.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        ###
        ### Load needed data.
        ###

        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject_r:
            project_status: Dict[str, Any] = json.load(status_fileobject_r)

        # Load settings file.
        with open(DATA_DIRECTORY / project_id / "settings.json", "r") as settings_fileobject_r:
            project_settings: Dict[str, Any] = json.load(settings_fileobject_r)

        # Get current iteration id.
        current_iteration_id: int = project_status["iteration_id"]

        ###
        ### Check parameters.
        ###

        # Check project status.
        if project_status["state"] != ICGUIStates.ITERATION_END:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The project with id '{project_id_str}' hasn't completed its clustering step on iteration '{iteration_id_str}'.".format(
                    project_id_str=str(project_id),
                    iteration_id_str=str(current_iteration_id),
                ),
            )

        ###
        ### Update data.
        ###

        # Define new iteration id.
        new_iteration_id: int = current_iteration_id + 1

        # Initialize status for the new iteration.
        project_status["iteration_id"] = new_iteration_id
        project_status["state"] = ICGUIStates.SAMPLING_TODO

        # Initialize settings for the new iteration.
        project_settings[str(new_iteration_id)] = {
            "sampling": (
                default_SamplingSettingsModel().to_dict()
                if (current_iteration_id == 0)
                else project_settings[str(current_iteration_id)]["sampling"]
            ),
            "preprocessing": project_settings[str(current_iteration_id)]["preprocessing"],
            "vectorization": project_settings[str(current_iteration_id)]["vectorization"],
            "clustering": project_settings[str(current_iteration_id)]["clustering"],
        }

        ###
        ### Store updated data.
        ###

        # Store project settings.
        with open(DATA_DIRECTORY / project_id / "settings.json", "w") as settings_fileobject_w:
            json.dump(project_settings, settings_fileobject_w, indent=4)

        # Store project status.
        with open(DATA_DIRECTORY / project_id / "status.json", "w") as status_fileobject_w:
            json.dump(project_status, status_fileobject_w, indent=4)

        # Return the new iteration id.
        return {
            "project_id": project_id,
            "iteration_id": new_iteration_id,
            "detail": "The project with id '{project_id_str}' is now on iteration with id '{iteration_id_str}'.".format(
                project_id_str=str(project_id),
                iteration_id_str=str(new_iteration_id),
            ),
        }


# ==============================================================================
# DEFINE ROUTES FOR TEXTS
# ==============================================================================


###
### ROUTE: Get texts.
###
@app.get(
    "/api/projects/{project_id}/texts",
    tags=["Texts"],
    status_code=status.HTTP_200_OK,
)
async def get_texts(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    without_deleted_texts: bool = Query(
        True,
        description="The option to not return deleted texts. Defaults to `True`.",
    ),
    sorted_by: TextsSortOptions = Query(
        TextsSortOptions.ALPHABETICAL,
        description="The option to sort texts. Defaults to `ALPHABETICAL`.",
    ),
    sorted_reverse: bool = Query(
        False,
        description="The option to reverse texts order. Defaults to `False`.",
    ),
    # TODO: filter_text
    # TODO: limit_size + offset
) -> Dict[str, Any]:
    """
    Get texts.

    Args:
        project_id (str): The ID of the project.
        without_deleted_texts (bool): The option to not return deleted texts. Defaults to `True`.
        sorted_by (TextsSortOptions, optional): The option to sort texts. Defaults to `ALPHABETICAL`.
        sorted_reverse (bool, optional): The option to reverse texts order. Defaults to `False`.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.

    Returns:
        Dict[str, Any]: A dictionary that contains texts.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    ###
    ### Load needed data.
    ###

    # Load texts.
    with open(DATA_DIRECTORY / project_id / "texts.json", "r") as texts_fileobject:
        texts: Dict[str, Any] = {
            text_id: text_value
            for text_id, text_value in json.load(texts_fileobject).items()
            if (without_deleted_texts is False or text_value["is_deleted"] is False)
        }

    ###
    ### Sort texts.
    ###

    # Define the values selection method.
    def get_value_for_texts_sorting(text_to_sort: Tuple[str, Dict[str, Any]]) -> Any:  # noqa: WPS430 (nested function)
        """Return the values expected for texts sorting.

        Args:
            text_to_sort (Tuple[Dict[str, Any]]): A text (from `.items()`).

        Returns:
            Any: The expected values of the text need for the sort.
        """
        # By text id.
        if sorted_by == TextsSortOptions.ID:
            return text_to_sort[0]
        # By text value.
        if sorted_by == TextsSortOptions.ALPHABETICAL:
            return text_to_sort[1]["text_preprocessed"]
        # By deletion status.
        #### if sorted_by == TextsSortOptions.IS_DELETED:
        return text_to_sort[1]["is_deleted"]

    # Sorted the texts to return.
    sorted_texts: Dict[str, Any] = dict(
        sorted(
            texts.items(),
            key=get_value_for_texts_sorting,
            reverse=sorted_reverse,
        )
    )

    # Return the requested texts.
    return {
        "project_id": project_id,
        "texts": sorted_texts,
        # Get the request parameters.
        "parameters": {
            "without_deleted_texts": without_deleted_texts,
            "sorted_by": sorted_by.value,
            "sorted_reverse": sorted_reverse,
        },
    }


###
### ROUTE: Delete a text.
###
@app.put(
    "/api/projects/{project_id}/texts/{text_id}/delete",
    tags=["Texts"],
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_text(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    text_id: str = Path(
        ...,
        description="The ID of the text.",
    ),
) -> Dict[str, Any]:
    """
    Delete a text.

    Args:
        project_id (str): The ID of the project.
        text_id (str): The ID of the text.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the text with id `text_id` to delete doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the current status of the project doesn't allow modification.

    Returns:
        Dict[str, Any]: A dictionary that contains the ID of deleted text.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        ###
        ### Load needed data.
        ###

        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
            project_status: Dict[str, Any] = json.load(status_fileobject)

        # Load texts file.
        with open(DATA_DIRECTORY / project_id / "texts.json", "r") as texts_fileobject_r:
            texts: Dict[str, Any] = json.load(texts_fileobject_r)

        # Load constraints file.
        with open(DATA_DIRECTORY / project_id / "constraints.json", "r") as constraints_fileobject_r:
            constraints: Dict[str, Any] = json.load(constraints_fileobject_r)

        ###
        ### Check parameters.
        ###

        # Check text id.
        if text_id not in texts.keys():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="In project with id '{project_id_str}', the text with id '{text_id_str}' to delete doesn't exist.".format(
                    project_id_str=str(project_id),
                    text_id_str=str(text_id),
                ),
            )

        # Check status.
        if (
            project_status["state"] != ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION  # noqa: WPS514
            and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
            and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The project with id '{project_id_str}' doesn't allow modification during this state (state='{state_str}').".format(
                    project_id_str=str(project_id),
                    state_str=str(project_status["state"]),
                ),
            )

        ###
        ### Update data.
        ###

        # Update status by forcing "outdated" status.
        if project_status["state"] == ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION:
            project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
        #### elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS:
        ####    project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
        #### elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS:
        ####    project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS

        # Update texts by deleting the text.
        texts[text_id]["is_deleted"] = True

        # Update constraints by hidding those associated with the deleted text.
        for constraint_id, constraint_value in constraints.items():
            data_id1: str = constraint_value["data"]["id_1"]
            data_id2: str = constraint_value["data"]["id_2"]

            if text_id in {
                data_id1,
                data_id2,
            }:
                constraints[constraint_id]["is_hidden"] = True

        ###
        ### Store updated data.
        ###

        # Store updated status in file.
        with open(DATA_DIRECTORY / project_id / "status.json", "w") as status_fileobject_w:
            json.dump(project_status, status_fileobject_w, indent=4)

        # Store updated texts in file.
        with open(DATA_DIRECTORY / project_id / "texts.json", "w") as texts_fileobject_w:
            json.dump(texts, texts_fileobject_w, indent=4)

        # Store updated constraints in file.
        with open(DATA_DIRECTORY / project_id / "constraints.json", "w") as constraints_fileobject_w:
            json.dump(constraints, constraints_fileobject_w, indent=4)

    # Return statement.
    return {
        "project_id": project_id,
        "text_id": text_id,
        "detail": "In project with id '{project_id_str}', the text with id '{text_id_str}' has been deleted. Several constraints have been hidden.".format(
            project_id_str=str(project_id),
            text_id_str=str(text_id),
        ),
    }


###
### ROUTE: Undelete a text.
###
@app.put(
    "/api/projects/{project_id}/texts/{text_id}/undelete",
    tags=["Texts"],
    status_code=status.HTTP_202_ACCEPTED,
)
async def undelete_text(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    text_id: str = Path(
        ...,
        description="The ID of the text.",
    ),
) -> Dict[str, Any]:
    """
    Undelete a text.

    Args:
        project_id (str): The ID of the project.
        text_id (str): The ID of the text.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the text with id `text_id` to undelete doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the current status of the project doesn't allow modification.

    Returns:
        Dict[str, Any]: A dictionary that contains the ID of undeleted text.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        ###
        ### Load needed data.
        ###

        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
            project_status: Dict[str, Any] = json.load(status_fileobject)

        # Load texts file.
        with open(DATA_DIRECTORY / project_id / "texts.json", "r") as texts_fileobject_r:
            texts: Dict[str, Any] = json.load(texts_fileobject_r)

        # Load constraints file.
        with open(DATA_DIRECTORY / project_id / "constraints.json", "r") as constraints_fileobject_r:
            constraints: Dict[str, Any] = json.load(constraints_fileobject_r)

        ###
        ### Check parameters.
        ###

        # Check text id.
        if text_id not in texts.keys():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="In project with id '{project_id_str}', the text with id '{text_id_str}' to undelete doesn't exist.".format(
                    project_id_str=str(project_id),
                    text_id_str=str(text_id),
                ),
            )

        # Check status.
        if (
            project_status["state"] != ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION  # noqa: WPS514
            and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
            and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The project with id '{project_id_str}' doesn't allow modification during this state (state='{state_str}').".format(
                    project_id_str=str(project_id),
                    state_str=str(project_status["state"]),
                ),
            )

        ###
        ### Update data.
        ###

        # Update status by forcing "outdated" status.
        if project_status["state"] == ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION:
            project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
        #### elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS:
        ####    project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
        #### elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS:
        ####    project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS

        # Update texts by undeleting the text.
        texts[text_id]["is_deleted"] = False

        # Update constraints by unhidding those associated with the undeleted text.
        for constraint_id, constraint_value in constraints.items():
            data_id1: str = constraint_value["data"]["id_1"]
            data_id2: str = constraint_value["data"]["id_2"]

            if text_id in {data_id1, data_id2}:
                constraints[constraint_id]["is_hidden"] = (
                    texts[data_id1]["is_deleted"] is True or texts[data_id2]["is_deleted"] is True
                )

        ###
        ### Store updated data.
        ###

        # Store updated status in file.
        with open(DATA_DIRECTORY / project_id / "status.json", "w") as status_fileobject_w:
            json.dump(project_status, status_fileobject_w, indent=4)

        # Store updated texts in file.
        with open(DATA_DIRECTORY / project_id / "texts.json", "w") as texts_fileobject_w:
            json.dump(texts, texts_fileobject_w, indent=4)

        # Store updated constraints in file.
        with open(DATA_DIRECTORY / project_id / "constraints.json", "w") as constraints_fileobject_w:
            json.dump(constraints, constraints_fileobject_w, indent=4)

    # Return statement.
    return {
        "project_id": project_id,
        "text_id": text_id,
        "detail": "In project with id '{project_id_str}', the text with id '{text_id_str}' has been undeleted. Several constraints have been unhidden.".format(
            project_id_str=str(project_id),
            text_id_str=str(text_id),
        ),
    }


###
### ROUTE: Rename a text.
###
@app.put(
    "/api/projects/{project_id}/texts/{text_id}/rename",
    tags=["Texts"],
    status_code=status.HTTP_202_ACCEPTED,
)
async def rename_text(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    text_id: str = Path(
        ...,
        description="The ID of the text.",
    ),
    text_value: str = Query(
        ...,
        description="The new value of the text.",
        min_length=3,
        max_length=256,
    ),
) -> Dict[str, Any]:
    """
    Rename a text.

    Args:
        project_id (str): The ID of the project.
        text_id (str): The ID of the text.
        text_value (str): The new value of the text.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the text with id `text_id` to rename doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the current status of the project doesn't allow modification.

    Returns:
        Dict[str, Any]: A dictionary that contains the ID of renamed text.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        ###
        ### Load needed data.
        ###

        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
            project_status: Dict[str, Any] = json.load(status_fileobject)

        # Load texts file.
        with open(DATA_DIRECTORY / project_id / "texts.json", "r") as texts_fileobject_r:
            texts: Dict[str, Any] = json.load(texts_fileobject_r)

        ###
        ### Check parameters.
        ###

        # Check text id.
        if text_id not in texts.keys():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="In project with id '{project_id_str}', the text with id '{text_id_str}' to rename doesn't exist.".format(
                    project_id_str=str(project_id),
                    text_id_str=str(text_id),
                ),
            )

        # Check status.
        if (
            project_status["state"] != ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION  # noqa: WPS514
            and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
            and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The project with id '{project_id_str}' doesn't allow modification during this state (state='{state_str}').".format(
                    project_id_str=str(project_id),
                    state_str=str(project_status["state"]),
                ),
            )

        ###
        ### Update data.
        ###

        # Update status by forcing "outdated" status.
        if project_status["state"] == ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION:
            project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
        #### elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS:
        ####    project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
        #### elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS:
        ####    project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS

        # Update texts by renaming the new text.
        texts[text_id]["text"] = text_value

        ###
        ### Store updated data.
        ###

        # Store updated status in file.
        with open(DATA_DIRECTORY / project_id / "status.json", "w") as status_fileobject_w:
            json.dump(project_status, status_fileobject_w, indent=4)

        # Store updated texts in file.
        with open(DATA_DIRECTORY / project_id / "texts.json", "w") as texts_fileobject_w:
            json.dump(texts, texts_fileobject_w, indent=4)

    # Return statement.
    return {
        "project_id": project_id,
        "text_id": text_id,
        "text_value": text_value,
        "detail": "In project with id '{project_id_str}', the text with id '{text_id_str}' has been renamed.".format(
            project_id_str=str(project_id),
            text_id_str=str(text_id),
        ),
    }


###
### ROUTE: Get HTML texts page.
###
@app.get(
    "/gui/projects/{project_id}/texts",
    tags=["Texts"],
    response_class=Response,
    status_code=status.HTTP_200_OK,
)
async def get_html_texts_page(
    request: Request,
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    sorted_by: TextsSortOptions = Query(
        TextsSortOptions.ALPHABETICAL,
        description="The option to sort texts. Defaults to `ALPHABETICAL`.",
    ),
    sorted_reverse: bool = Query(
        False,
        description="The option to reverse texts order. Defaults to `False`.",
    ),
    # TODO: filter_text
    # TODO: limit_size + offset
) -> Response:
    """
    Get HTML texts page.

    Args:
        request (Request): The request context.
        project_id (str): The ID of the project.
        sorted_by (TextsSortOptions, optional): The option to sort texts. Defaults to `ALPHABETICAL`.
        sorted_reverse (bool, optional): The option to reverse texts order. Defaults to `False`.

    Returns:
        Response: The requested page.
    """

    # Return HTML constraints page.
    try:
        return templates.TemplateResponse(
            name="texts.html",
            context={
                "request": request,
                # Get the project ID.
                "project_id": project_id,
                # Get the request parameters.
                "parameters": {
                    "without_deleted_texts": True,
                    "sorted_by": sorted_by.value,
                    "sorted_reverse": sorted_reverse,
                },
                # Get the project metadata (ID, name, creation date).
                "metadata": (await get_metadata(project_id=project_id))["metadata"],
                # Get the project status (iteration, step name and status, modelization state and conflict).
                "status": (await get_status(project_id=project_id))["status"],
                # Get the project texts.
                "texts": (
                    await get_texts(
                        project_id=project_id,
                        without_deleted_texts=False,
                        sorted_by=TextsSortOptions.ID,
                        sorted_reverse=False,
                    )
                )["texts"],
                # Get the project constraints.
                "constraints": (
                    await get_constraints(
                        project_id=project_id,
                        without_hidden_constraints=True,
                        sorted_by=ConstraintsSortOptions.ID,
                        sorted_reverse=False,
                    )
                )["constraints"],
            },
            status_code=status.HTTP_200_OK,
        )

    # Case of error: Return HTML error page.
    except HTTPException as error:
        # Return HTML error page.
        return templates.TemplateResponse(
            name="error.html",
            context={
                "request": request,
                "status_code": error.status_code,
                "detail": error.detail,
            },
            status_code=error.status_code,
        )


# ==============================================================================
# DEFINE ROUTES FOR CONSTRAINTS
# ==============================================================================


###
### ROUTE: Get constraints.
###
@app.get(
    "/api/projects/{project_id}/constraints",
    tags=["Constraints"],
    status_code=status.HTTP_200_OK,
)
async def get_constraints(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    without_hidden_constraints: bool = Query(
        True,
        description="The option to not return hidden constraints. Defaults to `True`.",
    ),
    sorted_by: ConstraintsSortOptions = Query(
        ConstraintsSortOptions.ID,
        description="The option to sort constraints. Defaults to `ID`.",
    ),
    sorted_reverse: bool = Query(
        False,
        description="The option to reverse constraints order. Defaults to `False`.",
    ),
    # TODO: filter_text
    # TODO: limit_size + offset
) -> Dict[str, Any]:
    """
    Get constraints.

    Args:
        project_id (str): The ID of the project.
        without_hidden_constraints (bool, optional): The option to not return hidden constraints. Defaults to `True`.
        sorted_by (ConstraintsSortOptions, optional): The option to sort constraints. Defaults to `ID`.
        sorted_reverse (bool, optional): The option to reverse constraints order. Defaults to `False`.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.

    Returns:
        Dict[str, Any]: A dictionary that contains constraints.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    ###
    ### Load needed data.
    ###

    # Load constraints.
    with open(DATA_DIRECTORY / project_id / "constraints.json", "r") as constraints_fileobject:
        constraints: Dict[str, Any] = {
            constraint_id: constraint_value
            for constraint_id, constraint_value in json.load(constraints_fileobject).items()
            if (without_hidden_constraints is False or constraint_value["is_hidden"] is False)
        }

    # Load texts.
    with open(DATA_DIRECTORY / project_id / "texts.json", "r") as texts_fileobject:
        texts: Dict[str, Any] = json.load(texts_fileobject)

    ###
    ### Sort constraints.
    ###

    # Define the values selection method.
    def get_value_for_constraints_sorting(  # noqa: WPS430 (nested function)
        constraint_to_sort: Tuple[str, Dict[str, Any]]
    ) -> Any:
        """Return the values expected for constraints sorting.

        Args:
            constraint_to_sort (Tuple[Dict[str, Any]]): A constraint (from `.items()`).

        Returns:
            Any: The expected values of the constraint need for the sort.
        """
        # By constraint id.
        if sorted_by == ConstraintsSortOptions.ID:
            return constraint_to_sort[0]
        # By texts.
        if sorted_by == ConstraintsSortOptions.TEXT:
            return (
                texts[constraint_to_sort[1]["data"]["id_1"]]["text"],
                texts[constraint_to_sort[1]["data"]["id_2"]]["text"],
            )
        # By constraint type.
        if sorted_by == ConstraintsSortOptions.CONSTRAINT_TYPE:
            return (
                constraint_to_sort[1]["constraint_type"] is None,
                constraint_to_sort[1]["constraint_type"] == "CANNOT_LINK",
                constraint_to_sort[1]["constraint_type"] == "MUST_LINK",
            )
        # By date of update.
        if sorted_by == ConstraintsSortOptions.DATE_OF_UPDATE:
            return constraint_to_sort[1]["date_of_update"] if constraint_to_sort[1]["date_of_update"] is not None else 0
        # By iteration of sampling.
        if sorted_by == ConstraintsSortOptions.ITERATION_OF_SAMPLING:
            return constraint_to_sort[1]["iteration_of_sampling"]
        # To annotation.
        if sorted_by == ConstraintsSortOptions.TO_ANNOTATE:
            return constraint_to_sort[1]["to_annotate"] is False
        # To review.
        if sorted_by == ConstraintsSortOptions.TO_REVIEW:
            return constraint_to_sort[1]["to_review"] is False
        # To fix conflict.
        #### if sorted_by == ConstraintsSortOptions.TO_FIX_CONFLICT:
        return constraint_to_sort[1]["to_fix_conflict"] is False

    # Sorted the constraints to return.
    sorted_constraints: Dict[str, Any] = dict(
        sorted(
            constraints.items(),
            key=get_value_for_constraints_sorting,
            reverse=sorted_reverse,
        )
    )

    # Return the requested constraints.
    return {
        "project_id": project_id,
        "constraints": sorted_constraints,
        # Get the request parameters.
        "parameters": {
            "without_hidden_constraints": without_hidden_constraints,
            "sorted_by": sorted_by.value,
            "sorted_reverse": sorted_reverse,
        },
    }


###
### ROUTE: Annotate a constraint.
###
@app.put(
    "/api/projects/{project_id}/constraints/{constraint_id}/annotate",
    tags=["Constraints"],
    status_code=status.HTTP_202_ACCEPTED,
)
async def annotate_constraint(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    constraint_id: str = Path(
        ...,
        description="The ID of the constraint.",
    ),
    constraint_type: Optional[ConstraintsValues] = Query(
        None,
        description="The type of constraint to annotate. Defaults to `None`.",
    ),
) -> Dict[str, Any]:
    """
    Annotate a constraint.

    Args:
        project_id (str): The ID of the project.
        constraint_id (str): The ID of the constraint.
        constraint_type (Optional[ConstraintsValues]): The type of constraint to annotate. Defaults to `None`.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the constraint with id `constraint_id` to annotate doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the current status of the project doesn't allow modification.

    Returns:
        Dict[str, Any]: A dictionary that contains the ID of annotated constraint.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        ###
        ### Load needed data.
        ###

        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
            project_status: Dict[str, Any] = json.load(status_fileobject)

        # Load constraints file.
        with open(DATA_DIRECTORY / project_id / "constraints.json", "r") as constraints_fileobject_r:
            constraints: Dict[str, Any] = json.load(constraints_fileobject_r)

        ###
        ### Check parameters.
        ###

        # Check constraint id.
        if constraint_id not in constraints.keys():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="In project with id '{project_id_str}', the constraint with id '{constraint_id_str}' to annotate doesn't exist.".format(
                    project_id_str=str(project_id),
                    constraint_id_str=str(constraint_id),
                ),
            )

        # Check status.
        if (
            project_status["state"] != ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION  # noqa: WPS514
            and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
            and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The project with id '{project_id_str}' doesn't allow modification during this state (state='{state_str}').".format(
                    project_id_str=str(project_id),
                    state_str=str(project_status["state"]),
                ),
            )

        ###
        ### Update data.
        ###

        # Update status by forcing "outdated" status.
        if project_status["state"] == ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION:
            project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
        #### elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS:
        ####    project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
        #### elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS:
        ####    project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS

        # Update constraints by updating the constraint history.
        constraints[constraint_id]["constraint_type_previous"].append(constraints[constraint_id]["constraint_type"])

        # Update constraints by annotating the constraint.
        constraints[constraint_id]["constraint_type"] = constraint_type
        constraints[constraint_id]["date_of_update"] = datetime.now().timestamp()

        # Force annotation status.
        constraints[constraint_id]["to_annotate"] = False

        ###
        ### Store updated data.
        ###

        # Store updated status in file.
        with open(DATA_DIRECTORY / project_id / "status.json", "w") as status_fileobject_w:
            json.dump(project_status, status_fileobject_w, indent=4)

        # Store updated constraints in file.
        with open(DATA_DIRECTORY / project_id / "constraints.json", "w") as constraints_fileobject_w:
            json.dump(constraints, constraints_fileobject_w, indent=4)

    # Return statement.
    return {
        "project_id": project_id,
        "constraint_id": constraint_id,
        "detail": "In project with id '{project_id_str}', the constraint with id '{constraint_id_str}' has been annotated at `{constraint_type_str}`.".format(
            project_id_str=str(project_id),
            constraint_id_str=str(constraint_id),
            constraint_type_str="None" if (constraint_type is None) else str(constraint_type.value),
        ),
    }


###
### ROUTE: Review a constraint.
###
@app.put(
    "/api/projects/{project_id}/constraints/{constraint_id}/review",
    tags=["Constraints"],
    status_code=status.HTTP_202_ACCEPTED,
)
async def review_constraint(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    constraint_id: str = Path(
        ...,
        description="The ID of the constraint.",
    ),
    to_review: bool = Query(
        True,
        description="The choice to review or not the constraint. Defaults to `True`.",
    ),
) -> Dict[str, Any]:
    """
    Review a constraint.

    Args:
        project_id (str): The ID of the project.
        constraint_id (str): The ID of the constraint.
        to_review (str): The choice to review or not the constraint. Defaults to `True`.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the constraint with id `constraint_id` to annotate doesn't exist.

    Returns:
        Dict[str, Any]: A dictionary that contains the ID of reviewed constraint.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        ###
        ### Load needed data.
        ###

        # Load constraints file.
        with open(DATA_DIRECTORY / project_id / "constraints.json", "r") as constraints_fileobject_r:
            constraints: Dict[str, Any] = json.load(constraints_fileobject_r)

        ###
        ### Check parameters.
        ###

        # Check constraint id.
        if constraint_id not in constraints.keys():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="In project with id '{project_id_str}', the constraint with id '{constraint_id_str}' to annotate doesn't exist.".format(
                    project_id_str=str(project_id),
                    constraint_id_str=str(constraint_id),
                ),
            )

        ###
        ### Update data.
        ###

        # Update constraints by reviewing the constraint.
        constraints[constraint_id]["to_review"] = to_review

        ###
        ### Store updated data.
        ###

        # Store updated constraints in file.
        with open(DATA_DIRECTORY / project_id / "constraints.json", "w") as constraints_fileobject_w:
            json.dump(constraints, constraints_fileobject_w, indent=4)

    # Return statement.
    return {
        "project_id": project_id,
        "constraint_id": constraint_id,
        "detail": "In project with id '{project_id_str}', the constraint with id '{constraint_id_str}' {review_conclusion}.".format(
            project_id_str=str(project_id),
            constraint_id_str=str(constraint_id),
            review_conclusion="need a review" if (to_review) else "has been reviewed",
        ),
    }


###
### ROUTE: Comment a constraint.
###
@app.put(
    "/api/projects/{project_id}/constraints/{constraint_id}/comment",
    tags=["Constraints"],
    status_code=status.HTTP_202_ACCEPTED,
)
async def comment_constraint(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    constraint_id: str = Path(
        ...,
        description="The ID of the constraint.",
    ),
    constraint_comment: str = Query(
        ...,
        description="The comment of constraint.",
        # min_length=0,
        max_length=256,
    ),
) -> Dict[str, Any]:
    """
    Comment a constraint.

    Args:
        project_id (str): The ID of the project.
        constraint_id (str): The ID of the constraint.
        constraint_comment (str): The comment of constraint.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the constraint with id `constraint_id` to annotate doesn't exist.

    Returns:
        Dict[str, Any]: A dictionary that contains the ID of commented constraint.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        ###
        ### Load needed data.
        ###

        # Load constraints file.
        with open(DATA_DIRECTORY / project_id / "constraints.json", "r") as constraints_fileobject_r:
            constraints: Dict[str, Any] = json.load(constraints_fileobject_r)

        ###
        ### Check parameters.
        ###

        # Check constraint id.
        if constraint_id not in constraints.keys():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="In project with id '{project_id_str}', the constraint with id '{constraint_id_str}' to annotate doesn't exist.".format(
                    project_id_str=str(project_id),
                    constraint_id_str=str(constraint_id),
                ),
            )

        ###
        ### Update data.
        ###

        # Update constraints by commenting the constraint.
        constraints[constraint_id]["comment"] = constraint_comment

        ###
        ### Store updated data.
        ###

        # Store updated constraints in file.
        with open(DATA_DIRECTORY / project_id / "constraints.json", "w") as constraints_fileobject_w:
            json.dump(constraints, constraints_fileobject_w, indent=4)

    # Return statement.
    return {
        "project_id": project_id,
        "constraint_id": constraint_id,
        "constraint_comment": constraint_comment,
        "detail": "In project with id '{project_id_str}', the constraint with id '{constraint_id_str}' has been commented.".format(
            project_id_str=str(project_id),
            constraint_id_str=str(constraint_id),
        ),
    }


###
### ROUTE: Approve all constraints.
###
@app.post(
    "/api/projects/{project_id}/constraints/approve",
    tags=["Constraints"],
    status_code=status.HTTP_201_CREATED,
)
async def approve_all_constraints(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
) -> Dict[str, Any]:
    """
    Approve all constraints.

    Args:
        project_id (str): The ID of the project.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the current status of the project doesn't allow constraints approbation.

    Returns:
        Dict[str, Any]: A dictionary that contains the confirmation of constraints approbation.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
            project_status: Dict[str, Any] = json.load(status_fileobject)

        # Check status.
        if project_status["state"] != ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The project with id '{project_id_str}' doesn't allow constraints approbation during this state (state='{state_str}').".format(
                    project_id_str=str(project_id),
                    state_str=str(project_status["state"]),
                ),
            )

        ###
        ### Update data.
        ###

        # Update status to clustering step.
        project_status["state"] = ICGUIStates.CLUSTERING_TODO

        ###
        ### Store updated data.
        ###

        # Store updated status in file.
        with open(DATA_DIRECTORY / project_id / "status.json", "w") as status_fileobject_w:
            json.dump(project_status, status_fileobject_w, indent=4)

    # Return statement.
    return {
        "project_id": project_id,
        "detail": "In project with id '{project_id_str}', the constraints have been approved.".format(
            project_id_str=str(project_id),
        ),
    }


###
### ROUTE: Get HTML constraints page.
###
@app.get(
    "/gui/projects/{project_id}/constraints",
    tags=["Constraints"],
    response_class=Response,
    status_code=status.HTTP_200_OK,
)
async def get_html_constraints_page(
    request: Request,
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    sorted_by: ConstraintsSortOptions = Query(
        ConstraintsSortOptions.ITERATION_OF_SAMPLING,
        description="The option to sort constraints. Defaults to `ITERATION_OF_SAMPLING`.",
    ),
    sorted_reverse: bool = Query(
        False,
        description="The option to reverse constraints order. Defaults to `False`.",
    ),
    # TODO: filter_text
    # TODO: limit_size + offset
) -> Response:
    """
    Get HTML constraints page.

    Args:
        request (Request): The request context.
        project_id (str): The ID of the project.
        sorted_by (ConstraintsSortOptions, optional): The option to sort constraints. Defaults to `ITERATION_OF_SAMPLING`.
        sorted_reverse (bool, optional): The option to reverse constraints order. Defaults to `False`.

    Returns:
        Response: The requested page.
    """

    # Return HTML constraints page.
    try:
        return templates.TemplateResponse(
            name="constraints.html",
            context={
                "request": request,
                # Get the project ID.
                "project_id": project_id,
                # Get the request parameters.
                "parameters": {
                    "without_hidden_constraints": True,
                    "sorted_by": sorted_by.value,
                    "sorted_reverse": sorted_reverse,
                },
                # Get the project metadata (ID, name, creation date).
                "metadata": (await get_metadata(project_id=project_id))["metadata"],
                # Get the project status (iteration, step name and status, modelization state and conflict).
                "status": (await get_status(project_id=project_id))["status"],
                # Get the project texts.
                "texts": (
                    await get_texts(
                        project_id=project_id,
                        without_deleted_texts=False,
                        sorted_by=TextsSortOptions.ID,
                        sorted_reverse=False,
                    )
                )["texts"],
                # Get the project constraints.
                "constraints": (
                    await get_constraints(
                        project_id=project_id,
                        without_hidden_constraints=True,
                        sorted_by=sorted_by,
                        sorted_reverse=sorted_reverse,
                    )
                )["constraints"],
            },
            status_code=status.HTTP_200_OK,
        )

    # Case of error: Return HTML error page.
    except HTTPException as error:
        # Return HTML error page.
        return templates.TemplateResponse(
            name="error.html",
            context={
                "request": request,
                "status_code": error.status_code,
                "detail": error.detail,
            },
            status_code=error.status_code,
        )


###
### ROUTE: Get HTML constraint annotation page.
###
@app.get(
    "/gui/projects/{project_id}/constraints/{constraint_id}",
    tags=["Constraints"],
    response_class=Response,
    status_code=status.HTTP_200_OK,
)
async def get_html_constraint_annotation_page(
    request: Request,
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    constraint_id: str = Path(
        ...,
        description="The ID of the constraint.",
    ),
) -> Response:
    """
    Get HTML constraint annotation page.

    Args:
        request (Request):  The request context.
        project_id (str): The ID of the project.
        constraint_id (str): The ID of the constraint.

    Returns:
        Response: The requested page.
    """

    # Return HTML constraints page.
    try:
        return templates.TemplateResponse(
            name="constraint_annotation.html",
            context={
                "request": request,
                # Get the project ID.
                "project_id": project_id,
                # Get the constraints ID.
                "constraint_id": constraint_id,
                # Get the project metadata (ID, name, creation date).
                "metadata": (await get_metadata(project_id=project_id))["metadata"],
                # Get the project status (iteration, step name and status, modelization state and conflict).
                "status": (await get_status(project_id=project_id))["status"],
                # Get the project texts.
                "texts": (
                    await get_texts(
                        project_id=project_id,
                        without_deleted_texts=False,
                        sorted_by=TextsSortOptions.ID,
                        sorted_reverse=False,
                    )
                )["texts"],
                "texts_html_escaped": {  # TODO: Escape HTML for javascript
                    text_id: {  # Force HTML escape.
                        key: (html.escape(value) if key in {"text_original", "text", "text_preprocessed"} else value)
                        for key, value in text_value.items()
                    }
                    for text_id, text_value in (
                        await get_texts(
                            project_id=project_id,
                            without_deleted_texts=False,
                            sorted_by=TextsSortOptions.ID,
                            sorted_reverse=False,
                        )
                    )["texts"].items()
                },
                # Get the project constraints.
                "constraints": (
                    await get_constraints(
                        project_id=project_id,
                        without_hidden_constraints=False,
                        sorted_by=ConstraintsSortOptions.ITERATION_OF_SAMPLING,
                        sorted_reverse=False,
                    )
                )["constraints"],
                # Get the project clustering result.
                "clusters": (await get_constrained_clustering_results(project_id=project_id, iteration_id=None))[
                    "clustering"
                ],
                # Get the project modelization inference result.
                "modelization": (await get_modelization(project_id=project_id))["modelization"],
            },
            status_code=status.HTTP_200_OK,
        )

    # Case of error: Return HTML error page.
    except HTTPException as error:
        # Return HTML error page.
        return templates.TemplateResponse(
            name="error.html",
            context={
                "request": request,
                "status_code": error.status_code,
                "detail": error.detail,
            },
            status_code=error.status_code,
        )


# ==============================================================================
# DEFINE ROUTES FOR SETTINGS
# ==============================================================================


###
### ROUTE: Get settings.
###
@app.get(
    "/api/projects/{project_id}/settings",
    tags=["Settings"],
    status_code=status.HTTP_200_OK,
)
async def get_settings(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    iteration_id: Optional[int] = Query(
        None,
        description="The ID of project iteration. If `None`, get the current iteration. Defaults to `None`.",
    ),
    settings_names: List[ICGUISettings] = Query(
        [
            ICGUISettings.PREPROCESSING,
            ICGUISettings.VECTORIZATION,
            ICGUISettings.SAMPLING,
            ICGUISettings.CLUSTERING,
        ],
        description="The list of names of requested settings to return. To select multiple settings kinds, use `CTRL + clic`.",
    ),
) -> Dict[str, Any]:
    """
    Get settings.

    Args:
        project_id (str): The ID of the project.
        iteration_id (Optional[int], optional): The ID of project iteration. If `None`, get the current iteration. Defaults to `None`.
        settings_names (List[ICGUISettings], optional): The list of names of requested settings to return. Defaults to `[ICGUISettings.PREPROCESSING, ICGUISettings.VECTORIZATION, ICGUISettings.SAMPLING, ICGUISettings.CLUSTERING,]`.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the iteration with id `iteration_id` doesn't exist.

    Returns:
        Dict[str, Any]: A dictionary that contains settings.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Load settings.
    with open(DATA_DIRECTORY / project_id / "settings.json", "r") as settings_fileobject:
        project_settings: Dict[str, Dict[str, Any]] = json.load(settings_fileobject)

    # Load status file.
    with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
        project_status: Dict[str, Any] = json.load(status_fileobject)

    # Get current iteration id if needed.
    if iteration_id is None:
        iteration_id = project_status["iteration_id"]

    # Otherwise check that requested iteration id exist.
    if str(iteration_id) not in project_settings.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' has no iteration with id '{iteration_id_str}'.".format(
                project_id_str=str(project_id),
                iteration_id_str=str(iteration_id),
            ),
        )

    # Return the requested settings.
    return {
        # Get the project ID.
        "project_id": project_id,
        # Get the iteration ID.
        "iteration_id": iteration_id,
        # Get the request parameters.
        "parameters": {
            "settings_names": [settings_name.value for settings_name in settings_names],
        },
        # Get the settings.
        "settings": {
            setting_name: settings_value
            for setting_name, settings_value in project_settings[str(iteration_id)].items()
            if setting_name in settings_names
        },
    }


###
### ROUTE: Update settings.
###
@app.put(
    "/api/projects/{project_id}/settings",
    tags=["Settings"],
    status_code=status.HTTP_201_CREATED,
)
async def update_settings(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    preprocessing: Optional[PreprocessingSettingsModel] = Body(
        None,
        description="The settings for data preprocessing. Used during `modelization_update` task. Keep unchanged if empty.",
    ),
    vectorization: Optional[VectorizationSettingsModel] = Body(
        None,
        description="The settings for data vectorization. Used during `modelization_update` task. Keep unchanged if empty.",
    ),
    sampling: Optional[SamplingSettingsModel] = Body(
        None,
        description="The settings for constraints sampling. Used during `constraints_sampling` task. Keep unchanged if empty.",
    ),
    clustering: Optional[ClusteringSettingsModel] = Body(
        None,
        description="The settings for constrained clustering. Used during `constrained_clustering` task. Keep unchanged if empty.",
    ),
) -> Dict[str, Any]:
    """
    Update settings.

    Args:
        project_id (str): The ID of the project.
        preprocessing (Optional[PreprocessingSettingsModel], optional): The settings for data preprocessing. Used during `clustering` step. Keep unchanged if empty.. Defaults to None.
        vectorization (Optional[VectorizationSettingsModel], optional): The settings for data vectorization. Used during `clustering` step. Keep unchanged if empty.. Defaults to None.
        sampling (Optional[SamplingSettingsModel], optional): The settings for constraints sampling. Used during `sampling` step. Keep unchanged if empty.. Defaults to None.
        clustering (Optional[ClusteringSettingsModel], optional): The settings for constrained clustering. Used during `clustering` step. Keep unchanged if empty. Defaults to None.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the status of the project doesn't allow settings modifications.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if parameters `preprocessing`, `vectorization`, `sampling` or `clustering` are not expected.
        HTTPException: Raises `HTTP_400_BAD_REQUEST` if parameters `preprocessing`, `vectorization`, `sampling` or `clustering` are invalid.

    Returns:
        Dict[str, Any]: A dictionary that contains the ID of updated settings.
    """

    # TODO: examples: https://fastapi.tiangolo.com/tutorial/schema-extra-example/#body-with-multiple-examples

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        ###
        ### Load needed data.
        ###

        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject_r:
            project_status: Dict[str, Any] = json.load(status_fileobject_r)
        iteration_id: int = project_status["iteration_id"]

        # Load settings file.
        with open(DATA_DIRECTORY / project_id / "settings.json", "r") as settings_fileobject_r:
            project_settings: Dict[str, Any] = json.load(settings_fileobject_r)

        list_of_updated_settings: List[ICGUISettings] = []

        ###
        ### Case of preprocessing settings.
        ###
        if preprocessing is not None:
            list_of_updated_settings.append(ICGUISettings.PREPROCESSING)

            # Check project status for preprocessing.
            if (
                project_status["state"] != ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION  # noqa: WPS514
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
            ):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="The 'preprocessing' settings of project with id '{project_id_str}' cant't be modified during this state (state='{state_str}'). No changes have been taken into account.".format(
                        project_id_str=str(project_id),
                        state_str=str(project_status["state"]),
                    ),
                )

            # Update status by forcing "outdated" status.
            if project_status["state"] == ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION:
                project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
            #### elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS:
            ####    project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
            #### elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS:
            ####    project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
            #### elif project_status["state"] == ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION:
            ####    project_status["state"] = ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION

            # Update the default settings with the parameters in the request body.
            for key_prep, value_prep in preprocessing.to_dict().items():
                project_settings[str(iteration_id)]["preprocessing"][key_prep] = value_prep

        ###
        ### Case of vectorization settings.
        ###
        if vectorization is not None:
            list_of_updated_settings.append(ICGUISettings.VECTORIZATION)

            # Check project status for vectorization.
            if (
                project_status["state"] != ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION  # noqa: WPS514
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
            ):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="The 'vectorization' settings of project with id '{project_id_str}' cant't be modified during this state (state='{state_str}'). No changes have been taken into account.".format(
                        project_id_str=str(project_id),
                        state_str=str(project_status["state"]),
                    ),
                )

            # Update status by forcing "outdated" status.
            if project_status["state"] == ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION:
                project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
            #### elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS:
            ####    project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
            #### elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS:
            ####    project_status["state"] = ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
            #### elif project_status["state"] == ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION:
            ####    project_status["state"] = ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION

            # Update the default settings with the parameters in the request body.
            for key_vect, value_vect in vectorization.to_dict().items():
                project_settings[str(iteration_id)]["vectorization"][key_vect] = value_vect

        ###
        ### Case of sampling settings.
        ###
        if sampling is not None:
            list_of_updated_settings.append(ICGUISettings.SAMPLING)

            # Check project status for sampling.
            if project_status["state"] != ICGUIStates.SAMPLING_TODO:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="The 'sampling' settings of project with id '{project_id_str}' cant't be modified during this state (state='{state_str}'). No changes have been taken into account.".format(
                        project_id_str=str(project_id),
                        state_str=str(project_status["state"]),
                    ),
                )

            # Update the default settings with the parameters in the request body.
            for key_sampl, value_sampl in sampling.to_dict().items():
                project_settings[str(iteration_id)]["sampling"][key_sampl] = value_sampl

        ###
        ### Case of clustering settings.
        ###
        if clustering is not None:
            list_of_updated_settings.append(ICGUISettings.CLUSTERING)

            # Check project status for clustering.
            if (
                project_status["state"] != ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION  # noqa: WPS514
                and project_status["state"] != ICGUIStates.INITIALIZATION_WITH_PENDING_MODELIZATION
                and project_status["state"] != ICGUIStates.INITIALIZATION_WITH_WORKING_MODELIZATION
                and project_status["state"] != ICGUIStates.SAMPLING_TODO
                and project_status["state"] != ICGUIStates.SAMPLING_PENDING
                and project_status["state"] != ICGUIStates.SAMPLING_WORKING
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS
                and project_status["state"] != ICGUIStates.ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS
                and project_status["state"] != ICGUIStates.CLUSTERING_TODO
            ):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="The 'clustering' settings of project with id '{project_id_str}' cant't be modified during this state (state='{state_str}'). No changes have been taken into account.".format(
                        project_id_str=str(project_id),
                        state_str=str(project_status["state"]),
                    ),
                )

            # Update the default settings with the parameters in the request body.
            for key_clus, value_clus in clustering.to_dict().items():
                project_settings[str(iteration_id)]["clustering"][key_clus] = value_clus

        ###
        ### Store updated data.
        ###

        # Store updated status in file.
        with open(DATA_DIRECTORY / project_id / "status.json", "w") as status_fileobject_w:
            json.dump(project_status, status_fileobject_w, indent=4)

        # Store updated settings in file.
        with open(DATA_DIRECTORY / project_id / "settings.json", "w") as settings_fileobject_w:
            json.dump(project_settings, settings_fileobject_w, indent=4)

    ###
    ### Return statement.
    ###
    return {
        "project_id": project_id,
        "detail": "The project with id '{project_id_str}' has updated the following settings: {settings_str}.".format(
            project_id_str=str(project_id),
            settings_str=", ".join(list_of_updated_settings),
        ),
    }


###
### ROUTE: Get HTML settings page.
###
@app.get(
    "/gui/projects/{project_id}/settings",
    tags=["Settings"],
    response_class=Response,
    status_code=status.HTTP_200_OK,
)
async def get_html_settings_page(
    request: Request,
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    iteration_id: Optional[int] = Query(
        None,
        description="The ID of project iteration. If `None`, get the current iteration. Defaults to `None`.",
    ),
    settings_names: List[ICGUISettings] = Query(
        [
            ICGUISettings.PREPROCESSING,
            ICGUISettings.VECTORIZATION,
            ICGUISettings.SAMPLING,
            ICGUISettings.CLUSTERING,
        ],
        description="The list of names of requested settings to return. To select multiple settings kinds, use `CTRL + clic`.",
    ),
) -> Response:
    """
    Get HTML settings page.

    Args:
        request (Request): The request context.
        project_id (str): The ID of the project.
        iteration_id (Optional[int], optional): The ID of project iteration. If `None`, get the current iteration. Defaults to `None`.
        settings_names (List[ICGUISettings], optional): The list of names of requested settings to return. Defaults to `[ICGUISettings.PREPROCESSING, ICGUISettings.VECTORIZATION, ICGUISettings.SAMPLING, ICGUISettings.CLUSTERING,]`.

    Returns:
        Response: The requested page.
    """

    # Return HTML project home page.
    try:  # noqa: WPS229 (too long try body)
        project_status: Dict[str, Any] = (await get_status(project_id=project_id))["status"]
        if iteration_id is None:
            iteration_id = project_status["iteration_id"]

        return templates.TemplateResponse(
            name="settings.html",
            context={
                "request": request,
                # Get the project ID.
                "project_id": project_id,
                # Get the iteration ID.
                "iteration_id": iteration_id,
                # Get the request parameters.
                "parameters": {
                    "settings_names": [settings_name.value for settings_name in settings_names],
                },
                # Get the project metadata (ID, name, creation date).
                "metadata": (await get_metadata(project_id=project_id))["metadata"],
                # Get the project status (iteration, step name and status, modelization state and conflict).
                "status": project_status,
                # Get the project settings (preprocessing, vectorization, sampling, clustering).
                "settings": (
                    await get_settings(project_id=project_id, iteration_id=iteration_id, settings_names=settings_names)
                )["settings"],
                # Get navigation information.
                "navigation": {
                    "previous": (None if (iteration_id == 0) else iteration_id - 1),
                    "next": (None if (iteration_id == project_status["iteration_id"]) else (iteration_id + 1)),
                },
            },
            status_code=status.HTTP_200_OK,
        )

    # Case of error: Return HTML error page.
    except HTTPException as error:
        # Return HTML error page.
        return templates.TemplateResponse(
            name="error.html",
            context={
                "request": request,
                "status_code": error.status_code,
                "detail": error.detail,
            },
            status_code=error.status_code,
        )


# ==============================================================================
# DEFINE ROUTES FOR MODELIZATION
# ==============================================================================


###
### ROUTE: Get modelization inference.
###
@app.get(
    "/api/projects/{project_id}/modelization",
    tags=["Data modelization"],
    status_code=status.HTTP_200_OK,
)
async def get_modelization(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
) -> Dict[str, Any]:
    """
    Get modelization inference.

    Args:
        project_id (str, optional): The ID of the project.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.

    Returns:
        Dict[str, Any]: A dictionary that contains modelization inference result.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Load the modelization inference results.
    with open(DATA_DIRECTORY / project_id / "modelization.json", "r") as modelization_fileobject:
        # Return the project modelization inference.
        return {
            "project_id": project_id,
            "modelization": json.load(modelization_fileobject),
        }


###
### ROUTE: Get 2D and 3D vectors.
###
@app.get(
    "/api/projects/{project_id}/vectors",
    tags=["Data modelization"],
    status_code=status.HTTP_200_OK,
)
async def get_vectors(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
) -> Dict[str, Any]:
    """
    Get 2D and 3D vectors.

    Args:
        project_id (str, optional): The ID of the project.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the iteration with id `iteration_id` doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the status of the project hasn't completed its clustering step.

    Returns:
        Dict[str, Any]: A dictionary that contains clustering result.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Load status file.
    with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
        project_status: Dict[str, Any] = json.load(status_fileobject)

    # Check project status.
    if (
        project_status["state"] != ICGUIStates.SAMPLING_TODO  # noqa: WPS514
        and project_status["state"] != ICGUIStates.SAMPLING_PENDING
        and project_status["state"] != ICGUIStates.SAMPLING_WORKING
        and project_status["state"] != ICGUIStates.ANNOTATION_WITH_UPTODATE_MODELIZATION
        and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
        and project_status["state"] != ICGUIStates.ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS
        and project_status["state"] != ICGUIStates.ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS
        and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
        and project_status["state"] != ICGUIStates.ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS
        and project_status["state"] != ICGUIStates.ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS
        and project_status["state"] != ICGUIStates.CLUSTERING_TODO
        and project_status["state"] != ICGUIStates.CLUSTERING_PENDING
        and project_status["state"] != ICGUIStates.CLUSTERING_WORKING
        and project_status["state"] != ICGUIStates.ITERATION_END
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The project with id '{project_id_str}' hasn't completed its modelization update step.".format(
                project_id_str=str(project_id),
            ),
        )

    # Load the 2D vectors.
    with open(DATA_DIRECTORY / project_id / "vectors_2D.json", "r") as vectors_2D_fileobject:
        vectors_2D: Dict[str, Dict[str, float]] = json.load(vectors_2D_fileobject)  # noqa: S301  # Usage of Pickle

    # Load the 3D vectors.
    with open(DATA_DIRECTORY / project_id / "vectors_3D.json", "r") as vectors_3D_fileobject:
        vectors_3D: Dict[str, Dict[str, float]] = json.load(vectors_3D_fileobject)  # noqa: S301  # Usage of Pickle

        # Return the project vectors.
        return {
            "project_id": project_id,
            "vectors_2d": vectors_2D,
            "vectors_3d": vectors_3D,
        }


###
### ROUTE: Prepare modelization update task.
###
@app.post(
    "/api/projects/{project_id}/modelization",
    tags=["Data modelization"],
    status_code=status.HTTP_202_ACCEPTED,
)
async def prepare_modelization_update_task(
    background_tasks: BackgroundTasks,
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
) -> Dict[str, Any]:
    """
    Prepare modelization update task.

    Args:
        background_tasks (BackgroundTasks): A background task to run after the return statement.
        project_id (str): The ID of the project.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the current status of the project doesn't allow the preparation of modelization update task.

    Returns:
        Dict[str, Any]: A dictionary that contains the confirmation of the preparation of modelization update task.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        ###
        ### Load needed data.
        ###

        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
            project_status: Dict[str, Any] = json.load(status_fileobject)

        ###
        ### Check parameters.
        ###

        # Check status.
        if (
            project_status["state"] != ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION  # noqa: WPS514
            and project_status["state"] != ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION
            and project_status["state"] != ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION
            and project_status["state"] != ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION
            and project_status["state"] != ICGUIStates.IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION
            and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS
            and project_status["state"] != ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The project with id '{project_id_str}' doesn't allow the preparation of modelization update task during this state (state='{state_str}').".format(
                    project_id_str=str(project_id),
                    state_str=str(project_status["state"]),
                ),
            )

        ###
        ### Update data.
        ###

        # Update status by forcing "pending" status.
        if project_status["state"] == ICGUIStates.INITIALIZATION_WITHOUT_MODELIZATION:
            project_status["state"] = ICGUIStates.INITIALIZATION_WITH_PENDING_MODELIZATION
        elif project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION:
            project_status["state"] = ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION
        elif project_status["state"] == ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION:
            project_status["state"] = ICGUIStates.IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION
        elif project_status["state"] == ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION:
            project_status["state"] = ICGUIStates.IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION
        elif project_status["state"] == ICGUIStates.IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION:
            project_status["state"] = ICGUIStates.IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION
        elif project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS:
            project_status["state"] = ICGUIStates.ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS
        #### elif  project_status["state"] == ICGUIStates.ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS:
        else:
            project_status["state"] = ICGUIStates.ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS

        # Prepare status by initializing "task" status.
        project_status["task"] = {
            "progression": 1,
            "detail": "Waiting for background task allocation...",
        }

        ###
        ### Store updated data.
        ###

        # Store updated status in file.
        with open(DATA_DIRECTORY / project_id / "status.json", "w") as status_fileobject_w:
            json.dump(project_status, status_fileobject_w, indent=4)

        ###
        ### Launch backgroundtask.
        ###

        # Add the background task.
        background_tasks.add_task(
            func=backgroundtasks.run_modelization_update_task,
            project_id=project_id,
        )

        # Return statement.
        return {  # pragma: no cover (need radis and worder)
            "project_id": project_id,
            "detail": "In project with id '{project_id_str}', the modelization update task has been requested and is waiting for a background task.".format(
                project_id_str=str(project_id),
            ),
        }


# ==============================================================================
# DEFINE ROUTES FOR CONSTRAINTS SAMPLING
# ==============================================================================


###
### ROUTE: Get constraints sampling results.
###
@app.get(
    "/api/projects/{project_id}/sampling",
    tags=["Constraints sampling"],
    status_code=status.HTTP_200_OK,
)
async def get_constraints_sampling_results(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    iteration_id: Optional[int] = Query(
        None,
        description="The ID of project iteration. If `None`, get the current iteration. Defaults to `None`.",
    ),
) -> Dict[str, Any]:
    """
    Get constraints sampling results.

    Args:
        project_id (str, optional): The ID of the project.
        iteration_id (Optional[int], optional): The ID of project iteration. If `None`, get the current iteration. Defaults to `None`.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the iteration with id `iteration_id` doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the status of the project hasn't completed its sampling step.

    Returns:
        Dict[str, Any]: A dictionary that contains sampling result.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Load settings.
    with open(DATA_DIRECTORY / project_id / "settings.json", "r") as settings_fileobject:
        project_settings: Dict[str, Dict[str, Any]] = json.load(settings_fileobject)

    # Load status file.
    with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
        project_status: Dict[str, Any] = json.load(status_fileobject)

    # Get current iteration id if needed.
    if iteration_id is None:
        if project_status["iteration_id"] == 0:
            iteration_id = 0
        elif (
            project_status["state"] == ICGUIStates.SAMPLING_TODO  # noqa: WPS514
            or project_status["state"] == ICGUIStates.SAMPLING_PENDING
            or project_status["state"] == ICGUIStates.SAMPLING_WORKING
            or project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION
            or project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION
            or project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION
            or project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_ERRORS
        ):
            iteration_id = project_status["iteration_id"] - 1
        else:
            iteration_id = project_status["iteration_id"]

    # Case of iteration `0`.
    if iteration_id == 0:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The iteration `0` has no sampling step.",
        )

    # Check project status.
    if iteration_id == project_status["iteration_id"] and (
        project_status["state"] == ICGUIStates.SAMPLING_TODO  # noqa: WPS514
        or project_status["state"] == ICGUIStates.SAMPLING_PENDING
        or project_status["state"] == ICGUIStates.SAMPLING_WORKING
        or project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION
        or project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION
        or project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION
        or project_status["state"] == ICGUIStates.IMPORT_AT_SAMPLING_STEP_WITH_ERRORS
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The project with id '{project_id_str}' hasn't completed its sampling step on iteration '{iteration_id_str}'.".format(
                project_id_str=str(project_id),
                iteration_id_str=str(iteration_id),
            ),
        )

    # Otherwise check that requested iteration id exist.
    if str(iteration_id) not in project_settings.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' has no iteration with id '{iteration_id_str}'.".format(
                project_id_str=str(project_id),
                iteration_id_str=str(iteration_id),
            ),
        )

    # Load the sampling results.
    with open(DATA_DIRECTORY / project_id / "sampling.json", "r") as sampling_fileobject:
        # Return the project sampling.
        return {
            "project_id": project_id,
            "iteration_id": iteration_id,
            "sampling": json.load(sampling_fileobject)[str(iteration_id)],
        }


###
### ROUTE: Prepare constraints sampling task.
###
@app.post(
    "/api/projects/{project_id}/sampling",
    tags=["Constraints sampling"],
    status_code=status.HTTP_202_ACCEPTED,
)
async def prepare_constraints_sampling_task(
    background_tasks: BackgroundTasks,
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
) -> Dict[str, Any]:
    """
    Prepare constraints sampling task.

    Args:
        background_tasks (BackgroundTasks): A background task to run after the return statement.
        project_id (str): The ID of the project.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the current status of the project doesn't allow the preparation of constraints sampling task.

    Returns:
        Dict[str, Any]: A dictionary that contains the confirmation of the preparation of constraints sampling task.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
            project_status: Dict[str, Any] = json.load(status_fileobject)

        # Check status.
        if project_status["state"] != ICGUIStates.SAMPLING_TODO:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The project with id '{project_id_str}' doesn't allow the preparation of constraints sampling task during this state (state='{state_str}').".format(
                    project_id_str=str(project_id),
                    state_str=str(project_status["state"]),
                ),
            )

        ###
        ### Update data.
        ###

        # Update status by forcing "pending" status.
        project_status["state"] = ICGUIStates.SAMPLING_PENDING

        # Prepare status by initializing "task" status.
        project_status["task"] = {
            "progression": 1,
            "detail": "Waiting for background task allocation...",
        }

        ###
        ### Store updated data.
        ###

        # Store updated status in file.
        with open(DATA_DIRECTORY / project_id / "status.json", "w") as status_fileobject_w:
            json.dump(project_status, status_fileobject_w, indent=4)

        ###
        ### Launch backgroundtask.
        ###

        # Add the background task.
        background_tasks.add_task(
            func=backgroundtasks.run_constraints_sampling_task,
            project_id=project_id,
        )

    # Return statement.
    return {  # pragma: no cover (need radis and worder)
        "project_id": project_id,
        "detail": "In project with id '{project_id_str}', the constraints sampling task has been requested and is waiting for a background task.".format(
            project_id_str=str(project_id),
        ),
    }


# ==============================================================================
# DEFINE ROUTES FOR CONSTRAINED CLUSTERING
# ==============================================================================


###
### ROUTE: Get constrained clustering results.
###
@app.get(
    "/api/projects/{project_id}/clustering",
    tags=["Constrained clustering"],
    status_code=status.HTTP_200_OK,
)
async def get_constrained_clustering_results(
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
    iteration_id: Optional[int] = Query(
        None,
        description="The ID of project iteration. If `None`, get the current iteration. Defaults to `None`.",
    ),
) -> Dict[str, Any]:
    """
    Get constrained clustering results.

    Args:
        project_id (str, optional): The ID of the project.
        iteration_id (Optional[int], optional): The ID of project iteration. If `None`, get the current iteration. Defaults to `None`.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the iteration with id `iteration_id` doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the status of the project hasn't completed its clustering step.

    Returns:
        Dict[str, Any]: A dictionary that contains clustering result.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Load status file.
    with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
        project_status: Dict[str, Any] = json.load(status_fileobject)

    # Load clustering.
    with open(DATA_DIRECTORY / project_id / "clustering.json", "r") as clustering_fileobject:
        project_clustering: Dict[str, Dict[str, Any]] = json.load(clustering_fileobject)

    # Set iteration id if needed.
    if iteration_id is None:
        if (
            project_status["iteration_id"] == 0
            or project_status["state"] == ICGUIStates.ITERATION_END
            or project_status["state"] == ICGUIStates.IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION
            or project_status["state"] == ICGUIStates.IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION
            or project_status["state"] == ICGUIStates.IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION
            or project_status["state"] == ICGUIStates.IMPORT_AT_ITERATION_END_WITH_ERRORS
        ):
            iteration_id = project_status["iteration_id"]
        else:
            iteration_id = project_status["iteration_id"] - 1

    # Check project status.
    if (
        iteration_id == project_status["iteration_id"]
        and project_status["state"] != ICGUIStates.ITERATION_END
        and project_status["state"] != ICGUIStates.IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION
        and project_status["state"] != ICGUIStates.IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION
        and project_status["state"] != ICGUIStates.IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION
        and project_status["state"] != ICGUIStates.IMPORT_AT_ITERATION_END_WITH_ERRORS
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The project with id '{project_id_str}' hasn't completed its clustering step on iteration '{iteration_id_str}'.".format(
                project_id_str=str(project_id),
                iteration_id_str=str(iteration_id),
            ),
        )

    # Otherwise check that requested iteration id exist.
    if str(iteration_id) not in project_clustering.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' has no iteration with id '{iteration_id_str}'.".format(
                project_id_str=str(project_id),
                iteration_id_str=str(iteration_id),
            ),
        )

    # Return the project clustering.
    return {
        "project_id": project_id,
        "iteration_id": iteration_id,
        "clustering": project_clustering[str(iteration_id)],
    }


###
### ROUTE: Prepare constrained clustering task.
###
@app.post(
    "/api/projects/{project_id}/clustering",
    tags=["Constrained clustering"],
    status_code=status.HTTP_202_ACCEPTED,
)
async def prepare_constrained_clustering_task(
    background_tasks: BackgroundTasks,
    project_id: str = Path(
        ...,
        description="The ID of the project.",
    ),
) -> Dict[str, Any]:
    """
    Prepare constrained clustering task.

    Args:
        background_tasks (BackgroundTasks): A background task to run after the return statement.
        project_id (str): The ID of the project.

    Raises:
        HTTPException: Raises `HTTP_404_NOT_FOUND` if the project with id `project_id` doesn't exist.
        HTTPException: Raises `HTTP_403_FORBIDDEN` if the current status of the project doesn't allow the preparation of constrained clustering task.
        HTTPException: Raises `HTTP_504_GATEWAY_TIMEOUT` if the task can't be prepared.

    Returns:
        Dict[str, Any]: A dictionary that contains the confirmation of the preparation of constrained clustering task.
    """

    # Check project id.
    if project_id not in (await get_projects()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project with id '{project_id_str}' doesn't exist.".format(
                project_id_str=str(project_id),
            ),
        )

    # Lock status file in order to check project status for this step.
    with FileLock(str(DATA_DIRECTORY / project_id / "status.json.lock")):
        ###
        ### Load needed data.
        ###

        # Load status file.
        with open(DATA_DIRECTORY / project_id / "status.json", "r") as status_fileobject:
            project_status: Dict[str, Any] = json.load(status_fileobject)

        ###
        ### Check parameters.
        ###

        # Check status.
        if project_status["state"] != ICGUIStates.CLUSTERING_TODO:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The project with id '{project_id_str}' doesn't allow the preparation of constrained clustering task during this state (state='{state_str}').".format(
                    project_id_str=str(project_id),
                    state_str=str(project_status["state"]),
                ),
            )

        ###
        ### Update data.
        ###

        # Update status by forcing "pending" status.
        project_status["state"] = ICGUIStates.CLUSTERING_PENDING

        # Prepare status by initializing "task" status.
        project_status["task"] = {
            "progression": 1,
            "detail": "Waiting for background task allocation...",
        }

        ###
        ### Store updated data.
        ###

        # Store updated status in file.
        with open(DATA_DIRECTORY / project_id / "status.json", "w") as status_fileobject_w:
            json.dump(project_status, status_fileobject_w, indent=4)

        ###
        ### Launch backgroundtask.
        ###

        # Add the background task.
        background_tasks.add_task(
            func=backgroundtasks.run_constrained_clustering_task,
            project_id=project_id,
        )

    # Return statement.
    return {  # pragma: no cover (need radis and worder)
        "project_id": project_id,
        "detail": "In project with id '{project_id_str}', the constrained clustering task has been requested and is waiting for a background task.".format(
            project_id_str=str(project_id),
        ),
    }


# ==============================================================================
# DEFINE ROUTES FOR ANALYTICS
# ==============================================================================

# TODO: Display clusters and FMC patterns.
# TODO: Display components and FMC patterns.
# TODO: Display according evolutions.
