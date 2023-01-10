// actor starting position
let xActor = 100
let yActor = 369

function showActor() {
  image(actorImage, xActor, yActor, 30, 30)
}

function moveActor() {
  if (keyIsDown(UP_ARROW)) {
    yActor -= 3
  }
  if (keyIsDown(DOWN_ARROW)) {
    yActor += 3
  }
}
