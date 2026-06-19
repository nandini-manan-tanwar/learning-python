questions=('Which animal can sleep standing up?',
          'What is the largest planet in our Solar System?',
          'Which fruit has seeds on the outside?',
          'What color do you get by mixing blue and yellow?',
          'Which bird is known for mimicking human speech?')

options=('A) Dolphin B) Horse        C) Penguin  D) Octopus',
         'A) Earth   B) Saturn       C) Jupiter  D) Neptune',
         'A) Apple   B) Strawberry   C) Orange   D) Watermelon',
         'A) Purple  B) Orange       C) Green    D) Red',
         'A) Eagle   B) Sparrow      C) Parrot   D) Owl')


answers=['B','C','B','C','C']
guesses=[]
q_no=0
score=0

for question in questions:
    print(question)
   
    for option in options [q_no]:
        print(option,end='')
    print()
    guess=(input('enter your guess (A,B,C,D)').upper()).strip()
    if guess=='A' or guess=='B' or guess=='C' or guess=='D':
        guesses.append(guess)
    else:
        guess=(input("you can enter only (A,B,C,D)").upper()).strip()
    
    
    print()
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
    q_no=q_no+1   
    
    
q_no=0  
for question in questions:
    if guesses[q_no]==answers[q_no]:
        score=score+1
 
    q_no=q_no+1

print(f'your score={score}')

 
        


