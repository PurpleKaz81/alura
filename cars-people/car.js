// car code
let yCars = [40, 96, 150]

// car 1
let xCar1 = 600
let car1Speed = 2

// car 2
let xCar2 = 600
let car2Speed = 2.5

// car 3
let xCar3 = 600
let car3Speed = 3

function showCar() {
  image(car1Image, xCar1, yCars[0], 50, 40)
  image(car2Image, xCar2, yCars[1], 50, 40)
  image(car3Image, xCar3, yCars[2], 50, 40)
}

function moveCar() {
  xCar1 -= car1Speed
  xCar2 -= car2Speed
  xCar3 -= car3Speed
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
