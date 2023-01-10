// car code
let xCars = [600, 600, 600]
let yCars = [40, 96, 150]
let carsSpeed = [2, 2.5, 3]

function showCar() {
  for (let i = 0; i < carImages.length; i += 1) {
    image(carImages[i], xCars[i], yCars[i], 50, 40)
    }
  }

function moveCar() {
  for (let i = 0; i < carImages.length; i += 1)
    xCars[i] -= carsSpeed[i]
  }

function initCarPosition() {
  for (i = 0; i < carImages.length; i += 1)
    if (xCars[i] < -50) {
      xCars[i] = 600
    }
  }
