
# _x = int (input("Enter a number: "))
# print(_x*5)

# l1 = []
# l1.append(34)
# l1.extend([2342,5345,34534])
# l1.insert(3,4444)
# l1.pop(0)
# l1.index(2342)
# print(l1.count(2342))
# print(l1)

# for i ,j  in enumerate(l1):
#     print(i,j)



# l1 = [ x+y  for x in range(45) for y in range(45) if (x+y)%10==0]
# print(l1)


# # Tuple 

# x = (1,2,3,4,5)
# x.count(4)
# x.index(3)

# packed_t = 1,34,55 # packed tuple
# print(packed_t)
# print(packed_t[0])

# set1 = {1,2,3,4,5}
# set1.add(34)
# set1.update([34,45,56])
# set1.remove(34)     
# print(set1)

# set2 = {3,4,5,6,7}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))


# d = {
#     1:"We are foo",
#     2:"We are bar",
#     3:"We are baz"
# }
# print(d[1])
# print(d.keys())
# print(d.values())
# print(d.items())

# with open("file.txt","w") as f:
#     f.write("Hello World")
#     f.write("\nThis is a new line")
#     f.seek(3)
#     f.write("X")


# try:
#     x = int(input("Enter a number: "))
#     print(10/x)
# except ValueError:
#     print("Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except:
#     print("An unexpected error occurred.")
# else:
#     print("Division successful.")
# finally:
#     print("This will always execute.")


# function1 = lambda x: x*5
# print(function1(10))

# print(locals())

# def func(d):
#     """its docstring"""
#     return d * 2

# print(func.__doc__)

# if(__name__ == "__main__"):
#     print("This code is running as a script.")


# import wrongmaths
# print(wrongmaths.maths.add(5, 1))
