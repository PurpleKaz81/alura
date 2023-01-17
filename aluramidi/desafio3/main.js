const buttonList = document.querySelectorAll('input[type=button]')
const telInput = document.querySelector('input[type=tel]')
telInput.tabIndex = -1
telInput.focus()

function setupButtonEventListeners(button) {
  button.addEventListener("mousedown", () => button.classList.add("ativa"))
  button.addEventListener("mouseup", () => button.classList.remove("ativa"))
  button.addEventListener("keydown", e => {
    if (e.key === " " || e.key === "Enter") button.classList.add("ativa")
  })
  button.addEventListener("keyup", () => button.classList.remove("ativa"))
  button.addEventListener("click", () => telInput.value += button.value)
}

for (let index = 0; index < buttonList.length; index++) {
  const button = buttonList[index]
  button.tabIndex = index + 1
  setupButtonEventListeners(button)
}

const firstButton = buttonList[0]
firstButton.addEventListener("keydown", e => {
  if (e.key === "Tab" && e.shiftKey) {
    e.preventDefault()
    telInput.focus()
  }
})

telInput.addEventListener("keydown", e => {
  if (e.key === " " || e.key === "Enter") telInput.classList.add("ativa")
});

telInput.addEventListener("keyup", () => telInput.classList.remove("ativa"))
