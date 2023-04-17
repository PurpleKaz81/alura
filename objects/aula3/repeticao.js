const cliente = {
  nome: "Joao",
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

for (let chave in cliente) {
  let tipo = typeof cliente[chave]
  if (tipo !== "object" && tipo !== "function") {
    // console.log(`A chave ${chave} tem o valor ${cliente[chave]}`)
  }
}

const paciente = {
  nome: "James T.",
  idade:30,
  email: "jt@email.com",
  identicacao: "Alpha01259859",
  funcao:"comandante",
  peso:80.1,
  altura:1.80,
  calcularIMC:function(){
    return (this.peso/(Math.pow(this.altura,2)))
  },
  nomeCompleto:function(){
    console.log(this.nome)
  }
}

let output = ""
for (let info in paciente) {
  if (typeof paciente[info] === "object" || typeof paciente[info] === "function") {
    continue
  } else {
    output += `${info} ==> ${paciente[info]} `
  }
}

console.log(output)

const nome = paciente.nome
console.log(`${nome} tem IMC: ${paciente.calcularIMC().toFixed(3)}`)
