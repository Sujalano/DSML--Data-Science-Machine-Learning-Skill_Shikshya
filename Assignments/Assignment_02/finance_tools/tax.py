def calculate_tax(base_price, tax_rate):
    tax_amount= (base_price * tax_rate)/100
    total_price= base_price+tax_amount
    return tax_amount, total_price