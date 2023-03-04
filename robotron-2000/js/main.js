const { ENTER, ESC } = { ENTER: "Enter", ESC: "Escape" }
const eventTypes = ["click", "keydown"]
const producao = document.querySelector("#producao")

const control = document.querySelectorAll(".controle-ajuste")

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

eventTypes.forEach((type) => producao?.addEventListener(type, handleAlertEvent))

const manipulateCount = (operation, control) => {
  const part = control.querySelector(".controle-contador")

  if (operation === "-") {
    part.value = parseInt(part.value) - 1
  } else {
    part.value = parseInt(part.value) + 1
  }
}

control.forEach((element) => {
  element.addEventListener("click", (event) => {
    event.preventDefault()
    manipulateCount(event.target.textContent, event.target.parentNode)
  })
})

sayHi()
