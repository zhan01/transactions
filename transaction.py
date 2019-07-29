class Customer:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def send(self, customer, amount):
        self.balance -= amount
        customer.balance += amount



alice = Customer('Alice', 100)
bob = Customer('Bob', 200) 

assert alice.balance == 100 
assert bob.balance == 200 
alice.send(bob, 10) 
assert alice.balance == 90 
assert bob.balance == 210 
bob.send(alice, 100) 
assert alice.balance == 190 
assert bob.balance == 110

charlie = Customer('Charlie', 250)
charlie.send(alice, 90)
charlie.send(bob, 100)
print("Charlie balance: ",charlie.balance)
print("Alice balance: ",alice.balance)
print("Bob balance: ",bob.balance)
assert alice.balance == 280
assert bob.balance == 210
assert charlie.balance == 60