# Write a series of conditional tests. Print a statement describing
# each test and your prediction for the results of each test. Your code
# should look something like this:
#
#-----------------------------------------------------------------------------
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
#
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
#-----------------------------------------------------------------------------
## Look closely at your results and make sure you understand why each
##   line evaluates to True or False.
## Create at least 10 tests. Have at least 5 tests evaluate to True
##   and another 5 tests evaluate to Fales.

bike = 'Honda'
print("\nIs bike == 'Honda'? I predict True.")
print(bike=='Honda')
print("\nIs bike == 'Kawasaki'? I predict False.")
print(bike=='Kawasaki')

car = 'Hyundai'
print("\nIs car == 'Hyundai'? I predict True.")
print(car=='Hyundai')
print("\nIs car == 'Honda'? I predict False.")
print(car=='Honda')

bat = 'aluminum'
print("\nIs bat == 'Aluminum'? I predict False.")
print(bat=='Alumninum')
print("\nIs bat == 'aluminum'? I predict True.")
print(bat=='aluminum')

sound = 'SOFT'
print("\nIs sound.lower() == 'soft' I predict True.")
print(sound.lower() == 'soft')
print("\nIs sound.upper() == 'soft' I predict False.")
print(sound.upper() == 'soft')

sound = 'loud'
print("\nIs sound.upper() == 'LOUD' I predict True.")
print(sound.upper() == 'LOUD')
print("\nIs sound.lower() == 'LOUD' I predict False.")
print(sound.lower() == 'LOUD')
