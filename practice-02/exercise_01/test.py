from SavingBank import SavingBank


def test():
    print("Para crear la cuenta ingrese los siguientes datos: \n")
    account_number = input("Nro de cuenta: ")
    cuil = input("CUIL: ")
    last_name = input("Apellido: ")
    first_name = input("Nombre: ")
    balance = float(input("Saldo: "))

    first_account = SavingBank(account_number, cuil, last_name, first_name, balance)
    second_account = SavingBank(account_number='2', cuil='20410266928', last_name='Gambarte', first_name='German',
                                balance=0)


    extraction = first_account.extract(10)
    if extraction == -1:
        print("La extracción falló")
    else:
        print("La extracción fué exitosa")
        print("Su saldo actual es:", extraction)

    extraction = second_account.extract(10)
    if extraction == -1:
        print("La extracción falló")
    else:
        print("La extracción fué exitosa")
        print("Su saldo actual es:", extraction)


    deposit =  first_account.deposit(10)
    if deposit == -1:
        print("El depósito falló")
    else:
        print("El depósito fué exitoso")
        print("Su saldo actual es:", deposit)

    deposit =  first_account.deposit(-10)
    if deposit == -1:
        print("El depósito falló")
    else:
        print("El depósito fué exitoso")
        print("Su saldo actual es:", deposit)


    is_valid_cuil = first_account.validate_cuil()

    if is_valid_cuil:
        print("El CUIL es válido")
    else:
        print("El CUIL no es válido")
