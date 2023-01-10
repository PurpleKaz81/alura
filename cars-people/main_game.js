function setup() {
  let cnv = createCanvas(500, 400)
  cnv.position(0, 0, "fixed")
}

function draw () {
  background(roadImage)
  showActor()
  showCar()
  moveActor()
  moveCar()
  initCarPosition()
}
