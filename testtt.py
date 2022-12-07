def fb(n):
    output = [0,1]
    i =0
    while i<n:
        i= output[-1]+output[-2]
        output.append(i)
    print(output)


fb(10)