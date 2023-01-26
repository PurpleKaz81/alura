let one = 1;
let stringOne = "1";
let thirty = 30;
let stringThirty = "30";
let ten = 10;
let stringTen = "10";

let test1 = (one == stringOne);
if (test1) {
  document.getElementById("test1").innerHTML =
    "The one and stringOne variables have the same value, but are not the same type.";
  console.log(
    "The one and stringOne variables have the same value, but are not the same type."
  );
} else {
  document.getElementById("test1").innerHTML =
    "The one and stringOne variables don't have the same value.";
  console.log("The one and stringOne variables don't have the same value.");
}

let test2 = (thirty === stringThirty);
if (test2) {
  document.getElementById("test2").innerHTML =
    "The thirty and stringThirty variables have the same value and type.";
  console.log(
    "The thirty and stringThirty variables have the same value and type."
  );
} else {
  document.getElementById("test2").innerHTML =
    "The thirty and stringThirty variables don't have the same type.";
  console.log(
    "The thirty and stringThirty variables don't have the same type."
  );
}

let test3 = (ten == stringTen);
if (test3) {
  document.getElementById("test3").innerHTML =
    "The ten and stringTen variables have the same value, but are not the same type.";
  console.log(
    "The ten and stringTen variables have the same value, but are not the same type."
  );
} else {
  document.getElementById("test3").innerHTML =
    "The ten and stringTen variables don't have the same value.";
  console.log("The ten and stringTen variables don't have the same value.");
}
