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

# Charima and Town Rep calculate PayRate Change
PayRate = Payrate*(TownRep/2)

if Charisma >5:
    Payrate = Payrate * (Charima/5)
