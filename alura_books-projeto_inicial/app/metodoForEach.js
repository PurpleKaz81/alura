const elementoParaInserirLivros = document.querySelector("#livros")
const elementoComValorTotalDeLivrosDisponiveis = document.querySelector("#valor_total_livros_disponiveis")

const exibirLivrosNaTela = (listaDeLivros) => {
  elementoComValorTotalDeLivrosDisponiveis.innerHTML = ""

  elementoParaInserirLivros.innerHTML = ""
  listaDeLivros.forEach((livro) => {
    let disponibilidade =
      livro.quantidade > 0 ? "livro_imagens" : "livro_imagens indisponivel"

    elementoParaInserirLivros.innerHTML += `
    <div class="livro">
      <img class="${disponibilidade}" src="${livro.imagem}" alt="${
      livro.alt
    }" />
      <h2 class="livro__titulo">
        ${livro.titulo}
      </h2>
      <p class="livro__descricao">${livro.autor}</p>
      <p class="livro__preco" id="preco">R$${livro.preco.toFixed(2)}</p>
      <div class="tags">
        <span class="tag">${livro.categoria}</span>
      </div>
    </div>
    `
  })
}
