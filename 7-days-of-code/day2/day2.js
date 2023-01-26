let firstName
while (true) {
  firstName = window.prompt("What's your first name?")
  if (firstName.match(/^[a-zA-Z-'\s]+$/) && firstName != "") {
    alert(`Hi, ${firstName}! Welcome`)
    break
  } else {
    alert("Please input a valid name (letters and spaces only).")
  }
}

let lastName
while (true) {
  lastName = window.prompt("What's your surname?")
  if (lastName.match(/^[a-zA-Z-'\s]+$/) && lastName != "") {
    alert(`Thanks, ${firstName}!`)
    break
  } else {
    alert("Please input a valid name (letters and spaces only)")
  }
}

let age
while (true) {
  age = window.prompt(`How old are you, ${firstName}?`)
  if (age.match(/^(1[0-2]\d|[1-9]?\d|0)$/) && age != "") {
    alert(`You don't look a day over 20, ${firstName}!`)
    break
  } else {
    alert("Please input a valid age (with numbers only)")
  }
}

let language
while (true) {
  language = window.prompt(`What language have you been focusing on?`)
  if (language.match(/^[a-zA-Z]+([-_ ]?[a-zA-Z0-9]+)*$/) && language != "") {
    alert(`A wise choice, ${firstName} ${lastName}.`)
    break
  } else {
    alert("Please input a valid language (using letters and spaces only)")
  }
}

let languageStudy
while (true) {
  languageStudy = window.prompt(`Do you enjoy studying programming languages? Type Y for yes and N for no`)
  if (languageStudy.match(/^y$/i)) {
    alert("That's wonderful news!")
    break
  } else if (languageStudy.match(/^n$/i)) {
    alert("Hmmmm, you probably prefer the language of love, doncha?")
    break
  } else {
    alert("Please input a valid answer, using only 'y' or 'n'")
  }
}

if (firstName && lastName && age && language && languageStudy) {
  document.getElementById("welcome").innerHTML = `Welcome to the Pleasuredome, ${firstName} ${lastName}. You're ${age} old, too young to reason and too grown up to dream. Relax when you wanna come 🫦`
  document.getElementById("relax").style.display = "block"
}
