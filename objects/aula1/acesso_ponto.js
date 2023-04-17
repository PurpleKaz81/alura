const cliente = {
  nome: "André",
  idade: 32,
  cpf: "11122233356",
  email: "andre@dominio.com",
}

const { nome, idade, ...rest } = cliente

console.log(`O nome de cliente é ${nome}, cujo CPF é ${cliente.cpf.substring(0, 3)}.***.***-**.`)
