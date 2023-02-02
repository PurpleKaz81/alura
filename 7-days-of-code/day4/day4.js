const number = Math.floor(Math.random() * 10) + 1

function validateUserInput(input) {
  return !isNaN(Number(input)) && input >= 1 && input <= 10
}

function handleInput(number) {
  let attempts = 2
  let userInput = window.prompt(`Hi there! Guess a whole number between 1 and 10. Let's see if you're right. You have ${attempts + 1} tries.`)
  let inputInvalid = false

  while (attempts >= 0) {
    if (!validateUserInput(userInput)) {
      alert("Please type in any whole number between 1 and 10 using only numbers. No decimals or fractions, please.")
      inputInvalid = true
      userInput = window.prompt(`Hi there! Guess a whole number between 1 and 10. Let's see if you're right`)
    } else {
      userInput = Number(userInput)
      if (userInput === number) {
        alert(`That's right, The number ${userInput} is correct!`)
        break
      } else if (attempts === 0) {
        alert(`You're done, FINISHED! The answer was ${number}. Move to the mountains and disappear.`)
        break
      } else {
        alert(`WRONG! God have mercy on your soul. You have ${attempts} more attempts`)
        inputInvalid = false
        userInput = window.prompt(`Guess a whole number between 1 and 10. Let's see if you're right`)
      }
    }
    if (!inputInvalid) {
      attempts--
    }
  }
}

window.onload = () => {
  handleInput(number)
}
