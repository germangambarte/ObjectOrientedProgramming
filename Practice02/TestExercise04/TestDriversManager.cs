using Exercise04;
namespace TestExercise04;

public class TestDriversManager
{
    [Fact]
    public void Test1()
    {
        DriversManager manager = new();
        manager.LoadDriver();
        Assert.Equal(5, manager.Drivers.Count);
    }
}