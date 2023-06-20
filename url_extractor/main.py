# sourcery skip: remove-unnecessary-cast
from url_extractor import URLExtractor as Extractor

url = "https://bytebank.com/cambio?quantidade={quantidade}&moedaOrigem=real&moedaDestino=dolar"
quantity = 100

extracted_parameters = Extractor(url, quantity)
extracted_parameters_2 = Extractor(url, quantity)
extracted_parameters.print_with_newline(
    f"O tamanho da URL é de {len(extracted_parameters)} caracteres.")
quantity_parameter = extracted_parameters.get_parameter("quantidade")
extracted_parameters.print_with_newline(quantity_parameter)
extracted_parameters.print_with_newline(
    str(extracted_parameters == extracted_parameters_2))

id_1 = str(id(extracted_parameters))
id_2 = str(id(extracted_parameters_2))

extracted_parameters.print_with_newline(id_1)
extracted_parameters.print_with_newline(id_2)

extracted_parameters.print_with_newline(id_1[5:] != id_2[5:])

conversion_result = extracted_parameters.calculate_conversion()
extracted_parameters.print_with_newline(
    Extractor.format_value_BRL(conversion_result))
