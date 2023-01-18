function handleError(error) {
  console.error(`Error: ${error}`)
  alert(`Error playing the sound. Please check the audio file and try again.`)
}

fetch("audioIds.json")
  .then((response) => response.json())
  .then((data) => {
    const buttonList = document.querySelectorAll(".tecla")

    buttonList.forEach((button) => {
      const instrument = button.classList[1]
      let audioId = data[instrument]

      button.onclick = () => {
        try {
          let audioElement = document.querySelector(audioId)
          audioElement.play()
        } catch (error) {
          handleError(error)
        }
      }

      button.addEventListener("keydown", (e) => {
        if (e.code === "Space" || e.code === "Enter") {
          button.classList.add("ativa")
        }
      })

      button.addEventListener("keyup", () => {
        button.classList.remove("ativa")
      })
    })
  })
  .catch((error) => {
    handleError(error)
  })
