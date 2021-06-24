def Sequence(user):
    
    my_list = []
 
    for i in user:
        if i in ["("]:
            my_list.append(i)
        else:
 
            if not my_list:
                return False
            current = my_list.pop()
            if current == '(':
                if i != ")":
                    return False

    if my_list:
        return False
    return True
 
 
# Driver Code
if __name__ == "__main__":
    user = "()()"

    if Sequence(user):
        print("Balanced")
    else:
        print("Not Balanced")

if __name__ == "__main__":
    user = "()("

    if Sequence(user):
        print("Balanced")
    else:
        print("Not Balanced")