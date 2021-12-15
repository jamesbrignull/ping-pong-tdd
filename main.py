def ping(arr):

    number_counts = {}

    for item in arr:
        if item not in number_counts.keys():
            number_counts[item] = 1
            continue
        number_counts[item] +=1

    for key, value in number_counts.items():
        if value % 2 != 0:
            return key   

   