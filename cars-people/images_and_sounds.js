// game images
let roadImage
let actorImage
let car1Image
let car2Image
let car3Image

let soundtrack
let hitSound
let pointSound

function preload() {
  roadImage = loadImage("images/road.png")
  actorImage = loadImage("images/player-1.png")
  car1Image = loadImage("images/car-1.png")
  car2Image = loadImage("images/car-2.png")
  car3Image = loadImage("images/car-3.png")
  carImages = [car1Image, car2Image, car3Image, car1Image, car2Image, car3Image]
  soundtrack = loadSound("sounds/trilha.mp3")
  hitSound = loadSound("sounds/colidiu.mp3")
  pointSound = loadSound("sounds/pontos.wav")
}
