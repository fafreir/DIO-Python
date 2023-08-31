def show_menu():
    print('\n')
    print('Menu:')  # Menu
    print('\t1 Deposit')  # Depósito
    print('\t2 Withdrawal')  # Saque
    print('\t3 Bank statement')  # Extrato
    print('\t4 Create User')
    print('\t5 Create account')
    print('\t6 List account')
    print('\t7 Quit')  # Sair
    # Selecione a opção desejada:
    return input('\nSelect the desired option: ')


def welcome():
    print("Welcome to D!O Bank.")  # Bem-vindo ao Banco DIO.


def deposit(balance, account, dep):

    if dep > 0:
        balance += dep
        print(balance)
        account += f'Deposit: R$ {dep:.2f}\n'

    else:
        print('Operation failed: negative values are not allowed.')
    return balance, account


def withdrawal(withd, balance, quantity, daily_withdrawal, limit_withdrawal,
               account):
    funds = withd <= balance
    limit_daily = quantity < daily_withdrawal
    limit_value = withd <= limit_withdrawal

    if funds:
        if limit_daily:
            if limit_value:
                quantity += 1
                balance -= withd
                account += f'Withdrawal: R$ {withd:.2f}\n'
            else:
                print("Operation failure: Maximum value of withdrawals exceeded.")
        else:
            print(
                'Operation failure: Check the withdrawal amount allowed in your plan.')
    else:
        print("Operation failure: Insufficient funds.")
    return balance, account, quantity


def bank_statement(account, balance):
    print('\n' + "*"*10 + ' Bank Statement ' + "*"*10)
    if account == '':
        print("No bank transactions.")
    else:
        print(account)
    print(f'Balance: R$ {balance:.2f}')
    print("*"*22 + "*"*(len('Bank statement')))


def users(cpflista):
    cpf = input("inform your CPF (just numbers): ")
    if cpf in filter_CPF(cpflista):
        print('User already registered.')
        return
    name = input("Inform your name: ")
    birth = input("Inform your birthdate (dd/mm/aaaa): ")
    address = input(
        "Inform your address (Street/Park/Avenue name, number - neighborhood, city/State acronym)")
    cpflista.append({'cpf': cpf})
    print("User successfully added.")
    return cpflista


def filter_CPF(cpflista):
    cpf_dict = {cpf['cpf'] for cpf in cpflista}
    return (cpf_dict)


def add_one(number_account):
    number_account += 1
    return number_account


def create_account(cpflista, agencia, user, accountlista):
    global number
    number = 0
    cpf = input("inform your CPF (just numbers): ")
    if cpf not in filter_CPF(cpflista):
        print("CPF not found, user registration required!")
        users(cpflista)
    accountlista.append(number)
    tamanho = len(accountlista)
    user.append({'cpf': cpf, 'agency': agencia, 'account': tamanho})
    print('Account created successfully.')
    return user, agencia


def list_account(user):
    for pessoa in user:
        cpfp = pessoa['cpf']
        agencyp = pessoa['agency']
        accountp = pessoa['account']
        print(cpfp, agencyp, accountp))


def list_account(user):
    for users in user:
        print(users)


def main():
    agencia = '0001'
    account = ''  # extrato
    daily_withdrawal = 3
    limit_withdrawal = 500.00
    quantity = 0
    balance = 0.0  # Saldo
    user = []
    cpflista = []
    accountlista = []
    while True:

        menu = show_menu()

        if menu == '1':
            dep = float(input('\nEnter the deposit amount: '))
            balance, account = deposit(balance, account, dep)

        elif menu == '2':
            withd = float(input("\nEnter withdrawal amount: "))
            balance, account, quantity = withdrawal(
                withd=withd, balance=balance,
                quantity=quantity,
                daily_withdrawal=daily_withdrawal,
                limit_withdrawal=limit_withdrawal,
                account=account)

        elif menu == '3':
            bank_statement(account, balance=balance)

        elif menu == '4':
            users(cpflista)

        elif menu == '5':
            create_account(cpflista, agencia, user, accountlista)

        elif menu == '6':
            list_account(user)

        elif menu == '7':
            break
        else:
            print("Incorrect Option, please choose the option available")


if __name__ == "__main__":
    main()
