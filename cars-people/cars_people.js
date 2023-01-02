// Get a reference to the canvas element in the HTML
const canvas = document.querySelector("#my-canvas")
canvas.width = 500
canvas.height = 400

// set canvas background image
canvas.style.backgroundImage = 'url("images/road.png")'

// create image objects array
let images = [
  new Image(),
  new Image(),
  new Image(),
  new Image()
]

// Source of each image
images[0].src = "images/player-1.png"
images[1].src = "images/car-1.png"
images[2].src = "images/car-2.png"
images[3].src = "images/car-3.png"

// draw images on canvas when they have finished loading
images.forEach ((image, index) => {
  image.onload = function() {
    // Get 2D rendering context for canvas
    const ctx = canvas.getContext('2d')

    // calculate aspect ratio for images
    const aspectRatio = image.naturalWidth / image.naturalHeight

    // calculate the width and height of image to fit canvas while maintaining aspect ratio
    let width = canvas.width / images.length
    let height = canvas.height
    if (width / height > aspectRatio) {
      width = height * aspectRatio
    } else {
    height = width / aspectRatio
    }

  // draw image on canvas
  ctx.drawImage(image, index * width, 0, width, height)
  }
})
