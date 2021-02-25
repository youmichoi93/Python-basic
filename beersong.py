word = 'bottles'
for beer_num in range(99,0,-1):
    print(beer_num,word,'of beer on the wall.')
    print(beer_num,'of beer.')
    print('Take on down.')
    print('pass it around.')
    if beer_num == 1:
        print('No more bottle of beer in thee world.')
    else:
        new_num = beer_num -1
        if new_num == 1:
             word = 'bottle'
        print(new_num,word,'of beer on then wall.')
print()


range(5)
list(range(5))
list(range(5,10))
list(range(0,10,2))
list(range(10,0,-2))
list(range(10,0,2))
list(range(99,0,-1))



temps = [32.0,212.0,0.0,81.6,100.0,45.3]
words = ['hello','word']
car_details = ['Toyota','RAV4',2.2,60807]
everything = [prices, temps, words,car_details]
odds_and_ends = [[1,2,3],['a','b','c'],['one','two','three']]