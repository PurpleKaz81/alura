const form = document.querySelector("#novoItem")
const list = document.querySelector("#lista")
const localStorageItems = JSON.parse(localStorage.getItem("items"))
const items = localStorageItems || []

const deleteButton = (id) => {
  const elementButton = document.createElement("button")
  elementButton.innerText = "X"

  elementButton.addEventListener("click", function () {
    deleteElement(this.parentNode, id)
  })

  return elementButton
}

const deleteElement = (item, id) => {
  item.remove()

  items.splice(
    items.findIndex((element) => element.id === id),
    1
  )

  localStorage.setItem("items", JSON.stringify(items))
}

const createElement = (item) => {
  // replicate <li class="item"><strong>7</strong>Camisas</li>
  const newItem = document.createElement("li")
  newItem.classList.add("item")

  const itemQuantity = document.createElement("strong")
  itemQuantity.innerHTML = item.quantity
  itemQuantity.dataset.id = item.id

  newItem.appendChild(itemQuantity)
  newItem.innerHTML += item.name

  newItem.appendChild(deleteButton(item.id))

  list.appendChild(newItem)
}

items.forEach(createElement)

const updateElement = (item) => {
  document.querySelector("[data-id='" + item.id + "']").innerHTML =
    item.quantity
}

form.addEventListener("submit", (event) => {
  event.preventDefault()
  const { nome: name, quantidade: quantity } = event.target.elements

  const itemExists = items.find((element) => element.name === name.value)

  const presentItem = { name: name.value, quantity: quantity.value }

  if (itemExists) {
    presentItem.id = itemExists.id
    updateElement(presentItem)
    items[items.findIndex((element) => element.id === itemExists.id)] =
      presentItem
  } else {
    presentItem.id = items.length ? items[items.length - 1].id + 1 : 0
    createElement(presentItem)
    items.push(presentItem)
  }

  localStorage.setItem("items", JSON.stringify(items))

  name.value = ""
  quantity.value = ""
})
