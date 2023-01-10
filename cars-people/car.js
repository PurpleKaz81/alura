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
