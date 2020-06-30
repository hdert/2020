"use strict";
var SELECT = document.getElementById("select");
var RADIO = document.getElementById("radio");
var DEFAULT = document.getElementById("defaultCostSort");
function checkSelect() {
    if (SELECT.options[SELECT.selectedIndex].value == "cost") {
        RADIO.style.display = "inline-block";
    }
    else {
        RADIO.style.display = "none";
        DEFAULT.checked = true;
    }
}
SELECT.onchange = function () {
    checkSelect();
};
checkSelect();
