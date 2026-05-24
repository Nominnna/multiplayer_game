# import mypackage as mymodule
# result = mymodule.greet("Тамир")
# print(result)

# from mypackage import add

# results = add(5, 3)
# print(results)

# import mypackage as mathmodule
# result = mathmodule.square(5)
# print(result)

# from mypackage import greet, add, square

# print(greet("Тамир")) 
# print(add(5, 3))
# print(square(5))      


from mypackage import say_hello , increase_number, decrease_number
name = "Тамир"
number = 5
say_hello(name)
score = increase_number(number)
print("Score after increase:", score)
score = decrease_number(number)
print("Score after decrease:", score)