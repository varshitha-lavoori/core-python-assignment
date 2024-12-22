cart=eval(input())
def total_prize(cart):
    total = sum(cart.values())
    if not cart:
        print("Cart is Empty")
    elif len(cart)>5:
        discount=total*0.1
        total-=discount
        print(int(total))
    else:
        print(total)
total_prize(cart)

