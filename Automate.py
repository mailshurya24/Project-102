import random
openWorld = ["Grand Theft Auto 5", "Assassin's Creed Valhalla", "Red Dead Redemption 2", "Far Cry 5"]
shooter = ["Call of Duty Modern Warfare", "Battlefield V", "Serious Sam 3", "DOOM Eternal"]
sports = ["FIFA 21", "NBA 2K21", "Madden NFL 21", "Forza Horizon 4"]
online = ["Grand Theft Auto Online", "Warzone", "Fortnite", "Apex Legends"]

print("I'm here to help you figure out which game to play!")
print("Caution: Video game piracy is illegal. All games mentioned here can be purchased on Steam or Epic Games.")
print("Have fun gaming!")
print("")
type2 = input("What would you like to play -- Open World, Shooter, Sports or Online? ")

if type2 == "Open World":
        choice = random.choice(openWorld)
        print("Try: " + choice)
elif type2 == "Shooter":
        choice = random.choice(shooter)
        print("Try: " + choice)
elif type2 == "Sports":
        choice = random.choice(sports)
        print("Try: " + choice)
elif type2 == "Online":
        choice = random.choice(online)
        print("Try: " + choice)        