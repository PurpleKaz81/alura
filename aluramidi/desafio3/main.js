const buttonList = document.querySelectorAll('input[type=button]')
const telInput = document.querySelector('input[type=tel]')
telInput.tabIndex = -1
telInput.focus()

for (index = 0; index < buttonList.length; index++) {
  const button = buttonList[index];
  button.tabIndex = index + 1

  button.addEventListener("mousedown", function() {
    button.classList.add("ativa")
  })
  button.addEventListener("mouseup", function() {
    button.classList.remove("ativa")
  })
  button.addEventListener("keydown", function(e) {
    if (e.key === " " || e.key === "Enter")
    button.classList.add("ativa")
  })
  button.addEventListener("keyup", function() {
    button.classList.remove("ativa")
  })
  button.addEventListener("click", function() {
    telInput.value += button.value
  })
}

const firstButton = buttonList[0]
firstButton.addEventListener("keydown", function(e) {
  if (e.key === "Tab" && e.shiftKey) {
    e.preventDefault()
    telInput.focus()
  }
})

telInput.addEventListener("keydown", function(e) {
  if (e.key === " " || e.key === "Enter")
  telInput.classList.add("ativa")
});

telInput.addEventListener("keyup", function() {
  telInput.classList.remove("ativa")
});
