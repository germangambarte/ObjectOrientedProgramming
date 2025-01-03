using Exercise01;

Test();
return;

void Test()
{
    Console.WriteLine("Ingrese los siguientes datos:");
    Console.Write("\tNro de cuenta: ");
    var accountNumber = Console.ReadLine()!;
    Console.Write("\tCuil: ");
    var cuil = Console.ReadLine()!;
    Console.Write("\tNombre: ");
    var firstName = Console.ReadLine()!;
    Console.Write("\tApellido: ");
    var lastName = Console.ReadLine()!;
    Console.Write("\tSaldo: ");
    var balance = decimal.Parse(Console.ReadLine()!);
    var firstAccount = new SavingBank(accountNumber,
        cuil,
        firstName,
        lastName,
        balance
    );
    var secondAccount = new SavingBank(
        accountNumber: "2",
        cuil: "20410266920",
        lastName: "Gambarte",
        firstName: "German",
        balance: 123
    );
    Console.WriteLine("\nExtract\n");
    var result = firstAccount.Extract(0);
    Console.WriteLine(result == -1 ? "Fallo la operación." : $"Saldo actual de {nameof(firstAccount)}: {result}");

    result = secondAccount.Extract(100);
    Console.WriteLine(result == -1 ? "Fallo la operación." : $"Saldo actual de {nameof(secondAccount)}: {result}");

    Console.WriteLine("\nDeposit\n");
    result = firstAccount.Deposit(0);
    Console.WriteLine(result == -1 ? "Fallo la operación." : $"Saldo actual de {nameof(firstAccount)}: {result}");

    result = secondAccount.Deposit(100);
    Console.WriteLine(result == -1 ? "Fallo la operación." : $"Saldo actual de {nameof(secondAccount)}: {result}");

    Console.WriteLine("\nValidateCuil\n");
    Console.WriteLine(firstAccount.ValidateCuil()
        ? $"CUIL de {nameof(firstAccount)} válido"
        : $"CUIL de {nameof(firstAccount)} no válido");
    Console.WriteLine(secondAccount.ValidateCuil()
        ? $"CUIL de {nameof(secondAccount)} válido"
        : $"CUIL de {nameof(secondAccount)} no válido");
}