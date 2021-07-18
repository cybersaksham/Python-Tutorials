import pickle

cars = ["BMW", "MARUTI SUZUKI", "AUDI", "BUGGATI"]
file = "mycar.pkl"
fileobj = open(file, 'wb')
pickle.dump(cars, fileobj)
fileobj.close()

fileobj2 = open(file, 'rb')
mycar = pickle.load(fileobj2)
print(mycar)
fileobj2.close()
