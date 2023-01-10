function setup() {
  createCanvas(500, 400)
}

function draw () {
  background(roadImage)
  showActor()
  show(car)
  moveActor()
  moveCar()
  initCarPosition()
}
