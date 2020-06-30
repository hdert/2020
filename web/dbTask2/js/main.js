"use strict";
var SELECT = document.getElementById("select");
var RADIO = document.getElementById("radio");
function checkSelect() {
    if (SELECT.options[SELECT.selectedIndex].value == "cost") {
        RADIO.style.display = "inline-block";
    }
    else {
        RADIO.style.display = "none";
    }
}
SELECT.onchange = function () {
    checkSelect();
};
checkSelect();
