const input = document.querySelector("#guessing-input>input");
const tryButton = document.querySelector("#try-button");
const playAgainButton = document.querySelector("#play-again");
const playAgainDiv = document.querySelector("[play-again-div]");

const previouesTentativeDisplay = document.querySelector("#previous-try");
const sucessMessageDiv = document.querySelector("#success-message");
const errorMessageDiv = document.querySelector("#error-message");
const hintDisplay = document.querySelector("#hint");

const HINT_FOR_BIGGER_TRY = "Um pouco menos...";
const HINT_FOR_SMALLER_TRY = "Um pouco mais...";
const PREVIOUS_TRY_INITIAL = "Você já tentou o(s) seguinte(s) número(s): ";

var numberToBeGuessed;
var tentativesQuantity;
var previouesTentative;

function resetGame() {
  numberToBeGuessed = Math.floor(Math.random() * 100 + 1);
  tentativesQuantity = 0;
  previouesTentative = PREVIOUS_TRY_INITIAL;
  previouesTentativeDisplay.innerHTML = previouesTentative;
  input.disabled = false;
  tryButton.disabled = false;
  errorMessageDiv.style.display = "none";
  sucessMessageDiv.style.display = "none";
  hintDisplay.style.display = "none";
  playAgainDiv.style.display = "none";

  console.log("Game is starting..." + numberToBeGuessed);
}

resetGame();

function freezeGame() {
  input.disabled = true;
  tryButton.disabled = true;
  playAgainDiv.style.display = "block";
}

function cleanInput() {
  input.value = "";
}

function checkTentative(tentative) {
  addTentative(tentative);
  if (tentative != numberToBeGuessed) {
    errorMessageDiv.style.display = "block";
    if (tentativesQuantity >= 10) {
      freezeGame();
    }
  } else {
    errorMessageDiv.style.display = "none";
    sucessMessageDiv.style.display = "block";
    freezeGame();
  }
}

function addTentative(tentative) {
  previouesTentative = previouesTentative + " " + tentative;
  previouesTentativeDisplay.style.display = "block";
  previouesTentativeDisplay.innerHTML = previouesTentative;
  tentativesQuantity = tentativesQuantity + 1;
}

function GuessTheNumber(tentative) {
  cleanInput();
  checkTentative(tentative);
}

tryButton.addEventListener("click", function () {
  GuessTheNumber(input.value);
});

playAgainButton.addEventListener("click", resetGame);
