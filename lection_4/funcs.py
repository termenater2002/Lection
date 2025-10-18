treug = []
for i in range(10):
    sloy = [1]
    
    if treug != []:
        last_sloy = treug[-1]
        for j in range(1, i):
            sloy.append(last_sloy[j-1] + last_sloy[j])
        sloy.append(1)
    
    treug.append(sloy)

for sloy in treug:
    print(sloy)
   
g = 15
for i in treug:
    g = g - 1
    if g <= 9:
        g = g - 1
    if g <= 1:
        g = g - 1        
    test_sloy = ' ' * g
    for ii in i:
        test_sloy = test_sloy + str(ii) + " "
    print(test_sloy)

    