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

