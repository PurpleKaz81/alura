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

const changeButtonValue = () => {
  const smirk = "\uD83D\uDE0F"
  robotron.classList.add("override")
  robotron.value = `You touched me... ${smirk}`.toLowerCase().replace(/^\w/, s => s.toUpperCase())
}

const handleEvent = (event) => {
  switch (event.type) {
    case "click":
      event.preventDefault()
      changeButtonValue()
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
