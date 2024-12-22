class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing")
            func()
            print(f"{self.name} is the 7th Hokage!")
        return wrapper

naruto = AnimeCharacter("Naruto", "Rasengan")

@naruto.introduce
def character_intro():
    print(f"I am {naruto.name} and I can use {naruto.ability}.")

character_intro()