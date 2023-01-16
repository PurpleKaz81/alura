function playSound(audioElementId) {
  document.querySelector(audioElementId).play()
}

const buttonList = document.querySelectorAll(".tecla")

for (let counter= 0; counter < buttonList.length; counter++) {
  const button = buttonList[counter]
  const instrument = button.classList[1]
  const audioId = `#som_${instrument}`

  button.onclick = function () {
    playSound(audioId)
  }

  button.onkeydown = function () {
    button.classList.add("ativa")
  }

  button.onkeyup = function () {
    button.classList.remove("ativa")
  }
}
