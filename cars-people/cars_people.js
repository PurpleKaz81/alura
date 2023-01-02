// Get a reference to the canvas element in the HTML
const canvas = document.querySelector("#my-canvas")
canvas.width = 500
canvas.height = 400

// create road image object
let roadImage = new Image()
roadImage.src = "images/road.png"

// draw image on canvas when it has finished loading
roadImage.onload = function() {
  // get 2D rendering context for canvas
  const ctx = canvas.getContext("2d")

  // calculate the aspect ratio of road image
  const aspectRatio = roadImage.naturalWidth / roadImage.naturalHeight

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
