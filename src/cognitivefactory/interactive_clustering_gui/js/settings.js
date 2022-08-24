/**************************************************
 ******************** SETTINGS ********************
 *************************************************/

/**
 * DESCRIPTION: Submit the settings update request.
 * @param {str} projectID: The ID of the project.
 * @param {dict} settings: The settings to send.
 */
function sendSettingsUpdateRequest({
    projectID,
    settings,
}={}) {

    // Define request for settings update.
    var settingsUpdateRequest = new XMLHttpRequest();
    settingsUpdateRequest.open(
        "PUT",
        url="/api/projects/"+String(projectID)+"/settings",
        true,
    )
    settingsUpdateRequest.setRequestHeader(
        "Content-Type", "application/json;charset=UTF-8"
    );

    // Define onload event of request for settings update.
    settingsUpdateRequest.onload = function() {

        // Load response.
        var settingsUpdateResponse = JSON.parse(
            settingsUpdateRequest.response
        );

        // Case of request error: Reload the page.
        if (settingsUpdateRequest.status != "201") {
            alert(
                "Error " + settingsUpdateRequest.status
                + " " + settingsUpdateRequest.statusText
                + ":\n" + JSON.stringify(settingsUpdateResponse.detail));
            location.reload();
            return;
        } else {
            ////alert(settingsUpdateResponse.detail);
            location.reload();
            return;
        }
    }

    // Send request for settings update.
    settingsUpdateRequest.send(
        JSON.stringify(settings)
    );
}

/**
 * EVENT: On preprocessing form updating.
 * DESCRIPTION: Update the `disabled` status of the submit button according to parameters correctness and page status.
 */
function updatePreprocessingSubmitButtonStatus() {

    // Reset submit button.
    document.getElementById("button_preprocessing_settings_submit").disabled = true;

    // Check `preprocessing.apply_stopwords_deletion`.
    // // var apply_stopwords_deletion = document.getElementById("preprocessing.apply_stopwords_deletion").children[1].children[0].children[0].checked;
    // Check `preprocessing.apply_parsing_filter`.
    // // var apply_parsing_filter = document.getElementById("preprocessing.apply_parsing_filter").children[1].children[0].children[0].checked;
    // Check `preprocessing.apply_lemmatization`.
    // // var apply_lemmatization = document.getElementById("preprocessing.apply_lemmatization").children[1].children[0].children[0].checked;
    // Check `preprocessing.spacy_language_model`.
    // // var spacy_language_model = document.getElementById("preprocessing.spacy_language_model").children[1].children[0].value;

    // Conclusion: all check OK.
    document.getElementById("button_preprocessing_settings_submit").disabled = false;
    return;
}

/**
 * EVENT: On preprocessing form resetting.
 * DESCRIPTION: Reset the form, then update the submit button status.
 */
function resetPreprocessingForm() {

    // Reset the form.
    document.getElementById("preprocessing_settings_form").reset();

    // Reset the submit button status.
    updatePreprocessingSubmitButtonStatus();
    document.getElementById("button_preprocessing_settings_submit").disabled = true;
}

/**
 * EVENT: On preprocessing settings submit button.
 * DESCRIPTION: Post the form in order to update settings.
 * @param {str} projectID: The ID of the project.
 */
function updatePreprocessingSettings({
    projectID,
}={}) {

    // Lock the form.
    document.getElementById("button_preprocessing_settings_submit").disabled = true;

    // Get required inputs for settings update.
    var settings = {
        "preprocessing": {
            "apply_stopwords_deletion": document.getElementById("preprocessing.apply_stopwords_deletion").children[1].children[0].children[0].checked,
            "apply_parsing_filter": document.getElementById("preprocessing.apply_parsing_filter").children[1].children[0].children[0].checked,
            "apply_lemmatization": document.getElementById("preprocessing.apply_lemmatization").children[1].children[0].children[0].checked,
            "spacy_language_model": document.getElementById("preprocessing.spacy_language_model").children[1].children[0].value,
        }
    }

    // Send the settings update request.
    sendSettingsUpdateRequest({
        projectID: projectID,
        settings: settings
    });
}

/**
 * EVENT: On vectorization form updating.
 * DESCRIPTION: Update the `disabled` status of the submit button according to parameters correctness and page status.
 */
