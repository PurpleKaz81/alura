import User from "./User.js"

export default class Docente extends User {
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
