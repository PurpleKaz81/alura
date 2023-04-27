class Model {
  constructor(firstName, lastName, height, weight, hairColor, piercings) {
    this.firstName = firstName
    this.lastName = lastName
    this.height = height
    this.weight = weight
    this.hairColor = hairColor
    this.piercings = piercings
  }

  friendZoned(julianaHeight, heightLimit) {
    if (this.height === julianaHeight) {
      return ""
    }
    return this.height < heightLimit ? "Friend-zoned" : "Doable"
  }

  modelInfoString(julianaHeight, heightLimit) {
    return `${this.firstName} | ${this.lastName} | ${this.height} | ${
      this.weight
    } | ${this.hairColor} | ${this.piercings} | ${this.friendZoned(
      julianaHeight,
      heightLimit
    )}`
  }

  logInfo(julianaHeight, heightLimit) {
    const modelInfo = models.map((model) =>
      model.modelInfoString(julianaHeight, heightLimit)
    )
    console.log(
      `FIRSTNAME | LASTNAME | HEIGHT | WEIGHT | HAIR COLOR | PIERCINGS | FRIEND-ZONED \n${modelInfo.join(
        "\n"
      )}`
    )
  }
}

const models = [
  new Model("Juliana", "Silva", 1.7, "60kg", "black", 10),
  new Model("Jeremiah", "Hicks", 1.87, "74kg", "brown", 5.3),
  new Model("Troy", "Sparks", 1.67, "67kg", "brown", 2),
  new Model("Sophia", "Wu", 1.65, "55kg", "black", 1),
  new Model("Chloe", "Chen", 1.73, "63kg", "blonde", 3),
  new Model("Isabella", "Garcia", 1.72, "58kg", "brown", 0),
  new Model("Richard", "Singh", 1.9, "61kg", "black", 2),
  new Model("Lily", "Patel", 1.74, "64kg", "red", 4),
  new Model("Harrison", "Choi", 1.68, "56kg", "blonde", 1),
  new Model("Amelia", "Lee", 1.87, "62kg", "brown", 2),
]

const printInfo = () => {
  models[0].logInfo(models[0].height, 1.85)
}

console.log("Here is a list of models and their information:\n")
printInfo()
console.log("\n")

const totalPiercings = models
  .slice(1)
  .reduce((acc, curr) => acc + curr.piercings, 0)

console.log(
  `The total number of piercings among the models in ${
    models[0].firstName
  }'s party is ${totalPiercings}, for a total of ${
    totalPiercings + models[0].piercings
  } with hers included.`
)
