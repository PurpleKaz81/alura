const clientList = () => {
  return fetch("http://localhost:3000/profile")
  .then (res => {
    return res.json()
  })
}

export const clientService = {
  clientList
}
