fetch("audioIds.json")
.then(response => response.json())
.then(data => {
  const buttonList = document.querySelectorAll(".tecla")

  for (let counter = 0; counter < buttonList.length; counter++) {
    const button = buttonList[counter]
    const instrument = button.classList[1]
    let audioId = data[instrument]

    button.onclick = function () {
      try {
        let audioElement = document.querySelector(audioId)
        audioElement.play()
      } catch (e) {
        console.error(`Error: ${e}`)
      }
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
.catch(error => {
  console.error(`An error has occurred: ${error}`)
})
