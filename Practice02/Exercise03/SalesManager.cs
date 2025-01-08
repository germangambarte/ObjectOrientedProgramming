namespace Exercise03;

public class SalesManager
{
    public decimal[,] Sales {  get; set; }

    public SalesManager()
    {
        Sales = new decimal[5, 7];
    }

    public void AddBill(int day, int branch, decimal bill)
    {
        if (day is < 1 or > 7)
        {
            throw new ArgumentException("Los días deben ser entre 1 y 7");
        }

        if (branch is < 1 or > 5)
        {
            throw new ArgumentException("Las sucursales deben ser entre 1 y 5");
        }
        
        Sales[branch-1, day-1] += bill;
    }

    public decimal GetTotalBillPerWeekByBranch(int branch)
    {
        if (branch is < 1 or > 5)
        {
            throw new ArgumentException("Las sucursales deben ser entre 1 y 5");
        }
        var total = 0M;
        var upperBound = Sales.GetUpperBound(0);
        for (var i = 0; i <= Sales.GetUpperBound(1); i++)
        {
            total += Sales[branch-1, i];
        }
        return total;
    }

    public decimal GetMaxBillOfTheDay(int day)
    {
        if (day is < 1 or > 7)
        {
            throw new ArgumentException("Los días deben ser entre 1 y 7");
        }
        var max = 0M;
        var indexMax = decimal.MinValue;
        for (var i = 0; i <= Sales.GetUpperBound(0); i++)
        {
            if (Sales[i, day-1] <= max) continue;
            max = Sales[i, day-1];
            indexMax = i;
        }

        return indexMax + 1;
    }
    
    public decimal GetMinBillOfTheWeek()
    {
        var min = decimal.MaxValue;
        var indexMin = decimal.MinValue;
        
        for (var i = 0; i <= Sales.GetUpperBound(0); i++)
        {
            for (var j = 0; j <= Sales.GetUpperBound(1); j++)
            {
                if (Sales[i, j] >= min) continue;
                min = Sales[i, j];
                indexMin = i;
            }
        }

        return indexMin +1;
    }
    
    public decimal GetTotalBillOfTheWeek()
    {
        var total = decimal.Zero;
        for (var i = 0; i <= Sales.GetUpperBound(0); i++)
        {
            for (var j = 0; j <= Sales.GetUpperBound(1); j++)
            {
                total += Sales[i, j];
            }
        }

        return total;
    }
}