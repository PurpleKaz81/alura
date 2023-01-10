// actor starting position
let xActor = 100
let yActor = 369
let hit = false

function showActor() {
  image(actorImage, xActor, yActor, 25, 25)
}

function moveActor() {
  if (keyIsDown(UP_ARROW)) {
    yActor -= 3
  }
  if (keyIsDown(DOWN_ARROW)) {
    yActor += 3
  }
}

function verifyCollision() {
  // collideRectCircle(x1, y1, width1, height1, cx, cy, diameter)
  for (let i = 0; i < carImages.length, i += 1) {
    hit = collideRectCircle(xCars[i], yCars[i], carWidth, carHeight)
  }
}
