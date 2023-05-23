# Nuestro programa va a tener 4 funciones principales a partir de 4 selecciones en forma de listas en la cual se le agregaron 5 jugadores con 6 datos tambien en forma de listas, este programa va a tener la habilidad de mostrar, añadir, eliminar y modificar jugadores cuales quiera.
Argentina = [["Lionel Andres Messi", "35", "1.70m", "68Kg", "ED"], ["Damián Martínez", "30", "1.80m", "75kg", "PO"],
            ["Angel di Madria", "34", "1.85m", "75kg", "ED"], ["Lisandro Martinez", "25", "1.75m","77kg","LB"],
            ["Laurato Martinez","25","1.74m","72kg","ST"]]
Colombia = [["Luis Fernando Diaz","25","1.80m","65kg","ED"], ["James Rodriguez","31","1.80m","75kg","CAM"],
            ["Juan Guillermo Cuadrado","35","1.82m","60kg","ED"], ["David Ospina","21","1.60m","55kg","PO"],
            ["Radamel Falcao Garcia","35","1.70m","85kg","ST"]]
Brasil = [["Neymar","25","1.70m","85kg","ED"], ["Ronandinho","44","1.70m","85kg","ED"],
        ["Ronaldo Nazario","45","1.60m","75kg","ST"], ["PELE","88","1.70m","85kg","DT"],
        ["Dani alves","39","1.79m","95kg","LB"]]
España = [["Iker Casillas","44","1.89m","65kg","PO"], ["Andres Iniesta","35","1.69m","85kg","CAM"],
        ["Xavi Hernandez","48","1.59m","55kg","CAM"], ["Raul Garcia","75","1.70m","45kg","ST"],
        ["Sergio Ramos","68","1. 83m","75kg","DEC"]]
Uruguay = [["Luis Suarez", "34", "1.72", "70Kg", "ST"], ["Federico Valverde", "28", "1.70", "68Kg", "CAM"],
        ["Muslera", "36", "1.76", "68Kg", "PO"], ["Edison Cavani", "40", "1.78", "69Kg", "DC"],
        ["Diego Godin", "41", "1.72", "66Kg", "CB" ]]
Belgica = [["Kevin de Bruyne", "29", "1.73", "69Kg", "CAM"], ["Thibaut Courtois", "32", "1.84", "60Kg", "PO"],
        ["Romelo Lukaku", "37", "1.78", "70Kg", "DC"], ["Eden Hazard", "40", "1.60", "67Kg", "ED"],
        ["Yannick Carrasco", "35", "1.70", "68Kg", "ED"]]
# se crea una funcion llamada mostrar para mostrar todas las selecciones y en que grupan estan con cada jugador.
def mostrar(seleccion, nombre_seleccion, grupo):
    print(f"{grupo}\nSeleccion {nombre_seleccion}")
    for jugador in seleccion:
        print(jugador)
# se creo una funcion llamado listado_selccion para mostrar la seleccion que se ponga en el parametro seleccion y que cada jugador tenga su enumeracion.
def listado_seleccion(seleccion):
    i = 0
    for jugador in seleccion:
        i = i + 1
        print(f"{i}: {jugador}")
# se creo una funcion llamada registro_jugador para que el programa pueda añadir varios jugadores con sus respectivos datos.
def registro_jugador(seleccion):
    print("Digite los siguientes datos")
    nombre = input("Ingrese el nombre del jugador: ")
    edad = int(input("Ingrese la edad del jugador: "))
    estatura = float(input("Igrese la estatura: "))
    peso = int(input("Igrese el peso: "))
    posicion = input("Ingrese la posicion del jugador: ")
    juga = [nombre, edad, estatura, peso, posicion]
    seleccion.append(juga)
    print("¡jugador guardado con éxito!")
# se creo una funcion llamada jugador a eliminar para saber el indice del jugador que se quiera eliminar y su metodo de eliminacion.
def jugador_a_eliminar(numero, seleccion):
    indice = numero - 1
    del seleccion[indice]