function updateVectorizationSubmitButtonStatus() {

    // Reset submit button.
    document.getElementById("button_vectorization_settings_submit").disabled = true;

    // Check `vectorization.vectorizer_type`.
    var vectorizer_type = document.getElementById("vectorization.vectorizer_type").children[1].children[0].value;
    if (vectorizer_type == "tfidf") {
        // Update hidden fileds.
        document.getElementById("vectorization.spacy_language_model").classList.add("hide");
    } else {  // if (vectorizer_type == "spacy") {
        // Update hidden fileds.
        document.getElementById("vectorization.spacy_language_model").classList.remove("hide");
        // Check `vectorization.spacy_language_model`.
        var spacy_language_model = document.getElementById("vectorization.spacy_language_model").children[1].children[0].value;
        if (spacy_language_model == "") {
            return;
        }
    }
    // Check `vectorization.random_seed`.
    var random_seed = parseInt(document.getElementById("vectorization.random_seed").children[1].children[0].value);
    if (isNaN(random_seed)) {
        return;
    } else {
        document.getElementById("vectorization.random_seed").children[1].children[0].value = Math.max(random_seed, 0);
    }

    // Conclusion: all check OK.
    document.getElementById("button_vectorization_settings_submit").disabled = false;
    return;
}

/**
 * EVENT: On vectorization form resetting.
 * DESCRIPTION: Reset the form, then update the submit button status.
 */
function resetVectorizationForm() {

    // Reset the form.
    document.getElementById("vectorization_settings_form").reset();

    // Reset the submit button status.
    updateVectorizationSubmitButtonStatus();
    document.getElementById("button_vectorization_settings_submit").disabled = true;
}

/**
 * EVENT: On vectorization settings submit button.
 * DESCRIPTION: Post the form in order to update settings.
 * @param {str} projectID: The ID of the project.
 */
function updateVectorizationSettings({
    projectID,
}={}) {

    // Lock the form.
    document.getElementById("button_vectorization_settings_submit").disabled = true;

    // Get required inputs for settings update.
    var settings = {
        "vectorization": {
            "vectorizer_type": document.getElementById("vectorization.vectorizer_type").children[1].children[0].value,
            "random_seed": parseInt(document.getElementById("vectorization.random_seed").children[1].children[0].value),
        }
    }
    if (settings["vectorization"]["vectorizer_type"] == "spacy") {
        settings["vectorization"]["spacy_language_model"] = document.getElementById("vectorization.spacy_language_model").children[1].children[0].value;
    }

    // Send the settings update request.
    sendSettingsUpdateRequest({
        projectID: projectID,
        settings: settings
    });
}

/**
 * EVENT: On sampling form updating.
 * DESCRIPTION: Update the `disabled` status of the submit button according to parameters correctness and page status.
 */
function updateSamplingSubmitButtonStatus () {

    // Reset submit button.
    document.getElementById("button_sampling_settings_submit").disabled = true;

    // Check `sampling.algorithm`.
    var algorithm = document.getElementById("sampling.algorithm").children[1].children[0].value;
    // Check `sampling.nb_to_select`.
    var nb_to_select = parseInt(document.getElementById("sampling.nb_to_select").children[1].children[0].value);
    if (isNaN(nb_to_select)) {
        return;
    } else {
        document.getElementById("sampling.nb_to_select").children[1].children[0].value = Math.max(nb_to_select, 5);
    }
    // Check `sampling.init_kargs`.
    if (algorithm == "custom") {
        // Update hidden fileds.
        document.getElementById("sampling.custom.clusters_restriction").classList.remove("hide");
        document.getElementById("sampling.custom.distance_restriction").classList.remove("hide");
        document.getElementById("sampling.custom.without_inferred_constraints").classList.remove("hide");
        // Check `sampling.custom.clusters_restriction`.
        var clusters_restriction = document.getElementById("sampling.custom.clusters_restriction").children[1].children[0].value;
        if (clusters_restriction == "") {
            return;
        }
        // Check `sampling.custom.distance_restriction`.
        var distance_restriction = document.getElementById("sampling.custom.distance_restriction").children[1].children[0].value;
        if (distance_restriction == "") {
            return;
        }
        // Check `sampling.custom.without_inferred_constraints`.
        // // var without_inferred_constraints = document.getElementById("sampling.custom.without_inferred_constraints").children[1].children[0].children[0].checked;
    } else { // if (algorithm != "custom") {
        // Update hidden fileds.
        document.getElementById("sampling.custom.clusters_restriction").classList.add("hide");
        document.getElementById("sampling.custom.distance_restriction").classList.add("hide");
        document.getElementById("sampling.custom.without_inferred_constraints").classList.add("hide");
    }

    // Check `sampling.random_seed`.
    var random_seed = parseInt(document.getElementById("sampling.random_seed").children[1].children[0].value);
    if (isNaN(random_seed)) {
        return;
    } else {
        document.getElementById("sampling.random_seed").children[1].children[0].value = Math.max(random_seed, 0);
    }

    // Conclusion: all check OK.
    document.getElementById("button_sampling_settings_submit").disabled = false;
    return;
}

