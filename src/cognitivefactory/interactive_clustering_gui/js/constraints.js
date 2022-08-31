/**************************************************
 ******************* CONSTRAINTS ******************
 *************************************************/

/**
 * EVENT: On constraints approval buttons.
 * DESCRIPTION: Approve constraints annotation for this iteration.
 * @param {str} projectID: The ID of the project.
 */
function approveConstraintsAnnotations({
    projectID,
}={}) {

    // Confirmation button.
    if (!confirm("Are you sure you want to approve all constraints ? This operation is not reversible and will lock all constraints until next project iteration.")) {
        return false;
    }

    // Define request for approval.
    var approvalRequest = new XMLHttpRequest();
    approvalRequest.open(
        "POST",
        "/api/projects/"+String(projectID)+"/constraints/approve",
        true,
    );

    // Define onload event of request for approval.
    approvalRequest.onload = function() {

        // Load response.
        var approvalResponse = JSON.parse(
            approvalRequest.response
        );

        // Case of request error: Alert the user of the error.
        if (approvalRequest.status != "201") {
            alert(
                "Error " + approvalRequest.status
                + " " + approvalRequest.statusText
                + ":\n" + JSON.stringify(approvalResponse.detail)
            );
            location.reload();
            return;
        }

        // Go to project home page.
        goToProjectHomePage({projectID:projectID});
    };

    // Send request for approval.
    approvalRequest.send();
}

/**
 * EVENT: On constraint update buttons.
 * DESCRIPTION: Annotate a constraint.
 * @param {str} projectID: The ID of the project.
 * @param {str} constraintID: The ID of the constraint.
 * @param {str} constraintType: The type of the constraint.
 * @param {str} goToNextConstraint: The ID of the next constraint to annotate.
 * @param {bool} goToSummaryPage: The option to load the constraints summay page.
 * @param {str} confirmOption: The option to ask confirmation before send request.
 * @param {bool} reloadOption: The option to reload alert after request acceptance.
 */
function updateConstraint({
    projectID,
    constraintID,
    constraintType,
    goToNextConstraint = null,
    goToSummaryPage = false,
    confirmOption = false,
    reloadOption = true,
}={}) {

    // Confirmation box before sending request.
    if (confirmOption == true || confirmOption == "true") {
        if (!confirm("Please confirm that you want to change the annotation of constraint '" + constraintID + "' from project '" + projectID + "' to '" + constraintType + "'.")) {
            location.reload();
            return;
        }
    }

    // Get required inputs for constraint update.
    var constraintUpdateQuery = "";
    if (constraintType !== null && constraintType != "") {
        constraintUpdateQuery += "?constraint_type=" + String(constraintType);
    }

    // Define request for constraint update.
    var constraintUpdateRequest = new XMLHttpRequest();
    constraintUpdateRequest.open(
        "PUT",
        "/api/projects/"+String(projectID)+"/constraints/"+String(constraintID)+"/annotate"+constraintUpdateQuery,
        true,
    );

    // Define onload event of request for constraint update.
    constraintUpdateRequest.onload = function() {

        // Load response.
        var constraintUpdateResponse = JSON.parse(
            constraintUpdateRequest.response
            );

        // Case of request error: Alert the user of the error.
        if (constraintUpdateRequest.status != "202") {
            alert(
                "Error " + constraintUpdateRequest.status
                + " " + constraintUpdateRequest.statusText
                + ":\n" + JSON.stringify(constraintUpdateResponse.detail));
            location.reload();
            return;
        }

        // Option to go to the next constraint to annotate.
        if (goToNextConstraint !== null && goToNextConstraint != "null") {
            goToConstraintsAnnotationPage({
                projectID:projectID,
                constraintID:goToNextConstraint,
            });
            return;
        }

        // Option to go to the constraints summay page.
        if (goToSummaryPage == true || goToSummaryPage == "true") {
            goToConstraintsSummaryPage({
                projectID:projectID,
            });
            return;
        }

        // Option to reload page to update.
        if (reloadOption == true || reloadOption == "true") {
            location.reload();
            return;
        }
    };

    // Send request for constraint update.
    constraintUpdateRequest.send();
}

/**
 * EVENT: On text deletion buttons.
 * DESCRIPTION: Delete a text.
 * @param {str} projectID: The ID of the project.
 * @param {str} textID: The ID of the text.
 * @param {bool} todelete: The option to delete or not the text.
 * @param {str} goToNextConstraint: The ID of the next constraint to annotate.
 * @param {bool} goToSummaryPage: The option to load the constraints summay page.
 * @param {bool} reloadOption: The option to reload alert after request acceptance.
 */
