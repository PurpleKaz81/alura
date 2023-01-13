function playPomSound() {
  document.querySelector("#som_tecla_pom").play()
}

const buttonList = document.querySelectorAll(".tecla")

let counter = 0

while (counter < 9) {
  buttonList[0].onclick = playPomSound
  counter += 1
  console.log(counter)
}
