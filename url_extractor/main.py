from url_extractor import URLExtractor as Extractor

url_extraction = Extractor("https://bytebank.com/cambio?quantidade=190&moedaOrigem=real&moedaDestino=dolar")
quantity_parameter = url_extraction.get_parameter("quantidade")
quantity = url_extraction.print_with_newline(quantity_parameter)

origin_parameter = url_extraction.get_parameter("moedaOrigem")
origin = url_extraction.print_with_newline(origin_parameter.title())
