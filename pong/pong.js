// set up canvas
const canvas = document.getElementById("game")
const ctx = canvas.getContext("2d")

// set up ball
let ballX = canvas.width / 2
let ballY = canvas.height / 2
let ballRadius = 10
let ballVelocityX = 5
let ballVelocityY = 5

// set up paddles
let paddleWidth = 10
let paddleHeight = 75
let paddleVelocity = 5
let leftPaddleY = (canvas.height - paddleHeight) / 2
let rightPaddleY = (canvas.height - paddleHeight) / 2

// set up score
let leftPaddleScore = 0
let rightPaddleScore = 0

// set up keyboard controls
let upPressed = false
let downPressed = false

document.addEventListener("keydown", keyDownHandler)
document.addEventListener("keyup", keyUpHandler)

function keyDownHandler(e) {
  if (e.key === "ArrowUp") {
    upPressed = true
  }
  if (e.key === "ArrowDown") {
    downPressed = true
  }
}

function keyUpHandler(e) {
  if (e.key === "ArrowUp") {
    upPressed = false
  }
  if (e.key === "ArrowDown") {
    downPressed = false
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
  ctx.fillText(leftPaddleScore, canvas.width / 4, 50);
  ctx.fillText(rightPaddleScore, canvas.width * 3 / 4, 50);
}

// move ball
function moveBall() {
  ballX += ballVelocityX
  ballY += ballVelocityY

  // collision detection
  if (ballX - ballRadius < 0) {
    // left paddle
    if (ballY > leftPaddleY && ballY < leftPaddleY + paddleHeight) {
      ballVelocityX = -ballVelocityX
      ballVelocityY = (ballY - (leftPaddleY + paddleHeight / 2)) * 0.20
    } else {
      rightPaddleScore++
      resetBall()
      resetPaddles()
    }
  }
  if (ballX + ballRadius > canvas.width) {
    //  right paddle
    if (ballY > rightPaddleY && ballY < rightPaddleY + paddleHeight) {
      ballVelocityX = -ballVelocityX
      ballVelocityY = (ballY - (rightPaddleY +paddleHeight / 2)) * 0.20
    } else {
      leftPaddleScore++
      resetBall()
      resetPaddles()
    }
  }
  if (ballY - ballRadius < 0 || ballY + ballRadius > canvas.height) {
    ballVelocityY = -ballVelocityY
  }
}

// move paddles
function movePaddles() {
  // left paddle
  if (upPressed && leftPaddleY > 0) {
    leftPaddleY -= paddleVelocity
  }
  if (downPressed && leftPaddleY < canvas.height - paddleHeight) {
    leftPaddleY += paddleVelocity
  }

  // right paddle
  if (ballY < rightPaddleY + paddleHeight / 2 && rightPaddleY > 0) {
    rightPaddleY -= paddleVelocity
  }
  if (ballY > rightPaddleY + paddleHeight / 2 && rightPaddleY < canvas.height - paddleHeight) {
    rightPaddleY += paddleVelocity
  }
}

// reset ball to center of canvas
function resetBall() {
  ballX = canvas.width / 2
  ballY = canvas.height / 2
}

// reset paddles to center of canvas
function resetPaddles() {
  leftPaddleY = (canvas.height - paddleHeight) / 2
  rightPaddleY = (canvas.height - paddleHeight) / 2
}

//  main game loop
function draw() {
  // clear canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height)

  // draw elements
  drawBall()
  drawPaddles()
  drawScore()

  // ball and paddle motion
  moveBall()
  movePaddles()

  // request new frame
  requestAnimationFrame(draw)
}

// start game loop
draw()
