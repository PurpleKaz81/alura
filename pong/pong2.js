// set up canvas
const canvas = document.getElementById("pong-canvas")
const ctx = canvas.getContext("2d")

// set up constants (ball, paddle)
const ballRadius = 10
const initialBallVelocityX = Math.random() < 0.5 ? -2 : 2
const initialBallVelocityY = Math.random() < 0.5 ? -2 : 2
const maxBallVelocity = 3
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

// set up frame rate in milliseconds
const frameRate = 1000 / 60

// set up game loop using setInterval
let gameInterval = setInterval(() => {
  updateGameState()
  renderGame()
}, frameRate)

// use setTimeout to delay the start of the game
setTimeout(() => {
  gameInterval = setInterval(() => {
    updateGameState()
    renderGame()
  }, frameRate)
}, 2000)

function updateGameState() {
// update ball position
ballX += ballVelocityX
ballY += ballVelocityY

  // spin coefficient variables
  let spin = 0.30

  // check for ball collision with left paddle
  if (ballX - ballRadius < paddleWidth) {
    if (ballY > leftPaddleY && ballY < leftPaddleY + paddleHeight) {
      let paddleCenterY = leftPaddleY + paddleHeight / 2
      let paddleMovement = ballY - paddleCenterY
      ballVelocityX = -ballVelocityX
      ballVelocityY = paddleMovement * spin + -1
      // limit ball's speed
      if (Math.abs(ballVelocityX) > maxBallVelocity) {
        ballVelocityX = Math.sign(ballVelocityX) + maxBallVelocity
      }
      if (Math.abs(ballVelocityY) > maxBallVelocity) {
        ballVelocityY = Math.sign(ballVelocityY) + maxBallVelocity
      }
    } else {
      rightScore++;
      ballReset();
    }
  }

  // check for ball collision with right paddle
  if (ballX + ballRadius > canvas.width - paddleWidth) {
    if (ballY > rightPaddleY && ballY < rightPaddleY + paddleHeight) {
      let paddleCenterY = rightPaddleY + paddleHeight / 2
      let paddleMovement = ballY - paddleCenterY
      ballVelocityX = -ballVelocityX
      ballVelocityY = paddleMovement * spin + -1
      // limit ball's speed
      if (Math.abs(ballVelocityX) > maxBallVelocity) {
        ballVelocityX = Math.sign(ballVelocityX) + maxBallVelocity
      }
      if (Math.abs(ballVelocityY) > maxBallVelocity) {
        ballVelocityY = Math.sign(ballVelocityY) + maxBallVelocity
      }
    } else {
      leftScore++;
      ballReset();
    }
  }

  // check for ball collision with top and bottom of canvas
  if (ballY - ballRadius < 0 || ballY + ballRadius > canvas.height) {
    ballVelocityY = -ballVelocityY
  }

  // Calculate the difference between the y-coordinate of the ball and the y-coordinate of the center of the right paddle
  let paddleCenterY = rightPaddleY + paddleHeight / 2
  let paddleMovement = ballY - paddleCenterY

  // Check if the ball is approaching the right paddle
  if (ballX + ballRadius > canvas.width - paddleWidth - 20 && ballVelocityX > 0) {
    // Add a random error margin to the paddle's movement
    let errorMargin = errorMargin(-1, 1)
    paddleMovement += errorMargin;
  } else {
  // Otherwise, move the paddle normally based on the calculated difference
    rightPaddleY += paddleMovement;
  }

  // limit right paddle movement to confines of canvas
  if (rightPaddleY < 0) {
    rightPaddleY = 0
  } else if (rightPaddleY + paddleHeight > canvas.height) {
    rightPaddleY = canvas.height - paddleHeight
  }

  // move left paddle with keyboard input
  if (keyIsDown) {
    leftPaddleY += keyDirection * 2.5
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

function errorMargin(min, max) {
  return Math.random() * (max-min) + min
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
  requestAnimationFrame(draw)
}

requestAnimationFrame(draw)
