#!/usr/bin/env python
# coding: utf-8

# # Computing 8 Assignment
# 
# 

# ---
# ## Background
# 
# Object oriented programming languages are often used when designing and developing complex systems such as video games. Objects are used to represent various aspects of the game such as players, enemies, items, maps, etc. **Role-playing** video games are a common genre of video games where users control the actions of a player or character. These games often involve some form of combat in addition to the player having attributes such as health, levels, damage, etc. In this assignment, you will be implementing a **Player** class for a video game. Our player class will keep track of the following features:
# 
# -	The player’s name
# -	The player’s health
# -	The player’s current level
# -	The player’s current “score”
# -	The score required to reach the next level
# -	The player’s set of attacks
# 
# In addition to the **Player** class, you will be implementing a function that will use the **Player** class. Please thoroughly read the requirements section to understand how to implement the methods and function!

# In[73]:


# YOUR CODE HERE
class Player:
    try:
        # create __init__ method that allows player to input a name as the only argument
        def __init__(self,name):
            #if a name was inputted, set it equal to self.name
            if name:
                self.name = name
            #if a name was not inputted, set the name as "Default"    
            else:
                self.name = "Default"
        
            #initialize the player's health, level, attacks etc.
            self.health = 100
            self.level = 0
            self.current_score = 0
            self.next_lvl_score = 50
            self.attacks = [["Fast attack",5],["Slow attack",15],["Default Special Attack",20]]
   
    except:
        print("Please check your inputs!")
        
    try:
        #method to get player's name
        def get_name(self):
            return self.name
    
        #method to get player's health
        def get_health(self):
            return self.health
    
        #method to get player's level
        def get_level(self):
            return self.level
    
        #method to get player's current score
        def get_score(self):
            return self.current_score
    
        #method to get player's score needed to reach next level
        def get_next_lvl_score(self):
            return self.next_lvl_score
    
        #method to get player's current attacks
        def get_attacks(self):
            return self.attacks
    
    except TypeError:
        print("Do not input any arguments.")
    
        #create mutator that raises the players health by the amount inputted
        #if the input is negative, it does nothing
    try:
        def raise_health(self,val):
            if val >= 0:
                #only adds to the health if the total will be less than 100
                if val + self.health <= 100:
                    self.health += val
                #otherwise sets the health at 100
                else:
                    self.health == 100
    except NameError:
        print("Input must be an integer.")
    except TypeError:
        print("Only input one integer.")
    
        #create mutator that replaces an existing attack with the inputs given
        #replaces the existing attack at index i, with new name and strength
    try:
        def replace_attack(self,i,name,strength):
            new_attack = [name,strength]
            self.attacks[i] = new_attack
        
        #create mutator that decreases the health of the player based on the input
        def take_damage(self,quantity):
            #only works if quantity is a positive integer
            if quantity > 0:
                #if the damage taken keeps health above 0, subtract quantity from health
                if self.health - quantity >= 0:
                    self.health -= quantity
                #otherwise, set health to be 0
                else:
                    self.health = 0
    
        #create mutator that uses the attack from attack list at index i and performs the attack on player_2
        def perform_attack(self,i,player_2):
            #calculates player_2's health and stores as a variable
            p2_health = player_2.get_health()
            #damage taken by attack is stored in the variable damage_given
            damage_given = self.attacks[i][1]
            player_2.take_damage(damage_given)
        
            #damage_given will be added to player's score if it is less than the score needed to reach next level
            if (damage_given + self.current_score) < self.next_lvl_score:
                self.current_score += damage_given
            #if damage_given is greater than or equal to score needed to reach next_level    
            elif (damage_given + self.current_score) >= self.next_lvl_score:
                #player's level increases by 1
                self.level += 1
                #player's current score is 0
                self.current_score = 0
                #score needed to reach next_level increases by 20
                self.next_lvl_score += 20
                #every attack strength is increased by 5
                for j in range(len(self.attacks)):
                    self.attacks[j][1] += 5
    except:
        print("Something went wrong.")
        print("Please check all your inputs and try again!")
    
    
            
                


# In[72]:


# YOUR CODE HERE
def simulate_battle(player_1, player_2, player_1_moves, player_2_moves):
    #initialize result variable
    result = ""
    #for every element in player_11_moves, perform the attack on player_2
    for i in player_1_moves:
        player_1.perform_attack(i,player_2)
        #if player_2's health falls to 0, player 1 wins
        if player_2.get_health() == 0:
            result = player_1.get_name()
            break
    #for every element in player_2_moves, perform the attack on player_1
    for i in player_2_moves:
        player_2.perform_attack(i,player_1)
        #if player_1's health falls to 0, player_2 wins
        if player_1.get_health() == 0:
            result = result = player_2.get_name()
            break
    #return the winner's name
    return result
            


# ```
# -------------TEST PLANS-------------------------------------------
# 
# Function: replace_attack(self,i,name,strength)
# 
# Input(normal): p = Player("")
#                p.replace_attack(0,"weak",20)
#                print(p.get_attacks() == [["weak",2],["Slow Attack",15],["Default Special Attack",20]])
# Output: True
# Expected Output: True
# Pass
# 
# Input(boundary): p = Player("John")
#                  p.replace_attack(2,"Super Attack",50)
#                  print(p.get_attacks() == [["Fast attack",5],["Slow attack",15],["Super Attack",50]])
# Output: True
# Expected Output: True
# Pass
# 
# Input(abnormal): p = Player("")
#                  p.replace_attack(hello,"Strongest",40)
#                  print(p.get_attacks()
# Output: NameError
# Expected Output: Error
# Pass
# ----------------------------------------------------------
# Function: take_damage(self,quantity)
# 
# Input(normal): p = Player("")
#                p.take_damage(30)
#                print(p.get_health())
# Output: 70
# Expected Output: 70
# Pass
# 
# Input(boundary): p = Player("")
#                  p.take_damage(101)
#                  print(p.get_health())
# Expected Output: 0
# Output: 0
# Pass
# 
# Input(abnormal): p = Player("")
#                  p.take_damage(Twenty)
#                  print(p.get_health())
# Output: NameError
# Expected Output: Error
# Pass
# ```

# ---
# ## Reflective Questions
# 
# 1. In the Program Requirements, the ***raise_health()*** mutator was specified to have 1 argument, but when you defined it, the mutator was defined to accept 2 parameters. What is the purpose of the first parameter? What happens if we omit this parameter?
# 
# 
# 2. Suppose we had a method ***rename_player(self,name)*** that renames your player object with *name*. Would this method be an accessor or mutator?
# 
# 
# 3. Is it possible to test that ***raise_health()*** works correctly using a single python statement (i.e. using a single line of code)?
# 
# Please answer all questions in the cell below!

# ```
# 1. The first parameter, self, is used to represent the instance of a class. It allows the user to access the attributes and methods associated with that class. If we omit this parameter, we will not be able to access the self.health attribute or be able to actually raise the player's health.
# 
# 2. The method rename_player(self,name) would be considered a mutator since it would change the value of the name given. Mutator functions change the value of a variable, while accessor methods simply reference the variable.
# 
# 3. It is only possible to test if raise_health() works correctly using a single line if a player has already been created. If a player has not yet been created, it will require more than one line to test if the raise_health() method works.
# ```
