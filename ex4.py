import random
tries = 0
cnt_head = 0
cnt_tail = 0

name = input('Who are you?\n')
print('Hello, ',name,'!')

print("Tossing a coin...")
while tries < 3:
    tries += 1
    coin = random.randint(1, 2)
    if coin == 1:
        cnt_head += 1
        print('Heads')
    if coin == 2:
        cnt_tail += 1
        print ('Tails')
        
print("Heads: ", cnt_head, ' Tails: ', cnt_tail)

if cnt_head > cnt_tail:
    print(name,  ' won!')
else: 
    print(name, ' lost!')