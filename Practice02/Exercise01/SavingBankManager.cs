namespace Exercise01;

public class SavingBankManager
{
    private List<SavingBank> _accounts = [];

    public void AddAccount(SavingBank newAccount)
    {
        _accounts.Add(newAccount);
    }

    public SavingBank? SearchByCuil(string cuil)
    {
        var nextAccount = _accounts[0];
        var i = 1;
        while (i < _accounts.Count && _accounts[i].Cuil != cuil)
        {
            nextAccount = _accounts[i++];
        }

        return nextAccount.Cuil == cuil ? nextAccount : null;
    }
}