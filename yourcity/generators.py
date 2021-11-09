

# Why Generators
# Generate a sequence of numbers one at a time (primitive)


# Tge old way
# def generate_even_numbers(start, end):
#     numbers = []
#     for i in range(start, end):
#         if i % 2 == 0:
#             numbers.append(i)
#     return numbers

# print(generate_even_numbers(9,100))



# def generate_even_numbers(start, end):
#     for i in range(start, end):
#         if i in range (start, end):
#             if i % 2 == 0:
#                 yield i

# even_numbers_generator = generate_even_numbers(0,100000)

# for i in even_numbers_generator:
#     print(i)


# def loop(generators):
#     while True:
#         for i, generator in enumerate(generators):
#             try:
#                 print(next(generator))
#             except StopIteration:
#                 del generators[i]



# Better variant, still synchronos


# def generate_even_numbers(start, end):
#     for i in range(start, end):
#         if i in range (start, end):
#             if i % 2 == 0:
#                 yield i

# even_numbers_generator = generate_even_numbers(0,10)
# another_even_numbers_generator = generate_even_numbers(100,110)

# def loop(generators):
#     while True:
#         if not generators:
#             return
#         for i, generator in enumerate(generators):
#             try:
#                 print(next(generator))
#             except StopIteration:
#                 del generators[i]

# loop([even_numbers_generator, another_even_numbers_generator])
# call two variants from 1 functions 😱


# yield


# def hello():
#     loop({})


# import time


# def loop(generators):
#     while True:
#         if not generators:
#             return
#         for i, generator in enumerate(generators):
#             try:
#                 print(next(generator))
#             except StopIteration:
#                 del generators[i]