# esta funcion de eliminacion general se hizo para que el usuario digite el numero del jugador que quiera eliminar y se llamo a la anterior funcion de jugador a eliminar para usar la posicion del elemento y eliminar, para que finalmente se llame a la funcion mostrar y que imprima la seleccion para mostrar que el jugador se elimino correctamente.
def eliminar_general(seleccion, nombre_seleccion):
    listado_seleccion(seleccion)
    print("Digite el numero del jugador que desea eliminar")
    jugador_eliminado = int(input())
    jugador_a_eliminar(jugador_eliminado, seleccion)
    mostrar(seleccion, f"{nombre_seleccion}", " ")
# esta funcion de modificar general se le llamo a listado seleccion para saber a que jugador se desea modificar y que el usuario al elegir el numero se utiliza la misma sintaxis del indice para encontrar la posicion del jugador que se quiera modificar, finalmente el usuario digita los datos como si fuera a registrar uno nuevo y se le reemplaza con el jugador que se eligio.
def modificar_general(seleccion, nombre_seleccion):
    listado_seleccion(seleccion)
    print("digite el numero del jugador que desea modificar")
    numero_jugador = int(input())
    indice = numero_jugador - 1
    jugador_a_modificar = seleccion[indice]
    print("Digite los siguientes datos")
    nombre = input("Ingrese el nombre del jugador: ")
    edad = int(input("Ingrese la edad del jugador: "))
    estatura = float(input("Igrese la estatura: "))
    peso = int(input("Igrese el peso: "))
    posicion = input("Ingrese la posicion del jugador: ")
    juga = [nombre, edad, estatura, peso, posicion]
    jugador_a_modificar[0:len(seleccion)] = juga
    mostrar(seleccion, f"{nombre_seleccion}", " ")
    print("Jugador modificado con exito")
