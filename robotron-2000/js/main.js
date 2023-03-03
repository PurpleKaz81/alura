const { ENTER, ESC } = { ENTER: "Enter", ESC: "Escape" }
const eventTypes = ["click", "keydown"]

const [robotron, somarBraco, subtrairBraco, braco] = [
  "#producao",
  "#somar-braco",
  "#subtrair-braco",
  "#braco"
].map((id) => document.querySelector(id))

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
  robotron.classList.add("override")
  robotron.value = `You touched me... ${smirk}`
    .toLowerCase()
    .replace(/^\w/, (s) => s.toUpperCase())
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

somarBraco.addEventListener("click", (event) => {
  event.preventDefault()
  braco.value = parseInt(braco.value) + 1
})

subtrairBraco.addEventListener("click", (event) => {
  event.preventDefault()
  braco.value = parseInt(braco.value) - 1
})

document.addEventListener("DOMContentLoaded", sayHi)
