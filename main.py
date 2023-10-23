from classes.game import Person, bcolors
from classes.Magic import Spell
from classes.Inventory import Item


#Create black magic
fire=Spell('Fire', 25, 600, 'black')
thunder=Spell('Thunder', 25, 600, 'black')
blizzard=Spell('Blizzard', 25, 600, 'black')
meteor=Spell('Meteor',40, 1200, 'black')
quake=Spell('Quake', 14, 140, 'black')

#create White magic
cure=Spell('Cure', 25, 620, 'white')
cura=Spell('Cura', 32, 1500, 'white')

#CReate some items
potion=Item('Potion','potion','Heals 50 hp', 50)
hipotion=Item('Hi-Potion', 'potion','Heals 100 hp', 100)
superpotion=Item('Super-Potion', 'potion', 'Heals 1000 hp', 1000)
elixer=Item('Elixer', 'elixer', 'Fully restores HP/MP of 1 party member', 99999)
hielixer=Item('Mega Elixer', 'elixer', 'Fully restores partys MP/HP', 99999)

grenade=Item('Grenade', 'attack', 'DEals 500 damage', 500)

player_spells= [fire, thunder, blizzard, meteor, cure, cura]
player_items=[{'item': potion, 'quantity':15},{'item':hipotion, 'quantity':5}, {'item':superpotion, 'quantity': 5}, {'item':elixer, 'quantity':5},
              {'item':hielixer, 'quantity':2}, {'item': grenade, 'quantity': 5}]

#instantiate people
#player=Person(460, 65, 60, 34, magic) #instantiated person class with HP, mp, atk, def, mgk
#enemy=Person(1200, 65, 45, 25, magic)
player1=Person('Valos: ', 3260, 132, 300, 34, player_spells, player_items)
player2=Person('Nick: ', 4160, 188, 311, 34, player_spells, player_items)
player3=Person('Robot: ', 3089, 174, 288, 34, player_spells, player_items)
enemy=Person('Magus', 11200, 701, 525, 25, [],[])
#magic=[{'name': 'Fire','cost':10,'dmg':100}, # the colon sets the value to the string
       #{'name': 'Thunder','cost':10,'dmg':124}, #dont forget commes at end of object between arrays
       #{'name': 'Blizzard','cost':10,'dmg':100}] # [] for array inside of which we create multiple objects, a list of dictionnairies

players=[player1, player2, player3]


#we create a looping script for attack pattern



running=True # setting a variable running = true
i=0
print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS' + bcolors.ENDC) #you cam make the tex red by wrapping it in the class color commands

while running:

       print('================================================')

       print ('\n\n')
       print('NAME               HP                                  MP')

       for player in players:
              player.get_stats()

       print('\n')

       enemy.get_enemy_stats()

       for player in players:

              player.choose_action()
              choice=input('    Choose Action ') # captures the users actions and sets to variable choice
              index=int(choice)-1 # because we don't list 0 as a choice in the menu

              if index==0:
                     dmg=player.generate_damage()
                     enemy.take_damage(dmg)
                     print('You attacked for', dmg, 'points of damage. Enemy HP:', enemy.get_hp())
              elif index==1:
                     player.choose_magic()
                     magic_choice=int(input('    Choose Magic: '))-1

                     if magic_choice==-1:
                            continue  # this is a sort of cheat that lets us go back


                    # magic_dmg=player.generate_spell_damage(magic_choice)
                     #spell=player.get_spell_name(magic_choice)
                     #cost=player.get_spell_mp_cost(magic_choice)

                     spell=player.magic[magic_choice] ####I think the integer we put in here picks the spell in the list.
                     magic_dmg=spell.generate_damage() ## Does this pick up damage bc it's in the same numbererd row as Atk in person class???????????????????????????????????????????

                     current_mp=player.get_mp()

                     if spell.cost>current_mp:
                            print(bcolors.FAIL+'\nNot enough mp\n'+bcolors.ENDC)
                            continue

                     player.reduce_mp(spell.cost) #changed from cost to spell .cost

                     if spell.type==str('white'): # this is what I tried to type myself
                            player.heal(magic_dmg)
                            print(bcolors.OKBLUE+'\n'+ spell.name+'heals for', str(magic_dmg), 'hp'+bcolors.ENDC)
                     elif spell.type=='black':
                            enemy.take_damage(magic_dmg)
                            print(bcolors.OKBLUE+'\n'+spell.name+' deals',str(magic_dmg),'points of damage'+bcolors.ENDC)


              elif index==2:
                     player.choose_item()
                     item_choice=int(input('    Choose item: '))-1

                     if item_choice==-1:
                            continue

                     item=player.items[item_choice]['item']

                     if player.items[item_choice]['quantity']==0:
                            print(bcolors.FAIL+'\n'+'you do not have enough inventory'+bcolors.ENDC)
                            continue

                     player.items[item_choice]['quantity']-=1

                     if item.type=='potion':
                            player.heal(item.prop)
                            print(bcolors.OKGREEN+'\n'+item.name, 'heals for', str(item.prop), 'hp'+bcolors.ENDC)

                     elif item.type=='elixer':
                            player.hp=player.maxhp
                            player.mp=player.maxmp
                            print(bcolors.OKGREEN+'\n'+item.name+'fully restores HP/MP'+bcolors.ENDC)

                            # if we only had item=player.items[item choice] in the line above, then we would need ['item'] on all sub callouts after.

                     elif item['item'].type=='attack':
                            enemy.take_damage(item.prop)
                            print(bcolors.FAIL+'\n'+item.name+'deals', str(item.prop), 'points of damage'+bcolors.ENDC)

       enemy_choice=1

       enemy_dmg=enemy.generate_damage()
       player1.take_damage(enemy_dmg)
       print('Enemy attacks for ', enemy_dmg,'player hp', player.get_hp())
       print('-------------------------------------------')
       print('Enemy HP:', bcolors.FAIL+ str(enemy.get_hp())+'/'+str(enemy.get_max_hp())+bcolors.ENDC+'\n')


       if enemy.get_hp()==0:
              print(bcolors.OKGREEN+'You win'+bcolors.ENDC)
              running=False

       elif player.get_hp()==0:           #could I just use another if?
              print(bcolors.FAIL+'You Loose'+bcolors.ENDC)
              running=False

#print(player.generate_spell_damage(0)) # we defined player in line 6, that where atks value is
#print(player.generate_spell_damage(1))

# print(player.generate_damage())
# print(player.generate_damage())
# print(player.generate_damage()) #person class does something, it generates damage, see game file

