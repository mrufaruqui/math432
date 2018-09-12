# from googletrans import Translator

# translator = Translator()

# dict1 = {"I":"আমি", "Welcom":"স্বাগতম", "Good":"ভাল"}
# dict2={ y:x for x,y in dict1.items()}
# dict3={}


# for i in dict1.values():
#     dict3[i]=translator.translate(i, dest='it').text
    
# print(dict1)
# print(dict2)
# print(dict3)

class MyException(Exception):
    '''MyCustom Exception'''
class MyNumber:
    number=None
    all_divs=None
    
    def __init__(self,number):
#         if(self.isDivisibleBy7(number) and self.isMultipleOf5(number)):
#             self.number = number
#         else:
#             raise MyException("number is not divisible by 7 and  multiple of 5")
        self.number = number
        self.all_divs = sorted(self.which_divisors(number))
        
    def __str__(self):
        return str(self.all_divs)
    
    def isDivisibleBy7(self):
        if(self.number%7==0):return True
        else:return False
        
    def isMultipleOf5(self):
         if(self.number%5!=0):return True
         else:return False
        
    def __del__(self):
    	pass
    	if self.number == 49 : assert self.all_divs == [7], 'number is not divisible by 7 and  multiple of 5'
    	if self.number == 75 : assert self.all_divs == [3,5,15,25], 'number is not divisible by 7 and  multiple of 5'
    	
    	#if isinstance((m = MyNumber(49), MyNumber): assert m.all_divs == [7],'number is not divisible by 7 and  multiple of 5'
        #assert print(MyNumber(75)) == '(49,[7])','number is not divisible by 7 and  multiple of 5'
    def which_divisors(self,int_val): 
        ret = []
        for i in range(2,int_val):
            if int_val % i == 0:
                ret.insert(-1,i)       
        return ret
m1 = MyNumber(49)
m2 = MyNumber(75)
print(m1)
print(m2)

# m = m1.all_divs == [7]
# print(m)
# print(m1.all_divs, type(m1.all_divs))
#print(m2, type(m2))
# print(type(m1.all_divs), type([7]))

