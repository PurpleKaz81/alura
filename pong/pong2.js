// set up canvas
const canvas = document.getElementById("pong-canvas")
const ctx = canvas.getContext("2d")

// set up constants (ball, paddle)
const ballRadius = 10
const initialBallVelocityX = 5
const initialBallVelocityY = 5
const paddleWidth = 10
const paddleHeight = 75

// set up variables (ball, paddle, score)
let ballX = canvas.width / 2
let ballY = canvas.height / 2
let ballVelocityX = initialBallVelocityX
let ballVelocityY = initialBallVelocityY
let leftPaddleY = (canvas.height - paddleHeight) / 2
let rightPaddleY = (canvas.height - paddleHeight) / 2
let leftScore = 0
let rightScore = 0

// set up keyboard variables for left paddle
let keyIsDown = false
let keyDirection = 0

function updateGameState() {
  // update ball position
  ballX += ballVelocityX
  ballY += ballVelocityY

  // check for ball collision with left paddle
  if (ballX - ballRadius < paddleWidth) {
    if (ballY > leftPaddleY && ballY < leftPaddleY + paddleHeight) {
      let spin = Math.floor(Math.random())
      ballVelocityX = -ballVelocityX;
      ballVelocityY = (ballY - (leftPaddleY + paddleHeight / 2)) * 0.35;
    } else {
      rightScore++;
      ballReset();
    }
  }

  // check for ball collision with right paddle
  if (ballX + ballRadius > canvas.width - paddleWidth) {
    if (ballY > rightPaddleY && ballY < rightPaddleY + paddleHeight) {
      ballVelocityX = -ballVelocityX;
      ballVelocityY = (ballY - (rightPaddleY + paddleHeight / 2)) * 0.35;
    } else {
      leftScore++;
      ballReset();
    }
  }

  // check for ball collision with top and bottom of canvas
  if (ballY - ballRadius < 0 || ballY + ballRadius > canvas.height) {
    ballVelocityY = -ballVelocityY
  }

  // move right paddle
  if (rightPaddleY + paddleHeight / 2 < ballY) {
    rightPaddleY += 5
  } else {
    rightPaddleY -= 5
  }

  // limit right paddle movement to confines of canvas
  if (rightPaddleY < 0) {
    rightPaddleY = 0
  } else if (rightPaddleY + paddleHeight > canvas.height) {
    rightPaddleY = canvas.height - paddleHeight
  }

  // Calculate the difference between the y-coordinate of the ball and the y-coordinate of the center of the right paddle
  let paddleCenterY = rightPaddleY + paddleHeight / 2;
  let paddleMovement = ballY - paddleCenterY;

  // Move the right paddle based on the calculated difference
  rightPaddleY += paddleMovement;

  // Limit the right paddle's movement to the confines of the canvas
  if (rightPaddleY < 0) {
    rightPaddleY = 0;
  } else if (rightPaddleY + paddleHeight > canvas.height) {
    rightPaddleY = canvas.height - paddleHeight;
  }

  // move left paddle with keyboard input
  if (keyIsDown) {
    leftPaddleY += keyDirection * 5
  }

  // limit left paddle movement to confines of canvas
  if (leftPaddleY < 0) {
    leftPaddleY = 0
  } else if (leftPaddleY + paddleHeight > canvas.height) {
    leftPaddleY = canvas.height - paddleHeight
  }
}

function renderGame() {
  // clear canvas
  ctx.fillStyle = "#000"
  ctx.fillRect(0, 0, canvas.width, canvas.height)

  // draw ball
  ctx.beginPath()
  ctx.arc(ballX, ballY, ballRadius, 0, Math.PI * 2)
  ctx.fillStyle = "#fff"
  ctx.fill()
  ctx.closePath()

  // draw left paddle
  ctx.fillStyle = "#fff"
  ctx.fillRect(0, leftPaddleY, paddleWidth, paddleHeight)

  // draw right paddle
  ctx.fillStyle = "#fff"
  ctx.fillRect(canvas.width - paddleWidth, rightPaddleY, paddleWidth, paddleHeight)

  // draw scores
  ctx.font = "48px sans-serif"
  ctx.textAlign = "center"
  ctx.fillText(leftScore, canvas.width * 1 / 4, 50)
  ctx.fillText(rightScore, canvas.width * 3 / 4, 50)
}

function ballReset() {
  ballX = canvas.width / 2
  ballY = canvas.height / 2
  ballVelocityX = initialBallVelocityX
  ballVelocityY = initialBallVelocityY
}

// add event listeners for keyDown and keyUp events
document.addEventListener("keydown", (e) => {
  if (e.key === "s") {
    keyIsDown = true
    keyDirection = 1
  } else if (e.key === "w") {
    keyIsDown = true
    keyDirection = -1
  }
})

document.addEventListener("keyup", (e) => {
  if (e.key === "w" || e.key === "s") {
    keyIsDown = false
    keyDirection = 0
  }
})

function draw() {
  updateGameState()
  renderGame()

  // request another frame
  requestAnimationFrame(draw)
}

requestAnimationFrame(draw)
