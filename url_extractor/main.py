def print_with_newline(*args):
    print(*args, end="\n\n")

url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url_parts = url.split("?")
url_base = url_parts[0]
url_parameters = url_parts[1]

parameters = url_parameters.split("&")

origin, destination, quantity = None, None, None

for param in parameters:
    key, value = param.split("=")
    if key == "moedaOrigem":
        origin = value
    elif key == "moedaDestino":
        destination = value
    elif key == "quantidade":
        quantity = value

print_with_newline("URL:", url)
print_with_newline("URL parts:", ", ".join(url_parts))
print_with_newline("URL parameters:", ", ".join(parameters))
print_with_newline("Origin currency:", origin)
print_with_newline("Destination currency:", destination)
print_with_newline("Quantity to convert:", quantity)
