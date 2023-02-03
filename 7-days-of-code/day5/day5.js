let categories = []
let groceries = {}

function getUserInput(promptMessage) {
  return prompt(promptMessage)
}

function capitalizeGrocery(grocery) {
  return grocery.charAt(0).toUpperCase() + grocery.slice(1).toLowerCase()
}

function validateGrocery(grocery) {
  return grocery.match(/^[A-Za-z\s-]+$/) && grocery != null && grocery != ""
}

function validateCategory(category) {
  let categories = /^(fruits|vegetables|frozen|booze|drinks|other)$/
  return category.toLowerCase().match(categories)
}

function categorizeGrocery(grocery, category) {
  let category = getUserInput(`${capitalizeGrocery(grocery)} falls under what category?`)
  if (!validateCategory(category)) {
    alert("Please type in a valid category.")
    return categorizeGrocery(grocery)
  }

  switch (category) {
    case "adult items":
      adult_items.push(grocery)
      break
    case "beverages":
      beverages.push(grocery)
      break
    case "books":
      books.push(grocery)
      break
    case "booze":
      booze.push(grocery)
      break
    case "explosives":
      explosives.push(grocery)
      break
    case "meats":
      meat.push(grocery)
      break
    case "munitions":
      munitions.push(grocery)
      break
    case "weapons":
      weapons.push(grocery)
      break
  }
}

function capitalizeCategory(category) {
  return category.charAt(0).toUpperCase() + category.slice(1).toLowerCase()
}

function validateChoice1(choice1) {
  return Number(choice1) === 1 || Number(choice1) === 2
}

function displayList() {
  for (let index = 0; index < groceries.length; index++) {
    groceries[index]
    let groceryList = document.querySelector("#grocery-list")
    let newItem = document.createElement("li")
    newItem.textContent = groceries[index]
    groceryList.appendChild(newItem)
  }
}

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
      grocery = capitalizeGrocery(grocery)
      groceries.push(grocery)
      categorizeGrocery()
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
        continue
      } else {
        grocery = capitalizeGrocery(grocery)
        groceries.push(grocery)
        displayList()
      }
    }
  }
}
