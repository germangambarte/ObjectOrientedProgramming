from SavingBank import SavingBank


class SavingBankController:
    __accounts: list

    def __init__(self):
        self.__saving_bank_accounts = []

    def add_account(self, account: SavingBank):
        self.__accounts.append(account)

    def search_by_cuil(self, cuil) -> None | SavingBank:
        i = 0
        next_account = self.__accounts[i]
        while i < len(self.__accounts) and next_account.get_cuil() != cuil:
            i += 1
            next_account = self.__accounts[i]
        if next_account.get_cuil() != cuil:
            return None
        else:
            return next_account




