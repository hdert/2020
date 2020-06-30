"use strict";

let SELECT = document.getElementById("select") as HTMLSelectElement;
let RADIO = document.getElementById("radio") as HTMLDivElement;
let DEFAULT = document.getElementById("defaultCostSort") as HTMLInputElement;

function checkSelect() {
  if (SELECT.options[SELECT.selectedIndex].value == "cost") {
    RADIO.style.display = "inline-block";
  } else {
    RADIO.style.display = "none";
    DEFAULT.checked = true;
  }
}

SELECT.onchange = function () {
  checkSelect();
};

checkSelect();
