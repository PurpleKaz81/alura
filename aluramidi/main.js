function playPomSound() {
  document.querySelector("#som_tecla_pom").play()
}

function playClapSound() {
  document.querySelector("#som_tecla_clap").play()
}

document.querySelector(".tecla_pom").onclick = playPomSound
