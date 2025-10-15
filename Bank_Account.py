class BAnkAccount:
    def __init__(self,account_number,initial_balance,pin):
        self.account_number = account_number
        self.balance = initail_balance
        seld.pin = pin

 
    def deposit(self, amount):
        if amount > 0:
            self. balance += amount
            print(f"\n{amount} تومان به حساب شما واریز شد. موجودی جدید: {self.balance} تومان.")
            
        else:
            print("\nمقدار واریزی باید مثبت باشد.")
            def withdraw(self, amount, entered_pin):
     if entered_pin != self.pin:
            print("رمز وارد شده اشتباه است.")
            return

        if amount <= 0:
            print("مبلغ برداشتی باید مثبت باشد.")
            return

        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} تومان از حساب شما کسر شد. موجودی جدید: {self.balance} تومان.")
        else:
            print(f"موجودی کافی نیست! شما می‌توانید حداکثر {self.balance} تومان برداشت کنید.")

    def check_balance(self, entered_pin):
        if entered_pin != self.pin:
            print("رمز وارد شده اشتباه است.")
            return
        print(f"موجودی فعلی حساب شما: {self.balance} تومان.")

# مثال استفاده:
my_account = BankAccount("123456789", 1000, "1234")

my_account.deposit(500)
my_account.withdraw(200, "1234")
my_account.withdraw(1000, "0000") # رمز اشتباه
my_account.withdraw(2000, "1234") # موجودی ناکافی
my_account.check_balance("1234")
my_account.check_balance("0000") # رمز اشتباه
