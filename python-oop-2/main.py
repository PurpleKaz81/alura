from products import products

print("Here's a list of all your products:", "\n")
for index, product_key in enumerate(products):
    product = products[product_key]
    print(
        f"{index + 1}) {product} - ({product.type.lower()} id: {product.id})",
        "\n")
