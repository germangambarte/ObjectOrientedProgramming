using System.Data.Common;
using System.Diagnostics;
using Microsoft.VisualBasic.FileIO;

namespace Exercise04;

public class DriversManager
{
    public List<Driver> Drivers { get; } = [];

    public void LoadDriver()
    {
        //var path = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "datosMotos.csv");

        using TextFieldParser parser = new("../../../../Exercise04/datosMotos.csv");
        parser.TextFieldType = FieldType.Delimited;
        parser.SetDelimiters(",");
        parser.ReadLine();

        while (!parser.EndOfData)
        {
            var row = parser.ReadFields()!;
            var newDriver = new Driver(
                plate: row[0],
                brand: row[1],
                firstName: row[2],
                lastName: row[3],
                mileage: int.Parse(row[4])
            );
            Drivers.Add(newDriver);
        }
    }
}