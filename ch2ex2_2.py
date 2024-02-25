#1.The volume of a sphere with radius r is 4/3πr³. What is the volume of a sphere with radius 5?
import math
r = 5
V = 4/3*math.pi*r**3
print('The volume of a sphere with radius 5 is', V)

#2.Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
cover_price = 24.95
discount = 0.4 # 40% = 0.4
new_price = cover_price * (1 - discount)
shipping = 3
next_shipping = 0.75  #75 cents = 0.75 dollars
copies = 60
book_cost = new_price * copies
shipping_cost = shipping + (next_shipping * (copies - 1))
total_cost = book_cost + shipping_cost
print('The total wholesale cost for 60 copies is: $', total_cost)
