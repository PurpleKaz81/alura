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
}

document.addEventListener("DOMContentLoaded", openingGif())

window.onload = () => {
  handleInput()
}
