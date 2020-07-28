class Ok:
	py = [3.14] # + 15 + 27

	def __init__(self, py):
		self.ok = self.py
		Ok.py.append(3 * py)

	def my(self, eye):
		#print(self.my(eye)) error
		return self.ok.pop()

	def __str__(self):
		return str(self.ok)[:4]

class Go(Ok):

	def my(self, help):
		return [help + 3, len(Ok.py)]

oh = Go(5)
Go.py = [3, 1, 4]
print(Ok.py)
oh.no = {'a': Go(9)} #k, v pair
print(oh.no['a'].ok)

print(Ok.py)
print("############################")
print(oh.py)
print(oh.my(3))


print("####grrrrR######")
print(oh.ok)
print(oh.no['just'].ok)

print(oh.ok + oh.no['just'].ok) #.ok ~ 3,1,4
print("####grrrrR######")



print(oh) ##due to string repr
print(Ok('go').my(5))
print(Ok.my(oh, 5))

print("#######")
a = Go(1)
print(a.py)
