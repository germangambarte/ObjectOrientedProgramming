import { SavingBank } from './SavingBank'

export class SavingBankManager {
    private accounts: SavingBank[]

    constructor() {
        this.accounts = []
    }

    addAccount(
        accountNumber: string,
        cuil: string,
        lastName: string,
        firstName: string,
        balance: number
    ): void {
        const newAccount = new SavingBank(
            accountNumber,
            cuil,
            lastName,
            firstName,
            balance
        )
        this.accounts.push(newAccount)
    }
    searchAccountByCuil(cuil: string): SavingBank | null {
        let i = 0
        let nextAccount = this.accounts[i]

        while (i < this.accounts.length && nextAccount.getCuil != cuil) {
            nextAccount = this.accounts[++i]
        }

        return nextAccount.getCuil == cuil ? nextAccount : null
    }
}
