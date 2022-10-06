const inputTentativa = document.querySelector("#input-tentativa");
const botaoEnviarTentativa = document.querySelector("#botao-enviar-tentativa");
const bannerSucesso = document.querySelector("#banner-sucesso");
const bannerErro = document.querySelector("#banner-erro");
const botaoResetarJogo = document.querySelector("#reset-jogo");

const TEXTO_ERRO_MAIOR = "Opa, você errou, tente um número menor.";
const TEXTO_ERRO_MENOR = "Opa, você errou, tente um número maior.";
const TEXTO_PADRAO_TENTATIVAS_USUARIO = "Você ja tentou os seguintes números: ";

var tentativasUsuario = document.querySelector("#tentativas-do-usuario");
var valorGeradoAleatoriamente = Math.floor(Math.random() * 100 + 1);
var quantidadeDeTentativas = 0;
var listaDeTentativas = [];

tentativasUsuario.innerHTML = TEXTO_PADRAO_TENTATIVAS_USUARIO;

function resetarJogo() {
  tentativasUsuario.innerHTML = TEXTO_PADRAO_TENTATIVAS_USUARIO;
  quantidadeDeTentativas = 0;
  bannerErro.style.display = "none";
  bannerSucesso.style.display = "none";
  botaoResetarJogo.style.display = "none";
  inputTentativa.disabled = false;
  botaoEnviarTentativa.disabled = false;
  valorGeradoAleatoriamente = Math.floor(Math.random() * 100 + 1);
  botaoEnviarTentativa.style.display = "inline";
}

function vericaValor() {
  const valorTentado = parseFloat(inputTentativa.value);
  inputTentativa.value = "";

  if (listaDeTentativas.includes(valorTentado)) {
    alert("Você inseriou um valor inválido, não insira valores repetidos.");
    return;
  } else {
    listaDeTentativas.push(valorTentado);
  }

  if (isNaN(valorTentado)) {
    alert("Você inseriou um valor inválido, insira somente números.");
    return;
  }

  if (valorTentado < 1 || valorTentado > 100) {
    alert("Você inseriu um valor inválido, inseria valores entre 1 e 100.");
    return;
  }

  if (!Number.isInteger(valorTentado)) {
    alert("Você inseriu um valor inválido, inseria apenas valores inteiros.");
    return;
  }

  if (quantidadeDeTentativas >= 9) {
    console.log("estou dentro do if");
    bannerErro.innerHTML =
      "O jogo acabou, o valor correto era: " + valorGeradoAleatoriamente;
    inputTentativa.disabled = true;
    botaoEnviarTentativa.disabled = true;
    botaoResetarJogo.style.display = "inline";
    botaoEnviarTentativa.style.display = "none";

    return;
  }

  tentativasUsuario.innerHTML =
    tentativasUsuario.innerHTML + " " + valorTentado;

  if (valorTentado > valorGeradoAleatoriamente) {
    bannerErro.style.display = "block";
    bannerErro.innerHTML = TEXTO_ERRO_MAIOR;
  } else if (valorTentado < valorGeradoAleatoriamente) {
    bannerErro.style.display = "block";
    bannerErro.innerHTML = TEXTO_ERRO_MENOR;
  } else {
    bannerErro.style.display = "none";
    bannerSucesso.style.display = "block";
    botaoResetarJogo.style.display = "inline";
    inputTentativa.disabled = true;
    botaoEnviarTentativa.disabled = true;
    botaoEnviarTentativa.style.display = "none";
  }

  quantidadeDeTentativas = quantidadeDeTentativas + 1;
}

botaoEnviarTentativa.addEventListener("click", vericaValor);
botaoResetarJogo.addEventListener("click", resetarJogo);
