// set up canvas
const canvas = document.getElementById("pong")
const ctx = canvas.getContext("2d")

// set up ball
let ballX = canvas.width / 2
let ballY = canvas.height / 2
let ballRadius = 10
let ballVelocityX = 5
let ballVelocityY = 5

