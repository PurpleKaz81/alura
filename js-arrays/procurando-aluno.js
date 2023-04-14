const students = ["João", "Juliana", "Ana", "Caio"]
const averages = [10, 8, 7.5, 9]

const studentAndAverageList = [students, averages]

const randomizeName = () => {
  const randomIndex = Math.floor(Math.random() * students.length)
  return students[randomIndex]
}

const randomlySelectedStudent = randomizeName()

const showNameAndGrade = (student) => {
  if (studentAndAverageList[0].includes(student)) {
    const [students, averages] = studentAndAverageList

    const index = students.indexOf(student)

    const studentAverage = averages[index]

    console.log(`The student, ${student}, has an average of ${studentAverage}.`)
  } else {
    console.log(`Student not found. You're going to jail!`)
  }
}

showNameAndGrade(randomlySelectedStudent)

const pessoa = {
  nome: "Rafael",
  sobrenome: "Kasinski",
  telefone: 11947887667,
  signo: "gêmeos",
  idade: 41
}

const { nome, idade } = pessoa

const printData = ({ nome, idade, ...rest }) => {
  console.log(`${nome}: ${idade}`)
  console.log(rest.signo)
}

printData(pessoa)
