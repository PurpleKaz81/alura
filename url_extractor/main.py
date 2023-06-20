from url_extractor import URLExtractor as Extractor

extracted_parameters = Extractor("https://bytebank.com/cambio?quantidade=190&moedaOrigem=real&moedaDestino=dolar")
quantity_parameter = extracted_parameters.get_parameter("quantidade")
quantity = extracted_parameters.print_with_newline(quantity_parameter)

