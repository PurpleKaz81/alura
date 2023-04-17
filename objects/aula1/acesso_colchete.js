const cliente = {
  nome: "André",
  idade: 32,
  cpf: "11122233356",
  email: "andre@dominio.com",
}

const { nome, idade, ...rest } = cliente

console.log(`O cliente é ${cliente["nome"]}, cujo CPF é ${cliente["cpf"].substring(0, 3)}.***.***-**.`)

const chaves = ["nome", "idade", "cpf", "email"]

chaves.forEach((chave => {
  console.log(`A chave ${chave} tem valor ${cliente[chave]}`)
}))
