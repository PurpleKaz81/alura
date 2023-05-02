import Admin from "./Admin.js"
import Docente from "./Docente.js"
import User from "./User.js"

const novoUser = new User("João", "Silva", "j@s.com", "01/01/2000")
console.log(novoUser.nome)
console.log(novoUser.sobrenome)
novoUser.nome = "Rafael Kasinski Pereira"
console.log(novoUser.nome)
console.log(novoUser.sobrenome)
novoUser.nomeCompleto = `${novoUser.nome} ${novoUser.sobrenome}`
console.log(novoUser.nomeCompleto)
