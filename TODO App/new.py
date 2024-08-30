# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()
#
# squares = [x**2 for x in range(10) if x % 2 == 0]
# print(squares)
#
# squares = [x**2 for x in range(10)]
# print(squares)
#
# squares = [x**2 for x in range(10)  if x % 2 == 0]
# print(squares)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# print (Person)

numbers = [1, 2, 3]
iterator = iter(numbers)  # Get an iterator for the list

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# print(next(iterator))  # Raises StopIteration

