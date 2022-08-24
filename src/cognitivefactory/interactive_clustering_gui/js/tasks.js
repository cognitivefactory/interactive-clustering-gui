/**************************************************
 ********************* EVENTS *********************
 *************************************************/

/**
 * EVENT: On button modelization update request.
 * DESCRIPTION: Request modelization update task and frequently check the status evolution.
 * @param {str} projectID: The ID of the project.
 */
function runModelizationUpdateTask({
    projectID,
}={}) {

    // Block the button.
    updateButtonStatus({
        button_id: "button_run_initialize_modelization",
        button_status: "wip",
        button_disabled: true,
    });
    // Block the button.
    updateButtonStatus({
        button_id: "button_run_modelization_update",
        button_status: "wip",
        button_disabled: true,
    });

    // Define request for modelization update task.
    var modelizationUpdateTaskRequest = new XMLHttpRequest();
    modelizationUpdateTaskRequest.open(
        "POST",
        "/api/projects/"+String(projectID)+"/modelization",
        true,
    );

    // Define onload event of request for modelization update task.
    modelizationUpdateTaskRequest.onload = function() {

        // Load response.
        var modelizationUpdateTaskResponse = JSON.parse(
            modelizationUpdateTaskRequest.response
        );

        // Case of request error: Alert the user of the error.
        if (modelizationUpdateTaskRequest.status != "202") {
            alert(
                "Error " + modelizationUpdateTaskRequest.status
                + " " + modelizationUpdateTaskRequest.statusText
                + ":\n" + JSON.stringify(modelizationUpdateTaskResponse.detail)
            );
            location.reload();
            return;
        }

        // Check status evolution.
        /*
        updateAllAccordingToProjectStatus({
            projectID:projectID
        });
        */
        // TODO: Reload the page.
        location.reload();
    };

    // Send request for modelization update task.
    modelizationUpdateTaskRequest.send();
}

/**
 * EVENT: On button constraints sampling request.
 * DESCRIPTION: Request constraints sampling task and frequently check the status evolution.
 * @param {str} projectID: The ID of the project.
 */
function runConstraintsSamplingTask({
    projectID,
}={}) {

    // Block the button.
    updateButtonStatus({
        button_id: "button_run_constraints_sampling",
        button_status: "wip",
        button_disabled: true,
    });

    // Define request for constraints sampling task.
    var constraintsSamplingTaskRequest = new XMLHttpRequest();
    constraintsSamplingTaskRequest.open(
        "POST",
        "/api/projects/"+String(projectID)+"/sampling",
        true,
    );

    // Define onload event of request for constraints sampling task.
    constraintsSamplingTaskRequest.onload = function() {

        // Load response.
        var constraintsSamplingTaskResponse = JSON.parse(
            constraintsSamplingTaskRequest.response
        );

        // Case of request error: Alert the user of the error.
        if (constraintsSamplingTaskRequest.status != "202") {
            alert(
                "Error " + constraintsSamplingTaskRequest.status
                + " " + constraintsSamplingTaskRequest.statusText
                + ":\n" + JSON.stringify(constraintsSamplingTaskResponse.detail)
            );
            location.reload();
            return;
        }

        // Check status evolution.
        /*
        updateAllAccordingToProjectStatus({
            projectID:projectID
        });
        */
        // TODO: Reload the page.
        location.reload();
    };

    // Send request for constraints sampling task.
    constraintsSamplingTaskRequest.send();
}

/**
 * EVENT: On button constrained clustering request.
 * DESCRIPTION: Run the constrained clustering request and frequently check the status evolution.
 * @param {str} projectID: The ID of the project.
 */
function runConstrainedClusteringTask({
    projectID,
}={}) {

    // Block the button.
    updateButtonStatus({
        button_id: "button_run_constrained_clustering",
        button_status: "wip",
        button_disabled: true,
    });

    // Define request for constrained clustering task.
    var constrainedClusteringTaskRequest = new XMLHttpRequest();
    constrainedClusteringTaskRequest.open(
        "POST",
        "/api/projects/"+String(projectID)+"/clustering",
        true,
    );

    // Define onload event of request for constrained clustering task.
    constrainedClusteringTaskRequest.onload = function() {

        // Load response.
        var constrainedClusteringTaskResponse = JSON.parse(
            constrainedClusteringTaskRequest.response
        );

        // Case of request error: Alert the user of the error.
        if (constrainedClusteringTaskRequest.status != "202") {
            alert(
                "Error " + constrainedClusteringTaskRequest.status
                + " " + constrainedClusteringTaskRequest.statusText
                + ":\n" + JSON.stringify(constrainedClusteringTaskResponse.detail)
            );
            location.reload();
            return;
        }

        // Check status evolution.
        /*
        updateAllAccordingToProjectStatus({
            projectID:projectID
        });
        */
        // TODO: Reload the page.
        location.reload();
    };

    // Send request for constrained clustering task.
    constrainedClusteringTaskRequest.send();
}

/**
 * EVENT: On button iteration creation submitting.
 * DESCRIPTION: Create the next iteration for this project.
 * @param {str} projectID: The ID of the project.
 */
function createNextIteration({
    projectID,
}={}) {

    // Block the button.
    updateButtonStatus({
        button_id: "button_create_next_iteration",
        button_status: "wip",
        button_disabled: true,
    });

    // Define request for iteration creation.
    var iterationCreationRequest = new XMLHttpRequest();
    iterationCreationRequest.open(
        "POST",
        "/api/projects/"+String(projectID)+"/iterations",
        true,
    );

    // Define onload event of request for iteration creation.
    iterationCreationRequest.onload = function() {

        // Load response.
        var iterationCreationResponse = JSON.parse(
            iterationCreationRequest.response
        );

        // Case of request error: Alert the user of the error.
        if (iterationCreationRequest.status != "201") {
            alert(
                "Error " + iterationCreationRequest.status
                + " " + iterationCreationRequest.statusText
                + ":\n" + JSON.stringify(iterationCreationResponse.detail)
            );
            location.reload();
            return;
        }

        // Reload the page for the new iteration.
        location.reload();
    };

    // Send request for iteration creation.
    iterationCreationRequest.send();
}
