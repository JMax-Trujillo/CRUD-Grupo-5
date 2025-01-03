from dosListas import lista_Ciclo_1, lista_Ciclo_2

name = lista_Ciclo_1[1][1]
name = "hola ,q tal"
# otro = name.replace(",", "")
# algo = otro.split(" ")
# print(algo)
otro = name.replace(",", "").split(" ")
s=''
for i in otro:
   s+= i + " "
   
print(s) 

num = [1,2,3,4,5,6,7,8,9]

new = num[2:]

print(new)