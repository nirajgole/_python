#
#*keyword:global is used to access a global variable and modify it
total=0
def get_total():
    global total
    total+=1
    return total;

#*keyword:nonlocal is used to access a nonlocal variable and modify it
#?usually used in nested function
def get_total2(): #parent
    total=0
    def add_total(): #child
        nonlocal total
        total+=1
        return total;
    return add_total;