const number = 5

function validateUserNumber(number) {
  return !isNaN(Number(number)) && number >= 1 && number <= 10
}

function handleInput(number) {
  let userNumber = window.prompt(`Hi there! Guess a whole number between 1 and 10. Let's see if you're right`)
  let counter = 3
  let inputInvalid = false

  while (counter >= 0) {
    if (!validateUserNumber(userNumber)) {
      alert("Please type in any whole number between 1 and 10 using only numbers. No decimals or fractions, please.")
      inputInvalid = true
      userNumber = window.prompt(`Hi there! Guess a whole number between 1 and 10. Let's see if you're right`)
    } else {
      userNumber = Number(userNumber)
      if (userNumber === number) {
        alert(`That's right, The number ${userNumber} is correct!`)
        break
      } else if (counter === 0) {
        alert(`You're done, FINISHED! The answer was ${number}. Move to the mountains and disappear.`)
        break
      } else {
        alert(`WRONG! God have mercy on your soul. You have ${counter} more attempts`)
        inputInvalid = false
        userNumber = window.prompt(`Hi there! Guess a whole number between 1 and 10. Let's see if you're right`)
      }
    }
    if (!inputInvalid) {
      counter--
    }
  }
}

window.onload = () => {
  handleInput(number)
}
