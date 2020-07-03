"use strict";

const SELECT = document.getElementById("select") as HTMLSelectElement;
const RADIO = document.getElementById("radio") as HTMLDivElement;
const DEFAULT = document.getElementById("defaultCostSort") as HTMLInputElement;

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
