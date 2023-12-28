from playsound import playsound
import time

# Vider le terminal
CLEAR = "\033[2J"

# Retourner au debut du terminal
CLEAR_AND_RETURN = "\033[2H"

# La fonction "alarm", prend pour paramettre formel la variable "secondes", le nombre de seconde qu'il faudra
# attendre. A chaque seconde, elle vas mettre a jour le temps restant et jouer un sons a  la fin.
def alarm(secondes):
    intervalle_temps = 0
    
    print(CLEAR)
    
    while intervalle_temps < secondes:
        time.sleep(1)
        intervalle_temps += 1
        temp_restant = secondes - intervalle_temps
        minutes_restantes = temp_restant // 60
        secondes_restantes = temp_restant % 60
        
        print(f"{CLEAR_AND_RETURN}Il reste: {minutes_restantes:02d} : {secondes_restantes:02d}")
    playsound("One Piece - Drums of Liberation .mp3")
  
print(CLEAR)
print(CLEAR_AND_RETURN)    
MINUTES = input("Combien de minutes: ")

# verfifie que le nombre enter est un chiffre
while not MINUTES.isdigit():
    print(CLEAR)
    print(CLEAR_AND_RETURN)
    MINUTES = input("Veillez rentrez un chiffre (minutes): ")
    
SECONDES = input("Combien de secondes: ")

# verfifie que le nombre enter est un chiffre
while not SECONDES.isdigit():
    print(CLEAR)
    print(CLEAR_AND_RETURN)
    SECONDES = input("Veillez rentrez un chiffre (seconde): ")
 
TOTAL = (int(MINUTES) * 60) + int(SECONDES)

alarm(TOTAL)
