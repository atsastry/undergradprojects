# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in):
    if str_in == "":
        return []
    if len(str_in) == 1:
        return [str_in]
    newL = []
    for i in range(len(str_in)):
        new_str = str_in[0:i] + str_in[i + 1:]
        res = perm_gen_lex(new_str)
        for item in res:
            perm = str_in[i] + item
            newL.append(perm)
    return newL
