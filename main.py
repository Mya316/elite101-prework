import os
import sys

def main():

    print ('Welcome to the Plushie Factory Chatbot!')
    assist = input('How may I help you?')
    #i want to make a plushie (continue script) or exit (goodbye message)
name = input('What will you name your plushie? ')
age = input('Wow! ' + name + ' is such a great name! How old is ' + name + '? ')
print (name + ' is ' + age + ' years old. Got it!')
choice = input('Please choose a color for your plushie: pink, or blue? ')
if choice == 'pink':
    print ('Pink! What a lovely color for ' + name + '!')
    gender = input('Finally, is ' + name + ' a girl, or a boy? ')
    print (name + ' is a ' + age + ' year old ' + choice + ', ' + gender + ' plushie. Got it!')

elif choice == 'blue':
    print ('Blue, a nice, calm color for ' + name + '!')
    gender = input('Finally, is ' + name + ' a girl, or a boy? ')
    print ( name + ' is a ' + age + ' year old ' + choice + ', ' + gender + ' plushie. Got it!')

print ('Your plushie is complete.')
while True:
        End = input('Exit, or Restart? ')
        if End == 'Exit': 
            print ('Goodbye!')
            break
        else:
          os.execv(sys.executable, ['python'] + sys.argv)
          main()




