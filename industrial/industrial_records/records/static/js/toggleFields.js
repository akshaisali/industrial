// static/js/toggleFields.js

function toggleFields() {
    var isHeading = document.getElementById("id_is_heading").checked;
    var fieldsToToggle = ["id_quantity", "id_make", "id_purpose", "id_price", "id_total"];

    for (var i = 0; i < fieldsToToggle.length; i++) {
        document.getElementById(fieldsToToggle[i]).disabled = isHeading;
    }
}

window.onload = function() {
    toggleFields(); // Call toggleFields() on page load to set initial state
};
