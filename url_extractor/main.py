from url_extractor import URLExtractor as Extractor

url_length = len(url)
url_parts = url.split("?")
url_base = url_parts[0]
url_parameters = url_parts[1]

parameters = url_parameters.split("&")

origin, destination, quantity = None, None, None

for param in parameters:
    key, value = param.split("=")
    if key == "moedaDestino":
        destination = value
    elif key == "moedaOrigem":
        origin = value
    elif key == "quantidade":
        quantity = value

print_with_newline("URL:", url)
print_with_newline(f"URL length: {url_length} characters")
print_with_newline("URL parts:", ", ".join(url_parts))
print_with_newline("URL parameters:", ", ".join(parameters))
print_with_newline("Origin currency:", origin)
print_with_newline("Destination currency:", destination)
print_with_newline("Quantity to convert:", quantity)
