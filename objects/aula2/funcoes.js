const cliente = {
  nome: "João",
  idade: 24,
  email: "joao@firma.com",
  telefone: ["1155555550", "1144444440"],
  saldo: 200,
  efetuaPagamento: function (valor) {
    if (valor > this.saldo) {
      console.log("Saldo insuficiente.")
    } else {
      this.saldo -= valor
      console.log(`Pagamento realizado! Novo saldo: ${this.saldo}.`)
    }
  }
}

cliente.efetuaPagamento(250)
cliente.efetuaPagamento(25)

const cliente2 = Object.create(cliente)
cliente2.idade = 40

console.log(cliente.idade)
console.log(cliente2.idade)
