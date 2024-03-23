/**************************************************
 ******************* ANNOTATION *******************
 *************************************************/

/**
 * EVENT: On window loading.
 * DESCRIPTION: Initialize shortcut keys and constraints graph.
 */
window.addEventListener(
    "load",
    initializeKeysEvents,
)
//window.addEventListener(
//    "load",
//    plotLocalConstraintsGraph,
//)

/**
 * DESCRIPTION: plot local constraints graph.
 * @param {str} projectID: The project id.
 * @param {str} constraintID: The current constraint id.
 * @param {dict} texts: Dictionary of texts.
 * @param {dict} constraints: Dictionary of constraints.
 * @param {dict} modelization: Dictionary of modelization.
 */
function plotLocalConstraintsGraph({
    projectID,
    constraintID,
    texts,
    constraints,
    modelization,
}={}){

    /* GET DATA */

    // Get curent constraint.
    var constraint = constraints[constraintID];
    
    // Get texts ids.
    var text_id1 = constraint.data.id_1;
    var text_id2 = constraint.data.id_2;

    /* SET CONFIGURATION */
    var CONFIG = {
        "NODES": {
            "COLOR": {
                "COMPONENT_1": "#FF9966",
                "COMPONENT_2": "#3399FF",
                "NOT_MODELIZED": "#999999",
            },
            "SIZE": 20,
        },
        "EDGES": {
            "COLOR": {
                "MUST_LINK": "#2D8817",
                "CANNOT_LINK": "#942E1C",
                "NOT_MODELIZED": "#999999",
            },
            "WEIGHT": {
                "MUST_LINK": 150,
                "CANNOT_LINK": 350,
                "NOT_MODELIZED": 350,
            },
            "WIDTH": {
                "ANNOTATED": 8,
                "INFERRED": 4,
                "NOT_MODELIZED": 2,
            },
            "DASHARRAY": {
                "NO_CONFLICT": "10, 0",
                "CONFLICT": "10, 5",
            }
        }
    }

    /* SET GRAPH NODES */

    // Get involved text ids.
    var involved_text_ids = [text_id1, text_id2];
    if (Object.keys(modelization).includes(text_id1)) {
        involved_text_ids = involved_text_ids.concat(modelization[text_id1].MUST_LINK);  // component of id 1.
    }
    if (Object.keys(modelization).includes(text_id2)) {
        involved_text_ids = involved_text_ids.concat(modelization[text_id2].MUST_LINK);  // component of id 2.
    }
    involved_text_ids = new Set(involved_text_ids);

    // Set graph nodes based on involved texts.
    var nodes = {};
    for (var text_id of involved_text_ids) {

        // Create the node.
        nodes[text_id] = {
            "id": String(text_id),
            "text": (
                !texts[text_id].is_deleted
            ) ? String(texts[text_id].text) : "<strike>"+String(texts[text_id].text)+"</strike>",
            "component": (
                !Object.keys(modelization).includes(text_id)
            ) ? null : modelization[text_id].COMPONENT,
            "color": CONFIG["NODES"]["COLOR"][
                (
                    !Object.keys(modelization).includes(text_id)
                ) ? "NOT_MODELIZED" : (
                    (
                        Object.keys(modelization).includes(text_id1)
                        && modelization[text_id].COMPONENT == modelization[text_id1].COMPONENT
                    ) ? "COMPONENT_1" : "COMPONENT_2"
                )
            ],
            "size": CONFIG["NODES"]["SIZE"],
            "fixed": (text_id == text_id1 || text_id == text_id2)
        };
    }

    /* SET GRAPH EDGES */

    // Set graph edges based on annotated or inferred constraints.
    var edges = {};
    for (var source_text_id of involved_text_ids) {
        for (var target_text_id of involved_text_ids) {
            if (source_text_id < target_text_id) {

                // Define constraint id.
                var new_constraint_id = "("+String(source_text_id)+","+String(target_text_id)+")";

                console.log("Constraint ID", new_constraint_id);

                // Case of annotated constraint.
                if (
                    Object.keys(constraints).includes(new_constraint_id)
                    && constraints[new_constraint_id].constraint_type !== null
                ) {
                    // Create the edge.
                    edges[new_constraint_id] = {
                        "id": new_constraint_id,
                        "source": nodes[source_text_id],
                        "target": nodes[target_text_id],
                        "color": CONFIG["EDGES"]["COLOR"][
                            (
                                !Object.keys(modelization).includes(source_text_id)
                                || !Object.keys(modelization).includes(target_text_id)
                            ) ? "NOT_MODELIZED" : constraints[new_constraint_id].constraint_type
                        ],
                        "weight": CONFIG["EDGES"]["WEIGHT"][
                            (
                                !Object.keys(modelization).includes(source_text_id)
                                || !Object.keys(modelization).includes(target_text_id)
                            ) ? "NOT_MODELIZED" : constraints[new_constraint_id].constraint_type
                        ],
                        "width": CONFIG["EDGES"]["WIDTH"][
                            (
                                !Object.keys(modelization).includes(source_text_id)
                                || !Object.keys(modelization).includes(target_text_id)
                            ) ? "NOT_MODELIZED" : "ANNOTATED"
                        ],
                        "dasharray": CONFIG["EDGES"]["DASHARRAY"][
                            (
                                constraints[new_constraint_id].to_fix_conflict
                            ) ? "CONFLICT" : "NO_CONFLICT"
                        ],
                    };
                }
                // Case of inferred constraint in a same component.
                else if (
                    Object.keys(modelization).includes(source_text_id)
                    && Object.keys(modelization).includes(target_text_id)
                    && modelization[source_text_id].COMPONENT == modelization[target_text_id].COMPONENT
                ) {
                    // Create the edge (if texts are in a same component).
                    edges[new_constraint_id] = {
                        "id": (
                            Object.keys(constraints).includes(new_constraint_id)
                        ) ? new_constraint_id : null,
                        "source": nodes[source_text_id],
                        "target": nodes[target_text_id],
                        "color": CONFIG["EDGES"]["COLOR"]["MUST_LINK"],
                        "width": CONFIG["EDGES"]["WIDTH"]["INFERRED"],
                        "weight": CONFIG["EDGES"]["WEIGHT"]["MUST_LINK"],
                        "dasharray": CONFIG["EDGES"]["DASHARRAY"]["NO_CONFLICT"],
                    };
                }
            }
        }
    }

    /* DEFINE SVG AND CONSTANTS */

    // Define canvas size.
    var margin = {top: 5, right: 5, bottom: 5, left: 5},
        width = document.getElementById("plot_local_constraints_graph").clientWidth - 30;
        height = 300;

    // Create the SVG element.
    var svg = d3.select("#plot_local_constraints_graph").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .attr("style", "border:1px solid black; margin: 10px auto;")
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.right + ")");

    // Create the rectangle element.
    var rectangleToHandleEvent = svg.append("rect")
        .attr("width", width)
        .attr("height", height)
        .style("fill", "none")
        .style("pointer-events", "all");

    /* INITIALIZE FORCE SIMULATION */

    // Initialize a force-directed dynamic graph layout.
    var force = d3.layout.force()
        .charge(-50)
        //.linkDistance(150)
        .linkDistance(
            function (e) {
                return e.weight;
            }
        )
        .size([width, height]);

    // Add node and edges and force simulation.
    force
        .nodes(Object.values(nodes))
        .links(Object.values(edges))
        .start();


    /* CREATE GRAPH */

    // Create the container element.
    var graphContainer = svg.append("g");

    // Create edges (<line> SVG element).
    var edgesOnGraph = graphContainer.append("g")
        .attr("class", ".edges")
        .selectAll("line")
        .data(Object.values(edges))
        .enter().append("line")
        .attr("stroke", function(edge) { return edge.color; })  // color
        .attr("id", function(edge) { return edge.id; })  // color
        .attr("weight", function(edge) { return edge.weight; })  // weight
        .attr("stroke-width", function(edge) { return edge.width; })  // width
        .attr("stroke-dasharray", function(edge) { return edge.dasharray; });  // dashed

    // Create nodes (<circle> SVG element).
    var nodesOnGraph = graphContainer.append("g")
        .attr("class", ".nodes")
        .selectAll("cicle")
        .data(Object.values(nodes))
        .enter().append("circle")
        .attr("r", function(node) { return node.size; })  // radius (weight)
        .attr("fill", function(node) { return node.color; });  // circle color

    // Create labels (text element).
    var labelsOnGraph = graphContainer.append("g")
        .attr("class", ".label")
        .selectAll("text")
        .data(Object.values(nodes))
        .enter().append("text")
        .attr("x", "33%")
        .attr("y", "33%")
        .attr("dy", ".35em")
        .attr("text-anchor", "middle")
        .text(function(node) { return node.id; });


    /* HANDLE ZOOM IN RECTANGLE */

    // Handle zoom event.
    var zoom = d3.behavior.zoom()
        .scaleExtent([0.5, 3])
        .on("zoom", function() {
            graphContainer.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
        });
    rectangleToHandleEvent
        .call(zoom);


    /* HANDLE NODE TEXT DISPLAYING AND LINK TO CONSTRAINT */

    // Define a tooltip that will contains node text.
    var tooltip = d3.select("body")
        .append("div")
        .style("position", "absolute")
        .style("visibility", "hidden")
        .style("color", "white")
        .style("padding", "8px")
        .style("background-color", "#626D71")
        .style("border-radius", "6px")
        .style("text-align", "center")
        .style("width", "auto")
        .text("");

    // Function on node hover: Display the tooltip.
    function displayTooltipOfNodeText(node) {
        tooltip.html(`${node.text}`); 
        return tooltip.style("visibility", "visible");
    }
    // Function on mouse move: Move the tooltip.
    function moveTooltipOfNodeText() {
        return tooltip
            .style("top", (d3.event.pageY-10)+"px")
            .style("left",(d3.event.pageX+10)+"px");
    }
    // Function on node not hover: Hide the tooltip.
    function hideTooltipOfNodeText() {
        return tooltip.style("visibility", "hidden");
    }
    
    // Handle tooltip on node.
    nodesOnGraph
        .attr("cursor", "pointer")
        .on("mouseover", displayTooltipOfNodeText)
        .on("mousemove", moveTooltipOfNodeText)
        .on("mouseout", hideTooltipOfNodeText);
    // Handle tooltip on label.
    labelsOnGraph
        .attr("cursor", "pointer")
        .on("mouseover", displayTooltipOfNodeText)
        .on("mousemove", moveTooltipOfNodeText)
        .on("mouseout", hideTooltipOfNodeText);

    
    /* HANDLE EDGE DISPLAYING AND LINK TO CONSTRAINT */

    // Function on edge click: Display the constraint.
    function goToConstraint(edge) {
        if (edge.id !== null) {
            goToConstraintsAnnotationPage({
                projectID: projectID,
                constraintID: `${edge.id}`,
            });
        }
    }

    // Handle event on edge.
    edgesOnGraph
        .attr("cursor", function(edge) { if (edge.id === null) {return "not-allowed";} else {return "pointer";} })
        .on("click", goToConstraint);


    /* HANDLE FORCE SIMULATION */

    // Handle drag on node.
    nodesOnGraph
        .call(force.drag);

    // Handle drag on label.
    labelsOnGraph
        .call(force.drag)

    // Bind positions of SVG elements to positions of dynamic force-directed graph (at each time step).
    force.on("tick", function() {
        edgesOnGraph
            .attr("x1", function(edge) { return Math.max(0 + margin.left, Math.min(edge.source.x, width - margin.right )); })
            .attr("y1", function(edge) { return Math.max(0 + margin.top, Math.min(edge.source.y, height - margin.bottom)); })
            .attr("x2", function(edge) { return Math.max(0 + margin.left, Math.min(edge.target.x, width - margin.right)); })
            .attr("y2", function(edge) { return Math.max(0 + margin.top, Math.min(edge.target.y, height - margin.bottom)); });
        nodesOnGraph
            .attr("cx", function(node) { return Math.max(0 + margin.left, Math.min(node.x, width - margin.right)); })
            .attr("cy", function(node) { return Math.max(0 + margin.top, Math.min(node.y, height - margin.bottom)); });
        labelsOnGraph
            .attr("x", function(text) { return Math.max(0 + margin.left, Math.min(text.x, width - margin.right)); })
            .attr("y", function(text) { return Math.max(0 + margin.top, Math.min(text.y, height - margin.bottom)); });
    });
}

