pets = ['dog', 
        'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
cnt = 0
while 'cat' in pets:
    pets.remove('cat')
    cnt+=1
    print("removing #", cnt, ' cat.')

print(pets)