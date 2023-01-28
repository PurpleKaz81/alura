function openingGif() {
  const gif = document.createElement("img")
  gif.src = "ts-life.gif"
  let gifContainer = document.getElementById("gif-container")
  gifContainer.appendChild(gif)
}

function capitalizeName(name) {
  return name.replace(/\b(\w)/g, s => s.toUpperCase())
}

function handleInput() {
  let fullName = window.prompt("What's you full name, champ?")
  let regexp = XRegExp('^[\\p{L}\\p{M}\\s.\'’-]+$')
  if (XRegExp.test(fullName, regexp) && fullName != "" && fullName != null) {
    fullName = capitalizeName(fullName)
    alert(`Thanks, ${fullName}!`)
  } else {
    alert("Do us a solid and write in a valid name, letters and spaces only")
    return handleInput()
  }

  let age = window.prompt("And how old are you?")
  if (age && age.match(/^(1[0-2]\d|[1-9]?\d|0)$/) && age != "" && age != null) {
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
