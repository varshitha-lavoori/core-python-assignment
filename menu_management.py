initial_menu=eval(input())
item=input("add_item=").strip('"')
item1=input("remove_item=").strip('"')
item2=input("check_item=").strip('"')
def add_items(initial_menu,item):
    initial_menu.append(item)

def remove_item(initial_menu,item1):
    if item1  in initial_menu:
        initial_menu.remove(item1)
    else:
        print("Removal does not exist.")
def check_item(initial_menu,item2):
    if item2 in initial_menu:
        print(f'Availability:"{item2}" is available')

add_items(initial_menu,item)
remove_item(initial_menu,item1)
check_item(initial_menu,item2)
print(f"Updated menu:{initial_menu}")
