from pokemon_data_file import pokemon_data
from move_data_file import move_data
from random import *
from objectFile import Pokemon
from objectFile import Move
from objectFile import Section

pokemon_list = []
move_list = []
Setof10 = range(12)
Setof865 = range(865)
Section1 = []
Section2 = []
Section3 = []
Section4 = []
Section5 = []
Section6 = []
indexInteger = 0
MinHP1 = 0
list_of_sections = []
print()

for each in Setof10:
    randomInteger = randint(0,809)
    name = pokemon_data[randomInteger]['name']['english']
    type = pokemon_data[randomInteger]['type'][0]
    hp = int(pokemon_data[randomInteger]['base']['HP']) * 5
    attack = pokemon_data[randomInteger]['base']['Attack']
    defense = pokemon_data[randomInteger]['base']['Defense']
    special_attack = pokemon_data[randomInteger]['base']['Sp. Attack']
    special_defense = pokemon_data[randomInteger]['base']['Sp. Defense']
    speed = pokemon_data[randomInteger]['base']['Speed']
    new_object = Pokemon(name, type, hp, attack, defense, special_attack, special_defense, speed)
    pokemon_list.append(new_object)

for each in Setof865:
    name = move_data[indexInteger]['Name']
    type = move_data[indexInteger]['Type']
    power = move_data[indexInteger]['Power']
    accuracy = move_data[indexInteger]['Acc.']
    new_move_object = Move(name, type, power, accuracy)
    move_list.append(new_move_object)
    indexInteger += 1

Section1.append(pokemon_list[0])
Section1.append(pokemon_list[1])
Section2.append(pokemon_list[2])
Section2.append(pokemon_list[3])
Section3.append(pokemon_list[4])
Section3.append(pokemon_list[5])
Section4.append(pokemon_list[6])
Section4.append(pokemon_list[7])
Section5.append(pokemon_list[8])
Section5.append(pokemon_list[9])
Section6.append(pokemon_list[10])
Section6.append(pokemon_list[11])

firstSection = Section1
secondSection = Section2
thirdSection = Section3
fourthSection = Section4
fifthSection = Section5
sixthSection = Section6

sectionNameList = ["Section1", "Section2", "Section3", "Section4", "Section5", "Section6"]
sectionList = [firstSection, secondSection, thirdSection, fourthSection, fifthSection, sixthSection]

sectionListIndex = 0
for each in sectionList:
    name = sectionNameList[sectionListIndex]
    obj = sectionList[sectionListIndex]
    winner = sectionList[sectionListIndex]
    new_list_obj = Section(name, obj, winner)
    list_of_sections.append(new_list_obj)
    sectionListIndex += 1

BaseStats = pokemon_list

for each in Section1:
    print(each.name + " has been chosen for section 1.")
print()
for each in Section2:
    print(each.name + " has been chosen for section 2.")
print()
for each in Section3:
    print(each.name + " has been chosen for section 3.")
print()
for each in Section4:
    print(each.name + " has been chosen for section 4.")
print()
for each in Section5:
    print(each.name + " has been chosen for section 5.")
print()
for each in Section6:
    print(each.name + " has been chosen for section 6.")

print()

def attackFunction0(fightVariable1):
    Attack1 = move_list[randint(0, 864)]
    fightVariable1.obj[1].hp -= int(Attack1.power)
    print(f"{(fightVariable1.obj[0].name)} (HP {fightVariable1.obj[0].hp}) used {Attack1.name} (Power {Attack1.power}) against {fightVariable1.obj[1].name} (HP {fightVariable1.obj[1].hp}).")

def attackFunction1(fightVariable1):
    Attack2 = move_list[randint(0, 864)]
    fightVariable1.obj[0].hp -= int(Attack2.power)
    print(f"{(fightVariable1.obj[1].name)} (HP {fightVariable1.obj[1].hp}) used {Attack2.name} (Power {Attack2.power}) against {fightVariable1.obj[0].name} (HP {fightVariable1.obj[0].hp}).")

