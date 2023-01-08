#how to use functions with outputs

def format_name(f_name,l_name):
    """Take a first and last name and format it to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "no valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"result: {formated_f_name}  {formated_l_name}"  
print(format_name(input("what is your first name ?"),input("what is your last name")))