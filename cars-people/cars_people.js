// Get a reference to the canvas element in the HTML
const canvas = document.querySelector("#my-canvas")
canvas.width = 500
canvas.height = 400

// create an image object
let roadImage = new Image()
roadImage.src = "images/road.png"
roadImage.onload = function() {
  const ctx = canvas.getContext("2d")
  ctx.drawImage(roadImage, 10, 10)
}