function deleteText({
    projectID,
    textID,
    toDelete,
    goToNextConstraint = null,
    goToSummaryPage = false,
    reloadOption = true,
}={}) {

    // Define request for text deletion.
    var textDeletionRequest = new XMLHttpRequest();
    if (toDelete) {
        textDeletionRequest.open(
            "PUT",
            "/api/projects/"+String(projectID)+"/texts/"+String(textID)+"/delete",
            true,
        );
    } else {
        textDeletionRequest.open(
            "PUT",
            "/api/projects/"+String(projectID)+"/texts/"+String(textID)+"/undelete",
            true,
        );
    }

    // Define onload event of request for text deletion.
    textDeletionRequest.onload = function() {

        // Load response.
        var textDeletionResponse = JSON.parse(
            textDeletionRequest.response
        );

        // Case of request error: Alert the user of the error.
        if (textDeletionRequest.status != "202") {
            alert(
                "Error " + textDeletionRequest.status
                + " " + textDeletionRequest.statusText
                + ":\n" + JSON.stringify(textDeletionResponse.detail));
            location.reload();
            return;
        }

        // Option to go to the next constraint to annotate.
        if (goToNextConstraint !== null && goToNextConstraint != "null") {
            goToConstraintsAnnotationPage({
                projectID:projectID,
                constraintID:goToNextConstraint,
            });
            return;
        }

        // Option to go to the constraints summay page.
        if (goToSummaryPage == true || goToSummaryPage == "true") {
            goToConstraintsSummaryPage({
                projectID:projectID,
            });
            return;
        }

        // Reload page to update.
        if (reloadOption == true) {
            location.reload();
            return;
        }
    };

    // Send request for text deletion.
    textDeletionRequest.send();
}


/**
 * EVENT: On text renaming buttons.
 * DESCRIPTION: Rename a text.
 * @param {str} projectID: The ID of the project.
 * @param {str} textID: The ID of the text.
 * @param {str} newTextValue: The new value of the text.
 * @param {bool} reloadOption: The option to reload alert after request acceptance.
 */
function renameText({
    projectID,
    textID,
    newTextValue,
    reloadOption = true,
}={}) {

    // Define request for text renaming.
    var textRenamingRequest = new XMLHttpRequest();
    textRenamingRequest.open(
        "PUT",
        "/api/projects/"+String(projectID)+"/texts/"+String(textID)+"/rename?text_value="+encodeURIComponent(String(newTextValue)),
        true,
    );

    // Define onload event of request for text renaming.
    textRenamingRequest.onload = function() {

        // Load response.
        var textRenamingResponse = JSON.parse(
            textRenamingRequest.response
            );

        // Case of request error: Alert the user of the error.
        if (textRenamingRequest.status != "202") {
            alert(
                "Error " + textRenamingRequest.status
                + " " + textRenamingRequest.statusText
                + ":\n" + JSON.stringify(textRenamingResponse.detail));
            location.reload();
            return;
        }

        // Reload page to update.
        if (reloadOption == true) {
            location.reload();
            return;
        }
    };

    // Send request for text renaming.
    textRenamingRequest.send();
}

/**
 * EVENT: On constraint review buttons.
 * DESCRIPTION: Review a constraint.
 * @param {str} projectID: The ID of the project.
 * @param {str} constraintID: The ID of the constraint.
 * @param {str} toReview: The choice to review or not the constraint.
 * @param {bool} reloadOption: The option to reload alert after request acceptance.
 */
function reviewConstraint({
    projectID,
    constraintID,
    toReview,
    reloadOption = true,
}={}) {

    // Define request for constraint review.
    var constraintReviewRequest = new XMLHttpRequest();
    constraintReviewRequest.open(
        "PUT",
        "/api/projects/"+String(projectID)+"/constraints/"+String(constraintID)+"/review?to_review="+String(toReview),
        true,
    );

    // Define onload event of request for constraint review.
    constraintReviewRequest.onload = function() {

        // Load response.
        var constraintReviewResponse = JSON.parse(
            constraintReviewRequest.response
            );

        // Case of request error: Alert the user of the error.
        if (constraintReviewRequest.status != "202") {
            alert(
                "Error " + constraintReviewRequest.status
                + " " + constraintReviewRequest.statusText
                + ":\n" + JSON.stringify(constraintReviewResponse.detail));
            location.reload();
            return;
        }

        // Reload page to update.
        if (reloadOption == true) {
            location.reload();
            return;
        }
    };

    // Send request for constraint review.
    constraintReviewRequest.send();
}

/**
 * EVENT: On constraint comment buttons.
 * DESCRIPTION: Comment a constraint.
 * @param {str} projectID: The ID of the project.
 * @param {str} constraintID: The ID of the constraint.
 * @param {str} comment: The comment of the constraint.
 * @param {bool} reloadOption: The option to reload alert after request acceptance.
 */
function commentConstraint({
    projectID,
    constraintID,
    comment,
    reloadOption = true,
}={}) {

    // Define request for constraint comment.
    var constraintCommentRequest = new XMLHttpRequest();
    constraintCommentRequest.open(
        "PUT",
        "/api/projects/"+String(projectID)+"/constraints/"+String(constraintID)+"/comment?constraint_comment="+String(comment),
        true,
    );

    // Define onload event of request for constraint comment.
    constraintCommentRequest.onload = function() {

        // Load response.
        var constraintCommentResponse = JSON.parse(
            constraintCommentRequest.response
            );

        // Case of request error: Alert the user of the error.
        if (constraintCommentRequest.status != "202") {
            alert(
                "Error " + constraintCommentRequest.status
                + " " + constraintCommentRequest.statusText
                + ":\n" + JSON.stringify(constraintCommentResponse.detail));
            location.reload();
            return;
        }

        // Reload page to update.
        if (reloadOption == true) {
            location.reload();
            return;
        }
    };

    // Send request for constraint comment.
    constraintCommentRequest.send();
}