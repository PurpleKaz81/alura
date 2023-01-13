function playPomSound() {
  document.querySelector("#som_tecla_pom").play()
}

const buttonList = document.querySelectorAll(".tecla")

let counter = 0

while (counter < buttonList.length) {
  buttonList[counter].onclick = playPomSound
  counter += 1
  console.log(counter)
}
