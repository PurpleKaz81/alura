const user = {
  nome: "Juliana",
  email: "j@j.com",
  nascimento: "2021/01/01",
  role: "admin",
  ativo: true,
  exibirInfos() {
    console.log(`${this.nome}, ${this.email}`)
  },
}

const exibir = function () {
  console.log(this.nome)
}

const exibirNome = exibir.bind(user)

exibirNome()
exibir()

const admin = {
  nome: "Rafael",
  email: "rafa@kasa.com",
  role: "admin",
  criarCurso() {
    console.log("Criando curso...")
  }
}

const exibir2 = function () {
  console.log(this.nome)
}

const exibirNome2 = exibir2.bind(admin)

exibirNome2()

Object.setPrototypeOf(admin, user)
admin.criarCurso()
admin.exibirInfos()

console.log(admin.__proto__.__proto__.__proto__)
console.log(Object.prototype)
console.log(Array.prototype)
console.log(String.prototype)

// line separating code in console, "------"
console.log("-".repeat(30))
console.log("Using the call() method")
// console.log the telefone emoji 30 times
console.log("\n")

function user2(nome, email) {
  this.nome = nome
  this.email = email

  this.exibeInfos = function () {
    const phrase = `${this.nome} tem o email ${this.email}`
    console.log(phrase)
  }
}

const newUser = new user2("Juliana", "m@m.com")

const outroUser = {
  nome: "Rodrigo",
  email: "r@gmail.com",
}

newUser.exibeInfos()
newUser.exibeInfos.call(outroUser)

const outroUser2 = {
  nome: "Fulano",
  email: "fualno@detal.com",
}

newUser.exibeInfos.call(outroUser2)

// repeat line 22
console.log("-".repeat(30))
console.log("Using the call() method again")
// console.log the telefone emoji 30 times
console.log("\n")

function exibeMensagem(nome, email) {
  console.log(`Usuário: ${nome} — email: ${email}`)
}

const user3 = {
  nome: "Rafaelson",
  email: "rafael@son.com",
  executaFuncao(fn) {
    fn.call(user, this.nome, this.email)
  },
}

user3.executaFuncao(exibeMensagem)

// repeat line 22
console.log("-".repeat(30))
console.log("Using the apply method")
// console.log the telefone emoji 30 times
console.log("\n")

function exibeMensagem2(nome, email) {
  console.log(`Usuária: \n${nome} — email: ${email}\n\u{1F614}`)
}

const user4 = {
  nome: "Meu Coração",
  email: "meucoracao@doidemais.baby",
  executaFuncao(fn) {
    fn.apply(user, [this.nome, this.email])
  },
}

user4.executaFuncao(exibeMensagem2)

// repeat line 22
console.log("-".repeat(30))
console.log("Trying out protoype")

function User() {}
User.prototype.profile = "student"
let student = new User()

console.log(student.profile)

student.__proto__
student.prototype
User.prototype
