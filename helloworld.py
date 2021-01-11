def velocidad(distancia, tiempo):
    resultado = ""
    data_a =(tiempo/3600)
    data_b =(distancia*1000)
    resultado = 'la velocidad es ' + str(distancia/data_a) + ' km/h o ' + str(data_b/tiempo) + ' m/s'
    return(resultado)

def xor(a, b):
  xor = False
  xor = a != b
  # desde aquí hacia abajo debes modificar el programa
  # modifica la variable xor
  # recuerda que los datos están en las variables a y b
  return xor
  
print(xor(5,7))