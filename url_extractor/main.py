# sourcery skip: remove-unnecessary-cast
from url_extractor import URLExtractor as Extractor

url = "https://bytebank.com/cambio?quantidade=190&moedaOrigem=real&moedaDestino=dolar"
extracted_parameters = Extractor(url)
extracted_parameters_2 = Extractor(url)
extracted_parameters.print_with_newline(f"O tamanho da URL é de {len(extracted_parameters)} caracteres.")
quantity_parameter = extracted_parameters.get_parameter("quantidade")
extracted_parameters.print_with_newline(quantity_parameter)
extracted_parameters.print_with_newline(str(extracted_parameters == extracted_parameters_2))

id_1 = str(id(extracted_parameters))
id_2 = str(id(extracted_parameters_2))

extracted_parameters.print_with_newline(id_1)
extracted_parameters.print_with_newline(id_2)

extracted_parameters.print_with_newline(id_1[5:] != id_2[5:])
