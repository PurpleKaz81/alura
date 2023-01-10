function setup() {
  createCanvas(500, 400).position(0, 0, "fixed")
  // soundtrack.loop()
}

function draw () {
  background(roadImage)
  showActor()
  showCar()
  moveActor()
  moveCar()
  initCarPosition()
  verifyCollision()
  scoreboard()
  addPoint()
}
