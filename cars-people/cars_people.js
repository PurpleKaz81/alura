// Get a reference to the canvas element in the HTML
const canvas = document.querySelector("#my-canvas")
canvas.width = 1400
canvas.height = 1200

// create image objects
let roadImage = new Image()
roadImage.src = "images/road.png"
let playerImage = new Image()
playerImage.src = "images/player-1.png"
let roadImage = new Image()
car1Image.src = "images/car-1.png"
let roadImage = new Image()
car2Image.src = "images/car-2.png"
let roadImage = new Image()
car3Image.src = "images/car-3.png"

// draw image on canvas when it has finished loading
roadImage.onload = function() {
  // get 2D rendering context for canvas
  const ctx = canvas.getContext("2d")

  // calculate images' aspect ratios
  const aspectRatio = roadImage.naturalWidth / roadImage.naturalHeight
  const aspectRatio = playerImage.naturalWidth / playerImage.naturalHeight

  // Calculate the width and height of the image to fit the canvas while maintaining the aspect ratio
  let width = canvas.width
  let height = canvas.height
  if (width / height > aspectRatio) {
    width = height * aspectRatio
  } else {
    height = width /aspectRatio
  }

  // draw road image on canvas
  ctx.drawImage(roadImage, 0, 0, width, height)
}
