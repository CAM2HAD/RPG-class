

from classes.Magic import Spell
import random #In order to generate damge we will use random

import pprint # this means pretty print


class bcolors: #This assigns variables to colors we can use in terminal, found on github see bookmarks
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items): # wee added items at course 41
        self.name=name
        self.maxhp = hp #setting max so we don<t overheal
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl=atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic= magic #in main magic is defined as an array with 3 objects inside [{}]
        self.actions= ["Attack", "Magic",'items']
        self.items=items



    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh) # use self.atk bc we are inside of a class



    #def generate_spell_damage(self,i): #add i as index number because it's an array s it can pass 0,1 or 2 ea line in main
        #mgl=self.magic[i]['dmg']-5 #self.magic is whre spells are stored, its an array and I pick which one
        #mgh=self.magic[i]['dmg']+5
        #return random.randrange(mgl,mgh)

    def take_damage(self, dmg):
        self.hp-=dmg #this takes damage amount from hp
        if self.hp<0:
            self.hp=0
        return self.hp

    def heal(self, dmg):
        self.hp+=dmg
        if self.hp>self.maxhp:
            self.hp=self.maxhp


    def get_hp(self): #utility classes to get property
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp-=cost #-= substracts value from variable and assigns that new value to variable

    # we now need a way to choose atk or magic and if magic chosen, which spell?

    def choose_action(self):
        i=1 #index set to 1
        print('\n'+'    '+bcolors.BOLD+str(self.name)+bcolors.ENDC)
        print(bcolors.OKBLUE+bcolors.BOLD+'    ACTIONS:'+bcolors.ENDC)
        for item in self.actions: # self.action has 2 items
            print('        '+str(i)+':',item)
            i+=1

    def choose_magic(self):
        i=1
        print('\n'+bcolors.OKBLUE+bcolors.BOLD+'    Magic:'+bcolors.ENDC)
        for spell in self.magic:
           print('        '+str(i)+':', spell.name, 'cost:', spell.cost)
           i+=1

           # print(str(i)+':', spell['name'], 'cost:', spell['cost']) #,'(cost', str(spell['cost'])+')'])
            # this is how you target a list in an index and not how you target an object in a class attribute
    def choose_item(self):
        i=1

        print('\n'+bcolors.OKGREEN+bcolors.BOLD+'ITEMS'+bcolors.ENDC)
        for item in self.items:
            print('        '+str(i)+'.', item['item'].name, ':', item['item'].description, 'x'+str(item['quantity'])) #what happen s is item in person class goes to player_items which is a dictionnary, we call the 'item' objct which ties to the class Item?
            i+=1

        # older code print ('\n'+bcolors.OKGREEN+bcolors.BOLD+'ITEMS'+bcolors.ENDC)

    def get_enemy_stats(self):

        hp_bar=''
        bar_tiks=(self.hp/self.maxhp)*100/2

        while bar_tiks>0:
            hp_bar+='█'
            bar_tiks-=1

        while len(hp_bar)<50:
            hp_bar+=''

        hp_string=str(self.hp) + '/'+str(self.maxhp)
        current_hp=''

        if len(hp_string)<11:        #This is upposed to add a blank in front of the number if the hp falls to 3 digits, see lesson 4-46.
            decreased=11-len(hp_string)

            while decreased>0:
                current_hp+=''
                decreased-=1 # you decrease this variable back down to 0 to exit the loop

            current_hp+=hp_string # adds a blank to the left of mp string I think
        else:
            current_hp=hp_string

        print('                 __________________________________________________')
        print(bcolors.BOLD+ str(self.name)+'  '+
                current_hp + '|'+bcolors.FAIL+ hp_bar +bcolors.ENDC+ '|')


    def get_stats(self):  #NOT 100% Sure how this function now works

        hp_bar=''
        bar_ticks=(self.hp/self.maxhp)*100/4

        mp_bar=''
        mp_ticks=(self.mp/self.maxmp)*100/10

        while bar_ticks>0:
            hp_bar+='█'
            bar_ticks-=1

        while len(hp_bar)<25:  # len() is one of Python's built-in functions. It returns the length of an object. For example, it can return the number of items in a list.
            hp_bar+=' '

        while mp_ticks>0:
            mp_bar+='█'
            mp_ticks-=1

        while len(mp_bar)<10:  # to modify length of mp bar see lesson 4-45 'working hp bars'
            mp_bar+=' '

        hp_string=str(self.hp) + '/'+str(self.maxhp)
        current_hp=''

        if len(hp_string)<9:        #This is upposed to add a blank in front of the number if the hp falls to 3 digits, see lesson 4-46.
            decreased=9-len(hp_string)

            while decreased>0:
                current_hp+=''
                decreased-=1 # you decrease this variable back down to 0 to exit the loop
            current_hp+=hp_string # adds a blank to the left of mp string I think
        else:
            current_hp=hp_string

        mp_string=str(self.mp)+ '/'+ str(self.maxmp)
        current_mp=''

        if len(mp_string)<7:
            decreased=7-len(mp_string)
            while decreased >0:
                current_mp+=''
                decreased-=1
            current_mp+=mp_string

        else:
            current_mp=mp_string


        print('                   _________________________             __________')
        print(bcolors.BOLD+ str(self.name)+''+
                current_hp + '|'+bcolors.OKGREEN+ hp_bar +bcolors.ENDC+ '|      '+
                current_mp+'|'+ bcolors.OKBLUE+ mp_bar +bcolors.ENDC+ '|')




