def es_primo(numero):
  primo = True
  if numero < 1:
        primo = False
  elif numero == 2:
        primo = True
  else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
    return True 
    
  # aquí debes implementar tu código
  # modificando la variable primo 
  # (no modifiques nada de las lineas anteriores)
  return primo
  

es_primo(13)