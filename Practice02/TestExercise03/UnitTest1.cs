using System.Numerics;
using Exercise03;

namespace TestExercise03;

public class UnitTest1
{
    [Fact]
    public void TestInitializedSales()
    {
        SalesManager manager = new();
        var expectedInitialSales = new decimal[,]
        {
            {0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0}
        };
        Assert.Equal(manager.Sales, expectedInitialSales);
    }

    [Fact]
    public void TestAddBill()
    {
        SalesManager manager = new();
        const int day = 1;
        const int branch = 1;
        const decimal firstBill = 123m;
        const decimal secondBill = 123m;
        manager.AddBill(day,branch,firstBill);
        Assert.Equal(firstBill, manager.Sales[branch-1,day-1]);
        manager.AddBill(day,branch,secondBill);
        Assert.Equal(firstBill + secondBill, manager.Sales[branch-1,day-1]);
    }
    
    [Fact]
    public void TestAddBillThrowsException()
    {
        SalesManager manager = new();
        const int day = 1;
        const int branch = 0;
        const decimal firstBill = 123m;
        Assert.Throws<ArgumentException>(() => manager.AddBill(day,branch,firstBill));
        Assert.Throws<ArgumentException>(() => manager.AddBill(day,branch,firstBill));
    }

    [Fact]
    public void TestGetTotalBillPerWeekByBranch()
    {
        SalesManager manager = new();

        const int branch = 1;
        var total = decimal.Zero;
        const decimal bill = 100m;
        
        for (var day = 1; day < 8; day++)
        {
            total += bill * day;
            manager.AddBill(day,branch,bill*day);
        }
        
        Assert.Equal(total, manager.GetTotalBillPerWeekByBranch(branch));
    }
    
    [Fact]
    public void TestGetTotalBillPerWeekByBranchThrowsException()
    {
        SalesManager manager = new();
        const int branch = 37;
        Assert.Throws<ArgumentException>(() => manager.GetTotalBillPerWeekByBranch(branch));
    }

    [Fact]
    public void TestGetMaxBillOfTheDay()
    {
        SalesManager manager = new();
        const int day = 3;
        const int maxBranch = 3;
        const int bill = 100;
        for (var i = 1; i < 6; i++)
        {
            if (i == maxBranch)
            {
                manager.AddBill(day,i,decimal.MaxValue);
            } 
            else
            {
                manager.AddBill(day,i,bill*i);
            }
        }
        Assert.Equal(maxBranch,manager.GetMaxBillOfTheDay(day));
    }
    
    [Fact]
    public void TestGetMaxBillOfTheDayThrowsException()
    {
        SalesManager manager = new();
        const int day = 0;
        Assert.Throws<ArgumentException>(() =>manager.GetMaxBillOfTheDay(day));
    }

    [Fact]
    public void TestGetMinBillOfTheWeek()
    {
        SalesManager manager = new();
        
        var total = decimal.Zero;
        for (var i = 1; i < 6; i++)
        {
            total += 200;
            manager.AddBill(i,i,200);
        }
        Assert.Equal(total,manager.GetTotalBillOfTheWeek());
    }
}