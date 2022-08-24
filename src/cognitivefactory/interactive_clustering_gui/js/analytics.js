/**************************************************
 ********************* EVENTS *********************
 *************************************************/


/**
 * DESCRIPTION: Get data.
 */
function getDataAndPlotGraphs() {
    
    // Get project information.
    var projectID = document.getElementById("project_id").textContent.trim();
    var iterationID = document.getElementById("iteration_id").textContent.trim();

    // Define request for data vectors getter.
    var dataVectorsGetterRequest = new XMLHttpRequest();
    dataVectorsGetterRequest.open(
        method="GET",
        url="/api/projects/"+String(projectID)+"/data/"+String(iterationID)+"/vectors",
        true,
    );

    // Define onload event of request for data vectors getter.
    dataVectorsGetterRequest.onload = function() {

        // Load response.
        var dataVectorsGetterResponse = JSON.parse(dataVectorsGetterRequest.response);

        // Case of iteration forbiden..
        if (dataVectorsGetterRequest.status == "403") {
            document.getElementById("plot_2d").innerText = "Please run clustering step before perform the analysis of this iteration."
            document.getElementById("plot_3d").innerText = "Please run clustering step before perform the analysis of this iteration."
        }
        // Case of request error: Alert the user of the error.
        else if (dataVectorsGetterRequest.status != "200") {
            alert("Error " + dataVectorsGetterRequest.status + " " + dataVectorsGetterRequest.statusText + ":\n" + JSON.stringify(dataVectorsGetterResponse.detail));
            location.reload();
            return;
        }

        // Plot the 3D graph.
        plot2Dand3DGraph(dataToPlot=dataVectorsGetterResponse["vectors"]);
    }

    // Send request for data vectors getter.
    dataVectorsGetterRequest.send();
}


/**
 * DESCRIPTION: Plot 2D and 3D Graph.
 * @param {dict} dataToPlot: The data formatted by the server.
 */
function plot2Dand3DGraph(dataToPlot) {

    // Determine the traces to plot.
    var groupDataByClusters = {}
    for (var [dataID, dataInfo] of Object.entries(dataToPlot)) {
        if (! (dataInfo["cluster_id"] in groupDataByClusters)) {
            groupDataByClusters[dataInfo["cluster_id"]] = [];
        }
        groupDataByClusters[dataInfo["cluster_id"]].push(dataID);
    }

    // Format traces to plot
    var tracesToPlot2D = [];
    var tracesToPlot3D = [];
    for (var [clusterID, listOfDataIDs] of Object.entries(groupDataByClusters)) {
        
        // Initialize the trace.
        var trace2D = {
            "x": [],
            "y": [],
            "mode": "markers",
            "marker": {
                "color": clusterID,
                "size": 8,
                "symbol": "circle",
                "line": {
                    "color": clusterID,
                    "width": 1,
                },
                "opacity": 0.8,
            },
            "type": "scatter2d",
            "name": "Cluster " + String(clusterID),
            "custom_data": [],
            "text": [],
        };
        var trace3D = {
            "x": [],
            "y": [],
            "z": [],
            "mode": "markers",
            "marker": {
                "color": clusterID,
                "size": 8,
                "symbol": "circle",
                "line": {
                    "color": clusterID,
                    "width": 1,
                },
                "opacity": 0.8,
            },
            "type": "scatter3d",
            "name": "Cluster " + String(clusterID),
            "custom_data": [],
            "text": [],
        };

        // Add each data of this trace.
        for (var dataIDInThisTrace of listOfDataIDs) {

            // Case of 2D trace.
            trace2D["x"].push(dataToPlot[dataIDInThisTrace]["vector_3d"]["x"]);
            trace2D["y"].push(dataToPlot[dataIDInThisTrace]["vector_3d"]["y"]);
            trace2D["custom_data"].push(dataIDInThisTrace);
            trace2D["text"].push(dataToPlot[dataIDInThisTrace]["text"]);

            // Case of 3D trace.
            trace3D["x"].push(dataToPlot[dataIDInThisTrace]["vector_3d"]["x"]);
            trace3D["y"].push(dataToPlot[dataIDInThisTrace]["vector_3d"]["y"]);
            trace3D["z"].push(dataToPlot[dataIDInThisTrace]["vector_3d"]["z"]);
            trace3D["custom_data"].push(dataIDInThisTrace);
            trace3D["text"].push(dataToPlot[dataIDInThisTrace]["text"]);
        }

        // Add the trace.
        tracesToPlot2D.push(trace2D);
        tracesToPlot3D.push(trace3D);
    }

    // Create the layout.
    var layout2D = {
        "margin": {
            "l": "0.25%",
            "r": "0.25%",
            "b": "0.25%",
            "t": "0.25%",
        },
        "title": "Plot data by clusters in 2D.",
    };
    var layout3D = {
        "margin": {
            "l": "0.25%",
            "r": "0.25%",
            "b": "0.25%",
            "t": "0.25%",
        },
        "title": "Plot data by clusters in 3D.",
    };

    // Plot the 2D graph.
    document.getElementById("plot_2d").innerHTML = null;
    Plotly.newPlot(
        "plot_2d",
        tracesToPlot2D,
        layout2D,
    );

    // Plot the 3D graph.
    document.getElementById("plot_3d").innerHTML = null;
    Plotly.newPlot(
        "plot_3d",
        tracesToPlot3D,
        layout3D,
    );
}
