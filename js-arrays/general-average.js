const salaJS = [7, 8, 8, 7, 10, 6.5, 4, 10, 7]
const salaJava = [6, 5, 8, 9, 5, 6]
const salaPython = [7, 3.5, 8, 9.5]

const calculateAverage = (classGrades) => {
  const sum = classGrades.reduce((acc, grade) => {
    return acc + grade
  }, 0)

  const classAverage = sum / classGrades.length
  return classAverage
}

console.log(`The average for the JS class is ${calculateAverage(salaJS)}`)
console.log(`The average for the Java class is ${calculateAverage(salaJava)}`)
console.log(`The average for the Python class is ${calculateAverage(salaPython)}`)
