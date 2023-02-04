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
  var pattern = /^[A-Za-z\s\d-&]+$/
  if (grocery === null) {
    return false
  }
  let matchResult = grocery.match(pattern)
  if (matchResult === null) {
    return false
  }
  return matchResult[0] === grocery
}

function validateCategory(category) {
  let lowerCaseCategories = Object.keys(categories).map(key => key.toLowerCase().replace(/\s+/g, '_'))
  return lowerCaseCategories.includes(category.toLowerCase().replace(/\s+/g, '_'))
}

function validateChoice1(choice1) {
  if (choice1 !== '1' && choice1 !== '2') {
    alert("Please input either '1' or '2'.")
    return false
  }
  return true
}

function categorizeGrocery(grocery) {
  let listOfCategories = Object.keys(categories).join(", ")

  let category = getUserInput(`${capitalizeGrocery(grocery)} falls under what category? The categories are ${listOfCategories}.`)

  if (!validateCategory(category)) {
    alert("Please type in a valid category")
    return categorizeGrocery(grocery)
  }

  let foundCategory = Object.keys(categories).find(key => key.toLowerCase() === category.toLowerCase())

  if (!foundCategory) {
    categories[category] = []
    foundCategory = category
  }

  categories[foundCategory].push(capitalizeGrocery(grocery))

  console.log(categories)
}

function addGrocery(groceryItem) {
  let choice1 = getUserInput("Would you like to shop today? Click '1' for yes and '2' for no.")
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
        alert("Please type in a valid name for an item")
        grocery = getUserInput("So what items will you buy? Type in one at a time.")
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
        alert("Please type in a valid name for an item")
        grocery
      } else {
        grocery = capitalizeGrocery(grocery)
        categorizeGrocery(grocery)
      }
    }
  }
}
