
import pyperclip, cal
numerator = int(input(" what is the numerator"))
denomanater = int(input("what is the denomanater"))
ans = int(numerator) / int(denomanater)
pyperclip.copy(str(ans))
print(str(ans)+" has been copied to clipboard")
input("keep going? (enter)")



frc = float(ans)
num = float(input("multipled by?"))
print("calculating")
anss = num * frc
pyperclip.copy(anss)
print(str(anss)+" has been copied to clipboard") 
