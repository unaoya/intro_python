print('hello world')

x = 'abc'
print(x)

print(type(x))
print(len(x))

print(x[2])
print(x[1])
print(x[0])

print(x.capitalize())

myouji = '梅崎'
namae = '直也'
fullname = myouji + namae
print(myouji)
print(namae)
print(fullname)

x = 3
y = 4.0
print(x)
print(y)
print(x+y)

print(type(x))
print(type(y))
print(type(x+y))

# x=3, y=4.0
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)

#n = 100
#m = 7
n = 100, 7, 3
print(n)

n, m = 2, 3
print(n**m)

print(type(True))
x = True
y = False
print(x and y)
print(x or y)

x = 3
y = 3
print(x == y)
print(x != y)

myouji_len = len(myouji)
namae_len = len(namae)
fullname_len = len(fullname)
print('check')
print(myouji_len + namae_len == fullname_len)
print(namae_len)

print('list')
x = [1,2,3,4,5]
print(x)
print(x[4])
print(x[1:3])
print(type(x))
print(len(x))
x.append(3)
print(x)
print(3 in x)
print(7 in x)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(8 in primes)
print(primes[2] + primes[4])

x = 2
if x > 0:
    print('positive')
elif x < 0:
    print('negative')
else:
    print('zero')

c = 1
while c < 10.1:
    print(c)
    c = c + 1

c = 1
goukei = 0
while c < 101:
    goukei = goukei + c
    c = c + 1
print(goukei)

n = 3
for i in range(3,8):
    print(i)
    print('hello')

x = 'abcde'
for i in x:
    print(i)

for i in range(1,31):
    if (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

def hello(n):
    hellos = list()
    for i in range(n):
        hellos.append('hello')
    return hellos
print(hello(5))

n = 5
for i in hello(n):
    print(i)

def is_prime(n):
    res = True
    for i in range(2,n):
        if n % i == 0:
            res = res and False
    return res
print('check')
for i in range(2,10):
    print(is_prime(i))

primes = list()
n = 2
while len(primes) < 100:
    if is_prime(n):
        primes.append(n)
    n = n + 1
print(primes)
print(sum(primes))


class Person():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def introduction(self):
        print('私は' + self.name + 'です。身長は' +
              str(self.height) + 'です。')

    def bmi(self):
        return self.height / (self.weight ** 2)

a = Person('山田', 170, 60)
print(a.name)
print(a.height)
a.introduction()
print(a.bmi())


class Stats():
    def __init__(self, names, scores):
        self.names = names
        self.scores = scores

    def mean(self):
        return sum(self.scores) / len(self.scores)

#    def var(self):
#        return sum(self.scores ** 2)/len(self.scores) - self.mean() ** 2

    def maximun(self):
        M = max(self.scores)
        ids = [i for i in range(len(self.scores)) if self.scores[i] == M]
        return M, [self.names[i] for i in ids]

    def minimun(self):
        m = min(self.scores)
        ids = [i for i in range(len(self.scores)) if self.scores[i] == m]
        return m, [self.names[i] for i in ids]

sugaku = Stats(['A', 'B', 'C'], [80, 70, 60])
print(sugaku.mean())
print(sugaku.maximun())
print(sugaku.minimun())

eigo = Stats(['A', 'B', 'C', 'D'],
             [100, 100, 90, 90])
print(eigo.maximun())
print(eigo.minimun())
