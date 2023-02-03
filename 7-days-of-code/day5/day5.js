let groceries = []

function getUserInput(promptMessage) {
  return prompt(promptMessage)
}

function capitalizeGrocery(grocery) {
  return grocery.charAt(0).toUpperCase() + grocery.slice(1).toLowerCase()
}

function validateGrocery(grocery) {
  return grocery.match(/^[A-Za-z\s-]+$/) && grocery != null && grocery != ""
}

function validateChoice1(choice1) {
  return !isNaN(Number(choice1)) && choice1 >= 1 && choice1 <= 2
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
      let grocery = getUserInput("Great! What items will you buy. Type in one at a time.")
      grocery = capitalizeGrocery(grocery)
      if (!validateGrocery(grocery)) {
        alert("Please type in a valid name for a grocery")
      } else {
        groceries.push(grocery)
      }
    }
  }
}

window.onload = () => {
  while (true) {
    addGrocery()
    let addAnotherItem = getUserInput("Would you like to add another item to your list? Type 'yes' or 'no' Add as many as you want.")
    if (addAnotherItem.toLowerCase() != "yes") break
  }
}
