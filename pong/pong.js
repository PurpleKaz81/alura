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

function draw() {
  // TODO clear canvas
  // TODO draw ball
  // TODO draw left paddle
  // TODO draw right paddle
  // TODO draw scores
  // TODO update ball position
  // TODO check for ball collision with paddles
  // TODO check for ball collision with edges
  // TODO check for ball collision with top and bottom
  // TODO move right paddle
  // TODO request another frame
}
