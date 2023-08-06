# int, int -> string
# Given integer num and base b, converts num to a string representation in base b
def convert(num, b):
    """recursive function that returns a string representing num in the base b"""
    quot = num // b
    remainder = num % b
    if remainder == 10:
        remainder = "A"
    if remainder == 11:
        remainder = "B"
    if remainder == 12:
        remainder = "C"
    if remainder == 13:
        remainder = "D"
    if remainder == 14:
        remainder = "E"
    if remainder == 15:
        remainder = "F"
    if quot == 0:
        return str(remainder)
    else:
        return str(convert(quot, b)) + str(remainder)


