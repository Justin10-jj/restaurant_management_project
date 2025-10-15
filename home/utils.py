def calculate_discount(orginal_price,discount_percentage):
    try:
        orginal_price<0:
        raise ValueError("orginal price cannot be negative")
    if discount_percentage<0 or discount_percentage>100:
        raise ValueError("discount percentage must be between 0 qnd 100")



        discount_amount=(orginal_price*discount_percentage)/100
        final_price=orginal_price-discount_amount
        return round(final_price,2)
    ecxept (ValueError,TyoeError)as e:
    print(f"Error calculating discount:{e}")
    return 0.0