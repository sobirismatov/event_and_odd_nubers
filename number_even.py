#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int=1333
#Print the number of even digits in the variable "var_int".
var_int1=var_int%10
var_int2=var_int//10%10
var_int3=var_int//100%10
var_int4=var_int//1000
print((var_int1+1)%2+(var_int2+1)%2+(var_int3+1)%2+(var_int4+1)%2)

