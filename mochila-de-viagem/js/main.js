const form = document.querySelector("#novoItem")
const list = document.querySelector("#lista")
const items = JSON.parse(localStorage.getItem("items")) || []

const createElement = (item) => {
  // replicate <li class="item"><strong>7</strong>Camisas</li>
  const newItem = document.createElement("li")
  newItem.classList.add("item")

  const itemQuantity = document.createElement("strong")
  itemQuantity.innerHTML = item.quantity
  itemQuantity.dataset.id = item.id

  newItem.appendChild(itemQuantity)
  newItem.innerHTML += item.name

  list.appendChild(newItem)
}

const updateElement = (item) => {
  document.querySelector("[data-id='"+item.id+"']").innerHTML = item.quantity
}


items.forEach((item) => {
  createElement(item)
})

form.addEventListener("submit", (event) => {
  event.preventDefault()
  const name = event.target.elements['nome']
  const quantity = event.target.elements['quantidade']

  const exists = items.find( element => element.name === name.value)

  const presentItem = {
    "name": name.value,
    "quantity": quantity.value
  }

  if (exists) {
    presentItem.id = exists.id
    updateElement(presentItem)
    items[exists.id] = presentItem
  } else {
    presentItem.id = items.length
    createElement(presentItem)
    items.push(presentItem)
  }


  localStorage.setItem("items", JSON.stringify(items))

  name.value = ""
  quantity.value = ""
})
