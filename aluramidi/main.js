function playPomSound() {
  document.querySelector("#som_tecla_pom").play()
}

const buttonList = document.querySelectorAll(".tecla")

buttonList[0].onclick = playPomSound
