const form = document.querySelector("#novoItem")
const list = document.querySelector("#lista")

const createElement = (name, quantity) => {
  // replicate <li class="item"><strong>7</strong>Camisas</li>
  const newItem = document.createElement("li")
  newItem.classList.add("item")

  const itemQuantity = document.createElement("strong")
  itemQuantity.innerHTML = quantity

  newItem.appendChild(itemQuantity)
  newItem.innerHTML += name

  list.appendChild(newItem)
}

form.addEventListener("submit", (event) => {
  event.preventDefault()
  const name = event.target.elements['nome'].value
  const quantity = event.target.elements['quantidade'].value

  createElement(name, quantity)
})
