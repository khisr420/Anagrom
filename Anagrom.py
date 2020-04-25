def check_data(S1, S2):
    temp = []
    ar1= S1.replace(" ", "").lower()
    ar2= S2.replace(" ", "").lower()
    
    for x in ar1:
        if x in ar2:
            temp.append(x)
        else:
            return False
    if len(temp) == len(ar2):
        print("it is anagrom")
    else:
        return False
