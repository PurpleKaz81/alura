const { ENTER, ESC } = { ENTER: "Enter", ESC: "Escape" }
const eventTypes = ["click", "keydown"]
const producao = document.querySelector("#producao")

const subtrair = document.querySelector("#subtrair-braco")
const somar = document.querySelector("#somar-braco")
const braco = document.querySelector("#braco")

const sayHi = () => {
  const message = "Tell yo mama I'm home."
  alert(message)
}

const sayHi2 = () => {
  const message2 = "Whaaaaaat?!"
  alert(message2)
}

const changeButtonValue = () => {
  const smirk = "\uD83D\uDE0F"
  producao.classList.add("override")
  producao.value = `You touched me... ${smirk}`
    .toLowerCase()
    .replace(/^\w/, (s) => s.toUpperCase())
}

const handleAlertEvent = (event) => {
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

const manipulateCount = (operation) => {
  if (operation === subtrair) {
    braco.value = parseInt(braco.value) - 1
  } else {
    braco.value = parseInt(braco.value) + 1
  }
}

document.addEventListener("DOMContentLoaded", () => {
  eventTypes.forEach((type) => producao.addEventListener(type, handleAlertEvent))

  somar.addEventListener("click", (event) => {
    event.preventDefault()
    manipulateCount(somar)
  })

  subtrair.addEventListener("click", (event) => {
    event.preventDefault()
    manipulateCount(subtrair)
  })

  sayHi()
})
