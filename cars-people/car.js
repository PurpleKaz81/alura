// car code
let xCars = [600, 600, 600, 600, 600, 600]
let yCars = [40, 96, 150, 210, 270, 318]
let carsSpeed = [2, 2.5, 3, 5, 3.3, 2.3]
let carWidth = 50
let carHeight = 40

function showCar() {
  for (let i = 0; i < carImages.length; i++) {
    image(carImages[i], xCars[i], yCars[i], carWidth, carHeight)
  }
}

function moveCar() {
  for (let i = 0; i < carImages.length; i++)
    xCars[i] -= carsSpeed[i]
}

function initCarPosition() {
  for (i = 0; i < carImages.length; i++)
    if (completedScreen(xCars[i])) {
      xCars[i] = 600
  }
}

function completedScreen(xCar) {
  return xCar < -50
}
