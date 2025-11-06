import random

words = {
    "easy": ["play", "mass", "ball", "plane", "tenis", "basketball"],
    "hard": ["handkerchief", "comand & concure 2", "mastercheif", "congratulations"]
}
def game(level):
    if level not in words:
        print("Ya yanlis word sectinnnn!!!")
        return

    word = random.choice(words[level])
    mixed = ''.join(random.sample(word, len(word)))
    print("Karışık kelime:", mixed)

    for i in range(3):
        guess = input("Tahmin: ").lower()
        if guess == word:
            print("Bildinnnnn!!!! Bravooooo!!!!!!")
            return
        print("Yapmaaa, Hayirrrr!")
    
    print("Asil kelime bu saftirik:", word)

lvl = input("Lutfen bir seviye sec(easy/hard): ").lower()
game(lvl)