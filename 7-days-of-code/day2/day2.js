let validFirstName = false
const firstName = window.prompt("What's your first name?")
if (firstName != "" && firstName != null) {
  alert(`Hi, ${firstName}! Welcome to the Pleasuredome.`)
  validFirstName = true
} else {
  alert("Please input a valid name.")
}

let lastName;
if (validFirstName) {
  lastName = window.prompt("What's your surname?")
  if (lastName != "" && lastName != null) {
    alert(`Thanks, ${firstName} ${lastName}! We're almost there.`)
  } else {
    alert("Please input a valid name.")
  }
}

let validAge = false
if (lastName) {
	const age = window.prompt("How old are you?")
  const parsedAge = parseInt(age)
	if (!isNaN(parsedAge) && parsedAge != "" && parsedAge != null) {
	  alert(`Looking fresh as ever, ${firstName} ${lastName}.`)
	  validAge = true
	} else {
	  alert("Please input a valid age.")
	}
}

let validLanguage = false
if (validAge) {
	const language = window.prompt("What programming language is your main focus of study right now?")
	if (language != "" && language != null) {
	  alert("I see...")
	  validLanguage = true
	} else {
	  alert ("Please input a valid language")
	}
}


if (validFirstName && lastName && validAge && validLanguage) {
  alert("Relax!")
}
