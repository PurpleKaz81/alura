const { ENTER, ESC } = { ENTER: "Enter", ESC: "Escape" }
const eventTypes = ["click", "keydown"]
const producao = document.querySelector("#producao")

const control = document.querySelectorAll("[data-control]")
const parts = {
  bracos: {
    forca: 29,
    poder: 35,
    energia: -21,
    velocidade: -5
  },

  blindagem: {
    forca: 41,
    poder: 20,
    energia: 0,
    velocidade: -20
  },
  nucleos: {
    forca: 0,
    poder: 7,
    energia: 48,
    velocidade: -24
  },
  pernas: {
    forca: 27,
    poder: 21,
    energia: -32,
    velocidade: 42
  },
  foguetes: {
    forca: 0,
    poder: 28,
    energia: 0,
    velocidade: -2
  }
}

// const sayHi = () => {
//   const message = "Tell yo mama I'm home."
//   alert(message)
// }

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
  const part = control.querySelector("[data-counter]")

  if (operation === "-") {
    part.value = parseInt(part.value) - 1
  } else {
    part.value = parseInt(part.value) + 1
  }
}

control.forEach((element) => {
  element.addEventListener("click", (event) => {
    event.preventDefault()
    manipulateCount(event.target.dataset.control, event.target.parentNode)
  })
})

// sayHi()
