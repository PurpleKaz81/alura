// actor starting position
let xActor = 85
let yActor = 369
let hit = false
let myPoints = 0

function showActor() {
  image(actorImage, xActor, yActor, 25, 25)
}

function moveActor() {
  if (keyIsDown(UP_ARROW)) {
    yActor -= 3
  }
  if (keyIsDown(DOWN_ARROW)) {
    if (actorCanMove()){
    yActor += 3
    }
  }
}

function verifyCollision() {
  // collideRectCircle(x1, y1, width1, height1, cx, cy, diameter)
  for (let i = 0; i < carImages.length; i++) {
    hit = collideRectCircle(xCars[i], yCars[i], carWidth, carHeight, xActor, yActor, 15)
      if (hit) {
        hitSound.play()
        backToStart()
        if (pointsGreaterThanZero()){
          myPoints -= 1
        }
      }
  }
}

function backToStart() {
  yActor = 369
}

function scoreboard() {
  textAlign(CENTER)
  text(myPoints, width / 5, 27)
  textSize(25)
  fill(color(255, 240, 60))
}

function addPoint() {
  if (yActor < 15) {
    myPoints += 1
    pointSound.play()
    backToStart()
  }
}

function pointsGreaterThanZero() {
  return myPoints > 0
}

function actorCanMove() {
  return yActor < 369
}
