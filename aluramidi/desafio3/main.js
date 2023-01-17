const buttonList = document.querySelectorAll('input[type=button]')
const telInput = document.querySelector('input[type=tel]')
telInput.tabIndex = -1
telInput.focus()

function setupButtonEventListeners(button) {
  const events = [
    {event: "mousedown", action: () => button.classList.add("ativa")},
    {event: "mouseup", action: () => button.classList.remove("ativa")},
    {event: "keydown", action: (e) => {
      if (e.key === " " || e.key === "Enter") button.classList.add("ativa")
    }},
    {event: "keyup", action: () => button.classList.remove("ativa")},
    {event: "click", action: () => telInput.value += button.value},
  ];

  events.forEach(({event, action}) => {
    button.addEventListener(event, action);
  });
}

for (let index = 0; index < buttonList.length; index++) {
  const button = buttonList[index]
  button.tabIndex = index + 1
  setupButtonEventListeners(button)
}

const firstButton = buttonList[0]
firstButton.addEventListener("keydown", e => {
  if (e.key === "Tab" && e.shiftKey) {
    e.preventDefault()
    telInput.focus()
  }
})

const telEvents = [
  {event: "keydown", action: e => {
    if (e.key === " " || e.key === "Enter") telInput.classList.add("ativa")
  }},
  {event: "keyup", action: () => telInput.classList.remove("ativa")},
];

telEvents.forEach(({event, action}) => {
    telInput.addEventListener(event, action);
});
