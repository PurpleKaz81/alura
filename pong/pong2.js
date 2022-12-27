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

// set gameLoop variable
let gameLoop

function updateGameState() {
  // update ball position
  ballX += ballVelocityX
  ballY += ballVelocityY

  // check for ball collision with left paddle
  if (ballX - ballRadius < paddleWidth) {
    if (ballY > leftPaddleY && ballY < leftPaddleY + paddleHeight) {
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
  if (ballY - ballRadius < 0 || ballY + ballRadius > canvas-height) {
    ballVelocityY = -ballVelocityY
  }

  // move right paddle
  if (rightPaddleY + paddleHeight / 2 < ballY) {
    rightPaddleY += 5
  } else {
    rightPaddleY -= 5
  }
}

function draw() {
  updateGameState()
  renderGame()
  requestAnimationFrame(draw)
}
