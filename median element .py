def median(thelist):
    median = 0
    sortedlist = sorted(thelist)
    lengthofthelist = len(sortedlist)
    centerofthelist = lengthofthelist / 2
    if len(sortedlist) == 1:
        for value in sortedlist:
            median += value
        return median

    elif len(sortedlist) % 2 == 0:
        temp = 0.0
        medianparties = []
        medianparties = sortedlist[centerofthelist -1 : centerofthelist +1 ]
        for value in medianparties:
            temp += value
            median = temp / 2
        return median

    else:
        medianpart = []
        medianpart = [sortedlist[centerofthelist]]
        for value in medianpart:
            median = value
        return median
