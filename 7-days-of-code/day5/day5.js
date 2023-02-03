let categories = {
  'Adult Items': [],
  'Beverages': [],
  'Books': [],
  'Booze': [],
  'Explosives': [],
  'Meats': [],
  'Munitions': [],
  'Weapons': []
}

function getUserInput(promptMessage) {
  return prompt(promptMessage)
}

function capitalizeGrocery(grocery) {
  return grocery.charAt(0).toUpperCase() + grocery.slice(1).toLowerCase()
}

function validateGrocery(grocery) {
  return grocery.match(/^[A-Za-z\s\d-]+$/);
}

function validateCategory(category) {
  return /^(adult_items|beverages|books|booze|explosives|meats|munitions|weapons)$/
    .test(category.toLowerCase())
}

function capitalizeCategory(category) {
  return category.charAt(0).toUpperCase() + category.slice(1).toLowerCase()
}

function validateChoice1(choice1) {
  if (choice1 !== '1' && choice1 !== '2') {
    alert("Please input either '1' or '2'.")
    return false
  }
  return true
}

// function displayList() {
//   for (let index = 0; index < groceries.length; index++) {
//     groceries[index]
//     let groceryList = document.querySelector("#grocery-list")
//     let newItem = document.createElement("li")
//     newItem.textContent = groceries[index]
//     groceryList.appendChild(newItem)
//   }
// }

function addGrocery(groceryItem) {
  let choice1 = getUserInput("Would you like to buy groceries today? Click '1' for yes and '2' for no.")
  if (!validateChoice1(choice1)) {
    alert("Please input either '1' or '2'.")
    return addGrocery()
  } else {
    if (choice1 == 2) {
      alert("I understand. Maybe some other time.")
      return addGrocery()
    } else {
      let grocery = getUserInput("Great! What items will you buy? Type in one at a time.")
      while (!validateGrocery(grocery)) {
        alert("Please type in a valid name for a grocery")
        grocery = getUserInput("So what items will you buy? Type in one at a time.")
      }

      function categorizeGrocery(grocery) {
        let listOfCategories = Object.keys(categories).join(", ")

        let category = getUserInput(`${capitalizeGrocery(grocery)} falls under what category? The categories are ${listOfCategories}.`)

        if (!validateCategory(category)) {
          alert("Please type in a valid category")
          return categorizeGrocery(grocery)
        }

        category = capitalizeCategory(category)
        if (!categories[category]) {
          categories[category] = []
        }
        categories[category].push(capitalizeGrocery(grocery))
        console.log(categories)
        addGrocery()
      }
      categorizeGrocery(grocery)
    }
  }
}

window.onload = () => {
  addGrocery()
  while (true) {
    let addAnotherItem = getUserInput("Would you like to add another item to your list? Type '1' for yes and anything else to exit.")
    if (addAnotherItem.toLowerCase() != "1") {
      alert("Ok, then. See you soon \u{1F61D}")
      break
    } else {
      let grocery = getUserInput("Great! Add an item.")
      if (!validateGrocery(grocery)) {
        alert("Please type in a valid name for a grocery")
        grocery
      } else {
        grocery = capitalizeGrocery(grocery)
        // displayList()
      }
    }
  }
}
