import ast
patients=ast.literal_eval(input("patients="))
search_item=input("search_disease=")
def matching():
    match=[patient["Name"] for patient in patients if patient["Disease"] == search_item]
    if match:
        print(f"Patients with {search_item}: {match}")
    else:
        print(f"No patients found with {search_item}")
matching()
