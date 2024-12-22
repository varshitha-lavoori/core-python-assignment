bare_fare=50
distance_fare=10
def fare_calc():
    trips=eval(input())
    tot=0
    for i,distance in enumerate(trips,start=1):
        total=0
        total+=(distance*distance_fare)+bare_fare
        print(f"Trip {i}: ${total}")
        tot+=total
    print(f"Total Fare: ${tot}")

fare_calc()



