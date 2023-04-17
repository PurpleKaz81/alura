const names = ['ana Julia', 'Caio vinícius', 'BIA silva']

const capitalizedNames = names.map((name) => name.toUpperCase())
console.log(capitalizedNames)

const defaultNames = names.map((name) =>
  name.split(' ')
    .map(word => word.slice(0, 1).toUpperCase() + word.slice(1).toLowerCase())
    .join(' ')
)

console.log(defaultNames)
