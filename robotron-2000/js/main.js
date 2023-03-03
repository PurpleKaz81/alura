const { ENTER, ESC } = { ENTER: "Enter", ESC: "Escape" }
const eventTypes = ["click", "keydown"]
const robotron = document.querySelector("#producao")

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

const handleEvent = (event) => {
  switch (event.type) {
    case "click":
      event.preventDefault()
      sayHi2()
      break
    case "keydown":
      if (event.key === ENTER || event.key === ESC) {
        alert.close()
      }
      break
  }
}

eventTypes.forEach((type) => robotron.addEventListener(type, handleEvent))

document.addEventListener("DOMContentLoaded", sayHi)
