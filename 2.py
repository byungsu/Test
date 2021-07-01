import product

def delivery(product, address):
    type = product.product_list[product]
    if type == "일반":
        return "+".join(address) + "(일)"
    if type == "편의점":
        return "@".join(address) + "(편)"
    if type == "지하철":
        return "@".join(address) + "(지)"
    if type == "KTX":
        return "=".join(address) + "(K)"
    if type == "국제":
        return "%".join(address) + "(국)"
    return ""

deli = delivery("의자", ("11AB", "22BC", "33DC"))
print(deli)
