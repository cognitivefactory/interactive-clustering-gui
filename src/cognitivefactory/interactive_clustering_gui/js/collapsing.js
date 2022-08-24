/**************************************************
 ******************* COLLAPSING *******************
 *************************************************/

/**
  * EVENT: On window loading.
  * DESCRIPTION: Initialize collapsible elements.
  */
window.addEventListener(
    "load",
    initializeCollapsibleElement,
)

/**
 * EVENT: On collapsible element click.
 * DESCRIPTION: Collapse the next element.
 * SOURCE:  https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_collapsible
 */
function initializeCollapsibleElement() {
    // Get all collapsible elements.
    var list_of_collapsible_elements = document.getElementsByClassName("collapsible");

    // Loop over collapsible elements.
    for (var index = 0; index < list_of_collapsible_elements.length; index++) {

        // Add "onclick" event listener.
        list_of_collapsible_elements[index].addEventListener(
            "click",
            function() {
                // Enable or disable hide class on next element.
                this.nextElementSibling.classList.toggle("hide");
            }
        );
    }
}

