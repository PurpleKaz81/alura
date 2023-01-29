function openingGif() {
  const gif = document.createElement("img")
  gif.src = "ts-life.gif"
  let gifContainer = document.getElementById("gif-container")
  gifContainer.appendChild(gif)
}

function capitalizeName(name) {
  return name.replace(/\b(\w)/g, s => s.toUpperCase())
}

function validateName(name) {
  let regexp = XRegExp('^[\\p{L}\\p{M}\\s.\'’-]+$')
  if (XRegExp.test(name, regexp) && name != "" && name != null) {
    return true;
  }
  return false;
}

function validateAge(age) {
  if (age && age.match(/^(1[0-2]\d|[1-9]?\d|0)$/) && age != "" && age != null) {
    return true;
  }
  return false;
}

function handleInput() {
  let fullName = window.prompt("What's you full name, champ?")
  if (validateName(fullName)) {
    fullName = capitalizeName(fullName)
    alert(`Thanks, ${fullName}!`)
  } else {
    alert("Do us a solid and write in a valid name, letters and spaces only")
    return handleInput()
  }

  let age = window.prompt("And how old are you?")
  if (validateAge(age)) {
    alert(`So far so good, ${capitalizeName(fullName)}, ${age} years old.`)
  } else {
    alert("No need to lie 😝 Just jot down your real age")
    return handleInput()
  }

  let question1Answer = document.getElementById("question1-answer")
  let question1 = window.prompt("Would you like to study front-end or back-end? Pick one")
  question1Answer.innerHTML = question1

  let question2Container = document.querySelector(".question2-container")
  let question2Answer = document.querySelector("#question2-answer")
  let question2
  if (question1.toLowerCase() === "front-end") {
    question2 = window.prompt("Which framework would you prefer: React or Vue? Pick one")
  } else if (question1.toLowerCase() === "back-end") {
    question2 = window.prompt("Which language would you prefer: C++ or Java? Pick one")
  } else {
    alert("Please input a valid answer")
    return handleInput()
  }
  question2Answer.innerHTML = question2
}

document.addEventListener("DOMContentLoaded", openingGif())

window.onload = () => {
  handleInput()
}
