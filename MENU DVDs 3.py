"""
Author: Sebastian Denhi Vega Saint Martin
Date: 03/05/2022
Description: This program connects with an SQL Database and shows a menu for the user so it can be edited and seen,
"""
import sqlite3
print(" ")
print("Bienvenido al programa de DVDs")

opc = -1

def submenu(tipo):
    """
    It takes a string as an argument, prints a menu, gets an integer from the user, and returns that
    integer
    
    :return: the value of opc_int.
    """
    opc_int= -1
    print("*********************************************************")
    print("Usted esta en el submenu para " + tipo + " por seleccion")
    print("Ingrese 1 para " + tipo + " por año")
    print("Ingrese 2 para " + tipo + " por director")
    print("Ingrese 3 para " + tipo + " duracion")
    print("Ingrese 4 para " + tipo + " nombre")
    if tipo == "eliminar":
        print("Ingrese 5 para " + tipo + " por codigo")
    print("Ingrese 0 para regresar al menú principal")
    opc_int = int(input("Ingrese una opción para iniciar: "))
    print("*********************************************************")

    if opc_int == 1:
        pass
    elif opc_int == 2:
        pass
    elif opc_int == 3:
        pass
    elif opc_int == 4:
        pass
    elif opc_int == 5 and tipo == "eliminar":
        pass
    elif opc_int == 0:
        pass      
            
    return opc_int
def add_dvd():
    """
    It asks the user for the title, year, length, and director of a movie, and then inserts that
    information into the database
    """
    conexion = connect_dvd()
    Titulo = str(input("Ingrese el titulo de la pelicula: "))
    Año = int(input("Ingrese el año de la pelicula: "))
    Long = int(input("Ingrese la longitud de la pelicula: "))
    Dir = str(input("Ingrese el director de la pelicula: "))
    conexion.execute("insert into DVDs(Titulo,A_lanza,Tam_min,Director) values (?,?,?,?)", (Titulo, Año, Long, Dir))
    conexion.commit()
    conexion.close()  
def edit_dvd():
    """
    It takes the user's input and updates the database with the new information
    """
    conexion = connect_dvd()
    var_opc = "None"
    if opc_e == 1:
        var_opc = "el año"
    elif opc_e == 2:
        var_opc = "el director"
    elif opc_e == 3:
        var_opc = "la duracion"
    elif opc_e == 4:
        var_opc = "el nombre"
    else:
        print("Error seleccione una opcion valida")
    

    print("Estas son las peliculas que tiene actualmente")
    show_table_dvd()
    i = int(input("Ingrese el codigo de la pelicula que quiere editar " + var_opc + ": "))
    edit = input("Ingresa " + var_opc + " nuevo/a de la pelicula: ")

    if opc_e == 1:
        cursor = conexion.execute("update DVDs set A_lanza = ? where codigo = ?", (edit, i, ))
    elif opc_e == 2:
        cursor = conexion.execute("update DVDs set Director = ? where codigo = ?", (edit, i, ))
    elif opc_e == 3:
        cursor = conexion.execute("update DVDs set Tam_min = ? where codigo = ?", (edit, i, ))
    elif opc_e == 4:
        cursor = conexion.execute("update DVDs set Titulo = ? where codigo = ?", (edit, i, ))

    print("Listo! " + var_opc + " de la pelicula con codigo " + str(i) + " fue editado a " + edit)
    conexion.commit()
    conexion.close()
def delete_dvd():
    """
    It deletes a row from the database based on the user's input
    """
    conexion = connect_dvd()
    var_opc = "None"
    elecc = 0
    if opc_d == 1:
        var_opc = "el año"
    elif opc_d == 2:
        var_opc = "el director"
    elif opc_d == 3:
        var_opc = "la duracion"
    elif opc_d == 4:
        var_opc = "el nombre"
    elif opc_d == 5:
        var_opc = "el codigo"
    else:
        print("Error seleccione una opcion valida")

    if opc_d == 1:
        print("Estas son sus peliculas")
        show_table_dvd()
        i = (input("Ingrese " + var_opc + " a eliminar: "))
        print("Esto eliminara todas las peliculas con Año: " + i)
        elecc = int(input("Desea continuar? (Si desea eliminar una sola pelicula elimine por codigo) \n1=si 2=no: "))
        if elecc == 1:
            cursor = conexion.execute("delete from DVDs where A_lanza = ?", (i, ))
        elif elecc == 2:
            print("Regresando al Menu")
        else:
            print("Error, seleccione una opcion valida, regresando al menu")
    elif opc_d == 2:
        print("Estas son sus peliculas")
        show_table_dvd()
        i = (input("Ingrese " + var_opc + " a eliminar: "))
        print("Esto eliminara todas las peliculas con Director: " + i)
        elecc == int(input("Desea continuar? (Si desea eliminar una sola pelicula elimine por codigo) \n1=si 2=no"))
        if elecc == 1:
            cursor = conexion.execute("delete from DVDs where Director = ?", (i, ))
        elif elecc == 2:
            print("Regresando al Menu")
        else:
            print("Error, seleccione una opcion valida, regresando al Menu")
    elif opc_d == 3:
        print("Estas son sus peliculas")
        show_table_dvd()
        i = (input("Ingrese " + var_opc + " a eliminar: "))
        print("Esto eliminara todas las peliculas con Duracion: " + i)
        elecc == int(input("Desea continuar? (Si desea eliminar una sola pelicula elimine por codigo) \n1=si 2=no"))
        if elecc == 1:
            cursor = conexion.execute("delete from DVDs where Tam_min = ?", (i, ))
        elif elecc == 2:
            print("Regresando al Menu")
        else:
            print("Error, seleccione una opcion valida, regresando al submenu")
    elif opc_d == 4:
        print("Estas son sus peliculas")
        show_table_dvd()
        i = (input("Ingrese " + var_opc + " a eliminar: "))
        print("Esto eliminara todas las peliculas con Titulo: " + i)
        elecc == int(input("Desea continuar? (Si desea eliminar una sola pelicula elimine por codigo) \n1=si 2=no"))
        if elecc == 1:
            cursor = conexion.execute("delete from DVDs where Titulo = ?", (i, ))
        elif elecc == 2:
            print("Regresando al Menu")
        else:
            print("Error, seleccione una opcion valida, regresando al Menu")
    elif opc_d == 5:
        print("Estas son sus peliculas")
        show_table_dvd()
        i = (input("Ingrese " + var_opc + " a eliminar: "))
        cursor = conexion.execute("delete from DVDs where codigo = ?", (i, ))

    conexion.commit()
    if elecc == 1:
            print("La pelicula con " + str(var_opc) + " " + str(i) + " fue eliminada")
    elif elecc == 2:
            pass
    conexion.close()
