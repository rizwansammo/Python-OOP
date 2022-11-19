class Joker:
    def __init__(self, name, power, is_he_psycho):
        self.name = name
        self.power = power
        self.is_he_psycho = is_he_psycho


#Write your class code here
j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")
if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')
#Write your code for 2,3 here
print("2. It prints 'different' because j1 and j2 are both objects. Which means they have different/unique memory locations, so they cannot be equal.")
print("3. It prints 'same' because j1.name and j2.name are instance variables containing the same string,'Heath Ledger'. Just before the 2nd if block the value of j2.name was changed to be same as j1.name.")
