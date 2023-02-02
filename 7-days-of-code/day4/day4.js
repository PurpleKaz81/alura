const number = Math.floor(Math.random() * 10) + 1

function validateUserNumber(number) {
  return !isNaN(Number(number)) && number <= 1 && number >= 10
}

function handleInput(number) {
  let userNumber
  if (!validateUserNumber(userNumber)) {
    userNumber = window.prompt(`Hi there! Choose a number between 1 and 10. Integers only`)
    if (!validateUserNumber(userNumber)) {
      alert("Please type in any whole number between 1 and 10 using only numbers. No decimals or fractions, please.")
      return handleInput()
    }
    alert(`Okay, then. ${userNumber} it is!`)
  }
}

window.onload = () => {
  handleInput()
}
