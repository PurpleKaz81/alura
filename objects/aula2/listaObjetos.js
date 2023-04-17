const cliente = {
  nome: "João",
  idade: 24,
  email: "joao@firma.com",
  telefone: ["1155555550", "1144444440"],
}

cliente.enderecos = [
  {
    rua: "R. Joseph Climber",
    numero: 1337,
    apartamento: true,
    complemento: "ap 934",
  },
]

cliente.enderecos.push(
  {
    rua: "R. Joseph Ladder",
    numero: 404,
    apartamento: false,
  }
)

const listaApenasApartamentos = cliente.enderecos.filter(
  (endereco) => endereco.apartamento === true
)

const listaNumeroPar = cliente.enderecos.filter(
  (endereco) => endereco.numero % 2 === 0
)

console.log(listaApenasApartamentos)
console.log(JSON.stringify(listaNumeroPar, null, 2))
