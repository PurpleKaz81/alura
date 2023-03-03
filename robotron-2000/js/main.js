document.addEventListener("DOMContentLoaded", () => {
  const { ENTER, ESC } = { ENTER: "Enter", ESC: "Escape" }
  const eventTypes = ["click", "keydown"]
  const producao = document.querySelector("#producao")
  const countButtons = document.querySelectorAll(".controle-ajuste")

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

  eventTypes.forEach((type) => producao.addEventListener(type, handleEvent))

  countButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault()
      const braco = document.querySelector("#braco")
      const increment = button.id === "somar" ? 1 : 1
      braco.value = parseInt(braco.value) + increment
    })
  })
  sayHi()
})
