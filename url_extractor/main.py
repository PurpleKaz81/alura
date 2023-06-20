from url_extractor import URLExtractor as Extractor

url = "https://bytebank.com/cambio?quantidade=190&moedaOrigem=real&moedaDestino=dolar"
extracted_parameters = Extractor(url)
extracted_parameters.print_with_newline(f"O tamanho da URL é de {len(extracted_parameters)} caracteres.")
quantity_parameter = extracted_parameters.get_parameter("quantidade")
quantity = extracted_parameters.print_with_newline(quantity_parameter)
print(extracted_parameters)
