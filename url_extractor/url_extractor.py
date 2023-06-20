class URLExtractor:
    origin, destination, amount = None, None, None

    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()
        self.url_parts = self.url.split("?")
        self.parameters = self.extract_parameters()

    def __len__(self):
        return len(self.url)

    def sanitize_url(self, url):
        return url.replace(" ", "").strip()

    def validate_url(self):
        if not self.url:
            print("The URL is empty.")
            raise ValueError("The URL is empty.")

    def get_url_base(self):
        return self.url_parts[0]

    def get_url_parameters(self):
        return self.url_parts[1]

    def extract_parameters(self):
        url_parameters = self.get_url_parameters()
        parameters = url_parameters.split("&")
        parameters_dict = {}
        for param in parameters:
            key, value = param.split("=")
            parameters_dict[key] = value
        return parameters_dict

    def get_parameter(self, key):
        return self.parameters.get(key, None)

    def print_with_newline(self, *args):
        print(*args, end="\n\n")

url_extractor = URLExtractor("https://bytebank.com/cambio?quantidade=190&moedaOrigem=real&moedaDestino=dolar")
amount_value = url_extractor.get_parameter("quantidade")
url_extractor.print_with_newline(amount_value)
