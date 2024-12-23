marks = eval(input())
def calculate_averages(marks):
    averages = {}
    for keys, values in marks.items():
        total = sum(values)
        avg = total / len(values)
        averages[keys] = round(avg, 2)
    return averages
def high_percent(averages):
    top = max(averages, key=averages.get)
    return top
averages = calculate_averages(marks)
print((f"Average marks:{averages}"))
top_perfromer=high_percent(averages)
print(f'Top Performer:"{top_perfromer}"')
