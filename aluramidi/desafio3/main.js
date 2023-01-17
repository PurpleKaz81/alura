const buttonList = document.querySelectorAll('input[type=button]');
const telInput = document.querySelector('input[type=tel]');
telInput.tabIndex = -1;
telInput.focus();

const addEventListeners = (element, events) => {
    events.forEach(({event, action}) => {
        element.addEventListener(event, action);
    });
};

const buttonEvents = [
    {event: "mousedown", action: e => e.target.classList.add("ativa")},
    {event: "mouseup", action: e => e.target.classList.remove("ativa")},
    {event: "keydown", action: e => {
        if (e.key === " " || e.key === "Enter") e.target.classList.add("ativa")
    }},
    {event: "keyup", action: e => e.target.classList.remove("ativa")},
    {event: "click", action: e => telInput.value += e.target.value},
];

const telEvents = [
    {event: "keydown", action: e => {
        if (e.key === " " || e.key === "Enter") telInput.classList.add("ativa")
    }},
    {event: "keyup", action: e => telInput.classList.remove("ativa")},
];

buttonList.forEach((button, index) => {
    button.tabIndex = index + 1;
    addEventListeners(button, buttonEvents);
});

const firstButton = buttonList[0];
firstButton.addEventListener("keydown", e => {
    if (e.key === "Tab" && e.shiftKey) {
        e.preventDefault();
        telInput.focus();
    }
});
addEventListeners(telInput, telEvents);
