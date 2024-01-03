/**************************************************
 ******************** PROJECTS ********************
 *************************************************/

/**
 * EVENT: On button project deleting.
 * DESCRIPTION: Delete the project.
 * @param {str} projectID: The ID of the project.
 */
function deleteProject({
    projectID,
    projectName,
}={}) {

    // Confirmation box before deletion.
    if (!confirm("Please confirm that you want to delete the project named '" + projectName + "' with ID '" + projectID + "'.")) {
        return false;
    }

    // Define request for project deletion.
    var projectDeletionRequest = new XMLHttpRequest();
    projectDeletionRequest.open(
        "DELETE",
        "/api/projects/"+String(projectID),
        true,
    );

    // Define onload event of request for project deletion.
    projectDeletionRequest.onload = function() {

        // Load response.
        var projectDeletionResponse = JSON.parse(
            projectDeletionRequest.response
        );

        // Case of request error: Alert the user of the error.
        if (projectDeletionRequest.status != "202") {
            alert(
                "Error " + projectDeletionRequest.status
                + " " + projectDeletionRequest.statusText
                + ":\n" + JSON.stringify(projectDeletionResponse.detail)
            );
            location.reload();
            return;
        }

        // Go to projects summary page.
        goToWelcomePage();
    };

    // Send request for project deletion.
    projectDeletionRequest.send();
}

/**
 * EVENT: On button project downloading.
 * DESCRIPTION: Download the project.
 * @param {str} projectID: The ID of the project.
 */
function downloadProject({
    projectID,
}={}) {

    // Define request to get project metadata in order to check if project still exist.
    var projectMetadataRequest = new XMLHttpRequest();
    projectMetadataRequest.open(
        "GET",
        "/api/projects/"+String(projectID)+"/metadata",
        true,
    );

    // Define onload event of request to get project metadata.
    projectMetadataRequest.onload = function() {

        // Load response.
        var projectMetadataResponse = JSON.parse(
            projectMetadataRequest.response
        );

        // Case of request error: Alert the user of the error.
        if (projectMetadataRequest.status != "200") {
            alert(
                "Error " + projectMetadataRequest.status
                + " " + projectMetadataRequest.statusText
                + ":\n" + JSON.stringify(projectMetadataResponse.detail)
            );
            location.reload();
            return;
        }

        // Project still exist: Download archive.
        var downloadProjectlink = document.createElement("a");
        downloadProjectlink.href = "/api/projects/"+String(projectID)+"/download";
        downloadProjectlink.click();
    };

    // Send request for project Downloading.
    projectMetadataRequest.send();
}
