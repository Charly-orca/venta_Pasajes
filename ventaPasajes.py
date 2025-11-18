
# carlos_Alberto_ochoa
# 362
# 4


# --- Variables Globales para el reporte final ---
total_recaudado = 0
pasajes_cucuta = 0
pasajes_bucaramanga = 0
pasajes_bochalema = 0


def Datos():
    """
    Muestra opciones, pregunta destino, clase y cantidad.
    Valida y retorna los datos.
    """

    # --- Validación de Destino ---
    destino_valido = ""
    while True:
        print("\n--- Destinos Disponibles ---")
        print("1. Cúcuta")
        print("2. Bucaramanga")
        print("3. Bochalema")

        # Usamos .title() para estandarizar (ej: "cucuta" -> "Cucuta")
        # Usamos .strip() para quitar espacios al inicio o final
        destino_input = input("Escriba el nombre del destino: ").title().strip()

        # Corregimos el acento si el usuario no lo pone
        if destino_input == "Cucuta":
            destino_input = "Cúcuta"

        if destino_input in ["Cúcuta", "Bucaramanga", "Bochalema"]:
            destino_valido = destino_input
            break  # Sale del bucle si el destino es válido
        else:
            print("Error: Destino no válido. Intente de nuevo.")

    # --- Validación de Clase ---
    clase_valida = 0
    while True:
        try:
            clase_input = int(input(f"Clase para {destino_valido} (1, 2 o 3): "))
            if 1 <= clase_input <= 3:
                clase_valida = clase_input
                break  # Sale del bucle si la clase es válida
            else:
                print("Error: La clase debe ser 1, 2 o 3.")
        except ValueError:
            print("Error: Debe ingresar un número.")

    # --- Validación de Cantidad ---
    cantidad_valida = 0
    while True:
        try:
            cantidad_input = int(input("Cantidad de pasajes a comprar: "))
            if cantidad_input > 0:
                cantidad_valida = cantidad_input
                break  # Sale del bucle si la cantidad es válida
            else:
                print("Error: Debe comprar al menos 1 pasaje.")
        except ValueError:
            print("Error: Debe ingresar un número.")

    return destino_valido, clase_valida, cantidad_valida


def ValorPa(destino, clase):
    """
    Recibe el destino (string) y la clase (int) y
    retorna el valor base del pasaje.
    """
    if destino == "Cúcuta":
        if clase == 1:
            return 20000
        elif clase == 2:
            return 15000
        elif clase == 3:
            return 12000

    elif destino == "Bucaramanga":
        if clase == 1:
            return 30000
        elif clase == 2:
            return 25000
        elif clase == 3:
            return 20000

    elif destino == "Bochalema":
        if clase == 1:
            return 10000
        elif clase == 2:
            return 8000
        elif clase == 3:
            return 5000

    return 0  # No debería ocurrir si Datos() valida bien


def Descu(cantidad):
    """
    Recibe la cantidad de pasajes y retorna
    el porcentaje de descuento (ej: 0.10 para 10%).
    """
    if cantidad <= 5:
        return 0.0  # 0% de descuento (Menos de 5 incluye 5)
    elif 6 <= cantidad <= 12:
        return 0.10  # 10% de descuento
    else:  # Más de 12
        return 0.20  # 20% de descuento


def Pago(cantidad, valor_base_pasaje, porcentaje_descuento):
    """
    Recibe cantidad, valor base y porcentaje de descuento.
    Retorna el valor final a pagar.
    """
    costo_bruto = cantidad * valor_base_pasaje
    valor_del_descuento = costo_bruto * porcentaje_descuento
    total_a_pagar = costo_bruto - valor_del_descuento

    return total_a_pagar, costo_bruto, valor_del_descuento


def Menu():
    """
    Función principal que muestra el menú y gestiona la venta.
    """
    # Indicar que usaremos las variables globales para modificarlas
    global total_recaudado, pasajes_cucuta, pasajes_bucaramanga, pasajes_bochalema

    while True:
        print("\n--- VIAJES ---")
        print("1. Vender pasaje")
        print("2. Salir")
        opcion = input("¿Cuál es su opción? ")

        if opcion == "1":
            # --- Proceso de Venta ---
            destino, clase, cantidad = Datos()

            valor_unitario = ValorPa(destino, clase)
            porcentaje_desc = Descu(cantidad)

            total_venta, costo_bruto, vlr_descuento = Pago(cantidad, valor_unitario, porcentaje_desc)

            # --- Mostrar Resumen de la Venta ---
            print("\n--- Resumen de Venta ---")
            print(f"Destino:         {destino}")
            print(f"Clase:           {clase}")
            print(f"Cantidad:        {cantidad}")
            print(f"Valor Unitario:  ${valor_unitario:,.0f}")
            print(f"Costo Bruto:     ${costo_bruto:,.0f}")
            print(f"Descuento ({porcentaje_desc * 100:.0f}%): -${vlr_descuento:,.0f}")
            print("-----------------------------")
            print(f"TOTAL A PAGAR:   ${total_venta:,.0f}")

            # --- Actualizar Totales Globales ---
            total_recaudado += total_venta
            if destino == "Cúcuta":
                pasajes_cucuta += cantidad
            elif destino == "Bucaramanga":
                pasajes_bucaramanga += cantidad
            elif destino == "Bochalema":
                pasajes_bochalema += cantidad

            input("\nPresione Enter para volver al menú...")

        elif opcion == "2":
            # --- Salir y Mostrar Reporte Final ---
            print("\n--- REPORTE FINAL DE VENTAS ---")
            print(f"Pasajes vendidos para Cúcuta:     {pasajes_cucuta}")
            print(f"Pasajes vendidos para Bucaramanga: {pasajes_bucaramanga}")
            print(f"Pasajes vendidos para Bochalema:   {pasajes_bochalema}")
            print("-----------------------------------")
            print(f"TOTAL RECAUDADO GENERAL:         ${total_recaudado:,.0f}")
            print("\n¡Gracias por usar el sistema! Adiós.")
            break  # Rompe el bucle while y termina el programa

        else:
            print("Error: Opción no válida. Intente de nuevo.")


# --- Punto de entrada principal del programa ---
if __name__ == "__main__":
    Menu()