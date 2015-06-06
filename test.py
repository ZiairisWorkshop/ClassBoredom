# Create a basic job.

#These variables are imported from main game:
Charisma = 2
Stamina = 2
Energy = 15

Coins = 18

TownRep = 34
Time = 892

# These variables are new.
PayRate = 5
Work = "False"

# Charisma and Town Rep calculate PayRate Change
PayRate = Payrate*(TownRep/2)

if Charisma >5:
    Payrate = Payrate * (Charisma/5)

# define work
def working(Charisma, Stamina, Energy, Coins, TownRep, Time)
