def modelo(opczap):
    if opczap == 1:
        return "joy", 45
    elif opczap == 2:
        return "middle", 60
    elif opczap == 3:
        return "split", 55
    elif opczap == 4:
        return "team", 70
    elif opczap == 5:
        return "edge", 80
def factura(cli, sub):
    iva = sub * 0.15
    tot = sub + iva
    print()
    print("factura")
    print("cliente:", cli)
    print("subtotal:", sub)
    print("iva:", iva)
    print("total:", tot)
def tienda():
    print("zapatos fade")
    print("bienvenido")
    cli = input("ingrese su nombre: ")
    subgen = 0
    op = 0
    while op != 6 and op != 7:
        print()
        print("1 joy $45")
        print("2 middle $60")
        print("3 split $55")
        print("4 team $70")
        print("5 edge $80")
        print("6 pagar")
        print("7 salir")
        op = int(input("seleccione una opcion: "))
        if op >= 1 and op <= 5:
            modelzp, pre = modelo(op)
            cant = int(input("ingrese cantidad: "))
            sub = pre * cant
            subgen = subgen + sub
            print("producto agregado")
            print("modelo:", modelzp)
            print("subtotal acumulado:", subgen)
            print()
            print("1 comprar otro")
            print("2 pagar")
            op2 = int(input("opcion: "))
            if op2 == 2:
                op = 6
        elif op == 6:
            if subgen > 0:
                factura(cli, subgen)
            else:
                print("no hay productos en el carrito")
                print("gracias por visitarnos")
        elif op == 7:
            print("gracias por visitarnos")
        else:
            print("opcion no valida")
op3 = 1
while op3 == 1:
    tienda()
    print()
    print("1 iingresar nuevamente")
    print("2 salir")
    op3 = int(input("opcion: "))
print("sistema finalizado")
