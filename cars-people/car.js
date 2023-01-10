// car code
let xCars = [600, 600, 600]
let yCars = [40, 96, 150]
let carsSpeed = [2, 2.5, 3]

function showCar() {
  image(car1Image, xCars[0], yCars[0], 50, 40)
  image(car2Image, xCars[1], yCars[1], 50, 40)
  image(car3Image, xCars[2], yCars[2], 50, 40)
}

function moveCar() {
  xCars[0] -= carsSpeed[0]
  xCars[1] -= carsSpeed[1]
  xCars[2] -= carsSpeed[2]
}

function initCarPosition() {
  if (xCars[0] < -50) {
    xCars[0] = 600
  }
  if (xCars[1] < -50) {
    xCars[1] = 600
  }
  if (xCars[2] < -50) {
    xCars[2] = 600
  }
}
