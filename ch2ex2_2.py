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

#3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
start_time = (6*60 + 52)*60
easy_time = (8*60 + 15)*2
tempo_time = (7*60 + 12)*3
breakfast_hour = (start_time + easy_time + tempo_time)/(60*60)
breakfast_minute  = (breakfast_hour - int(breakfast_hour))*60
print('Time returned: ', int(breakfast_hour), ':', int(breakfast_minute))
