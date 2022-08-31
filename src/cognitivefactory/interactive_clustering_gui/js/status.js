/**************************************************
 ********************* STATUS *********************
 *************************************************/

/**
  * EVENT: On window loading.
  * DESCRIPTION: Initialize collapsible elements.
  */
window.addEventListener(
    "load",
    function(){
        updateAllAccordingToProjectStatus({
            projectID:document.getElementById("project_id").textContent.trim(),
        })
    },
)

/**
 * DESCRIPTION: Display the HTML element.
 * @param {str} htmlID: The HTML element ID.
 */
function displayElement(
    htmlID
) {
    var element = document.getElementById(htmlID);
    if (element === null) {
        return;
    }

    element.classList.remove("hide");
}

/**
 * DESCRIPTION: Hide the HTML element.
 * @param {str} htmlID: The HTML element ID.
 */
function hideElement(
    htmlID
) {
    var element = document.getElementById(htmlID);
    if (element === null) {
        return;
    }
    
    element.classList.add("hide");
}

/**
 * DESCRIPTION: Update the status of a button.
 * @param {str} button_id: The id of the button.
 * @param {str} button_status: The status of the button.
 * @param {str} button_disabled: The availability of the button.
 */
function updateButtonStatus({
    button_id,
    button_status,
    button_disabled,
}={}) {

    // Get the button (end if it doesn't exist).
    var button = document.getElementById(button_id);
    if (button === null) {
        return;
    }

    // Set the availability.
    if (button_disabled == true) {
        button.disabled = true;
    } else if (button_disabled == false) {
        button.disabled = false;
    }

    // Reset previous status.
    button.classList.remove("action_todo");
    button.classList.remove("action_wip");
    button.classList.remove("action_error");
    button.classList.remove("action_done");

    // Set the current status.
    if (button_status == "todo") {
        button.classList.add("action_todo");
    } else if (button_status == "wip") {
        button.classList.add("action_wip");
    } else if (button_status == "error") {
        button.classList.add("action_error");
    } else if (button_status == "done") {
        button.classList.add("action_done");
    }
}

/**
 * DESCRIPTION: Update the status of a details.
 * @param {str} details_id: The id of the details.
 * @param {str} details_open: The open status of the details.
 */
function updateDetailsOpenStatus({
    details_id,
    details_open,
}={}) {

    // Get the details (end if it doesn't exist).
    var details = document.getElementById(details_id);
    if (details === null) {
        return;
    }

    // Set the open status.
    if (details_open == true) {
        details.open = true;
    } else if (details_open == false) {
        details.open = false;
    }
}

/**
 * DESCRIPTION: Update the loading bar status.
 * @param {str} loadingbarID: The HTML loading bar ID.
 * @param {int} task_progression: The width of the loading bar.
 * @param {str} task_detail: The message to display in the loading bar.
 */
function updateLoadingBarStatus({
    loadingbarID,
    task_status = "running",
    task_progression = null,
    task_detail = null,
}={}) {

    // Adjust parameters.
    if (task_progression == 0) {
        task_progression = 2;
    }

    // Get the loadingbar (end if it doesn't exist).
    var loadingbar = document.getElementById(loadingbarID);
    if (loadingbar === null) {
        return;
    }
    var loadingbar_bar = loadingbar.getElementsByClassName("loadingbar_bar")[0];
    var loadingbar_icon = loadingbar.getElementsByClassName("loadingbar_icon")[0];
    var loadingbar_text = loadingbar.getElementsByClassName("loadingbar_text")[0];

    // Reset previous status.
    loadingbar_bar.classList.remove("loadingbar_bar_running");
    loadingbar_bar.classList.remove("loadingbar_bar_completed");
    loadingbar_bar.classList.remove("loadingbar_bar_error");
    loadingbar_icon.classList.remove("loadingbar_icon_running");
    loadingbar_icon.classList.remove("loadingbar_icon_completed");
    loadingbar_icon.classList.remove("loadingbar_icon_error");

    // Set the current status.
    if (task_status == "running") {
        if (task_progression === null) {
            task_progression = 2;
        }
        loadingbar_bar.style.width = String(task_progression)+"%";
        loadingbar_bar.classList.add("loadingbar_bar_running");
        loadingbar_icon.classList.add("loadingbar_icon_running");
        if (task_detail === null) {
            task_detail = "Waiting for task detail...";
        }
        loadingbar_text.innerHTML = "<em>"+String(task_detail)+"</em>";
    } else if (task_status == "done") {
        loadingbar_bar.style.width = "100%";
        loadingbar_bar.classList.add("loadingbar_bar_completed");
        loadingbar_icon.classList.add("loadingbar_icon_completed");
        if (task_detail === null) {
            task_detail = "Task is done ! :)";
        }
        loadingbar_text.innerHTML = "<em>"+String(task_detail)+"</em>";
    } else /*if (task_status == "error")*/ {
        if (task_progression === null) {
            task_progression = 100;
        }
        loadingbar_bar.style.width = String(task_progression)+"%";
        loadingbar_bar.classList.add("loadingbar_bar_error");
        loadingbar_icon.classList.add("loadingbar_icon_error");
        if (task_detail === null) {
            task_detail = "Task in error... :(";
        }
        loadingbar_text.innerHTML = "<em>"+String(task_detail)+"</em>";
    }
}

