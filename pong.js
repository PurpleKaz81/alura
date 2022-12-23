// set up canvas
const canvas = document.getElementById("pong")
const ctx = canvas.getContext("2d")

// set up ball
let ballX = canvas.width / 2
let ballY = canvas.height / 2
let ballRadius = 10
let ballVelocityX = 5
let ballVelocityY = 5

// set up paddles
let paddleHeight = 75
let paddleWidth = 10
let leftPaddleY = (canvas.height - paddle.height) / 2
let rightPaddleY = (canvas.height - paddle.height) / 2

// set up score
let leftPaddleScore = 0
let rightPaddleScore = 0

// set up keyboard controls
let upPressed = false
let downPressed = false
let wPressed = false
let sPressed = false

document.addEventListener("keydown", keyDownHandler)
document.addEventListener("keyup", keyUpHandler)

function keyDownHandler(e) {
  if (e.key === "ArrowUp") {
    upPressed = true
  }
  if (e.key === "ArrowDown") {
    downPressed = true
  }
  if (e.key === "w") {
    wPressed = true
  }
  if (e.key === "s") {
    sPressed = true
  }
}

function keyUpHandler(e) {
  if (e.key === "ArrowUp") {
    upPressed = false
  }
  if (e.key === "ArrowDown") {
    downPressed = false
  }
  if (e.key === "w") {
    wPressed = false
  }
  if (e.key === "s") {
    sPressed = false
  }
}

// draw ball on canvas
function drawBall() {
  ctx.beginPath()
  ctx.arc(ballX, ballY, ballRadius, 0, Math.PI * 2)
  ctx.fillStyle = "#fff"
  ctx.fill()
  ctx.closePath()
}

// draw paddles on canvas
function drawPaddles() {
  // left paddle
  ctx.fillStyle = "#fff"
  ctx.fillRect(0, leftPaddleY, paddleWidth, paddleHeight)

  // right paddle
  ctx.fillStyle = "#fff"
  ctx.fillRect(canvas.width - paddleWidth, rightPaddleY, paddleWidth, paddleHeight)
}
//  draw score on canvas
function drawScore() {
  ctx.font = '30px Arial';
  ctx.fillStyle = '#fff';
  ctx.textAlign = 'center';
  ctx.fillText(leftScore, canvas.width / 4, 50);
  ctx.fillText(rightScore, canvas.width * 3 / 4, 50);
}

// reset ball to center of canvas
function resetBall() {
  ballX = canvas.width / 2
  ballY = canvas.height / 2
}

