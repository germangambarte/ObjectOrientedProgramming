namespace Exercise02;

public class PharmacyController
{
    private decimal[,] Billings = new decimal[BranchsQuantity, DaysQuantity];
    private const int DaysQuantity = 7;
    private const int BranchsQuantity = 5;

    public void AddBilling(int day, int branch, decimal amount)
    {
        Billings[day, branch] += amount;
    }

    public decimal TotalBillingByBranch(int branch)
    {
        decimal sum = 0;
        for (var i = 0; i <= Billings.GetUpperBound(1); i++)
        {
            sum += Billings[branch, i];
        }

        return sum;
    }

    public int BranchWithHighestBillingByDay(int day)
    {
        var max = decimal.MinValue;
        var highestBranch = int.MinValue;
        for (var i = 0; i <= Billings.GetUpperBound(1); i++)
        {
            var bill = Billings[i, day];
            if (bill <= max) continue;
            max = bill;
            highestBranch = i;
        }

        return highestBranch;
    }

    public int BranchWithLowestBillingOfTheWeek()
    {
        var min = decimal.MaxValue;
        var lowestBranch = int.MinValue;

        for (var i = 0; i <= Billings.GetUpperBound(0); i++)
        {
            var sum = decimal.MinValue;
            for (var j = 0; j <= Billings.GetUpperBound(1); j++)
            {
                sum += Billings[i, j];
            }

            if (sum >= min) continue;
            min = sum;
            lowestBranch = i;
        }

        return lowestBranch;
    }

    public decimal TotalBilling()
    {
        var sum = decimal.MinValue;
        for (var i = 0; i <= Billings.GetUpperBound(0); i++)
        {
            for (var j = 0; j <= Billings.GetUpperBound(1); j++)
            {
                sum += Billings[i, j];
            }
        }

        return sum;
    }
}