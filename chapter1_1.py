#3.8练习
from pprint import pprint

years_list = [1980,1981,1982,1983,1984,1985]
thing = ['mozzarella','cinderella','salmonella']
surprise = ['Groucho','Chico','Harpo']
thing = [name.capitalize() for name in thing]
print(thing)
H = ''.join(surprise[2:3])
print(H[::-1].lower().capitalize())
e2f = {'dog' : 'chien', 'cat' :'chat', 'walrus' : 'morse'}
pprint(e2f['walrus'])
f2e = dict()
for key,values in e2f.items():
    f2e[values] = key
pprint(f2e)
e2f_set = {value for value in e2f.values()}
other_set = {'chat','norese'}
pprint(e2f_set)
pprint(e2f_set - other_set)
life = {'animals':{'cats':['Henri','Grumpy','Lucy'],'octopi': {},'emus':{}},'plants':{},'others':{}}
pprint(list(life.keys()))
pprint(list(life['animals'].keys()))
cat_list = life['animals']
pprint(cat_list['cats'])
print('------------------------------------------------------------------------')
# 4.13 练习
guess_me = 7
if guess_me > 7:
    print('too high')
elif guess_me == 7:
    print('just right')
else:
    print('too low')
start = 1
while start <= guess_me:
    print('too low')
    if start == guess_me:
        print('found it!')
        break
    elif start > guess_me:
        print('oops')
        break
    start += 1
print([num for num in range(10) if num%2 == 0])
squares = {keys: keys**2 for keys in range(10)}
print(squares)
def test(func):
    def new_function(*args,**kwargs):
        print('start')
        result = func(*args,**kwargs)
        print('result:',result)
        print('end')
        return result
    return new_function
@test
def add_ints(a,b):
    return a+b
add_ints(3,4)
# class OopsException(Exception):
#     print('Caught an oops')
# words = ['hello','WO']
# for word in words:
#     if word.isupper():
#         raise OopsException(word)
titles = ['Creature of Habit','Crewel Fate']
plots = ['a nun turns into a monster','A haunted yarn shop']
movies = dict(zip(titles,plots))
pprint(movies)