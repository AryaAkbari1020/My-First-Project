import time
def simple_stopwatch():
    """
    کورنومتر ساده که سه دور پنج ثانیه ای را می شمارد
    و قبل از هر دور منتظر دستور شروع کاربر می ماند.
    """
    for i in range(1, 4): 
        input(f"برای شروع دور {i} اینتر بزنید...") 
        print(f"شروع دور {i}...")
        time.sleep(5)  
        print(f"پایان دور {i}!")
    print("تمام شد! ممنون از همراهیتون. ")


simple_stopwatch()
imple_stopwatch()