/**
 * DESCRIPTION: Initialize keys events.
 */
function initializeKeysEvents(){
    // Event listener for navigation "MUST_LINK".
    document.addEventListener(
        "keydown",
        (event) => {
            if (
                event.key == "a"
                && document.activeElement.id != "constraint_comment"
            ) {
                console.log("Event:"+String(event.key)+" >> "+"button_annotation_must_link");
                document.getElementById("button_annotation_must_link").onclick();
            }
        }
    )
    // Event listener for navigation "SKIP".
    document.addEventListener(
        "keydown",
        (event) => {
            if (
                event.key == " "
                && document.activeElement.id != "constraint_comment"
            ) {
                console.log("Event:"+String(event.key)+" >> "+"button_annotation_skip");
                document.getElementById("button_annotation_skip").onclick();
            }
        }
    )
    // Event listener for navigation "CANNOT_LINK".
    document.addEventListener(
        "keydown", (event) => {
            if (
                event.key == "r"
                && document.activeElement.id != "constraint_comment"
            ) {
                console.log("Event:"+String(event.key)+" >> "+"button_annotation_cannot_link");
                document.getElementById("button_annotation_cannot_link").onclick();
            }
        }
    )
    // Event listener for navigation "previous".
    document.addEventListener(
        "keydown", (event) => {
            if (
                event.key == "ArrowLeft"
                && document.activeElement.id != "constraint_comment"
            ) {
                console.log("Event:"+String(event.key)+" >> "+"button_navigation_previous");
                if (document.getElementById("button_navigation_previous").disabled == false) {
                    document.getElementById("button_navigation_previous").onclick();
                }
            }
        }
    )
    // Event listener for navigation "annotation home".
    document.addEventListener(
        "keydown",
        (event) => {
            if (
                event.key == "ArrowDown"
                && document.activeElement.id != "constraint_comment"
            ) {
                console.log("Event:"+String(event.key)+" >> "+"button_navigation_home");
                document.getElementById("button_navigation_home").onclick();
            }
        }
    )
    // Event listener for navigation "next".
    document.addEventListener(
        "keydown",
        (event) => {
            if (
                event.key == "ArrowRight"
                && document.activeElement.id != "constraint_comment"
            ) {
                console.log("Event:"+String(event.key)+" >> "+"button_navigation_next");
                if (document.getElementById("button_navigation_next").disabled == false) {
                    document.getElementById("button_navigation_next").onclick();
                }
            }
        }
    )
}