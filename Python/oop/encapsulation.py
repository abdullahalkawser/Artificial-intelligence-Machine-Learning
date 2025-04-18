class BankAccounts:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public Attribute
        self._bank_name = "XYZ Bank"  # Protected Attribute
        self.__balance = balance  # Private Attribute

    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        """Public method to withdraw money"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        """Public method to access the private balance"""
        return self.__balance

# Creating an object
account = BankAccounts("123456789", 5000)

# Accessing Public Attributes
print("Account Number:", account.account_number)  # Works

# Accessing Protected Attributes (allowed but discouraged)
print("Bank Name:", account._bank_name)  # Works, but should be avoided

# Accessing Private Attributes (will cause an error)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Accessing Private Attributes using a Public Method
# Accessing balance using a getter
print("Balance:", account.get_balance())  # Works

# Depositing and Withdrawing Money

# Updating balance using a setter
# account.set_balance(7000)
account.deposit(2000)
account.withdraw(1000)

# Accessing Private Attribute with Name Mangling (not recommended)
print("Balance using name mangling:", account._BankAccounts__balance)  # Works but not 
# recommended  Recommended Approach 1: Using Getter & Setter Methods



"""Explanation
self.account_number → Public: Can be accessed from anywhere.
self._bank_name → Protected: Can be accessed but should be treated as private (by convention).
self.__balance → Private: Cannot be accessed directly outside the class.
get_balance() → Public method to access private attributes.
deposit() & withdraw() → Public methods to modify private data securely.
Name Mangling (_ClassName__variable): Python internally renames private variables, allowing access but discouraging it."""


"""Advantages of Encapsulation
✔ Data Hiding – Prevents accidental modification of sensitive data.
✔ Security – Protects critical information from external modifications.
✔ Control – Only specific methods control how the data is accessed and modified."""

"""Conclusion: Why Should You Use Encapsulation?
✔ Protects sensitive data from unauthorized access
✔ Prevents accidental modifications and maintains data integrity
✔ Makes code easier to maintain, scale, and debug
✔ Encourages abstraction by exposing only necessary details

Would you like me to give a real-world analogy for better understanding?"""