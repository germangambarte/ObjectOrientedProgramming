namespace Exercise04;

public class Driver
{
    public string Plate { get; private set; }
    public string Brand { get; private set; }
    public string FirstName { get; private set; }
    public string LastName { get; private set; }
    public int Mileage { get; private set; }

    public Driver(string plate, string brand, string firstName, string lastName, int mileage)
    {
        Plate = plate;
        Brand = brand;
        FirstName = firstName;
        LastName = lastName;
        Mileage = mileage;
    }
}