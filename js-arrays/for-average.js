const grades = [10, 6.5, 8, 6.5]

let sum = 0
for (let i = 0; i < grades.length; i++)  {
  sum += grades[i]
}

const average1 = sum / grades.length

// console.log(`Your average is ${average1}`)

const grades1 = [10, 6.5, 8, 6.5]
const grades2 = [10, 6.5, 8, 7, 9]
const grades3 = [6.5, 8, 9, 10]

const allGrades = [grades1, grades2, grades3]

let average2 = 0

for (let i = 0; i < allGrades.length; i++) {
  for (let j = 0; j < allGrades[i].length; j++) {
    average2 += allGrades[i][j]/allGrades[i].length
  }
}

average2 = average2 / allGrades.length

// console.log(`Your average is ${average2.toFixed(3)}`)

const gradesArray = [
  [10, 6.5, 8, 6.5],
  [10, 6.5, 8, 7, 9],
  [6.5, 8, 9, 10],
]

const allGrades2 = gradesArray.flat()

const sum2 = allGrades2.reduce((acc, grade) => acc + grade, 0)

const average3 = sum2 / allGrades2.length

console.log(`Your average is ${average3.toFixed(3)}`)
