const createNewLine = (nome, email) => {
  const newClientLine = document.createElement("tr")
  const content = `
    <td class="td" data-td>${nome}</td>
    <td>${email}</td>
    <td>
      <ul class="tabela__botoes-controle">
        <li><a href="../telas/edita_cliente.html" class="botao-simples botao-simples--editar">Editar</a></li>
        <li><button class="botao-simples botao-simples--excluir" type="button">Excluir</button></li>
      </ul>
    </td>
    `

  newClientLine.innerHTML = content
  return newClientLine
}

const table = document.querySelector("[data-tabela]")

const http = new XMLHttpRequest()

http.open("GET", "http://localhost:3000/profile")

http.send()

http.onload = () => {
  const data = JSON.parse(http.response)
  data.forEach((element) => {
  table.appendChild(createNewLine(element.nome, element.email))
  })

  const http2 = new XMLHttpRequest()
  http2.open("GET", "http://localhost:3000/profile/semanaPassada")

  http2.onload = () => {
    const data2 = JSON.parse(http2.response)
    data2.forEach((element) => {
      table.appendChild(createNewLine(element.nome, element.email))
    })

    const http3 = new XMLHttpRequest()
    http3.open("GET", "http://localhost:3000/profile/semanaRetrasada")

    http3.onload() = () => {
      const data3 = JSON.parse(http3.response)
      data3.forEach((element) => {
        table.appendChild(createNewLine(element.nome, element.email))
      })
    }

    http3.send()
  }

  http2.send()
}
