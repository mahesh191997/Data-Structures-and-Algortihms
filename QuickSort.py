def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[-1]
        i = 0
        for j in range(len(x)-1):
            if(x[j]<pivot):
                x[j],x[i] = x[i], x[j]
                i += 1
        x[-1],x[i] = x[i],x[-1]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part+second_part
