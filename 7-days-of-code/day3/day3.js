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
  if (fullName.match(/^[a-zA-Z-'\s]+$/) && fullName != "") {
    alert(`Thanks, ${capitalizeName(fullName)}!`)
  } else {
    alert("Do us a solid and write in a valid name, letters and spaces only")
  }
}

openingGif()
handleInput()
