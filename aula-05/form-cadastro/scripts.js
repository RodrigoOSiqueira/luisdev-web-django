const faqItens = $(".faq-item");

// Definições do nome de usuário
const inputNomeUsuario = $("#nome-usuario");
const erroMessageUsuario = $("#erro-nome-usuario");

// Definições do email
const blocoEmail = $("#bloco-email");
const inputEmail = $("#email");
const erroEmail = $("#erro-email");

// Definições senha
const blocoSenha = $("#bloco-senha");
const inputSenha = $("#senha");
const erroSenha = $("#erro-senha");

// Definições confirma senha
const blocoConfirmasenha = $("#bloco-confirma-senha");
const inputConfirmaSenha = $("#confirma-senha");
const erroConfirmaSenha = $("#erro-confirma-senha");

// Definições botão
const blocoBotao = $("#bloco-botao");

const ENTER_CODE = "Enter"; // Verificar se estou escrevendo as constantes de valor constante da forma correta

console.log(blocoBotao);

faqItens.on("click", function () {
  const itemClicado = $(this);
  const resposta = itemClicado.children("[faq-item-texto]");
  resposta.slideToggle(500);
});

function validaNomeUsuario(nomeUsuario, input) {
  if (nomeUsuario.length <= 10) {
    erroMessageUsuario.show(200);
  } else {
    erroMessageUsuario.hide(200);
    blocoEmail.slideDown();
    input.blur();
    // blocoEmail.focus(); Entender porque isso não funciona
  }
}

function validaEmail(email, input) {
  if (email.includes("@") && email.includes(".com")) {
    // Email válido
    erroEmail.hide(200);
    blocoSenha.slideDown();
    input.blur();
  } else {
    // Email inválido
    erroEmail.show(200);
  }
}

function validaSenha(senha, input) {
  if (senha.length <= 10) {
    // Senha inválida
    erroSenha.show(200);
  } else {
    // Senha válida
    erroSenha.hide(200);
    input.blur();
    blocoConfirmasenha.slideDown();
  }
}

function validaConfirmaSenha(confirmacaoSenha, input) {
  if (confirmacaoSenha === inputSenha.val()) {
    // Confirmação de senha válida
    erroConfirmaSenha.hide(200);
    blocoBotao.slideDown();
  } else {
    // Confirmação de senha inválida
    erroConfirmaSenha.show(200);
  }
}

inputNomeUsuario.on("keyup change", function (event) {
  const valorInput = $(event.target).val();

  if (event.code == ENTER_CODE) {
    validaNomeUsuario(valorInput, $(this));
  }
});

inputEmail.on("keyup change", function (event) {
  const valorInput = $(event.target).val();

  if (event.code == ENTER_CODE) {
    validaEmail(valorInput, $(this));
  }
});

inputSenha.on("keyup change", function (event) {
  const valorInput = $(event.target).val();

  if (event.code == ENTER_CODE) {
    validaSenha(valorInput, $(this));
  }
});

inputConfirmaSenha.on("keyup change", function (event) {
  const valorInput = $(event.target).val();

  if (event.code == ENTER_CODE) {
    validaConfirmaSenha(valorInput, $(this));
  }
});
