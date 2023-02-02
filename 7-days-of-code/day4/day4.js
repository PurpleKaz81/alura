const number = 5

// Math.floor(Math.random() * 10) + 1

function validateUserNumber(number) {
  return !isNaN(Number(number)) && number >= 1 && number <= 10
}

function handleInput(number) {
  let userNumber = window.prompt(`Hi there! Guess a whole number between 1 and 10. Let's see if you're right`)
  if (!validateUserNumber(userNumber)) {
    alert("Please type in any whole number between 1 and 10 using only numbers. No decimals or fractions, please.")
    return handleInput(number)
  }

  userNumber = Number(userNumber)
  for (let counter = 3; counter >= 0; counter--) {
    if (userNumber === number) {
      alert(`That's right, The number ${userNumber} is correct!`)
      break
    } else if (counter === 0) {
      alert(`You're done, FINISHED! The answer was ${number}. Move to the mountains and disappear.`)
    } else {
      alert(`WRONG! God have mercy on your soul. You have ${counter} more attempts`)
      let newUserNumber = window.prompt(`Hi there! Guess a whole number between 1 and 10. Let's see if you're right`)
      if (!validateUserNumber(newUserNumber)) {
        alert("Please type in any whole number between 1 and 10 using only numbers. No decimals or fractions, please.")
        return handleInput(number)
      }
      userNumber = Number(newUserNumber)
    }
  }
}

window.onload = () => {
  handleInput(number)
}
