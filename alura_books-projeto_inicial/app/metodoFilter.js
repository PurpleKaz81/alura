const botoes = document.querySelectorAll(".btn")
botoes.forEach((btn) => btn.addEventListener("click", filtrarLivros))

function filtrarPorCategoria(categoria) {
  return livros.filter((livro) => livro.categoria == categoria)
}

function filtrarPorDisponibilidade() {
  return livros.filter((livro) => livro.quantidade > 0)
}

function exibirValorTotalDosLivrosDisponiveisNaTela(valorTotal) {
  elementoComValorTotalDeLivrosDisponiveis.innerHTML = `
  <div class="livros__disponiveis">
    <p>Todos os livros disponíveis por R$<span id="valor">${valorTotal}</span></p>
  </div>
  `
}

function filtrarLivros() {
  const elementoBtn = document.querySelector(`#${this.id}`)
  const categoria = elementoBtn.value
  let livrosFiltrados =
    categoria == "disponiveis"
      ? filtrarPorDisponibilidade()
      : filtrarPorCategoria(categoria)
  exibirLivrosNaTela(livrosFiltrados)

  if (categoria == "disponiveis") {
    const valorTotal = calcularValorTotalDeLivrosDisponiveis(livrosFiltrados)
    exibirValorTotalDosLivrosDisponiveisNaTela(valorTotal)
  }
}
