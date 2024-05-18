print('How many kilometers do you cycle today?')
kms = input()
miles = float(kms)/1.6
miles = round(miles,2)
print(f'Your {kms}km ride was {miles}mi')
