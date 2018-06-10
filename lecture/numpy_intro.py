import numpy as np

a = np.array([0,1,2,3])
print(a)
print(a.ndim, a.shape)

b = np.array([[0,1,2],[3,4,5]])
print(b)
print(b.ndim, b.shape)

d = np.array([[1,4],[2,5],[3,6]])
print(d)
print(d.ndim, d.shape)

e = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(e)
print(e.ndim, e.shape)

a = np.arange(10)
print(a)
b = np.arange(1,9,2)
print(b)
c = np.linspace(0,1,6)
print(c)
d = np.linspace(0,1,6, endpoint=False)
print(d)

a = np.arange(10)
print(a)
print(a[0])
print(a[2])
print(a[-1])
print(a[2:9])
print(a[2:9:3])
print(a[::-1])
print(a[2:9][::-1])

print(a%3==0)
print(a[a%3==0])
a[a%3==0] = 1
print(a)

idx = np.array([[3,4],[9,7]])
print(a[idx])

a = np.array([[1,2],[3,4]])
print(a[0,1])

# print(np.arange(0,51,10))
#print(np.arange(0,51,10)[:,np.newaxis])
#print(np.arange(6))
#print(np.arange(6 + np.arange(0,51,10)[:,np.newaxis]))

a = np.random.rand(4)
print(a)

x = np.random.normal(loc=0, scale=1, size=10)
print(x)

a = np.array([[1,2],[3,4]])
b = np.array([[1,0],[0,-1]])
print(a)
print(a.transpose())
print(np.linalg.inv(a))

print(a+b)
print(a*b)
print(np.dot(a,b))