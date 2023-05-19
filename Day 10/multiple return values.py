def name(f_name, l_name):
    if f_name == "" or l_name == "":
        return f"You didn't provide any input."
    for_f_name = f_name.title()
    for_l_name = l_name.title()
    return f"Result: {for_f_name} {for_l_name}"

print(name(input("What is your first name? "),input("What is your last name? ")))
