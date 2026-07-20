import random

fruits=("apple","banana","pineapple","pear","mango")

hangman_art={0:("   ",
                "   ",
                "   ",),
            1:("  O ",
                "   ",
                "   ",),
            2:("  O ",
                " |  ",
                "   ",),
            3:("  O  ",
                "/|  ",
                "   ",),
            4:("  O  ",
                "/|\\  ",
                "   ",),
            5:("  O ",
                "/|\\  ",
                "/  ",),
            6:("   O  ",
               "  /|\\  ",
               "  / \\ ",),
            }

def display_man(wrong_guesses):
  for line in hangman_art[wrong_guesses]:
     print(line)

def display_hint(hint):
  hint=print("".join(hint))

def display_answer(answer):
  pass

def main():
  answer=random.choice(fruits)
  hint=["_"]*len(answer)
  wrong_guesses=0
  is_running=True
  while is_running:
    guessed_letter=(input('enter the letter you guessed').lower())
    display_man(wrong_guesses)
    display_hint(hint)
    
   
    for i in range(len(answer)):
          if answer[i]==guessed_letter:
             hint[i]=guessed_letter  

if __name__ == "__main__":
    main()