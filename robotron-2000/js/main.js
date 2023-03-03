const { ENTER, ESC } = { ENTER: "Enter", ESC: "Escape" }

const sayHi = () => {
  const message = "Hi, bitch! Tell yo mama I'm home."
  console.log(message)
  alert(message)
}

const sayHi2 = () => {
  const message2 = "Whaaaaaat?!"
  console.log(message2)
  alert(message2)
}

const robotron = document.querySelector("#producao")

const handleEvent = (event) => {
  if (event.type === "click") {
    event.preventDefault()
    sayHi2()
  } else if (event.type === "keydown") {
    if (event.key === ENTER || event.key === ESC) {
      alert.close()
    }
  }
}

const eventTypes = ["click", "keydown"]

eventTypes.forEach((type) => robotron.addEventListener(type, handleEvent))

document.addEventListener("DOMContentLoaded", sayHi)
