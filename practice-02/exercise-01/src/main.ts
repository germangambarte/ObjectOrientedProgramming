import readline from 'node:readline/promises'
import { SavingBank } from './SavingBank'

const input = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

console.log('Ingrese los siguientes datos:')

let accountNumber: string = await input.question('\tNro de cuenta: ')
let cuil: string = await input.question('\tCuil: ')
let lastName: string = await input.question('\tApellido: ')
let firstName: string = await input.question('\tNombre: ')
let balance: number = Number(await input.question('\tSaldo: '))

input.close()

const firstAccount = new SavingBank(
    accountNumber,
    cuil,
    lastName,
    firstName,
    balance
)
const secondAccount = new SavingBank(
    '2',
    '20410266920',
    'Gambarte',
    'German',
    0
)

console.log('\nExtract:\n')
let result = firstAccount.extract(100)
console.log(
    result == null
        ? 'Fallo la operación'
        : `Saldo actual (firstAccount): ${result}`
)
result = secondAccount.extract(100)
console.log(
    result == null
        ? 'Fallo la operación'
        : `Saldo actual (seccondAccount): ${result}`
)

console.log('\nDeposit:\n')
result = firstAccount.deposit(0)
console.log(
    result == null
        ? 'Fallo la operación'
        : `Saldo actual (firstAccount): ${result}`
)
result = secondAccount.deposit(100)
console.log(
    result == null
        ? 'Fallo la operación'
        : `Saldo actual (secondAccount): ${result}`
)

console.log('\nValidate cuil:\n')
console.log(
    firstAccount.validateCuil()
        ? 'Cuil de firstAccount válido'
        : 'Cuil de firstAccount no válido'
)
console.log(
    secondAccount.validateCuil()
        ? 'Cuil de secondAccount válido'
        : 'Cuil de secondAccount no válido'
)