def show_table_dvd():
    """
    It connects to the database, executes a query, prints the results, and closes the connection
    """
    conexion = connect_dvd()
    cursor = conexion.execute("select codigo,Titulo,A_lanza,Tam_min,Director from DVDs")
    for fila in cursor:
        print(fila)
    conexion.close()
def show_line_dvd():
    """
    It connects to the database, asks the user for an ID, then searches the database for a row with that
    ID, and if it finds one, it prints the row
    """
    conexion = connect_dvd()
    id_db = int(input("Ingresa el ID de la pelicula: "))
    cursor = conexion.execute("select Titulo,A_lanza,Tam_min,Director from DVDs where codigo =?", (id_db, ))
    fila = cursor.fetchone()
    if fila != None:
        print(fila)
    else:
        print("No existe un elemento con este ID.")
    conexion.close()
def show_all_lines_dvd():
    """
    It connects to the database, asks the user for a value, and then uses that value to search the
    database for a match
    """
    conexion = connect_dvd()
    var_opc = "None"
    if opc_b == 1:
        var_opc = "el año"
    elif opc_b == 2:
        var_opc = "el director"
    elif opc_b == 3:
        var_opc = "la duracion"
    elif opc_b == 4:
        var_opc = "el nombre"
    else:
        print("Error seleccione una opcion valida")

    i = (input("Ingrese " + var_opc + " para buscar: "))
    if opc_b == 1:
        cursor = conexion.execute("select Titulo,A_lanza,Tam_min,Director from DVDs where A_lanza=?", (i, ))
    elif opc_b == 2:
        cursor = conexion.execute("select Titulo,A_lanza,Tam_min,Director from DVDs where Director=?", (i, ))
    elif opc_b == 3:
        cursor = conexion.execute("select Titulo,A_lanza,Tam_min,Director from DVDs where Tam_min=?", (i, ))
    elif opc_b == 4:
        cursor = conexion.execute("select Titulo,A_lanza,Tam_min,Director from DVDs where Titulo=?", (i, ))
        
    filas = cursor.fetchall()
    if len(filas)>0:
        for fila in filas:
            print(fila)
    else:
        print("No existen peliculas con esta seleccion")
    conexion.close()
def connect_dvd():
    """
    It connects to the database and returns the connection object
    :return: The connection to the database.
    """
    conexion = sqlite3.connect("DVDs.db")
    return conexion
def create_dvd():
    """
    It creates a table called DVDs in the database called dvd.db
    """
    conexion = connect_dvd()
    try:
        conexion.execute("""create table DVDs (codigo integer primary key autoincrement,
                         Titulo text, A_lanza integer, Tam_min integer, Director text)""")
        print("Se creo la tabla DVDs")
        
    except sqlite3.OperationalError:
        print(" ")
    conexion.close()
create_dvd()


while opc != 0:
    print("--------------------------------------------------------------------------- ")
    print("Ingrese 1 para añadir un DVD")
    print("Ingrese 2 para editar la informacion de un DVD")
    print("Ingrese 3 para eliminar un DVD")
    print("Ingrese 4 para mostrar todos los DVDs")
    print("Ingrese 5 para buscar un DVD por ID")
    print("Ingrese 6 para buscar todos los DVDs por Año/Director/Duracion/Nombre")
    print("Ingrese 0 para terminar el programa")
    opc = int(input("Ingrese una opción para iniciar: "))
    print("---------------------------------------------------------------------------")
    
    if opc == 1:
        add_dvd()
    elif opc == 2:
        opc_e = submenu("editar")
        edit_dvd()
    elif opc == 3:
        opc_d = submenu("eliminar")
        delete_dvd()
    elif opc == 4:
        show_table_dvd()
    elif opc == 5:
        show_line_dvd()
    elif opc ==6:
        opc_b = submenu("buscar")
        show_all_lines_dvd()
    elif opc == 0:
        print("La sesion termino \nGracias por utilizar este programa, vuelva pronto")
        break