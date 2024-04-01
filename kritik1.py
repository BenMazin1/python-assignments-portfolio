testVals = [-1, 0, 0.25, 0.5, 0.75, 1]

for j in range (0, len(testVals)):
    currentVal = testVals[j]

    if currentVal < 0 or currentVal > 1:
        print ("Error!")
    else:
        aprox = 0
        error = 1
        i = 0
        n = 0
        while error > 0.0001:
            CurrentAprox = ((-1)**i * (currentVal**((2*i)+1)))/((2*i)+1)
            aprox = aprox + CurrentAprox
            error = (currentVal**((2*n)+1))/((2*n)+1)
            i = i+1
            n = i-1
        results = (aprox, i, error)
        print (results)