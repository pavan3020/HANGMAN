import random#to generate random word to guess
import getpass#to give the secret word input in multipalyer so the other couldn't see it
import HMstages# different stages of hangman list for better visualization

#Choosing level of guesing the word 
levelchoose=['easy','medium','hard']
while True:
	level=input("Choose level:(1:easy/2:medium/3:hard):")
	if level in ['1','2','3']:
		break
	else:
		print("Choose valid option")

#allocating hints according to chose level
if level == '3':
	hint = 1
elif level=='2':
	hint=2
else:
	hint=3
print(f"You've choosen \"🎚️ {levelchoose[int(level)-1]} level\" and you've ({hint} hints)",'💡'*hint)

while True:
	n = input("Enter 1 for multiplayer mode or enter any number to play solo: ")
	if n.isdigit():
		break
	else:
		print("Enter valid number")
#Choosing player mode {multiplayer /singe}
if n == '1':#if multimode a player(player1) enters a word player2 guesses the word
    random_word = getpass.getpass("Player 1, enter a word: ").lower()#used getpass so the secret word is not revealed
else:
    words = ["apple", "banana", "carrot","dog",'elephant','crocodile','zebra','lion']
    random_word = random.choice(words).lower()


chose = ['_' for _ in random_word]
enterchars=[]
print("\nIt's time to guess the word!\n\n🎯"," ".join(chose),"\n\nStart")
#lives(chances) are allocated by length of guessable word
lives = 6
#loop of guessing the word
while lives > 0:
    char = input("\n--------------------------\nGuess a letter: ").lower()
    enterchars.append(char)
    if char not in random_word:
        lives -= 1
        print("❌ No match!\tYou lost one life\n Your hang status:⬇️")
        print(HMstages.stages[lives])       
        
        if hint >0:
            use_hint = input("\n💡 Do you want a hint? (enter \"1:yes\" to use / hit \"enter\" to skip): ").lower()
            if use_hint == "1" or use_hint=="yes":
                hint-= 1  
                print("\nYou've used your hint\tremaining hints:",hint)
                
                while True:  
                    try:
                        h = int(input(f"Enter position to reveal (1-{len(random_word)}): "))
                        if 1 <= h <= len(random_word):
                            print("\n💡 HINT: The letter at position", h, "is:", random_word[h - 1])
                            break  # Exit loop if input is valid
                        else:
                            print("\n⚠\n️ Invalid position! Choose a number between 1 and", len(random_word))
                    except ValueError:
                        print("\n⚠️ Please enter a valid number.")
        
    else:
        for i in range(len(random_word)):
            if char == random_word[i]:
                chose[i] = char
        print("\n✅ Matched!")

    print("\nCurrent word:", " ".join(chose))
    print("\nYour guesses are :"," ".join(enterchars))


    if '_' not in chose:
        print("\n\n🎉 YOU WON! The word was:", random_word)
        break

    print("\n❤️ Remaining Lives:",lives,"❤️" * lives)#remainder of remaining lives


if lives == 0:
    print("\n💀 OH NO! You're dead. The word was:", random_word)
