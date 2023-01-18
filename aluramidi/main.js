function playSound(audioElement) {
  const element = document.querySelector(audioElement)

  if (element && element.localName === "audio") {
    element.play()
  } else {
    alert("Element not found, or invalid selector")
  }
}

const buttonList = document.querySelectorAll(".tecla")

for (let counter = 0; counter < buttonList.length; counter++) {
  const button = buttonList[counter]
  const instrument = button.classList[1]
  const audioIds = {
    "tecla_pom": "#som_tecla_pom",
    "tecla_clap": "#som_tecla_clap",
    "tecla_tim": "#som_tecla_tim",
    "tecla_puff": "#som_tecla_puff",
    "tecla_splash": "#som_tecla_splash",
    "tecla_toim": "#som_tecla_toim",
    "tecla_psh": "#som_tecla_psh",
    "tecla_tic": "#som_tecla_tic",
    "tecla_tom": "#som_tecla_tom"
  }

  let audioId = audioIds[instrument]

  button.onclick = function () {
    playSound(audioId)
  }

  button.onkeydown = function (e) {
    if (e.code === "Space" || e.code === "Enter") {
      button.classList.add("ativa")
    }
  }

  button.onkeyup = function () {
    button.classList.remove("ativa")
  }
}
