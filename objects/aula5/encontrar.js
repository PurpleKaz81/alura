const clientes = require("./clientes.json")

// console.log(clientes)

const encontrar = (lista, chave, valor) => lista.find((item) => item[chave].includes(valor))

const encontrado = encontrar(clientes, "nome", "Kirby")
console.log(encontrado)

const encontrado2 = encontrar(clientes, "telefone", "1918820860")
console.log(encontrado2)
