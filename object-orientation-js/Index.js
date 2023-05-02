import Admin from "./Admin.js"
import Docente from "./Docente.js"
import User from "./User.js"

const novoDocente = new Docente("Guilherme", "g@g.com", "2021-01-01")
const novoAdmin = new Admin("Rafael", "r@k.com", "2021-01-01")
console.log(novoDocente.exibirInfos())
console.log(novoAdmin.exibirInfos())
