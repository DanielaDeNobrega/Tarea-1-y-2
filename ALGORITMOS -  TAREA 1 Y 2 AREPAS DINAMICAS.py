# Conversiones de tazas a gramos
taza_harina_pan = 200  # aproximadamente 200 gramos en una taza de harina PAN
cucharadita_sal = 5  # aproximadamente 5 gramos en una cucharadita de sal

# Conversiones de tazas a mililitros
taza_agua = 240  # aproximadamente 240 mililitros en una taza
cucharada_aceite = 15  # aproximadamente 15 mililitros en una cucharada de aceite

# Solicitar al usuario que ingrese las cantidades de ingredientes
    cantidad_taza_agua = float(input("Ingresa la cantidad de tazas de agua: "))
    cantidad_taza_harina_pan = float(input("Ingresa la cantidad de tazas de harina PAN: "))
    cantidad_cucharadita_sal = float(input("Ingresa la cantidad de cucharaditas de sal: "))
    cantidad_cucharada_aceite = float(input("Ingresa la cantidad de cucharadas de aceite: "))

    # Calcular el total de ingredientes en gramos y mililitros
    total_gramos = cantidad_taza_harina_pan * taza_harina_pan + cantidad_cucharadita_sal * cucharadita_sal
    total_mililitros = cantidad_taza_agua * taza_agua + cantidad_cucharada_aceite * cucharada_aceite

    print("Total de ingredientes en gramos: {total_gramos} gramos")
    print("Total de ingredientes en mililitros: {total_mililitros} mililitros")

