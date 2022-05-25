from Car import Car
import HashTable


table = HashTable.HashTable(10)
car = Car(12, "red")
car2 = Car(12, "red")

print(hash(car))
print(hash(car2))

dict = {car: 1, car2: 2}
print(dict)

