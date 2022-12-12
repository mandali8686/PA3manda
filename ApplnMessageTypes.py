# Sample code for CS4283-5283
# Vanderbilt University
# Instructor: Aniruddha Gokhale
# Created: Fall 2022
# 
# Purpose: Provides the definition of supported messages
#

# import the needed packages
import sys
import random
from enum import Enum  # for enumerated types
# @TODO import whatever more packages are needed

# add to the python system path so that packages can be found relative to
# this directory
sys.path.insert (0, "../")

############################################
#  Enumeration for Message Types
############################################
class MessageTypes (Enum):
  # One can extend this as needed. For now only these two
  UNKNOWN = -1
  GROCERY = 1
  HEALTH = 2
  RESPONSE = 3
  
 ############################################
#  Enumeration for Milk Types
############################################
class MilkType (Enum):
  one_percent=1
  two_percent=2
  fat_free=3
  whole=4
  almond=5
  cashew=6
  oat=7
  soymilk=8
############################################
#  Enumeration for Bread Types
############################################
class BreadType (Enum):
  sourdough=1
  rye_bread=2
  baguette=3
  croissant=4
  white_break=5
  whole_grain=6
  burger_bun=7
  bread_stick=8
############################################
#  Enumeration for Meat Types
############################################
class MeatType (Enum) :
  beef=1
  pork=2
  chicken=3
  turkey=4
  lamb=5
  goat=6
  fish=7
  

############################################
#  Grocery Order Message
############################################
class GroceryOrderMessage:
  msg_type:str
  tomato:float
  cucumber:float
  onion:float
  green_bean:float
  broccoli:float
  jalapineo:float
  coke:int
  beer:int
  diet_coke:int
  sprite:int
  root_beer:int
  lemonade:int
  milk:list
  bread:list
  meat:list

  '''Grocery Order Message'''
  def __init__ (self):
    self.dummy = "This is a grocery order message"
    #self.order="Order"
    self.msg_type=str(MessageTypes(1))
    self.tomato=random.random()
    self.cucumber=random.random()
    self.onion=random.random()
    self.green_bean=random.random()
    self.broccoli=random.random()
    self.jalapineo=random.random()
    self.coke=random.randint(0,100)
    self.beer=random.randint(0,100)
    self.diet_coke=random.randint(0,100)
    self.sprite=random.randint(0,100)
    self.root_beer=random.randint(0,100)
    self.lemonade=random.randint(0,100)
    self.milk=[str(MilkType(random.randint(1,8))),random.randint(0,100)]
    self.bread=[str(BreadType(random.randint(1,8))),random.randint(0,100)]
    self.meat=[str(MeatType(random.randint(1,7))),random.randint(0,100)]

    # @TODO - the above is simply to test the code. You need to get rid of that dummy
    # and replace it with the complex data struture we have for the grocery order
    # as represented in the host (as a Python language data structure)

  def __str__ (self):
    '''Pretty print the contents of the message'''
    #print(self.order)
    print("type: {}".format(self.msg_type))
    print("contents:")
    print("   veggies:")
    print("       tomato:{}".format(self.tomato))
    print("       cucumber:{}".format(self.cucumber))
    print("       onion:{}".format(self.onion))
    print("       green bean:{}".format(self.green_bean))
    print("       broccoli:{}".format(self.broccoli))
    print("       jalapineo:{}".format(self.jalapineo))
    print("   drinks:")
    print("      cans:")
    print("         coke:{}".format(self.coke))
    print("         beer:{}".format(self.beer))
    print("         diet coke:{}".format(self.diet_coke))
    print("       bottles:")
    print("         sprite:{}".format(self.sprite))
    print("         root beer:{}".format(self.root_beer))
    print("         lemonade:{}".format(self.lemonade))
    print("   milk:{}".format(self.milk))
    print("   bread:{}".format(self.bread))
    print("   meat:{}".format(self.meat))
    return self.dummy

    #@TODO - remove the above print stmt and instead create a pretty print logic
    
############################################
#  Health Status Message
############################################

############################################
#  Enumeration for Dispenser Code
############################################
class DispenserCode (Enum):
  NONE=0
  OPTIMAL=1
  PARTIAL=2
  BLOCKAGE=3
############################################
#  Enumeration for Good and Bad
############################################
class GBCode (Enum):
  NONE=0
  GOOD=1
  BAD=2

class HealthStatusMessage:
  msg_type:str
  dispenser:str
  icemaker:int
  lightbulb:str
  fridge_temp:int
  freezer_temp:int
  sensor_status:int
  power:int
  '''Health Status Message'''
  def __init__ (self):
    #self.health="Health"
    self.msg_type=str(MessageTypes(2))
    self.dispenser=str(DispenserCode(random.randint(1,3)))
    self.icemaker=random.randint(1,10)
    self.lightbulb=str(GBCode(random.randint(1,2)))
    self.fridge_temp=random.randint(0,20)
    self.freezer_temp=random.randint(-20,20)
    self.sensor_status=str(GBCode(random.randint(1,2)))
    self.power=random.randint(1,100)
    self.dummy = "This is a health status message"
    
    

    # @TODO - the above is simply to test the code. You need to get rid of that dummy
    # and replace it with the complex data struture we have for the health status
    # as represented in the host (as a Python language data structure)

  def __str__ (self):
    '''Pretty print the contents of the message'''
    #print(self.health)
    print("type: {}".format(self.msg_type))
    print("contents: ")
    print("     dispenser: {}".format(self.dispenser))
    print("     icemaker: {}".format(self.icemaker))
    print("     lightbulb: {}".format(self.lightbulb))
    print("     fridge_temp: {}".format(self.fridge_temp))
    print("     freezer_temp: {}".format(self.freezer_temp))
    print("     sensor_status: {}".format(self.sensor_status))
    print("     power: {}".format(self.power))
    return self.dummy

    #@TODO - remove the above print stmt and instead create a pretty print logic
    
############################################
#  Response Message
############################################

############################################
#  Enumeration for Response Code
############################################
class ResponseCode(Enum):
  NONE=0
  OK=1
  BAD_REQUEST=2
  
class ResponseMessage:
  '''Response Message'''
  def __init__ (self,code,contents):
    self.dummy = "This is a response message"
    self.code = str(ResponseCode(code))
    self.contents = contents

    # @TODO @ done - the above is simply to test the code. You need to get rid of that dummy
    # and replace it with the data struture we have for the response message 
    # as represented in the host (as a Python language data structure)

  def __str__ (self):
    '''Pretty print the contents of the message'''
    print("code: {}".format(self.code))
    print("contents: {}".format(self.contents))
    return self.dummy

    #@TODO - remove the above print stmt and instead create a pretty print logic
    



