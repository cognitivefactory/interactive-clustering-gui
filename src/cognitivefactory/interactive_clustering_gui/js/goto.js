/**************************************************
 ********************* GO TO **********************
 *************************************************/

/**
 * DESCRIPTION: Go to the welcome page.
 */
function goToWelcomePage() {
    location.assign("/");
}

/**
 * DESCRIPTION: Go to the help page.
 */
function goToHelpPage() {
    location.assign("/gui/help");
}

/**
 * DESCRIPTION: Mail to contacts.
 */
function mailToContacts() {
    location.assign("mailto:erwan.schild@e-i.com?cc=eidph330@e-i.com&subject=[congitivefactory/interactive-clustering-gui]");
}

/**
 * DESCRIPTION: Go to the projects listing and creation page.
 */
function goToProjectsSummaryPage() {
    location.assign("/gui/projects");
}

/**
 * DESCRIPTION: Go to the project home page.
 * @param {str} projectID: The ID of the project.
 */
function goToProjectHomePage({
    projectID,
}={}) {
    location.assign("/gui/projects/"+String(projectID));
}

/**
 * DESCRIPTION: Go to the constraints summary page.
 * @param {str} projectID: The ID of the project.
 * @param {str} sortedBy: The option to sort constraints.
 * @param {str} sortedReverse: The option to reverse constraints order.
 */
function goToConstraintsSummaryPage({
    projectID,
    sortedBy = "iteration_of_sampling",
    sortedReverse = true,
}={}) {
    location.href = "/gui/projects/"+String(projectID)+"/constraints"+"?sorted_by="+String(sortedBy)+"&sorted_reverse="+String(sortedReverse);
}

/**
 * DESCRIPTION: Go to the texts summary page.
 * @param {str} projectID: The ID of the project.
 * @param {str} sortedBy: The option to sort texts.
 * @param {str} sortedReverse: The option to reverse texts order.
 */
function goToTextsSummaryPage({
    projectID,
    sortedBy = "alphabetical",
    sortedReverse = false,
}={}) {
    location.href = "/gui/projects/"+String(projectID)+"/texts"+"?sorted_by="+String(sortedBy)+"&sorted_reverse="+String(sortedReverse);
}

/**
 * DESCRIPTION: Go to the constraint annotation page.
 * @param {str} projectID: The ID of the project.
 * @param {str} constraintID: The ID of the constraint to annotate.
 */
function goToConstraintsAnnotationPage({
    projectID,
    constraintID,
}={}) {
    location.assign("/gui/projects/"+String(projectID)+"/constraints/"+String(constraintID));
}

/**
 * DESCRIPTION: Go to the settings page.
 * @param {str} projectID: The ID of the project.
 * @param {str, optional} iterationID: The ID of the iteration. Can be null.
 * @param {str, optional} settingsNames: The names of settings to set. Can be null.
 */
function goToSettingsPage({
    projectID,
    iterationID = null,
    settingsNames = ['preprocessing', 'vectorization', 'sampling', 'clustering'],
}={}) {
    var query = "";
    // Iteration query.
    if (iterationID !== null) {
        query += "?"+"iteration_id="+String(iterationID);
    }
    // Settings names query.
    if (settingsNames != null) {
        if (query == "") {
            query += "?";
        }
        else {
            query += "&";
        }
        for (var i = 0; i<settingsNames.length; i++) {
            if (i != 0) {
                query += "&"
            }
            query += "settings_names="+String(settingsNames[i])
        }
    }
    console.log(query)
    location.assign("/gui/projects/"+String(projectID)+"/settings"+query);
}

/**
 * DESCRIPTION: Go to the analytics page.
 * @param {str} projectID: The ID of the project.
 */
function goToAnalyticsPage({
    projectID,
}={}) {
    location.assign("/gui/projects/"+String(projectID)+"/analytics");
}
