namespace Exercise01;

public class SavingBank
{
    public string AccountNumber { get; private set; }
    public string Cuil { get; private set; }
    public string LastName { get; private set; }
    public string FirstName { get; private set; }
    public decimal Balance { get; private set; }

    public SavingBank(string accountNumber, string cuil, string lastName, string firstName, decimal balance)
    {
        AccountNumber = accountNumber;
        Cuil = cuil;
        LastName = lastName;
        FirstName = firstName;
        Balance = balance;
    }

    public void ShowData()
    {
        Console.WriteLine("Datos de la cuenta:");
        Console.WriteLine($"\tNúmero de cuenta: {AccountNumber}");
        Console.WriteLine($"\tCuil: {Cuil}");
        Console.WriteLine($"\tApellido: {LastName}");
        Console.WriteLine($"\tNombre: {FirstName}");
        Console.WriteLine($"\tSaldo: {Balance}");
    }

    public decimal Extract(decimal amount)
    {
        if (amount <= 0)
        {
            Console.WriteLine("La cifra debe ser mayor a $0.");
            return -1;
        }

        if (amount > Balance)
        {
            Console.WriteLine("Saldo insuficiente.");
            return -1;
        }

        Balance -= amount;
        return Balance;
    }

    public decimal Deposit(decimal amount)
    {
        if (amount <= 0)
        {
            Console.WriteLine("La cifra debe ser mayor a $0.");
            return -1;
        }

        Balance += amount;
        return Balance;
    }

    public bool ValidateCuil()
    {
        if (Cuil.Length != 11)
        {
            Console.WriteLine("Cuil no válido.");
            return false;
        }

        var genre = Cuil.Substring(0, 2);
        var validationDigit = Cuil.Substring(Cuil.Length - 1, 1);
        int[] validGenres = [20, 23, 27, 30];
        int[] factorsForDniValidation = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2];

        if (!validGenres.Contains(int.Parse(genre)))
        {
            Console.WriteLine("Género no válido");
            return false;
        }

        var sum = 0;
        for (var i = 0; i < 10; i++)
        {
            sum += int.Parse(Cuil[i].ToString()) * factorsForDniValidation[i];
        }

        var module = sum % 11;
        switch (module)
        {
            case 0 when validationDigit == "0":
            case 1 when validationDigit == "9" && genre == "23":
            case 1 when validationDigit == "4" && genre == "23":
                return true;
            default:
                return int.Parse(validationDigit) == 11 - module;
        }
    }
}