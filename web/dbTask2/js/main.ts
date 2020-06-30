"use strict";

let SELECT = document.getElementById("select") as HTMLSelectElement;
let RADIO = document.getElementById("radio") as HTMLDivElement;

function checkSelect() {
  if (SELECT.options[SELECT.selectedIndex].value == "cost") {
    RADIO.style.display = "inline-block";
  } else {
    RADIO.style.display = "none";
  }
}

SELECT.onchange = function () {
  checkSelect();
};

checkSelect();
