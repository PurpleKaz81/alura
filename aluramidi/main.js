function playSound(audioElement) {
  const element = document.querySelector(audioElement)

  if (element && element.localName === "audio") {
    element.play()
  } else {
    alert("Element not found, or invalid selector")
  }
}


fetch("audioIds.json")
.then(response => response.json())
.then(data => {
  const buttonList = document.querySelectorAll(".tecla")

  for (let counter = 0; counter < buttonList.length; counter++) {
    const button = buttonList[counter]
    const instrument = button.classList[1]
    let audioId = data[instrument]

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
})
.catch(error => console.error(error))
