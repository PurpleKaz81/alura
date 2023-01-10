// car code
let yCars = [40, 96, 150]
let carsSpeed = [2, 2.5, 3]

// car 1
let xCar1 = 600

// car 2
let xCar2 = 600

// car 3
let xCar3 = 600

function showCar() {
  image(car1Image, xCar1, yCars[0], 50, 40)
  image(car2Image, xCar2, yCars[1], 50, 40)
  image(car3Image, xCar3, yCars[2], 50, 40)
}

function moveCar() {
  xCar1 -= carsSpeed[0]
  xCar2 -= carsSpeed[1]
  xCar3 -= carsSpeed[2]
}

function initCarPosition() {
  if (xCar1 < -50) {
    xCar1 = 600
  }
  if (xCar2 < -50) {
    xCar2 = 600
  }
  if (xCar3 < -50) {
    xCar3 = 600
  }
}
