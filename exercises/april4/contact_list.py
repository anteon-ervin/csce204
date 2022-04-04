from person import Person

friend = Person("Sandra", "White", "803-454-6677")
friend.display()

friend2 = Person("Bobby", "White", "803-454-6789")
friend2.display()

people = (
    Person("Sandra", "White", "803-454-6677"),
    Person("Bobby", "White", "803-454-6677"),
    Person("Daniel", "White", "803-454-5577"),
    Person("Kimie", "White", "803-454-9977")
)

for person in people:
    person.display()