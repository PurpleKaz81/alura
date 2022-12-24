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

function draw() {
  // clear canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height)
  console.log('canvas cleared')

  // draw ball
  ctx.beginPath()
  ctx.arc(ballX, ballY, ballRadius, 0, Math.PI * 2)
  ctx.fillStyle = "#fff"
  ctx.fill()
  ctx.closePath()
  console.log('ball created')

  // draw left paddle
  ctx.fillStyle = "#fff"
  ctx.fillRect(0, leftPaddleY, paddleWidth, paddleHeight)
  console.log('left paddle drawn')

  // draw right paddle
  ctx.fillStyle = "#fff"
  ctx.fillRect(canvas.width - paddleWidth, rightPaddleY, paddleWidth, paddleHeight)
  console.log('right paddle drawn')

  // draw scores
  ctx.font = "48px sans-serif"
  ctx.textAlign = "center"
  ctx.fillText(leftScore, canvas.width * 1 / 4, 50)
  ctx.fillText(rightScore, canvas.width * 3 / 4, 50)
  console.log('scores drawn')

  // update ball position
  ballX += ballVelocityX
  ballY += ballVelocityY
  console.log('ball position updated')

  // check for ball collision with paddles
  if (ballX - ballRadius < paddleWidth) {
    if (ballY > leftPaddleY && ballY < leftPaddleY + paddleHeight) {
      ballVelocityX = -ballVelocityX
      ballVelocityY = (ballY - (leftPaddleY + paddleHeight / 2)) * 0.35
    } else {
      rightScore++
      ballReset()
    }
    if (ballY > rightPaddleY && ballY < rightPaddleY + paddleHeight) {
      ballVelocityX = -ballVelocityX
      ballVelocityY = (ballY - (rightPaddleY + paddleHeight / 2)) * 0.35
    } else {
      leftScore++
      ballReset()
    }
    console.log('checked for ball collision with paddles')
  }

  // check for ball collision with top and bottom
  if (ballY - ballRadius < 0 || ballY + ballRadius > canvas.height) {
    ballVelocityY = -ballVelocityY
  }
  // move right paddle
  if (rightPaddleY + paddleHeight / 2 < ballY) {
    rightPaddleY += 5
  } else {
    rightPaddleY -= 5
  }

  // request another frame
  requestAnimationFrame(draw)
}

// set keyDownHandler function
const keyDownHandler = (e) => {
  if (e.key === "w") {
    leftPaddleY -= 20
  } else if (e.key === "s"){
    leftPaddleY += 20
  }
}

// TODO reset ball
function ballReset() {
  ballX = canvas.width / 2
  ballY = canvas.height / 2
  ballVelocityX = initialBallVelocityX
  ballVelocityY = initialBallVelocityY
}

// TODO start game
function startGame() {
  gameLoop = requestAnimationFrame(draw)
}

// TODO stop game
function stopGame() {
  cancelAnimationFrame(gameLoop)
}

// TODO reset game
function resetGame() {
  stopGame()
}

// TODO add event pertinent listeners: keydown and resizing window
document.addEventListener("keydown", keyDownHandler)
window.addEventListener("resize", () => {
  // resize canvas viz window
  canvas.width = window.innerWidth
  canvas.height = window.innerHeight
  // TODO reset ball within resizing event listener
  ballReset()
})

// TODO start game
startGame()