def whileLoop0(fightVariable1):
    while MinHP1 > 0:
        attackFunction0(fightVariable1)
        if fightVariable1.obj[1].hp < 0:
            print(fightVariable1.obj[1].name + " has fainted. " + fightVariable1.obj[0].name + " wins the duel.")
            fightVariable1.winner = fightVariable1.obj[0]
            break
        if fightVariable1.obj[0].hp < 0:
            print(fightVariable1.obj[0].name + " has fainted. " + fightVariable1.obj[1].name + " wins the duel.")
            fightVariable1.winner = fightVariable1.obj[1]
            break
        attackFunction1(fightVariable1)
        if fightVariable1.obj[0].hp < 0:
            print(fightVariable1.obj[0].name + " has fainted. " + fightVariable1.obj[1].name + " wins the duel.")
            fightVariable1.winner = fightVariable1.obj[1]
            break
        if fightVariable1.obj[1].hp < 0:
            print(fightVariable1.obj[1].name + " has fainted. " + fightVariable1.obj[0].name + " wins the duel.")
            fightVariable1.winner = fightVariable1.obj[0]
            break
    print()

def whileLoop1(fightVariable1):
    while MinHP1 > 0:
        attackFunction1(fightVariable1)
        if fightVariable1.obj[0].hp < 0:
            print(fightVariable1.obj[0].name + " has fainted. " + fightVariable1.obj[1].name + " wins the duel.")
            fightVariable1.winner = fightVariable1.obj[1]
            break
        if fightVariable1.obj[1].hp < 0:
            print(fightVariable1.obj[1].name + " has fainted. " + fightVariable1.obj[0].name + " wins the duel.")
            fightVariable1.winner = fightVariable1.obj[0]
            break
        attackFunction0(fightVariable1)
        if fightVariable1.obj[1].hp < 0:
            print(fightVariable1.obj[1].name + " has fainted. " + fightVariable1.obj[0].name + " wins the duel.")
            fightVariable1.winner = fightVariable1.obj[0]
            break
        if fightVariable1.obj[0].hp < 0:
            print(fightVariable1.obj[0].name + " has fainted. " + fightVariable1.obj[1].name + " wins the duel.")
            fightVariable1.winner = fightVariable1.obj[1]
            break
    print()

def speed0(fightVariable1):
    print(f"{fightVariable1.obj[0].name} (SP {fightVariable1.obj[0].speed}) is faster than {fightVariable1.obj[1].name} (SP {fightVariable1.obj[1].speed}).")
    whileLoop0(fightVariable1)
def speed1(fightVariable1):
    print(f"{fightVariable1.obj[1].name} (SP {fightVariable1.obj[1].speed}) is faster than {fightVariable1.obj[0].name} (SP {fightVariable1.obj[0].speed}).")
    whileLoop1(fightVariable1)

def Fight(fightVariable1):
    print(f"{fightVariable1.name} battle begins with the following Pokémon: ")
    print(f"{(fightVariable1.obj[0].name)} (HP {fightVariable1.obj[0].hp}).")
    print(f"{(fightVariable1.obj[1].name)} (HP {fightVariable1.obj[1].hp}).")
    print()
    if Section1[0].speed > Section1[1].speed:
        speed0(fightVariable1)
    else:
        speed1(fightVariable1)

for each in Section1:
    if MinHP1 < each.hp:
        MinHP1 = each.hp

Fight(list_of_sections[0])
Fight(list_of_sections[1])
Fight(list_of_sections[2])
Fight(list_of_sections[3])
Fight(list_of_sections[4])
Fight(list_of_sections[5])

print(f"{list_of_sections[0].winner.name} is the winner of {list_of_sections[0].name}.")
print(f"{list_of_sections[1].winner.name} is the winner of {list_of_sections[1].name}.")
print(f"{list_of_sections[2].winner.name} is the winner of {list_of_sections[2].name}.")
print(f"{list_of_sections[3].winner.name} is the winner of {list_of_sections[3].name}.")
print(f"{list_of_sections[4].winner.name} is the winner of {list_of_sections[4].name}.")
print(f"{list_of_sections[5].winner.name} is the winner of {list_of_sections[5].name}.")

print()
print()

Section1.append(list_of_sections[0].winner)
Section1.append(list_of_sections[1].winner)
Section2.append(list_of_sections[2].winner)
Section2.append(list_of_sections[3].winner)
Section3.append(list_of_sections[4].winner)
Section3.append(list_of_sections[5].winner)

#Fight(list_of_sections[0])
#Fight(list_of_sections[1])
#Fight(list_of_sections[2])
