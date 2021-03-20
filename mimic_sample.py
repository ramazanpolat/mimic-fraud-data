from mimic import Mimic, Person, Number

for ix, customer in enumerate(Mimic.generate(count=100, skip_ratio=0.1)):
    customer.id = ix
    customer.fname = Person.first_name()
    customer.lname = Person.last_name()
    customer.username = Person.username(first_name=customer.fname, last_name=customer.lname)
    customer.email = Person.email(first_name=customer.fname, last_name=customer.lname)
    customer.age = Number.between(18, 70)

    # customer.city = City.name()

    print(customer)
    for order in Mimic.generate(count=3, skip_ratio=0.5):
        order.customer_id = customer.id
        print('\t', order)
