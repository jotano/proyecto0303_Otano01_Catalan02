serie = [1, 54, 6, 78, 9, 123, 5, 4]

def fmax(serie):
    max = None
    for i in serie:
        if max is None or i > max:
            max = i
    
    return(max)

print("Serie", serie)
