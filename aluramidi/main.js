function playSound(audioElementId) {
  document.querySelector(audioElementId).play()
}

const buttonList = document.querySelectorAll(".tecla")

let counter = 0

while (counter < buttonList.length) {
  buttonList[counter].onclick = function () {
    playSound("#som_tecla_tom")
  }
  counter += 1
  console.log(counter)
}
