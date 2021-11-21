##-- Primitive Combinators --##

def I_combinator(string):
    """Ix = x"""
    return string

def K_combinator(string):
    """Kxy = x"""
    if type(encoding(string)[0]) == str:
        return encoding(string)[0]
    else:
        return encoding(encoding(string)[0])

def B_combinator(string):
    """Bxyz = x(yz)"""
    l = encoding(string)
    return encoding([l[0],[l[1],l[2]]])

def C_combinator(string):
    """Cxyz = xzy"""
    l = encoding(string)
    return encoding([l[0],l[2],l[1]])
    
def W_combinator(string):
    """Wxy = xyy"""
    l = encoding(string)
    return encoding([l[0],l[1],l[1]])

def S_combinator(string):
    """Sxyz = xz(yz)"""
    l = encoding(string)
    return encoding([l[0],l[2],[l[1],l[2]]])

def Y_combinator(string):
    """Yx = B(WI)(BWB)x"""
    l = encoding(string)
    return B_combinator("(WI)(BWB)" + string)

def M_combinator(string):
    """Mx = xx"""
    return string + string

def F_combinator(string):
    """Fxy = y"""
    if type(encoding(string)[1]) == str:
        return encoding(string)[1]
    else:
        return encoding(encoding(string)[1])
    
##--                       --##

##-- Functions --##

def parenthese_match(string):
    """take from string until matching close parenthese found.
    string should start with the ( that is to be to matched."""
    
    open_parentheses = 0
    close_parentheses = 0
    
    index = 0
    count = 0
    
    for char in string:
        count += 1
        
        if char == "(":
            open_parentheses += 1
            
        elif char == ")":
            close_parentheses += 1
            
            if open_parentheses == close_parentheses:
                index += count
                break
                
    if index == 0:
        print("Parse error. Trailing close parentheses not found.")
        return
    
    else:
        return string[0:index]
    
def encoding(data):
    """CL string to list OR CL list to string"""
    
    if type(data) == str:
        d = data 
        _list = []
        
        while len(d) > 0:
            if d[0] == "(":
                p = parenthese_match(d) 
                _list.append(encoding(p[1:-1])) 
                d = d[len(p):]
                
            elif d[0] == ")":
                d = d[1:]
                                
            else:
                _list.append(d[0])
                d = d[1:]
        
        if len(_list) == 1 and type(_list[0]) == list:
            return _list[0]
        
        else:
            return _list
        
    elif type(data) == list:
        string = ""
        
        for i in data:
            if type(i) == str:
                string += i
            else:
                string += "("
                string += encoding(i)
                string += ")"
        
        return string 
        
    else:
        return f"Type Error. Got: {type(data)}, Expected 'str' or 'list'"
    
def evaluate(string):
    cl_list = encoding(string)
    
    while type(cl_list[0]) == list: # strip leading parentheses
        cl_list = [i for i in cl_list[0]] + cl_list[1:]
    
    # "X": (function, arg_num)
    _map = {"I": (I_combinator,1), "K": (K_combinator,2), "B": (B_combinator,3), "C": (C_combinator,3), 
            "W": (W_combinator,2), "S": (S_combinator,3), "Y": (Y_combinator,1), "M": (M_combinator,1)}
    
    combinator_return = _map[cl_list[0]][0](encoding(cl_list[1:(_map[cl_list[0]][1]+1)]))
    tail = encoding(cl_list[(_map[cl_list[0]][1]+1):])
    
    return combinator_return + tail

def recur(string,print_steps=False,write_steps=False):
    steps = [string]

    while True:
        try:
            ns = evaluate(string)
            steps.append(ns)
            string = ns
                
            # cycle
            if len(set(steps)) != len(steps) : 
                break
            
            # no cycle
            else: 
                pass
            
        except:
            break
    
    if print_steps:
        for i in steps:
            print(i)
            
    if write_steps:
        file = input("filename : ")
        
        with open(file + ".txt", "w") as f:
            for i in steps:
                f.write(i)
                f.write("\n")
        
    return steps[-1]

##--           --##