# en este apartado ya se entra al pograma haciendo un bucle while dando la introduccion y que el usuario escoga cualquier de las 4 funciones que tiene el programa.
def bucle_menu():
    i=0
    while (i==0):
        print("Bienvenidos a la cooa mundial 2026")
        print("***Menú***"),
        print("1. Mostrar listas\n2. Registrar jugador\n3. Eliminar jugador\n4. Modificar\n5. salir")
        opcion = int(input())
        if opcion == 1:   # para saber que hacer despues de que el usuario seleccion cualquier opcion utilizamos las condicionales.
            def bucle_submenu(): # aqui se crea una funcion para crear otro bucle para separar el menu y los submenu que se va a tener en el programa y que el usurio tenga la opcion de volver al menu o submenu anterior.
                m=0
                while m == 0:
                    print("Mostrar lista por:\n1. Grupo\n2. seleccion\n3. volver\n4. salir")
                    opcion_mostrar = int(input())
                    if opcion_mostrar == 1: # en esta condicional llamamos a la funcion de mostrar y poniendo los parametros de cada seleccion.
                        mostrar(Argentina, "Argentina", "Grupo A")
                        mostrar(Colombia, "Colombia", " ")
                        mostrar(Brasil, "Brasil", "Grupo B")
                        mostrar(España, "España", " ")
                        mostrar(Uruguay, "Uruguay", "Grupo C")
                        mostrar(Belgica, "Belgica", " ")
                    elif opcion_mostrar == 2:
                        k = 0
                        while k == 0:
                            print("Selecciones:\n1. Argentina\n2. Colombia\n3. Brasil\n4. España\n5. Uruguay\n6. Belgica\n7. volver")
                            opcion_mostrar_selecciones = int(input())
                            if opcion_mostrar_selecciones == 1:
                                mostrar(Argentina, "Argentina", " ")
                            elif opcion_mostrar_selecciones == 2:
                                mostrar(Colombia, "Colombia", " ")
                            elif opcion_mostrar_selecciones == 3:
                                mostrar(Brasil, "Brasil", " ")
                            elif opcion_mostrar_selecciones == 4:
                                mostrar(España, "España", " ")
                            elif opcion_mostrar_selecciones == 5:
                                mostrar(Uruguay, "Uruguay", " ")
                            elif opcion_mostrar_selecciones == 6:
                                mostrar(Belgica, "Belgica", " ")
                            elif opcion_mostrar_selecciones == 7:
                                bucle_submenu()
                            else:
                                print("Opcion invalida")
                    elif opcion_mostrar ==3:
                        bucle_menu()
                    elif opcion_mostrar == 4:
                        exit()
                    else:
                        print("Opcion invalida")
            bucle_submenu()
        elif opcion == 2:
            l = 0
            while l == 0:
                print("¿A que seleccion lo desea registrar?")
                print("Selecciones:\n1. Argentina\n2. Colombia\n3. Brasil\n4. España\n5. Uruguay\n6. Belgica\n7. volver\n8.salir")
                opcion_registro = int(input())
                if opcion_registro == 1: #en esta condicional de registrar jugador llamamos a la funcion que nos permite añadir a los jugadores que el usuario desee.
                    print("***Registrar jugador***")
                    registro_jugador(Argentina)
                    mostrar(Argentina[len(Argentina)-1], "Argentina", " ")
                elif opcion_registro == 2:
                    registro_jugador(Colombia)
                    mostrar(Colombia[len(Colombia)-1], "Colombia", " ")
                elif opcion_registro == 3:
                    registro_jugador(Brasil)
                    mostrar(Brasil[len(Brasil)-1], "Brasil", " ")
                elif opcion_registro == 3:
                    registro_jugador(España)
                    mostrar(España[len(España)-1], "España", " ")
                elif opcion_registro == 3:
                    registro_jugador(Uruguay)
                    mostrar(Uruguay[len(Uruguay)-1], "Uruguay", " ")
                elif opcion_registro == 3:
                    registro_jugador(Belgica)
                    mostrar(Belgica[len(Belgica)-1], "Belgica", " ")
                elif opcion_registro == 7:
                    bucle_menu()
                elif opcion_registro == 8:
                    exit()
                else:
                    print("opcion invalida")
        elif opcion == 3:
            print("*** eliminar ***")
            print("¿A que seleccion es el jugador que desea eliminar?")
            print("Selecciones:\n1. Argentina\n2. Colombia\n3. Brasil\n4. España\n5. Uruguay\n6. Belgica\n7. volver\n8.salir")
            eliminado = int(input()) #en esta condicional llamamos a la funcion que nos permite eliminar al jugador que el usuario escoga a partir del numero de su posicion
            if eliminado == 1:
                eliminar_general(Argentina, "Argentina")
            elif eliminado == 2:
                eliminar_general(Colombia, "Colombia")
            elif eliminado == 3:
                eliminar_general(Brasil, "Brasil")
            elif eliminado == 4:
                eliminar_general(España, "España")
            elif eliminado == 5:
                eliminar_general(Uruguay, "Uruguay")
            elif eliminado == 6:
                eliminar_general(Belgica, "Belgica")
            elif eliminado == 7:
                bucle_menu()
            elif eliminado == 8:
                exit()
            else:
                print("opcion invalida")
        elif opcion == 4:
            print("***Modificar***")
            print("¿A que seleccion es el jugador que deseas modificar?")
            print("Selecciones:\n1. Argentina\n2. Colombia\n3. Brasil\n4. España\n5. Uruguay\n6. Belgica\n7. volver\n8.salir")
            modificar = int(input()) # en esta condicional llamamos a la funcion modificar para que a partir de la posicion del jugador que el usuario escoga se cree uno nuevo y se le reeemplace.
            if modificar == 1:
                modificar_general(Argentina, "Argentina")
            elif modificar == 2:
                modificar_general(Colombia, "Colombia")
            elif modificar == 3:
                modificar_general(España, "España")
            elif modificar == 4:
                modificar_general(España, "España")
            elif modificar == 5:
                modificar_general(Uruguay, "Uruguay")
            elif modificar == 6:
                modificar_general(Belgica, "Belgica")
            elif modificar == 7:
                bucle_menu()
            elif modificar == 8:
                exit() #exit nos permite salir del bucle y cerrar el programa
            else:
                print("opcion invalida")
        else:
            print("opcion invalida")
bucle_menu()