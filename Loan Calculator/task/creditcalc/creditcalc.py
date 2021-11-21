import math

print('What do you want to calculate? \n'
      'type "n" for number of monthly payments,\n'
      'type "a" for annuity monthly payment amount,\n'
      'type "p" for loan principal:')
choose_type = input()


def number_of_monthly():
    loan_principal = int(input('Enter the loan principal:\n'))
    monthly_payment = int(input('Enter the monthly payment:\n'))
    loan_interest = float(input('Enter the loan interest:\n'))

    interest_rate = (loan_interest / 100) / 12
    number_of_month = math.ceil(math.log((monthly_payment / (monthly_payment - interest_rate * loan_principal)),
                                         1 + interest_rate))
    year, month = divmod(number_of_month, 12)

    if year >= 1 and month >= 1:
        print(f"It will take {year}", "years" if year != 1 else "year", f"and {month}",
              "months" if month != 1 else "month", "to repay this loan!")
    elif year == 0 and month >= 1:
        print(f"It will take {month}", "months" if month != 1 else "month", "to repay this loan!")
    else:
        print(f"It will take {year}", "years" if year != 1 else "year", "to repay this loan!")


def annuity_monthly_payment():
    loan_principal = int(input('Enter the loan principal:\n'))
    number_of_periods = int(input('Enter the number of periods:\n'))
    loan_interest = float(input('Enter the loan interest:\n'))

    interest_rate = (loan_interest / 100) / 12
    monthly_payment = loan_principal * (interest_rate * pow(1 + interest_rate, number_of_periods)) / (
                pow(1 + interest_rate, number_of_periods) - 1)
    print(f"Your monthly payment = {math.ceil(monthly_payment)}")


def calc_loan_principal():
    annuity_payment = float(input('Enter the annuity payment:\n'))
    number_of_periods = int(input('Enter the number of periods: \n'))
    loan_interest = float(input('Enter the loan interest: \n'))

    interest_rate = (loan_interest / 100) / 12
    loan_principal = annuity_payment / ((interest_rate * pow(1 + interest_rate, number_of_periods)) / (
            pow(1 + interest_rate, number_of_periods) - 1))
    print(f"Your monthly payment = {round(loan_principal)}")


if choose_type == "n":
    number_of_monthly()
elif choose_type == "a":
    annuity_monthly_payment()
elif choose_type == "p":
    calc_loan_principal()
