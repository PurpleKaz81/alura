import re


class URLExtractor:
    """A class to extract and manipulate URLs containing currency conversion data from bytebank.com."""

    def __init__(self, url, quantity):
        self.url = self.sanitize_url(url.format(quantidade=quantity))
        self.validate_url()
        self.url_parts = self.url.split("?")
        self.parameters = self.extract_parameters()
        self.conversion_rate = {"real": 4.79, "dolar": 1}

    def __str__(self):
        """Return a string representation of the URL and its parameters."""
        parameter_keys = list(self.parameters.keys())
        if len(parameter_keys) > 2:
            first_two_parameter_keys_str = ", ".join(parameter_keys[:-1])
            last_parameter_str = parameter_keys[-1]
            parameters_str = f"{first_two_parameter_keys_str}, and {last_parameter_str}"
        elif len(parameter_keys) == 2:
            parameters_str = f"{parameter_keys[0]} and {parameter_keys[1]}"
        else:
            parameters_str = parameter_keys[0] if parameter_keys else ""
        return f"{self.url} has parameters {parameters_str}. The base is {self.get_url_base()}"

    def __len__(self):
        """Return the length of the URL."""
        return len(self.url)

    def __eq__(self, other):
        """Check the equality of this URL with another URL."""
        return self.url == other.url

    @staticmethod
    def sanitize_url(url):
        """Remove unwanted characters from the URL."""
        return url.replace(" ", "").strip() if isinstance(url, str) else ""

    @staticmethod
    def is_valid_url(url):
        """Check if the URL is valid and contains all required components."""
        default_url = re.compile(
            '(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        required_params = ["quantidade", "moedaOrigem", "moedaDestino"]

        return bool(default_url.match(url)) and all(
            param in url for param in required_params)

    @staticmethod
    def format_value_BRL(value):
        """Format a value as BRL currency."""
        return f"R${value:.2f}"

    @staticmethod
    def format_value_USD(value):
        """Format a value as USD currency."""
        return f"US${value:.2f}"

    def validate_url(self):
        """Verify that the input URL is valid and contains all required components."""
        if not self.url:
            raise ValueError("The URL is empty.")
        elif not self.is_valid_url(self.url):
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
        param_dict = {
            param.split("=")[0]: param.split("=")[1]
            for param in parameters
        }
        # convert quantity to integer
        param_dict["quantidade"] = float(param_dict["quantidade"])
        return param_dict

    def get_parameter(self, key):
        """Get the value of a specific parameter in the URL."""
        return self.parameters.get(key)

    def print_with_newline(self, *args):
        """Print the arguments, ending with a newline character."""
        print(*args, end="\n\n")

    def calculate_conversion(self):
        """Calculate the conversion of one currency to another based on the parameters."""
        origin = self.parameters.get("moedaOrigem")
        destination = self.parameters.get("moedaDestino")
        quantity = self.parameters.get("quantidade")

        if origin not in self.conversion_rate or destination not in self.conversion_rate:
            raise ValueError("Currency not supported.")

        origin_rate = self.conversion_rate[origin]
        destination_rate = self.conversion_rate[destination]
        return (quantity / origin_rate) * destination_rate