/**
 * DESCRIPTION: Update all fields of the window according to project status.
 * @param {str} projectID: The ID of the project.
 */
function updateAllAccordingToProjectStatus({
    projectID,
}={}) {

    // Define request to get project status.
    var getProjectStatusRequest = new XMLHttpRequest();
    getProjectStatusRequest.open(
        "GET",
        "/api/projects/"+String(projectID)+"/status",
        true,
    );

    // Define onload event of request to get project status.
    getProjectStatusRequest.onload = function() {

        // Load response.
        var getProjectStatusResponse = JSON.parse(
            getProjectStatusRequest.response
        );

        // Case of request error: Alert the user of the error.
        if (getProjectStatusRequest.status != "200") {
            alert(
                "Error " + getProjectStatusRequest.status
                + " " + getProjectStatusRequest.statusText
                + ":\n" + JSON.stringify(getProjectStatusResponse.detail)
            );
            location.reload();
            return;
        }

        // Get status information.
        var iteration_id = getProjectStatusResponse.status.iteration_id;
        var state = getProjectStatusResponse.status.state;
        var task = getProjectStatusResponse.status.task;
        if (task === null) {
            task = {
                "progression": null,
                "detail": null
            }
        }

        // Boolean to determine if update need frequently new update.
        var redoUpdateAllAccordingToProjectStatus = false;

        /*** (1) CASE OF INITIALZE MODELIZATION. ***/
        if (  // Case of INITIALIZATION/IMPORT in TODO.
            [
                "INITIALIZATION_WITHOUT_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION",
            ].includes(state)
        ) {
            displayElement("row_step_initialize_modelization");
            updateButtonStatus({
                button_id: "button_run_initialize_modelization",
                button_status: "todo",
                button_disabled: false,
            });
            updateDetailsOpenStatus({
                details_id: "details_step_initialize_modelization",
                details_open: true,
            });
            hideElement("loadingbar_initialize_modelization");
        } else if (  // Case of INITIALIZATION/IMPORT in PENDING/WORKING.
            [
                "INITIALIZATION_WITH_PENDING_MODELIZATION",
                "INITIALIZATION_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION",
            ].includes(state)
        ) {
            displayElement("row_step_initialize_modelization");
            updateButtonStatus({
                button_id: "button_run_initialize_modelization",
                button_status: "wip",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_step_initialize_modelization",
                details_open: true,
            });
            displayElement("loadingbar_initialize_modelization");
            updateLoadingBarStatus({
                loadingbarID: "loadingbar_initialize_modelization",
                task_status: "running",
                task_progression: task.progression,
                task_detail: task.detail,
            });
            redoUpdateAllAccordingToProjectStatus = true;
        } else if (  // Case of INITIALIZATION/IMPORT in ERRORS.
            [
                "INITIALIZATION_WITH_ERRORS",
                "IMPORT_AT_SAMPLING_STEP_WITH_ERRORS",
                "IMPORT_AT_ANNOTATION_STEP_WITH_ERRORS",
                "IMPORT_AT_CLUSTERING_STEP_WITH_ERRORS",
                "IMPORT_AT_ITERATION_END_WITH_ERRORS",
            ].includes(state)
        ) {
            displayElement("row_step_initialize_modelization");
            updateButtonStatus({
                button_id: "button_run_initialize_modelization",
                button_status: "error",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_step_initialize_modelization",
                details_open: true,
            });
            displayElement("loadingbar_initialize_modelization");
            updateLoadingBarStatus({
                loadingbarID: "loadingbar_initialize_modelization",
                task_status: "error",
                task_progression: 100,
                task_detail: "Modelization in error... :(",
            });
        } else {  // Case of INITIALIZATION/IMPORT in DONE.
            updateDetailsOpenStatus({
                details_id: "details_step_initialize_modelization",
                details_open: false,
            });
            if (
                document.getElementById("loadingbar_initialize_modelization") !== null
                && !document.getElementById("loadingbar_initialize_modelization").classList.contains("hide")
            ) {
                /*
                updateButtonStatus({
                    button_id: "button_run_initialize_modelization",
                    button_status: "done",
                    button_disabled: true,
                });
                updateLoadingBarStatus({
                    loadingbarID: "loadingbar_initialize_modelization",
                    task_status: "done",
                    task_detail: "Modelization done !",
                });
                */
                // TODO: Reload the page.
                location.reload();
            }/* else {
                hideElement("row_step_initialize_modelization");
                hideElement("loadingbar_initialize_modelization");
            }*/
        }

        /*** (2) CASE OF CONSTRAINTS SAMPLING. ***/
        if (  // Case of INITIALIZATION/IMPORT steps.
            [
                "INITIALIZATION_WITHOUT_MODELIZATION",
                "INITIALIZATION_WITH_PENDING_MODELIZATION",
                "INITIALIZATION_WITH_WORKING_MODELIZATION",
                "INITIALIZATION_WITH_ERRORS",
                "IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_ERRORS",
                "IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_ERRORS",
                "IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_ERRORS",
                "IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_ERRORS",
            ].includes(state)
        ) {
            hideElement("row_step_sampling");
            hideElement("loadingbar_sampling");
        } else if (  // Case of ITERATION 0.
            iteration_id == 0
        ) {
            hideElement("row_step_sampling");
            hideElement("loadingbar_sampling");
        } else if (  // Case of SAMPLING in TODO.
            [
                "SAMPLING_TODO",
            ].includes(state)
        ) {
            displayElement("row_step_sampling");
            updateButtonStatus({
                button_id: "button_run_constraints_sampling",
                button_status: "todo",
                button_disabled: false,
            });
            updateDetailsOpenStatus({
                details_id: "details_step_sampling",
                details_open: true,
            });
            hideElement("loadingbar_sampling");
        } else if (  // Case of SAMPLING in PENDING/WORKING.
            [
                "SAMPLING_PENDING",
                "SAMPLING_WORKING",
            ].includes(state)
        ) {
            displayElement("row_step_sampling");
            updateButtonStatus({
                button_id: "button_run_constraints_sampling",
                button_status: "wip",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_step_sampling",
                details_open: true,
            });
            displayElement("loadingbar_sampling");
            updateLoadingBarStatus({
                loadingbarID: "loadingbar_sampling",
                task_status: "running",
                task_progression: task.progression,
                task_detail: task.detail,
            });
            redoUpdateAllAccordingToProjectStatus = true;
        } else {  // Case of SAMPLING in DONE.
            displayElement("row_step_sampling");
            updateButtonStatus({
                button_id: "button_run_constraints_sampling",
                button_status: "done",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_step_sampling",
                details_open: false,
            });
            if (
                document.getElementById("loadingbar_sampling") !== null
                && !document.getElementById("loadingbar_sampling").classList.contains("hide")
            ) {
                /*
                updateLoadingBarStatus({
                    loadingbarID: "loadingbar_sampling",
                    task_status: "done",
                    task_detail: "Constraints sampling done !",
                });
                */
                // TODO: Reload the page.
                location.reload();
            }/* else {
                hideElement("loadingbar_sampling");
            }*/
        }

        /*** (3) CASE OF CONSTRAINTS ANNOTATION. ***/
        if (  // Case of INITIALIZATION/IMPORT steps.
            [
                "INITIALIZATION_WITHOUT_MODELIZATION",
                "INITIALIZATION_WITH_PENDING_MODELIZATION",
                "INITIALIZATION_WITH_WORKING_MODELIZATION",
                "INITIALIZATION_WITH_ERRORS",
                "IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_ERRORS",
                "IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_ERRORS",
                "IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_ERRORS",
                "IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_ERRORS",
            ].includes(state)
        ) {
            hideElement("row_step_annotation_and_modelization");
            hideElement("loadingbar_annotation_and_modelization");
        } else if (  // Case of ITERATION 0.
            iteration_id == 0
        ) {
            hideElement("row_step_annotation_and_modelization");
            hideElement("loadingbar_annotation_and_modelization");
        } else if (  // Case of ANNOTATION in NOT TODO.
            [
                "SAMPLING_TODO",
                "SAMPLING_PENDING",
                "SAMPLING_WORKING",
            ].includes(state)
        ) {
            displayElement("row_step_annotation_and_modelization");
            updateButtonStatus({
                button_id: "button_go_to_annotations",
                button_status: "todo",
                button_disabled: true,
            });
            updateButtonStatus({
                button_id: "button_run_modelization_update",
                button_status: "done",
                button_disabled: true,
            });
            updateButtonStatus({
                button_id: "button_approve_annotations",
                button_status: "todo",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_annotation_and_modelization",
                details_open: false,
            });
            hideElement("loadingbar_annotation_and_modelization");
        } else if (  // Case of ANNOTATION in TODO UPTODATE.
            [
                "ANNOTATION_WITH_UPTODATE_MODELIZATION",
            ].includes(state)
        ) {
            displayElement("row_step_annotation_and_modelization");
            updateButtonStatus({
                button_id: "button_go_to_annotations",
                button_status: "wip",
                button_disabled: false,
            });
            updateButtonStatus({
                button_id: "button_run_modelization_update",
                button_status: "done",
                button_disabled: true,
            });
            updateButtonStatus({
                button_id: "button_approve_annotations",
                button_status: "todo",
                button_disabled: false,
            });
            updateDetailsOpenStatus({
                details_id: "details_annotation_and_modelization",
                details_open: true,
            });
            if (
                document.getElementById("loadingbar_annotation_and_modelization") !== null
                && !document.getElementById("loadingbar_annotation_and_modelization").classList.contains("hide")
            ) {
                /*
                updateLoadingBarStatus({
                    loadingbarID: "loadingbar_annotation_and_modelization",
                    task_status: "done",
                    task_progression: 100,
                    task_detail: "Modelization correctly up to date ! :D",
                });
                */
                // TODO: Reload the page.
                location.reload();
            }/* else {
                hideElement("loadingbar_annotation_and_modelization");
            }*/
        } else if (  // Case of ANNOTATION in TODO OUTDATED without conflicts.
            [
                "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS",
            ].includes(state)
        ) {
            displayElement("row_step_annotation_and_modelization");
            updateButtonStatus({
                button_id: "button_go_to_annotations",
                button_status: "wip",
                button_disabled: false,
            });
            updateButtonStatus({
                button_id: "button_run_modelization_update",
                button_status: "todo",
                button_disabled: false,
            });
            updateButtonStatus({
                button_id: "button_approve_annotations",
                button_status: "todo",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_annotation_and_modelization",
                details_open: true,
            });
            hideElement("loadingbar_annotation_and_modelization");
        } else if (  // Case of ANNOTATION in TODO OUTDATED with conflicts.
            [
                "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
            ].includes(state)
        ) {
            displayElement("row_step_annotation_and_modelization");
            updateButtonStatus({
                button_id: "button_go_to_annotations",
                button_status: "wip",
                button_disabled: false,
            });
            updateButtonStatus({
                button_id: "button_run_modelization_update",
                button_status: "error",
                button_disabled: false,
            });
            updateButtonStatus({
                button_id: "button_approve_annotations",
                button_status: "todo",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_annotation_and_modelization",
                details_open: true,
            });
            if (
                document.getElementById("loadingbar_annotation_and_modelization") !== null
                && !document.getElementById("loadingbar_annotation_and_modelization").classList.contains("hide")
            ) {
                /*
                updateLoadingBarStatus({
                    loadingbarID: "loadingbar_annotation_and_modelization",
                    task_status: "error",
                    task_progression: 100,
                    task_detail: "Some conflicts discovered in the modelization... :(",
                });
                */
                // TODO: Reload the page.
                location.reload();
            }/* else {
                hideElement("loadingbar_annotation_and_modelization");
            }*/
        } else if (  // Case of ANNOTATION in PENDING/WORKING without conflicts.
            [
                "ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS",
                "ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS",
            ].includes(state)
        ) {
            displayElement("row_step_annotation_and_modelization");
            updateButtonStatus({
                button_id: "button_go_to_annotations",
                button_status: "wip",
                button_disabled: false,
            });
            updateButtonStatus({
                button_id: "button_run_modelization_update",
                button_status: "wip",
                button_disabled: true,
            });
            updateButtonStatus({
                button_id: "button_approve_annotations",
                button_status: "todo",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_annotation_and_modelization",
                details_open: true,
            });
            displayElement("loadingbar_annotation_and_modelization");
            updateLoadingBarStatus({
                loadingbarID: "loadingbar_annotation_and_modelization",
                task_status: "running",
                task_progression: task.progression,
                task_detail: task.detail,
            });
            redoUpdateAllAccordingToProjectStatus = true;
        } else if (  // Case of ANNOTATION in PENDING/WORKING with conflicts.
            [
                "ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS",
                "ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS",
            ].includes(state)
        ) {
            displayElement("row_step_annotation_and_modelization");
            updateButtonStatus({
                button_id: "button_go_to_annotations",
                button_status: "wip",
                button_disabled: false,
            });
            updateButtonStatus({
                button_id: "button_run_modelization_update",
                button_status: "wip",
                button_disabled: true,
            });
            updateButtonStatus({
                button_id: "button_approve_annotations",
                button_status: "todo",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_annotation_and_modelization",
                details_open: true,
            });
            displayElement("loadingbar_annotation_and_modelization");
            updateLoadingBarStatus({
                loadingbarID: "loadingbar_annotation_and_modelization",
                task_status: "running",
                task_progression: task.progression,
                task_detail: task.detail,
            });
            redoUpdateAllAccordingToProjectStatus = true;
        } else {  // Case of ANNOTATION in DONE.
            displayElement("row_step_annotation_and_modelization");
            updateButtonStatus({
                button_id: "button_go_to_annotations",
                button_status: "done",
                button_disabled: true,
            });
            updateButtonStatus({
                button_id: "button_run_modelization_update",
                button_status: "done",
                button_disabled: true,
            });
            updateButtonStatus({
                button_id: "button_approve_annotations",
                button_status: "done",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_annotation_and_modelization",
                details_open: false,
            });
            if (
                document.getElementById("loadingbar_annotation_and_modelization") !== null
                && !document.getElementById("loadingbar_annotation_and_modelization").classList.contains("hide")
            ) {
                /*
                updateLoadingBarStatus({
                    loadingbarID: "loadingbar_annotation_and_modelization",
                    task_status: "done",
                    task_progression: 100,
                    task_detail: "Modelization correctly up to date ! :D",
                });
                */
                // TODO: Reload the page.
                location.reload();
            }/* else {
                hideElement("loadingbar_annotation_and_modelization");
            }*/
        }

        /*** (4) CASE OF CONSTRAINTS CLUSTERING. ***/
        if (  // Case of INITIALIZATION/IMPORT steps.
            [
                "INITIALIZATION_WITHOUT_MODELIZATION",
                "INITIALIZATION_WITH_PENDING_MODELIZATION",
                "INITIALIZATION_WITH_WORKING_MODELIZATION",
                "INITIALIZATION_WITH_ERRORS",
                "IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_ERRORS",
                "IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_ERRORS",
                "IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_ERRORS",
                "IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_ERRORS",
            ].includes(state)
        ) {
            hideElement("row_step_clustering");
            hideElement("loadingbar_clustering");
        } else if (  // Case of CLUSTERING in NOT TODO.
            [
                "SAMPLING_TODO",
                "SAMPLING_PENDING",
                "SAMPLING_WORKING",
                "ANNOTATION_WITH_UPTODATE_MODELIZATION",
                "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITHOUT_CONFLICTS",
                "ANNOTATION_WITH_PENDING_MODELIZATION_WITHOUT_CONFLICTS",
                "ANNOTATION_WITH_WORKING_MODELIZATION_WITHOUT_CONFLICTS",
                "ANNOTATION_WITH_OUTDATED_MODELIZATION_WITH_CONFLICTS",
                "ANNOTATION_WITH_PENDING_MODELIZATION_WITH_CONFLICTS",
                "ANNOTATION_WITH_WORKING_MODELIZATION_WITH_CONFLICTS",
            ].includes(state)
        ) {
            displayElement("row_step_clustering");
            updateButtonStatus({
                button_id: "button_run_constrained_clustering",
                button_status: "todo",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_step_clustering",
                details_open: false,
            });
            hideElement("loadingbar_clustering");
        } else if (  // Case of CLUSTERING in TODO.
            [
                "CLUSTERING_TODO",
            ].includes(state)
        ) {
            displayElement("row_step_clustering");
            updateButtonStatus({
                button_id: "button_run_constrained_clustering",
                button_status: "todo",
                button_disabled: false,
            });
            updateDetailsOpenStatus({
                details_id: "details_step_clustering",
                details_open: true,
            });
            hideElement("loadingbar_clustering");
        } else if (  // Case of CLUSTERING in PENDING/WORKING.
            [
                "CLUSTERING_PENDING",
                "CLUSTERING_WORKING",
            ].includes(state)
        ) {
            displayElement("row_step_clustering");
            updateButtonStatus({
                button_id: "button_run_constrained_clustering",
                button_status: "wip",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_step_clustering",
                details_open: true,
            });
            displayElement("loadingbar_clustering");
            updateLoadingBarStatus({
                loadingbarID: "loadingbar_clustering",
                task_status: "running",
                task_progression: task.progression,
                task_detail: task.detail,
            });
            redoUpdateAllAccordingToProjectStatus = true;
        } else {  // Case of CLUSTERING in DONE.
            displayElement("row_step_clustering");
            updateButtonStatus({
                button_id: "button_run_constrained_clustering",
                button_status: "done",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_step_clustering",
                details_open: false,
            });
            if (
                document.getElementById("loadingbar_clustering") !== null
                && !document.getElementById("loadingbar_clustering").classList.contains("hide")
            ) {
                /*
                updateLoadingBarStatus({
                    loadingbarID: "loadingbar_clustering",
                    task_status: "done",
                    task_detail: "Constrained clustering done !",
                });
                */
                // TODO: Reload the page.
                location.reload();
            }/* else {
                hideElement("loadingbar_clustering");
            }*/
        }


        /*** (5) CASE OF ITERATION END. ***/
        if (  // Case of INITIALIZATION/IMPORT steps.
            [
                "INITIALIZATION_WITHOUT_MODELIZATION",
                "INITIALIZATION_WITH_PENDING_MODELIZATION",
                "INITIALIZATION_WITH_WORKING_MODELIZATION",
                "INITIALIZATION_WITH_ERRORS",
                "IMPORT_AT_SAMPLING_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_SAMPLING_STEP_WITH_ERRORS",
                "IMPORT_AT_ANNOTATION_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_ANNOTATION_STEP_WITH_ERRORS",
                "IMPORT_AT_CLUSTERING_STEP_WITHOUT_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_CLUSTERING_STEP_WITH_ERRORS",
                "IMPORT_AT_ITERATION_END_WITHOUT_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_PENDING_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_WORKING_MODELIZATION",
                "IMPORT_AT_ITERATION_END_WITH_ERRORS",
            ].includes(state)
        ) {
            hideElement("row_next_iteration");
        } else if (  // Case of ITERATION_END not in TODO.
            state != "ITERATION_END"
        ) {
            displayElement("row_next_iteration");
            updateButtonStatus({
                button_id: "button_create_next_iteration",
                button_status: "todo",
                button_disabled: true,
            });
            updateDetailsOpenStatus({
                details_id: "details_next_iteration",
                details_open: false,
            });
        } else {  // Case of ITERATION_END not in TODO.
            displayElement("row_next_iteration");
            updateButtonStatus({
                button_id: "button_create_next_iteration",
                button_status: "todo",
                button_disabled: false,
            });
            updateDetailsOpenStatus({
                details_id: "details_next_iteration",
                details_open: true,
            });
        }

        // Need a new update ?
        if (redoUpdateAllAccordingToProjectStatus == true) {

            // Redo.
            setTimeout(
                function() {
                    updateAllAccordingToProjectStatus({
                        projectID:projectID
                    });
                },
                1000,
            );

        }
    };

    // Send request to get project status.
    getProjectStatusRequest.send();
}
