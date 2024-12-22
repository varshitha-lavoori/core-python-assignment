ratings=(eval(input("ratings =")))
def customer():
    count=0
    a = len(ratings)
    if not ratings:
        print("No ratings available")
    else:
        for i,rating in enumerate(ratings,start=1):
            if rating>=4 and rating<=5:
                count+=1
        perc=(count/a)*100
        print(f"Positive Feedback: {perc}%")
customer()



