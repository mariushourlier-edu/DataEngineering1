def remove_spaces(st):
    st2 = ""
    for i in range (len(st)):
        if st[i] != " "  or (i > 0 and st[i-1] != " "):
            st2 += st[i]
    return st2        

def str_intelligible(st):
    isOpenBalise = False
    isClosedBalise = True
    st_sans_balises = ""
    st_sans_char_spec = ""
    isOpenSpec = False
    isClosedSpec = True 

    i = 0
    while i != len(st):
        while i != len(st) and isClosedBalise and (st[i] != "<"):
            st_sans_balises += st[i]
            i += 1 
        isOpenBalise = True 
        isClosedBalise = False
        while i != len(st) and (isClosedBalise == False) and (st[i] != ">"):
            i += 1
        isOpenBalise = False    
        isClosedBalise = True

    st_sans_char_spec = st_sans_balises

    i = 0
    while i != len(st_sans_balises):
        while i != len(st_sans_balises) and isClosedSpec and (st_sans_balises[i] != "&"):
            st_sans_char_spec += st_sans_balises[i]
            i += 1
        isOpenSpec = True 
        isClosedSpec = False
        i += 1
        while i != len(st_sans_balises) and (isClosedSpec == False) and (st_sans_balises[i] != ";"):
            i += 1 
        isOpenSpec = False    
        isClosedSpec = True    

    return st_sans_char_spec


def recup_domaine(st):
    first_dot = False
    second_dot = False
    i = 0
    st_result = ""
    while (i != len(st)) or (second_dot == False):
        while (i != len(st)) and (first_dot == False) st[i] != ".":
            i += 1
        first_dot = True
        i += 1
        while (i != len(st)) and (second_dot == False) st[i] != ".":
            st2 += st[i]
            i += 1
    return st2        
