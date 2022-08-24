/**************************************************
 **************** PROJECTS LISTING ****************
 *************************************************/

/**
  * EVENT: On window loading.
  * DESCRIPTION: Initialize shortcut keys.
  */
window.addEventListener(
    "load",
    initializeProjectsListingKeysEvents,
)

/**
 * DESCRIPTION: Initialize keys events.
 */
function initializeProjectsListingKeysEvents() {
    // Event listener for navigation "CREATE_PROJET".
    document.addEventListener(
        "keydown",
        (event) => {
            if (event.key == "Enter") {
                if (
                    ! document.getElementById("popup_project_creation").classList.contains("hide")
                    & document.getElementById("button_create_project").disabled == false
                ) {
                    createProject();
                }
                else if (
                    ! document.getElementById("popup_project_import").classList.contains("hide")
                    & document.getElementById("button_import_project").disabled == false
                ) {
                    importProject();
                }
            }
        }
    )
    // Event listener for navigation "CANCEL_PROJET".
    document.addEventListener(
        "keydown",
        (event) => {
            if (event.key == "Escape") {
                if (! document.getElementById("popup_project_creation").classList.contains("hide")) {
                    closePopup("popup_project_creation");
                }
                if (! document.getElementById("popup_project_import").classList.contains("hide")) {
                    closePopup("popup_project_import");
                }
            }
        }
    )
    // When the user clicks anywhere outside of the close, close it.
    window.onclick = function(event) {
        if (event.target == document.getElementById("popup_project_creation")) {
            closePopup("popup_project_creation");
        }
        if (event.target == document.getElementById("popup_project_import")) {
            closePopup("popup_project_import");
        }
    }
}

/**
 * EVENT: On project creation form submitting.
 * DESCRIPTION: Post the form in order to create a new project.
 */
function createProject() {
    // Lock the form.
    document.getElementById("button_create_project").disabled = true;

    // Get required inputs for project creation.
    var projectName = document.getElementById("input_project_name").value.trim();
    var projectCreationBody = new FormData();
    projectCreationBody.append(
        "dataset_file", document.getElementById("input_dataset_file").files[0]
    );

    // Define request for project creation.
    var projectCreationRequest = new XMLHttpRequest();
    projectCreationRequest.open(
        "POST",
        "/api/projects"+"?"+"project_name="+String(projectName),
        true,
    );

    // Define onload event of request for project creation.
    projectCreationRequest.onload = function() {

        // Load response.
        var projectCreationResponse = JSON.parse(
            projectCreationRequest.response
        );

        // Case of request error: Alert the user of the error.
        if (projectCreationRequest.status != "201") {
            alert(
                "Error " + projectCreationRequest.status
                + " " + projectCreationRequest.statusText
                + ":\n" + JSON.stringify(projectCreationResponse.detail)
            );
            location.reload();
            return;
        }
        // Case of accepted request: Redirect to the project home page.
        goToProjectHomePage({
            projectID:projectCreationResponse.project_id
        })
    };

    // Send request for project creation.
    projectCreationRequest.send(
        projectCreationBody
    );
}

/**
 * EVENT: On project creation form updating.
 * DESCRIPTION: Update the `disabled` status of the submit button according to parameters correctness and page status (project creation progress).
 */
function updateProjectCreationSubmitButton() {
    // Reset sumbit button.
    document.getElementById("button_create_project").disabled = true;

    // Check `project_name`.
    var projectName = document.getElementById("input_project_name").value.trim();
    if (typeof(projectName)!="string" || projectName.length<3 || projectName.length>64) {
        return;
    }
    // Check `dataset_file`.
    var datasetFile = document.getElementById("input_dataset_file").files[0];
    var allowedFiletype = [
        "text/csv",  // .csv
        "application/vnd.ms-excel",  // .csv
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",  // .xlsx
    ];
    if (datasetFile===undefined || !allowedFiletype.includes(datasetFile.type)) {
        return;
    }

    // Conclusion: all check OK.
    document.getElementById("button_create_project").disabled = false;
    return;
}

/**
 * EVENT: On project creation form resetting.
 * DESCRIPTION: Reset form, then update the submit button status.
 */
function resetProjectCreationForm() {
    // Reset the submit button status.
    document.getElementById("button_create_project").disabled = true;
    // Reset the form.
    document.getElementById("project_creation").reset();
}


/**
 * EVENT: On project import form submitting.
 * DESCRIPTION: Post the form in order to import a project.
 */
function importProject() {
    // Lock the form.
    document.getElementById("button_import_project").disabled = true;

    // Get required inputs for project import.
    var projectImportBody = new FormData();
    projectImportBody.append(
        "project_archive", document.getElementById("input_archive_file").files[0]
    );

    // Define request for project import.
    var projectImportRequest = new XMLHttpRequest();
    projectImportRequest.open(
        "PUT",
        "/api/projects"+"?",
        true,
    );

    // Define onload event of request for project import.
    projectImportRequest.onload = function() {

        // Load response.
        var projectImportResponse = JSON.parse(
            projectImportRequest.response
        );

        // Case of request error: Alert the user of the error.
        if (projectImportRequest.status != "201") {
            alert(
                "Error " + projectImportRequest.status
                + " " + projectImportRequest.statusText
                + ":\n" + JSON.stringify(projectImportResponse.detail)
            );
            location.reload();
            return;
        }
        // Case of accepted request: Redirect to the project home page.
        goToProjectHomePage({
            projectID:projectImportResponse.project_id
        })
    };

    // Send request for project import.
    projectImportRequest.send(
        projectImportBody
    );
}

/**
 * EVENT: On project import form updating.
 * DESCRIPTION: Update the `disabled` status of the submit button according to parameters correctness and page status (project import progress).
 */
function updateProjectImportSubmitButton() {
    // Reset sumbit button.
    document.getElementById("button_import_project").disabled = true;

    // Check `archive_file`.
    var archiveFile = document.getElementById("input_archive_file").files[0];
    var allowedFiletype = [
        "application/x-zip-compressed",  // .zip
    ];
    if (archiveFile===undefined || !allowedFiletype.includes(archiveFile.type)) {
        return;
    }

    // Conclusion: all check OK.
    document.getElementById("button_import_project").disabled = false;
    return;
}

/**
 * EVENT: On project import form resetting.
 * DESCRIPTION: Reset form, then update the submit button status.
 */
function resetprojectImportForm() {
    // Reset the submit button status.
    document.getElementById("button_import_project").disabled = true;
    // Reset the form.
    document.getElementById("project_import").reset();
}

/**
 * EVENT: On button popup open.
 * DESCRIPTION: Open the popup.
 * @param {str} popupID: The popup id.
 */
function openPopup(popupID) {
    document.getElementById(popupID).classList.remove("hide");
}

/**
 * EVENT: On button popup close.
 * DESCRIPTION: Open the popup.
 * @param {str} popupID: The popup id.
 */
function closePopup(popupID) {
    document.getElementById(popupID).classList.add("hide");
}
