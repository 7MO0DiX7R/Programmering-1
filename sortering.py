def bubble(thelist):

    for _ in range(len(thelist)):
        for i in range(1, len(thelist)):
            if thelist[i] < thelist[i - 1]:

                thelist[i], thelist[i - 1] = thelist[i - 1], thelist[i]

    return thelist


sorted_list = bubble([48412, 19, 7, 261954, 3989, 384, 90421])
print(sorted_list)
