import re


class URLExtractor:
    """A class to extract and manipulate URLs containing currency conversion data from bytebank.com."""
    origin, destination, amount = None, None, None

    def __init__(self, url):
        """Initialize the URLExtractor object and extract the parameters of the input URL."""
        self.url = self.sanitize_url(url)
        self.validate_url()
        self.url_parts = self.url.split("?")
        self.parameters = self.extract_parameters()

    def sanitize_url(self, url):
        """Remove unwanted characters from the URL."""
        return url.replace(" ", "").strip() if type(url) == str else ""

    def is_valid_url(self, url):
        """Check if the URL is valid and contains all required components."""
        default_url = re.compile(
            '(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

        return bool(
            default_url.match(url) and all(
                param in url
                for param in ["quantidade", "moedaOrigem", "moedaDestino"]))

    def validate_url(self):
        """Verify that the input URL is valid and contains all required components."""
        if not self.url:
            print("The URL is empty.")
            raise ValueError("The URL is empty.")
        elif not self.is_valid_url(self.url):
            print("The URL is not valid.")
            raise ValueError("The URL is not valid.")

    def get_url_base(self):
        """Return the base URL without parameters."""
        return self.url_parts[0]

    def get_url_parameters(self):
        """Return the URL parameters as a single string."""
        return self.url_parts[1]

    def extract_parameters(self):
        """Extract the parameters from the URL as a dictionary."""
        url_parameters = self.get_url_parameters()
        parameters = url_parameters.split("&")
        parameters_dict = {}
        for param in parameters:
            key, value = param.split("=")
            parameters_dict[key] = value
        return parameters_dict

    def get_parameter(self, key):
        """Get the value of a specific parameter in the URL."""
        return self.parameters.get(key, None)

    def print_with_newline(self, *args):
        """Print the arguments, ending with a newline character."""
        print(*args, end="\n")