/**
 * EVENT: On sampling form resetting.
 * DESCRIPTION: Reset the form, then update the submit button status.
 */
function resetSamplingForm() {

    // Reset the form.
    document.getElementById("sampling_settings_form").reset();

    // Reset the submit button status.
    updateSamplingSubmitButtonStatus();
    document.getElementById("button_sampling_settings_submit").disabled = true;
}

/**
 * EVENT: On sampling settings submit button.
 * DESCRIPTION: Post the form in order to update settings.
 * @param {str} projectID: The ID of the project.
 */
function updateSamplingSettings({
    projectID,
}={}) {

    // Lock the form.
    document.getElementById("button_sampling_settings_submit").disabled = true;

    // Get required inputs for settings update.
    var settings = {
        "sampling": {
            "algorithm": document.getElementById("sampling.algorithm").children[1].children[0].value,
            "nb_to_select": parseInt(document.getElementById("sampling.nb_to_select").children[1].children[0].value),
            "random_seed": parseInt(document.getElementById("sampling.random_seed").children[1].children[0].value),
        }
    }
    if (settings["sampling"]["algorithm"] == "custom") {
        settings["sampling"]["init_kargs"] = {
            "clusters_restriction": document.getElementById("sampling.custom.clusters_restriction").children[1].children[0].value,
            "distance_restriction": document.getElementById("sampling.custom.distance_restriction").children[1].children[0].value,
            "without_inferred_constraints": document.getElementById("sampling.custom.without_inferred_constraints").children[1].children[0].children[0].checked,
        }
    }

    // Send the settings update request.
    sendSettingsUpdateRequest({
        projectID: projectID,
        settings: settings
    });
}

/**
 * EVENT: On clustering form updating.
 * DESCRIPTION: Update the `disabled` status of the submit button according to parameters correctness and page status.
 */
function updateClusteringSubmitButtonStatus () {

    // Reset submit button.
    document.getElementById("button_clustering_settings_submit").disabled = true;

    // Check `clustering.algorithm`.
    var algorithm = document.getElementById("clustering.algorithm").children[1].children[0].value;
    // Check `clustering.nb_clusters`.
    var nb_clusters = parseInt(document.getElementById("clustering.nb_clusters").children[1].children[0].value);
    if (isNaN(nb_clusters)) {
        return;
    } else {
        document.getElementById("clustering.nb_clusters").children[1].children[0].value = Math.max(nb_clusters, 2);
    }
    // Check `clustering.init_kargs`.
    if (algorithm == "kmeans") {
        // Update hidden fileds.
        document.getElementById("clustering.kmeans.model").classList.remove("hide");
        document.getElementById("clustering.kmeans.max_iteration").classList.remove("hide");
        document.getElementById("clustering.kmeans.tolerance").classList.remove("hide");
        document.getElementById("clustering.hierarchical.linkage").classList.add("hide");
        document.getElementById("clustering.spectral.model").classList.add("hide");
        document.getElementById("clustering.spectral.nb_components").classList.add("hide");
        // Check `clustering.kmeans.model`.
        // // var model = document.getElementById("clustering.kmeans.model").children[1].children[0].value;
        // Check `clustering.kmeans.max_iteration`.
        var max_iteration = parseInt(document.getElementById("clustering.kmeans.max_iteration").children[1].children[0].value);
        if (isNaN(max_iteration)) {
            return;
        } else {
            document.getElementById("clustering.kmeans.max_iteration").children[1].children[0].value = Math.max(max_iteration, 0);
        }
        // Check `clustering.kmeans.tolerance`.
        var tolerance = parseFloat(document.getElementById("clustering.kmeans.tolerance").children[1].children[0].value);
        if (isNaN(tolerance)) {
            return;
        } else {
            document.getElementById("clustering.kmeans.tolerance").children[1].children[0].value = Math.max(tolerance, 0.0);
        }
    } else if (algorithm == "hierarchical") {
        // Update hidden fileds.
        document.getElementById("clustering.kmeans.model").classList.add("hide");
        document.getElementById("clustering.kmeans.max_iteration").classList.add("hide");
        document.getElementById("clustering.kmeans.tolerance").classList.add("hide");
        document.getElementById("clustering.hierarchical.linkage").classList.remove("hide");
        document.getElementById("clustering.spectral.model").classList.add("hide");
        document.getElementById("clustering.spectral.nb_components").classList.add("hide");
        // Check `clustering.hierarchical.linkage`.
        // // var linkage = document.getElementById("clustering.hierarchical.linkage").children[1].children[0].value;
    } else { // if (algorithm == "spectral") {
        // Update hidden fileds.
        document.getElementById("clustering.kmeans.model").classList.add("hide");
        document.getElementById("clustering.kmeans.max_iteration").classList.add("hide");
        document.getElementById("clustering.kmeans.tolerance").classList.add("hide");
        document.getElementById("clustering.hierarchical.linkage").classList.add("hide");
        document.getElementById("clustering.spectral.model").classList.remove("hide");
        document.getElementById("clustering.spectral.nb_components").classList.remove("hide");
        // Check `clustering.spectral.model`.
        // // var model = document.getElementById("clustering.spectral.model").children[1].children[0].value;
        // Check `clustering.spectral.nb_components`.
        var nb_components = parseInt(document.getElementById("clustering.spectral.nb_components").children[1].children[0].value);
        if (isNaN(nb_components)) {
        } else {
            document.getElementById("clustering.spectral.nb_components").children[1].children[0].value = Math.max(nb_components, nb_clusters);
        }
    }
    // Check `clustering.random_seed`.
    var random_seed = parseInt(document.getElementById("clustering.random_seed").children[1].children[0].value);
    if (isNaN(random_seed)) {
        return;
    } else {
        document.getElementById("clustering.random_seed").children[1].children[0].value = Math.max(random_seed, 0);
    }

    // Conclusion: all check OK.
    document.getElementById("button_clustering_settings_submit").disabled = false;
    return;
}

