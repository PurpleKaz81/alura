function playSound(audioElementId) {
  document.querySelector(audioElementId).play()
}

const buttonList = document.querySelectorAll(".tecla")

let counter = 0

while (counter < buttonList.length) {
  const button = buttonList[counter]
  const instrument = button.classList[1]

  const audioId = `#som_${instrument}`

  // console.log(audioId)

  button.onclick = function () {
    playSound(audioId)
  }
  counter += 1
  // console.log(counter)
}
