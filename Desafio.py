def show_menu():
    print('\n')
    print('Menu:')  # Menu
    print('\t1 Deposit')  # Depósito
    print('\t2 Withdrawal')  # Saque
    print('\t3 Bank statement')  # Extrato
    print('\t4 Quit')  # Sair
    # Selecione a opção desejada:
    return input('\nSelect the desired option: ')


def welcome():
    print("Welcome to D!O Bank.")  # Bem-vindo ao Banco DIO.


balance = 0.0  # Saldo
account = ''  # extrato
daily_withdrawal = 3
limit_withdrawal = 500.00
quantity = 0

welcome()
while True:
    menu = show_menu()
    # Deposit - Depósito
    if menu == '1':
        # Insira o valor do depósito:
        deposit = float(input('\nEnter the deposit amount: '))

        if deposit > 0:
            balance += deposit
            print(balance)
            account += f'Deposit: R$ {deposit:.2f}\n'
        else:
            print('Operation failed: negative values are not allowed.')

    # Withdrawal - Saque
    elif menu == '2':
        withdrawal = float(input("Enter withdrawal amount: "))

        # Check the balance - Analisar o saldo
        if withdrawal <= balance:
            # Check daily withdraw - analisar a quantos saques diários
            if quantity < daily_withdrawal:
                # Check limit value - analisar o valor limite de saque
                if withdrawal <= limit_withdrawal:
                    quantity += 1
                    print(f'quantity: {quantity}')
                    balance -= withdrawal
                    print(balance)
                    account += f'Withdrawal: R$ {withdrawal:.2f}\n'
                else:
                    # Valor máximo excedido
                    print("Operation failure: Maximum value of withdrawals exceeded.")
            else:
                # limite de saque diário
                print(
                    'Operation failure: Check the withdrawal amount allowed in your plan.')

        else:
            # saldo insuficiente
            print("Operation failure: Insufficient funds.")

    elif menu == '3':
        print('\n' + "*"*10 + ' Bank Statement ' + "*"*10)
        if account == '':
            print("No bank transactions.")
        else:
            print(account)
        print(f'Balance: R$ {balance:.2f}')

        print("*"*22 + "*"*(len('Bank statement')))

    elif menu == '4':
        break

    else:
        print("Incorrect value, please choose menu options.")
