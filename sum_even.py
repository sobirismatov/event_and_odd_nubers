#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int=1234
#Create a variable "sum_even" and assign it 0.
sum_even=0
#Find the sum of the even digits in the variable "var_int".
var_int=1234%10
var_int1=1234//100
var_int2=var_int1%10
sum_even1=var_int+var_int2
print("1234 sondagi juft raqamlar", var_int, "va", var_int2," juft raqamlar yig`indisi",sum_even1,"ga teng")