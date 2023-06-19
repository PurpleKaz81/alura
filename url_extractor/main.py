def print_with_newline(*args):
    print(*args, end="\n\n")

url = "https://gimmemoneybank.com/currency_conversion?source=USD&target=EUR|amount=100"

url_length = len(url)
question_mark_index = url.find("?")
url_base = url[:question_mark_index]
url_parameters = url[question_mark_index + 1:]

print_with_newline(url_length)
print_with_newline(question_mark_index)
print_with_newline(url_base)
print_with_newline(url_parameters)
