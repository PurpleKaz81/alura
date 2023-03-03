function capitalizeName(name) {
  return name.replace(/\b(\w)/g, (s) => s.toUpperCase())
}

function validateName(name) {
  let regexp = XRegExp("^[\\p{L}\\p{M}\\s.'’-]+$")
  return XRegExp.test(name, regexp) && name != "" && name != null
}

function validateAge(age) {
  return age && age.match(/^(1[0-2]\d|[1-9]?\d|0)$/) && age != "" && age != null
}

function capitalizeLanguage(language) {
  return language.replace(/\b(\w)/g, (s) => s.toUpperCase())
}

function handleInput() {
  let fullName
  while (!validateName(fullName)) {
    fullName = window.prompt("What's your full name, champ?")
    if (!validateName(fullName)) {
    	alert("Do us a solid and write in a valid name, letters and spaces only")
    }
  }
  fullName = capitalizeName(fullName)
  let firstName = fullName.split(" ")[0]
  alert(`Thanks, ${firstName}!`)

  let age
  while (!validateAge(age)) {
    age = window.prompt("And how old are you?")
    if (!validateAge(age)) {
      alert("No need to lie 😝 Just type in your age, anywhere between 0 and 130 with no decimals")
    }
  }
  alert(`So far so good, ${capitalizeName(fullName)}, ${age} years old.`)

  let language
  while (!language) {
    const choice1 = window.prompt(`Would you like to focus on "front-end" or "back-end", ${firstName}? Click "1" for front-end and "2" for back-end.`)
    if (choice1 === "1") {
      language = prompt("Great! Would you like to focus on React or Vue")
      break
    } else if (choice1 === "2") {
      language = prompt("Great! Would you like to focus on Java or C++?")
      break
    } else if (choice1 === null || choice1 === "") {
      alert("Please input a valid value.")
    }
  }

  let career
  while (true) {
    const choice2 = window.prompt(`Great stuff! And would you like to focus on ${capitalizeLanguage(language)} or go on to become a full-stack developer, ${firstName}? Click "1" for your language or "2" for full-stack web development.`)
    if (choice2 === "1") {
      career = alert("That's a wonderful future, ol' love!")
      break
    } else if (choice2 === "2") {
      career = alert("Andrew Tate would be proud, m'boy!")
      break
    } else if (choice2 === null || choice2 === "") {
      alert("Please input a valid value.")
    }
  }

  let extra = window.prompt(`Is there another technology you'd like to work on, ${firstName}? Click "ok" if that's the case.`)
  while (extra === "ok") {
    let newTech = prompt("Which one?")
    alert(`${newTech} sounds good, champ!`)
    extra = window.prompt(`Any other tech in mind, ${firstName}? Click ok if so.`)
  }
}

window.onload = () => {
  handleInput()
}
