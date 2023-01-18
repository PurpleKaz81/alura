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
  let audioId = ""

  switch (instrument) {
    case "tecla_pom":
      audioId = "#som_tecla_pom"
      break
    case "tecla_clap":
      audioId = "#som_tecla_clap"
      break
    case "tecla_tim":
      audioId = "#som_tecla_tim"
      break
    case "tecla_puff":
      audioId = "#som_tecla_puff"
      break
    case "tecla_splash":
      audioId = "#som_tecla_splash"
      break
    case "tecla_toim":
      audioId = "#som_tecla_toim"
      break
    case "tecla_psh":
      audioId = "#som_tecla_psh"
      break
    case "tecla_tic":
      audioId = "#som_tecla_tic"
      break
    case "tecla_tom":
      audioId = "#som_tecla_tom"
      break
    default:
      console.error("Invalid classname")
  }

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
