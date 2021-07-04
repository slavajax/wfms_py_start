name = 'John'
age = 33

# print('My name is ' + name + '. I\'m ' + str(age) + ' years old.')
print('My name is %s. I\'m %d years old.' % (name, age))
print('My name is %(name)s. I\'m %(age)d years old.' % {'name': name, 'age': age})
print('My name is %(name)s. I\'m %(age)d years old.' % {'name': name, 'age': age})

print(f'Me name is {name}. I\'m {age} years old.')
print('Title: %s, Price: %.2f' % ('Sony', 40))  # 40.00

print('My name is {}. I\'m {}'.format(name, age))
print('My name is {name}. I\'m {age}'.format(name=name, age=age))
