score = input('Enter Score: ')

try:
    score = float(score)
except:
    print('Bad score')
    quit()

if float(score) < 0.0 or float(score) > 1.0:
    print('Bad score')
    quit()

if float(score) >= 0.9:
    print('A')
elif float(score) >= 0.8:
    print('B')
elif float(score) >= 0.7:
    print('C')
elif float(score) >= 0.6:
    print('D')
else:
    print('F')

