
# From input:
# 7: 487 offset by 54
# 3: 421 offset by 23
# 1: 41 offset by 13
# 2: 37 offset by 17
# 6: 29 offset by 52
# 0: 23 offset by 0
# 4: 17 offset by 40
# 5: 19 offset by 42
# 8: 13 offset by 67

constraints = [
    lambda t: (t + 54) % 487 == 0,
    lambda t: (t + 23) % 421 == 0,
    lambda t: (t + 13) % 41 == 0,
    lambda t: (t + 17) % 37 == 0,
    lambda t: (t + 52) % 29 == 0,
    lambda t: (t + 0) % 23 == 0,
    lambda t: (t + 40) % 17 == 0,
    lambda t: (t + 42) % 19 == 0,
    lambda t: (t + 67) % 13 == 0,
]

found = []
diff = 0
lastFound = 9763809 # start at zero
for i in range(487 - 54 , 10000000, 487):
    #if (i + 54) % 487 == 0 and (i + 23) % 421 == 0:
    if constraints[0](i) and constraints[1](i):
        lastFound  = i
        #print(f"{i} - 54 for 487")
        #print(f"{i} - 23 for 421")
        found.append(i)
        if (len(found) >= 2):
            diff = found[1]-found[0]
            print(f"Diff: {found[1]-found[0]}")
            break

# New diff: 205027
# t: 537594  -  2 contstraints passed
# New diff: 8406107
# t: 9763809  -  3 contstraints passed
startConstraints = 3
for currentConstraintsCount in range(startConstraints, len(constraints)):
    found = []
    
    for t in range(lastFound, 200000000000000, diff):
        currentConstraintsPassed = True
        for i in range(currentConstraintsCount):
            currentConstraintsPassed &= constraints[i](t)
        if currentConstraintsPassed:
            # Get the diff from the previous
            if currentConstraintsCount == len(constraints):
                # We found it!
                print("###############")
                print(f"Timestamp: {t}")
                print(f"Constraints passed: {currentConstraintsCount}")
            found.append(t)
            if len(found) >= 2:
                diff = found[1]-found[0]
                print(f"New diff: {diff}")
                print(f"t: {t}  -  {currentConstraintsCount} contstraints passed")
                break
        else:
            #print(f"Failed to pass {currentConstraintsCount} constraints")
            pass

    if len(found) < 2:
        # something went wrong, couldn't find a difference that matched all the given contstraints
        print(f"Last t found: {found[-1]}")
        break
            
                



# # use diff to create a new step!
# found = []
# for i in range(lastFound, 100000000, diff):

#     if (i + 54) % 487 == 0 and (i + 23) % 421 == 0:
#         print(f"{i} - 54 for 487")
#         print(f"{i} - 23 for 421")
#         #found.append(i)