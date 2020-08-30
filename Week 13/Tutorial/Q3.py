import pyliststack as stack


def transfer(s,t):
    while not s.isEmpty():
        t.push(s.pop())


def recEmptyStack(s):
    if s.isEmpty():
        return s
    else:
        s.pop()
        recEmptyStack(s)


#test code
s = stack.Stack()
t = stack.Stack()

for i in range(10,60,10):
    s.push(i)


print("Before")
print('S: ', s)
print('T: ', t)


print('ewaea')
transfer(s,t)

print('eeee')
print("After")
print('S: ', s)
print('T: ', t)
