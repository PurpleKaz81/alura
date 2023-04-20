const form = document.querySelector("#novoItem")
const list = document.querySelector("#lista")
const items = []

form.addEventListener("submit", (event) => {
  event.preventDefault()
  const name = event.target.elements['nome']
  const quantity = event.target.elements['quantidade']

  createElement(name.value, quantity.value)

  name.value = ""
  quantity.value = ""
})

const createElement = (name, quantity) => {
  // replicate <li class="item"><strong>7</strong>Camisas</li>
  const newItem = document.createElement("li")
  newItem.classList.add("item")

  const itemQuantity = document.createElement("strong")
  itemQuantity.innerHTML = quantity

  newItem.appendChild(itemQuantity)
  newItem.innerHTML += name

  list.appendChild(newItem)

  const presentItem = {
    "name": name,
    "quantity": quantity
  }

  items.push(presentItem)

  localStorage.setItem("item", JSON.stringify(items))
}
