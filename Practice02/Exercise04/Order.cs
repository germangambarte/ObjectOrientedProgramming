namespace Exercise04;

public class Order
{
    public int Id { get; private set; }
    public string DeliveryPlate { get; private set; }
    public string[] Ordered { get; private set; }
    public int EstimatedDeliveryTime { get; private set; }
    public int RealDeliveryTime { get; private set; }
    public decimal OrderedPrice { get; private set; }

    public Order(int id,
        string deliveryPlate,
        string[] ordered,
        int estimatedDeliveryTime,
        decimal orderedPrice,
        int realDeliveryTime = 0)
    {
        Id = id;
        DeliveryPlate = deliveryPlate;
        Ordered = ordered;
        EstimatedDeliveryTime = estimatedDeliveryTime;
        RealDeliveryTime = realDeliveryTime;
        OrderedPrice = orderedPrice;
    }
}