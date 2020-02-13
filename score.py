x = float(input('Enter score:\n'))
if x > 1 or x < 0:
    print('Bad score')
else:
    if x < 0.6:
        print('F')
    if x >= 0.9:
        print('A')
    if x >= 0.8:
        print('B')
    if x >= 0.7:
        print('C')
    if x >= 0.6:
        print('D')
