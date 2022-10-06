const valueButtons = document.querySelectorAll("[number-button]");
const operationButtons = document.querySelectorAll("[operation-button]");
const display = document.querySelector("#display");
const allClearButton = document.querySelector("#all-clear");
const deleteButton = document.querySelector("#delete");
const equalButton = document.querySelector("#equal");

var displayedValue = "";
var computedValue = "";
var selectedOperation = "";

function clearAll() {
  displayedValue = "";
  updateDisplay(displayedValue);
}

function deleteLast() {
  displayedValue = displayedValue.slice(0, displayedValue.length - 1);
  updateDisplay(displayedValue);
}

function processSelectedValue(value) {
  displayedValue = concatenateValue(value);
  updateDisplay(displayedValue);
}

function concatenateValue(value) {
  if (value == "." && displayedValue.includes(".")) return displayedValue;
  return displayedValue + value;
}

function updateDisplay(value) {
  display.innerText = value;
}

function processOperationSelected(operation) {
  if (!displayedValue) {
    alert("Você precisa digitar os números antes da operação");
  }
  selectedOperation = operation;
  computedValue = displayedValue;
  displayedValue = "";
  updateDisplay(displayedValue);
}

function processEqualButton() {
  if (!computedValue || !selectedOperation || !displayedValue) {
    alert(
      "Você deve selecionar dois valores e uma operação antes de ver o resultado"
    );
    return;
  }
  var result;

  switch (selectedOperation) {
    case "+":
      result = String(parseFloat(computedValue) + parseFloat(displayedValue));
      break;
    case "-":
      result = String(parseFloat(computedValue) - parseFloat(displayedValue));
      break;
    case "*":
      result = String(parseFloat(computedValue) * parseFloat(displayedValue));
      break;
    case "/":
      result = String(parseFloat(computedValue) / parseFloat(displayedValue));
      break;
  }

  displayedValue = result;
  computedValue = "";
  updateDisplay(displayedValue);
}

for (button of valueButtons) {
  button.addEventListener("click", function (event) {
    processSelectedValue(event.target.innerText);
  });
}

for (button of operationButtons) {
  button.addEventListener("click", function (event) {
    processOperationSelected(event.target.innerText);
  });
}

allClearButton.addEventListener("click", clearAll);
deleteButton.addEventListener("click", deleteLast);
equalButton.addEventListener("click", processEqualButton);
