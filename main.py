
# docummentation 

"""_summary_

    Returns:
        _type_: _description_ : for def()
        
        return True = "User enters 'q' to exit and function returns True"
        return False = "The program runs normally and the user wants to continue converting values ​​so the program returns False."
        
        And in the event of an exception, loop over this part of the code until the user enters a correct value.

        For the rest I'll let you figure it out for yourself.

"""
# Conversion de unite1 vers unnite2

def do_conversion(unit1: str, unit2: str, facteur: float):
    value_str = input(f"Conversion {unit1} -> {unit2}. give up the value in {unit1} (or 'q' to quit) : ")
    if value_str == "q":
        return True
    try:
        value_float = float(value_str)
    except ValueError:
        print("ERROR: You must enter a numeric value!!!")
        print("(Use dots for decimals)")
        return do_conversion(unit1, unit2, facteur)
        
    convert_value = round(value_float * facteur, 2)
    print(f"The result of the conversion is : {value_float} {unit1} -> {convert_value} {unit2}")
    return False
        

while True:
    print("This programme give you possibility to do unity conversion")
    print("1- Pouces to cm")
    print("2- cm to pouce")
    choise = input("Your choise {1 or 2}: ")
    if choise == "1" or choise == "2":
        break
    print("ERROR: You must choose between 1 and 2 \n")


while True:
    if choise == "1":
        if do_conversion("pouces", "cm", 2.54):
            break
    if choise == "2":
        if do_conversion("cm", "pouces", 0.394):
            break
