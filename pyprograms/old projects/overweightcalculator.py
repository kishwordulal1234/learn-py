price = float(input("inter the price:"))
discount = float(input("inter the discount amoutn:"))
discount_price = price * discount / 100
final_price = price - discount_price
print(f"the discounted amount = {final_price} ")