import User from "./User.js"

class Admin extends User {
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

const novoAdmin = new Admin("Rodrigo", "r@r.com", "2021-01-01")
const novoAdmin2 = new Admin("Alan", "a@a.com", "2021-01-01", "estudante")
console.log(novoAdmin.criarCurso("JS", "20"))
console.log(novoAdmin2)
console.log(novoAdmin2.criarCurso("Python", "20"))
