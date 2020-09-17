import random
import math

def GenerateOTP():

   digits="0123456789"
   otp=" "
   
   for i in range(6):
      otp+=digits[math.floor(random.random()*10)]
   return otp
      
   
print("your one time password is ",GenerateOTP())