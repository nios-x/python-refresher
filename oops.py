# class Car:
#     def __init__(self, name):
#         print("Initializing Car...")
#         self.name = name
#     def __str__(self):
#         return "Car: " + self.name

# class Tesla(Car):
#     def __init__(self, name):
#         super().__init__("Tesla " + name)
#         print("Initializing Tesla...")
#     def autopilot(self):
#         return "Autopilot activated for " + self.name
# class Lambo(Car):
#     def __init__(self, name):
#         super().__init__("Lambo " + name)
#         print("Initializing Lambo...")
#     def drift(self):
#         return "Drifting with " + self.name


# class HybridCar(Tesla, Lambo):
#     def __init__(self, name):
#         Tesla.__init__(self,name)
#         Lambo.__init__(self,name)
#         print("Initializing HybridCar...")


# # x = Car("BMW")
# # y = Tesla("Model S")
# z= HybridCar("Model X")
# z.autopilot()
# z.drift()
# print(z)
# # print(x)
# # print(y)



# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius   # Public variable
#         self._radius = radius   # Protected variable
#         self.__radius = radius  # Private variable
        
#     def area(self):
#         return 3.14 * self.radius ** 2
# x = Circle(34)
# print(x.radius)      # Accessing public variable
# print(x._radius)     # Accessing protected variable (not recommended)
# # print(x.__radius)    # Accessing private variable (will raise an error)

# ## Magic Methods
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __str__(self):
#         return f"Point({self.x}, {self.y})"
    
#     def __add__(self, other):
#         if isinstance(other, Point):
#             return Point(self.x + other.x, self.y + other.y)
#         return NotImplemented
#     def __eq__(self, other):
#         if isinstance(other, Point):
#             return self.x == other.x and self.y == other.y
#         return NotImplemented

# """
# 1. __init__ - Initaialises a new instance of a class
# 2. __repr__ - Returns a string representation of the object for debugging
# 3. __str__ - Returns a user-friendly string representation of the object
# 4. __add__ - Defines behavior for the addition operator (+)
# 5. __eq__ - Defines behavior for the equality operator (==)
# 6. __sub__ - Defines behavior for the subtraction operator (-)
# 7. __mul__ - Defines behavior for the multiplication operator (*)
# 8. __truediv__ - Defines behavior for the division operator (/)
# 9. __len__ - Defines behavior for the len() function
# 10. __getitem__ - Defines behavior for indexing (e.g., obj[key])
# 11. __setitem__ - Defines behavior for setting an item (e.g., obj[key] = value)
# 12. __delitem__ - Defines behavior for deleting an item (e.g., del obj
# """

# class MyError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)

# try:
#     raise MyError("This is a custom error message.")
# except MyError as e:
#     print(f"Caught an error: {e.message}")


# # Iterators and Generators
# list1 = [1, 2, 3]
# it = iter(list1)

# print(next(it)) # Output: 1
# print(next(it))  # Output: 2
# print(next(it))  # Output: 3
# # print(next(it))  # Raises StopIteration


# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count *= 2

# for i in count_up_to(10):
#     print(i)  # Output: 1, 2, 4, 8  

# Decorators
# def my_decorator(func):
#     def wrapper():
#         print("Before the function call.")
#         func()
#         print("After the function call.")
#     return wrapper

# @my_decorator
# def happy():
#     print("Happy")

# happy()