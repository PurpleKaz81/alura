// Get a reference to the canvas element in the HTML
const canvas = document.querySelector("#my-canvas")
canvas.width = 1000
canvas.height = 650

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

    // set global composite operation to "destination-over"
    ctx.globalCompositeOperation = "destination-over"

    // draw image on canvas
    if (index === 0) {
      // draw background image centered on canvas
      ctx.drawImage(image, (canvas.width - width) / 2, (canvas.height - height) / 2, width, height)
    } else {
      // draw other images on top of background image
      ctx.drawImage(image, (index - 1) * width, 0, width, height)
    }
  }
})
