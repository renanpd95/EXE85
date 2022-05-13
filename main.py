import os

n = 1
cont = 0
par = 0
impar = 0

while(n > 0):
  #Inserir e verificar se o número é par ou impar
  num = float(input("Digite um número: "))
  if(num % 2 == 0):
      par = par + 1
  elif(num % 2 == 1):
      impar = impar + 1
    
  #Continuação do programa?  
  conti = str(input("Deseja continuar o programa (S/N): "))
  if(conti == "S" or conti == "Sim" or conti == "SIM" or conti == "s" or conti ==   "yes" or conti == "YES"): 
    n = 1
  else:
    n=0
    
else:
  os.system('clear')
  print("Quatidade de números par:",par)
  print("Quantidade números impar",impar)
    
    

