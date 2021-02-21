"""
Session 0: Basic structures, functions, print, basic
"""
# a = 1
# b = 2.4
# c = 'To pouli sou'
# d = "Kolokythia toumpana"
# listA = [1, 2, 3]
# listB = [a, b, c]
# e = 'peos'
# print(1)
# print(d)
# print(e)
# print('peos')


# - Write a program that asks for your name and then says hello with your name
# - Bonus: print the length of their name
# - Bonus: If name is Batman say Nanananana
# - Bonus: Allow users of the function to define their input messages

# print('Enter your name')
# x = input('')
# print('Hello '+ x)

def say_hi(message):
  name = input(message)
  if name.lower() == 'batman':
    print('Ths manas soy to mouni re malaka Batman')
    return

  print('Hello {}'.format(name))
  print('Number of letters: {}'.format(len(name)))
  return

def Exodia():
  name1 = input ('Enter Name1: ')
  name2 = input ('Enter Name2: ')
  name3 = input ('Enter Name3: ')
  name4 = input ('Enter Name4: ')
  print('Hello baby {}, {}, {}, {}'.format(name1,name2,name3,name4))


# say_hi('Dwse mou to onoma sou ')
say_hi('What\'s your name  ')
