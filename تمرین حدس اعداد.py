import random

secret_number=random.randint(1,9)
guess=None
attempts=0

print( "حدس بزنيد عددي بين 1تا 9")

while guess!=secret_number:
    
    guess=int(input("حدس شما:"))
    attempts+=1
    if guess<secret_number:
        print("حدس شما اشتباه است")
else:
      ("guess>secret_number:")
      print("تبريک بچه خوشگل زدي تو هدف")

print(f"بار حدس زديد {attempts}شما")
