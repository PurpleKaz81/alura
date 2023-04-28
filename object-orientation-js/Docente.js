import User from "./User.js"

class Docente extends User {
  constructor(nome, email, nascimento, role = "docente", ativo = true) {
    super(nome, email, nascimento, role, ativo)
  }

  isDocente() {
    return this.role === "docente"
  }

  aprovaEstudante(estudante, curso) {
    if (curso === "Língua da Chacota") {
      return `Não trabalhamos com o curso de ${curso}, man.`
    }

    return this.isDocente()
      ? `Estudante ${estudante} aprovado no curso de ${curso}.`
      : `Rápido! Leve ${this.nome} aos leões, é impostor!`
  }
}

const novoDocente = new Docente("Mariana", "m@m.com", "2021-01-01")
console.log(novoDocente)
console.log(novoDocente.exibirInfos())
console.log(novoDocente.aprovaEstudante("Juliana", "Ruby"))

const novoDocente2 = new Docente("Thiago", "t@t.com", "2000-09-09", "aluno")
console.log(novoDocente2)
console.log(novoDocente2.exibirInfos())
console.log(novoDocente2.aprovaEstudante("Juliana", "Ruby"))

const novoDocente3 = new Docente("Monja", "monga@cohen.com", "893-08-18")
console.log(novoDocente3)
console.log(novoDocente3.exibirInfos())
console.log(novoDocente3.aprovaEstudante("Claudia", "Scala"))

const novoDocente4 = new Docente("Mano", "mano@brown", "1974-05-05")
console.log(novoDocente4)
console.log(novoDocente4.exibirInfos())
console.log(novoDocente4.aprovaEstudante("Fulano", "Língua da Chacota"))