/**
 * EVENT: On clustering form resetting.
 * DESCRIPTION: Reset the form, then update the submit button status.
 */
function resetClusteringForm() {

    // Reset the form.
    document.getElementById("clustering_settings_form").reset();

    // Reset the submit button status.
    updateClusteringSubmitButtonStatus();
    document.getElementById("button_clustering_settings_submit").disabled = true;
}

/**
 * EVENT: On clustering settings submit button.
 * DESCRIPTION: Post the form in order to update settings.
 * @param {str} projectID: The ID of the project.
 */
function updateClusteringSettings({
    projectID,
}={}) {

    // Lock the form.
    document.getElementById("button_clustering_settings_submit").disabled = true;

    // Get required inputs for settings update.
    var settings = {
        "clustering": {
            "algorithm": document.getElementById("clustering.algorithm").children[1].children[0].value,
            "nb_clusters": parseInt(document.getElementById("clustering.nb_clusters").children[1].children[0].value),
            "random_seed": parseInt(document.getElementById("clustering.random_seed").children[1].children[0].value),
        }
    }
    if (settings["clustering"]["algorithm"] == "kmeans") {
        settings["clustering"]["init_kargs"] = {
            "model": document.getElementById("clustering.kmeans.model").children[1].children[0].value,
            "max_iteration": parseInt(document.getElementById("clustering.kmeans.max_iteration").children[1].children[0].value),
            "tolerance": parseFloat(document.getElementById("clustering.kmeans.tolerance").children[1].children[0].value)
        }
    } else if (settings["clustering"]["algorithm"] == "hierarchical") {
        settings["clustering"]["init_kargs"] = {
            "linkage": document.getElementById("clustering.hierarchical.linkage").children[1].children[0].value,
        }
    } else if (settings["clustering"]["algorithm"] == "spectral") {
        settings["clustering"]["init_kargs"] = {
            "model": document.getElementById("clustering.spectral.model").children[1].children[0].value,
        }
        var nb_components = parseInt(document.getElementById("clustering.spectral.nb_components").children[1].children[0].value);
        if (isNaN(nb_components)) {
            settings["clustering"]["init_kargs"]["nb_components"] = null;
        } else {
            settings["clustering"]["init_kargs"]["nb_components"] = nb_components;
        }
    }

    // Send the settings update request.
    sendSettingsUpdateRequest({
        projectID: projectID,
        settings: settings
    });
}