serie = [1, 54, 6, 78, 9, 123, 5, 4]

def fmax(serie):
    max = None
    for i in serie:
        if max is None or i > max:
            max = i
    
    return(max)

print("Serie", serie)
print("\nMax Number:", fmax(serie))


def fmin(serie):
    min_val = None
    for i in serie:
        if min_val is None or i < min_val:
            min_val = i
    return min_val

print(fmin(serie))

def fcount(serie):
    count = 0
    for _ in serie:
        count += 1
    return count

print(fcount(serie))

def favg(serie):
    if not serie:
        return None
    
    total = 0
    count = 0
    for i in serie:
        total += i
        count += 1
    return total / count

print(favg(serie))