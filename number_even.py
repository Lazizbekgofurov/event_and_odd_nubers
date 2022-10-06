#A four-digit integer is given. Find the number of even digits in it.
var_int= 2999
r1=var_int//1000
r2=var_int//100%10
r3=var_int//10
r4=var_int%10

print(r1%2+r2%9+r3%9+r4%9)
#print('juft sonni toping%6')
#Create a variable "var_int" and assign it a four-digit integer value.
#print('toq sonni toping%a')
#Print the number of even digits in the variable "var_int".