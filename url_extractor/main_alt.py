def print_with_newline(*args):
    print(*args, end="\n\n")


def extract_parameters(url_parameters):
    source, target, amount = None, None, None
    and_params = url_parameters.split("&")
    for param in and_params:
        key_value = param.split("=", maxsplit=1)
        key = key_value[0]
        value = key_value[1] if len(key_value) > 1 else None
        if key == "source":
            source = value
        elif key == "target":
            if "|" in value:
                target, amount = value.split("|", maxsplit=1)
            else:
                target = value
        elif key == "amount" and not amount:
            amount = value

    source = source.split("&")[0] if source else None
    target = target.split("|")[0] if target else None
    amount = amount.split("=")[1] if amount else None

    return source, target, amount


url = "https://gimmemoneybank.com/currency_conversion?source=USD&target=EUR|amount=100"
url_length = len(url)

slash_index = url.find("/", url.find(".com") + len(".com"))
question_mark_index = url.find("?")
ampersand_index = url.find("&")
pipe_index = url.find("|")

url_base = url[:slash_index]
all_indices = f"Slash: {slash_index}, Question mark: {question_mark_index}, Ampersand: {ampersand_index}, and Pipe: {pipe_index}"
functionality = " ".join(url[slash_index + 1:question_mark_index].split('_'))
url_parameters = url[question_mark_index + 1:]

source, target, amount = extract_parameters(url_parameters)

operation = f"Source: {source} | Target: {target} | Amount: {amount}"

print_with_newline(f"The url is {url_length} characters long.")
print_with_newline("Indices:", all_indices)
print_with_newline("Base URL:", url_base)
print_with_newline("Operation:", functionality)
print_with_newline("Parameters:", url_parameters)
print_with_newline("Operation:", operation)
