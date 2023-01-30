function openingGif() {
  const gif = document.createElement("img")
  gif.src = "ts-life.gif"
  let gifContainer = document.getElementById("gif-container")
  gifContainer.appendChild(gif)
}

function capitalizeName(name) {
  return name.replace(/\b(\w)/g, (s) => s.toUpperCase())
}

function validateName(name) {
  let regexp = XRegExp("^[\\p{L}\\p{M}\\s.'’-]+$")
  if (XRegExp.test(name, regexp) && name != "" && name != null) {
    return true
  }
  return false
}

function validateAge(age) {
  if (age && age.match(/^(1[0-2]\d|[1-9]?\d|0)$/) && age != "" && age != null) {
    return true
  }
  return false
}

let question1Modal = document.getElementById("question1-modal")
question1Modal.style.display = "none"


function handleInput() {
  let fullName = window.prompt("What's you full name, champ?")
  if (validateName(fullName)) {
    fullName = capitalizeName(fullName)
    let firstName = fullName.split(" ")[0]
    alert(`Thanks, ${firstName}!`)
  } else {
    alert("Do us a solid and write in a valid name, letters and spaces only")
    return handleInput()
  }

  let age
  while (!validateAge(age)) {
    age = window.prompt("And how old are you?")
    if (!validateAge(age)) {
      alert(
        "No need to lie 😝 Just type in your age, anywhere between 0 and 130 with no decimals"
      )
    }
  }
  alert(`So far so good, ${capitalizeName(fullName)}, ${age} years old.`)

  let question1Modal = document.getElementById("question1-modal")
  question1Modal.style.display = "block"

  const frontEndButton = document.getElementById("front-end-button")
  const backEndButton = document.getElementById("back-end-button")
  const question1Answer = document.getElementById("question1-answer")

  frontEndButton.addEventListener("click", () => {
    return new Promise(resolve => {
      question1Answer.textContent = `Great, ${fullName}, you've chosen front-end!`
      question1Modal.style.display = "none"
      resolve()
    })
  })

  backEndButton.addEventListener("click", () => {
    return new Promise((resolve) => {
      question1Answer.textContent = `Great, ${fullName}, you've chosen back-end!`
      question1Modal.style.display = "none"
      resolve()
    })
  })
}

document.addEventListener("DOMContentLoaded", openingGif)

window.onload = () => {
  handleInput()
}
