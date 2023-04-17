const clientes = require("./clientes.json")

const filtrarApartamentosSemComplemento = (clientes) =>
  clientes.filter((cliente) => {
    return (
      cliente.endereco.apartamento &&
      !cliente.endereco.hasOwnProperty("complemento")
    )
  })

const filtrados = filtrarApartamentosSemComplemento(clientes)
console.log(filtrados)
