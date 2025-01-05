export class SavingBank {
    private accountNumber: string
    private cuil: string
    private lastName: string
    private firstName: string
    private balance: number

    constructor(
        accountNumber: string,
        cuil: string,
        lastName: string,
        firstName: string,
        balance: number
    ) {
        this.accountNumber = accountNumber
        this.cuil = cuil
        this.lastName = lastName
        this.firstName = firstName
        this.balance = balance
    }
    showData(): void {}
    extract(amount: number): number | null {
        if (amount <= 0) {
            console.log('La cifra debe ser mayor a $0,00')
            return null
        }
        if (amount > this.balance) {
            console.log('Saldo insuficiente.')
            return null
        }

        this.balance -= amount
        return this.balance
    }

    deposit(amount: number): number | null {
        if (amount <= 0) {
            console.log('La cifra debe ser mayor a $0,00')
            return null
        }

        this.balance += amount
        return this.balance
    }
    validateCuil(): boolean {
        if (this.cuil.length != 11) return false

        const genre = Number(this.cuil.substring(0, 2))
        const validationDigit = Number(this.cuil.substring(10))

        if (![20, 23, 27, 30].includes(genre)) return false

        const result = this.factorsValidationResult()

        if (result == 0 && validationDigit == 0) return true

        if (result == 1 && genre == 23) {
            if (validationDigit == 9 || validationDigit == 4) return true
        }
        return 11 - result == validationDigit
    }
    get getCuil() {
        return this.cuil
    }

    private factorsValidationResult(): number {
        const validationFactors = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        let sum = 0

        for (let i = 0; i < validationFactors.length; i++) {
            sum += Number(this.cuil[i]) * validationFactors[i]
        }

        return sum % 11
    }
}
