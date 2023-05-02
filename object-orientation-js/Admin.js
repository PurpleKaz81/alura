import User from "./User.js"

export default class Admin extends User {
  constructor(nome, email, nascimento, role = "admin", ativo = true) {
    super(nome, email, nascimento, role, ativo)
  }

  isAdmin() {
    return this.role === "admin"
  }

  criarCurso(nomeDoCurso, vagas) {
    return this.isAdmin()
      ? `Curso de ${nomeDoCurso} criado com ${vagas} vagas.`
      : "Acesso negado. Jogue dum penhasco"
  }
}
