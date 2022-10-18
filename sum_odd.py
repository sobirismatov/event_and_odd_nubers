#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int=1234
#Create a variable "sum_even" and assign it 0.
sum_even=0
#Find the sum of the odd digits in the variable "var_int".
var_int=1234//10
var_int1=var_int%10
var_int2=var_int//100
sum_even1=var_int1+var_int2
print(sum_even1)