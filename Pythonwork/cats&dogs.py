from pathlib import Path

cats = Path( "D:/Freeideas/cats.txt")
pets_wild = cats.read_text()

try:
    print(pets_wild)
except FileNotFoundError:
    print("Sorry, file not found.")

print()

dogs = Path("dogs.txt")
pets = dogs.read_text()

try:
    print(pets)

except FileNotFoundError:
    print("Sorry, file not found.")


def read_pets_list(pet):
    """Display pets as provided in a list."""
    try:
        animal = Path(pet)
        tell_animal = animal.read_text()

        print(f"\n{tell_animal}")

    except FileNotFoundError:
        # print(f"\nSorry, the file {pet} does not exist.")
        pass


dogs = read_pets_list("dogs.txt")
cats = read_pets_list("D:/Freeideas/cats.txt")
birds = read_pets_list("birds.txt")
weird_pets = read_pets_list("weird_pets.txt")

# I have faced some issues while trying to read on the text, I do not know how
# to solve it.
moby_dick = Path("moby.txt")
with open("moby.txt", "r", encoding="utf-8") as file:
    read_moby= file.read()

specials = ",.?!/()"
for special in specials:
    if special in read_moby:
        read_moby = read_moby.replace(special, " ")

word_list = read_moby.split()
lower_word_list = [word.lower() for word in word_list]
count_nothing = lower_word_list.count("for")
print(f"\n{count_nothing}")

print()
word_count = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key, value in word_count.items():
    print(f"{key.title()} occurs: {value}")


try:

    for line in read_moby.split():
        # print(line)
        read_moby.count("sea")
except UnicodeEncodeError:
     print("Ooops!")



