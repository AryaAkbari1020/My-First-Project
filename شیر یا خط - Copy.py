import random
def play_coin_flip(): 
    score = 0
    game_on = True
    
    while game_on:
        coin_result = random.choice(["شیر", "خط"])
        user_guess = input("حدس شما چیه؟ (شیر/خط): ").strip()
        
        if user_guess == coin_result:
            score += 1
            print(f"آفرین! درست حدس زدی. امتیاز شما: {score}")
        else:
            print(f"اوه! متأسفم، اشتباه حدس زدی. سکه {coin_result} اومد.")
            print(f"بازی تموم شد. امتیاز نهایی شما: {score}")
            game_on = False
            
        if game_on:
            play_again = input("می‌خوای دوباره بازی کنی؟ (بله/خیر): ").strip()
            if play_again != "بله":
                game_on = False
                print("ممنون از بازی شما! خدانگهدار.")
