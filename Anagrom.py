def check_data(ar1, ar2):
    temp = []
    for x in ar1:
        if x in ar2:
            temp.append(x)
    if len(temp) == len(ar1):
        print("it is anagrom")
    else:
        return False
