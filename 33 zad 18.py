import random
def bull_compare(number,user_guess): #Modul do sprawdzania bykow
    bull =0
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            bull+=1


    return bull
def cow_compare(number,user_guess):#Modul do sprawdzania krow
    q = list(number)
    a = list(user_guess)
    #print('to jest lista podana przez komputer', q)
    #print('to jest lista podana przez uzytkownika', a)
    cow = 0
    for w in q:
        if w in a:
            cow += 1
    return cow
if __name__=='__main__':#Glowny program
    playing=True
    number = str(random.randint(1001,9999))
    print('Liczba losowa podana przez komputer',number)
    guesses = 0#Pisanie za ktorym razem sie trafilo

    while playing:
        user_guess = input('give me your best guess!')
        if user_guess == "exit":
            break
        bullcount=bull_compare(number,user_guess)
        cow1=cow_compare(number,user_guess)
        guesses+=1
        print("You have " + str(bullcount) + " bull" )
        if bullcount!=4:
            print('WOOW! ZDOBYLES TYLE KROW ' +str(cow1))
        if bullcount==4:
            playing=False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
            break
        else:
            print("Your guess isn't quite right, try again.")


#ponizej komendy do testow
print('liczba krow',cow1)
#print('liczba bykow',cowbull[1])
#print('liczba krow',cowbull[0])
#cowbullcount = cowbull



