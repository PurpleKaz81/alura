const grades = [7, 7, 8, 9]
const newGrades = [4, ...grades, 10]

const gradeList = newGrades.join(", ")
const oxfordComma = ", and"

console.log(`The new grades are ${gradeList.replace(/,([^,]*)$/, oxfordComma + "$1")}`)
console.log(`The original grades are ${grades}.`)
