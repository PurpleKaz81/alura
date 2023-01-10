// car code
let xCars = [600, 600, 600]
let yCars = [40, 96, 150]
let carsSpeed = [2, 2.5, 3]
let carWidth = 50
let carHeight = 40

function showCar() {
  for (let i = 0; i < carImages.length; i += 1) {
    image(carImages[i], xCars[i], yCars[i], carWidth, carHeight)
  }
}

function moveCar() {
  for (let i = 0; i < carImages.length; i += 1)
    xCars[i] -= carsSpeed[i]
}

function initCarPosition() {
  for (i = 0; i < carImages.length; i += 1)
    if (completedScreen(xCars[i])) {
      xCars[i] = 600
  }
}

function completedScreen(xCar) {
  return xCar < -50
}
