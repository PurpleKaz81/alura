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
  return /^(?!.*[^A-Za-z\s\d&-]).+$/.test(grocery);
}

function validateCategory(category) {
  let lowerCaseCategories = Object.keys(categories).map(key => key.toLowerCase().replace(/\s+/g, '_'))
  return lowerCaseCategories.includes(category.toLowerCase().replace(/\s+/g, '_'))
}

function validateChoice1(choice1) {
  switch (choice1) {
    case "1":
    case "2":
      return true

      break

    default:
      alert("Please input either '1' or '2'.")
      return false
  }
}

function validateChoice2(choice2) {
  switch (choice2) {
    case "1":
    case "2":
      return true

      break

    default:
      alert("Please input either '1' or '2'.")
      return false
  }
}

function categorizeGrocery(grocery) {
  let listOfCategories = Object.keys(categories).join(", ")

  let category = ""
  while (!validateCategory(category)) {
    category = getUserInput(`${capitalizeGrocery(grocery)} falls under what category? The categories are:\n${listOfCategories}.`)
    if (!validateCategory(category)) {
      alert("Please type in a valid category")
    }
  }

  let foundCategory = Object.keys(categories).find(key => key.toLowerCase() === category.toLowerCase())

  if (!foundCategory) {
    categories[category] = []
    foundCategory = category
  }

  categories[foundCategory].push(capitalizeGrocery(grocery))

  displayList()
}

let counter = 0

function addGrocery(groceryItem) {
  counter++
  if (counter > 10) {
    counter = 0
    return
  }
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

function removeGrocery(groceryItem) {
  counter++
  if (counter > 10) {
    counter = 0
    return
  }
  let choice2 = getUserInput("Would you like to remove any items today? Click '1' for yes and '2' for no.")
  if (!validateChoice2(choice2)) {
    alert("Please input either '1' or '2'.")
    return removeGrocery()
  } else {
    let negativeGrocery = getUserInput("Which item will you remove? Type in the item's name.")
    while (!validateGrocery(negativeGrocery)) {
      alert("Please type in a valid name for an item")
      negativeGrocery = getUserInput("So what item will you remove? Type in one at a time.")
    }
  }
  let foundCategory = Object.keys(categories).find(key => categories[key].includes(capitalizeGrocery(negativeGrocery)))

  if (!foundCategory) {
    alert("No such item was found in the list")
  } else {
    let index = categories[foundCategory].indexOf(capitalizeGrocery(negativeGrocery))
    categories[foundCategory].splice(index, 1)

    if (category[foundCategory].length === 0) {
      delete categories[foundCategory]
    }
  }
}

function displayList() {
  let list = document.querySelector("#grocery-list")
  list.style.listStyleType = "none"
  list.innerHTML = ""

  for (const category of Object.keys(categories)) {
    let items = categories[category]
    if (items.length > 0) {
      let categoryElement = document.createElement("li")
      categoryElement.innerHTML = `<b>${category}:</b>`
      list.appendChild(categoryElement)
      let itemsList = document.createElement("ul")
      itemsList.style.listStyleType = "decimal"
      for (const item of items) {
        let itemElement = document.createElement("li")
        itemElement.innerHTML = item
        itemsList.appendChild(itemElement)
      }
      list.appendChild(itemsList)
    }
  }
}

window.onload = () => {
  addGrocery()
  while (true) {
    let addAnotherItem = getUserInput("Would you like to add another item to your list? Type '1' for yes and anything else to exit.")
    if (addAnotherItem != "1") {
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
  console.log(categories)
}
