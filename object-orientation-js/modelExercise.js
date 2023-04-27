class Model {
  constructor(firstName, lastName, height, weight, hairColor, piercings) {
    this.firstName = firstName
    this.lastName = lastName
    this.height = height
    this.weight = weight
    this.hairColor = hairColor
    this.piercings = piercings

    this.friendZoned = (height, julianaHeight, heightLimit) => {
      if (height === julianaHeight) {
        return ""
      }
      return parseFloat(height) < heightLimit ? "Friend-zoned" : "Doable"
    }

    this.logInfo = (julianaHeight, heightLimit) => {
      console.log(`FIRSTNAME | LASTNAME | HEIGHT | WEIGHT | HAIR COLOR | PIERCINGS | FRIEND-ZONED \n${models
        .map(
          ({ firstName, lastName, height, weight, hairColor, piercings}) =>
            `${firstName} | ${lastName} | ${height} | ${weight} | ${hairColor} | ${piercings} | ${this.friendZoned(height, julianaHeight, heightLimit)}`
        )
        .join("\n")}
      `)
    }
  }
}

const model1 = new Model("Juliana", "Silva", 1.70, "60kg", "black", 10)

const model2 = new Model("Jeremiah", "Hicks", 1.87, "74kg", "brown", 5.3)

const model3 = new Model("Troy", "Sparks", 1.67, "67kg", "brown", 2)

const model4 = new Model("Sophia", "Wu", 1.65, "55kg", "black", 1)

const model5 = new Model("Chloe", "Chen", 1.73, "63kg", "blonde", 3)

const model6 = new Model("Isabella", "Garcia", 1.72, "58kg", "brown", 0)

const model7 = new Model("Richard", "Singh", 1.90, "61kg", "black", 2)

const model8 = new Model("Lily", "Patel", 1.74, "64kg", "red", 4)

const model9 = new Model("Harrison", "Choi", 1.68, "56kg", "blonde", 1)

const model10 = new Model("Amelia", "Lee", 1.87, "62kg", "brown", 2)

const models = [
  model1,
  model2,
  model3,
  model4,
  model5,
  model6,
  model7,
  model8,
  model9,
  model10,
]

const printInfo = () => {
  models[0].logInfo(model1.height, 1.85)
}

console.log("Here is a list of models and their information:\n")
printInfo()
console.log("\n")

const totalPiercings = models
  .slice(1)
  .reduce((acc, curr) => acc + curr.piercings, 0)

console.log(`The total number of piercings among the models in ${model1.firstName}\'s party is ${totalPiercings}, for a total of ${totalPiercings + model1.piercings} with hers included.`)
