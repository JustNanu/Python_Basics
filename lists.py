#lists almost everything

anime_list = ['opm', 'death_note', 'aot', 'kaguya_sama', 'jojos', 'steins_gate', 'denon_slayer', 'jujutsu_kaisen', 
         'hunterxhunter']

print(anime_list) 

favourite = anime_list[-1].title()

#using individual values from lists
message = "My favourite anime is " + favourite + "."

print(message)

#replacing/modifying a list
anime_list[-3] = 'demon_slayer'

print(anime_list)

#appendig a list(inserting an element at last)
anime_1 = input("Enter an anime name: ")

anime_list.append(anime)

print(anime_list)

#inserting an element at desired position
anime_2 = input("Enter an anime name: ")
anime_list.insert(0, anime_2)

print(anime_list)

#poping- removing an element from a list and then using that value
ongoing_anime = anime_list.pop(0)

print(ongoing_anime)
print(anime_list)
