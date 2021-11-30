import argparse
from math import ceil, log, floor

parser = argparse.ArgumentParser(description="This program calculates differentiated or annuity loan payments.")
parser.add_argument('--type', choices=["diff", "annuity"],
                    help='Choose type of calculation\n Possible values is "diff" and "annuity"')
parser.add_argument('--principal', type=int, help='monthly payment')
parser.add_argument('--payment', type=int)
parser.add_argument('--interest', type=float, help='is specified without a percent sign')
parser.add_argument('--periods', type=int)
args = parser.parse_args()

type_of_calc = args.type
principal = args.principal
payment = args.payment
periods = args.periods
interest = args.interest


def check_type(type_):
    if type_ is not None:
        return type_ if type_ in ["diff", "annuity"] else False


def check_pay_error(type_, payment_):
    if check_type(type_) == "diff" and payment_ is not None:
        return False
    else:
        return True


def check_count_params():
    count = 0
    for param in args.__dict__.values():
        if param is not None:
            count += 1
    return False if count < 4 else True


def check_negative(principal_, payment_, periods_, interest_):
    parameters_ = [principal_, payment_, periods_, interest_]
    count = 0
    none_params = 0
    for param in parameters_:
        if param is None:
            none_params += 1
        elif param > 0:
            count += 1
    if len(parameters_) - none_params == count:
        return True


def differentiated_payments(principal_, periods_, interest_):
    overpayment_ = 0
    interest_ = interest_ / 1200
    for count in range(1, periods_ + 1):
        dif_payment = ceil((principal_ / periods_) + interest_ *
                           (principal_ - ((principal_ * (count - 1)) / periods_)))
        overpayment_ += dif_payment - int(principal_ / periods_)
        print(f"Month {count}: payment is {dif_payment}")
    print(f"\nOverpayment = {overpayment_}")


def month_to_years(periods_):
    year, month = divmod(periods_, 12)
    if year >= 1 and month >= 1:
        print(f"It will take {year}", "years" if year != 1 else "year",
              f"and {month} months" if month != 1 else "month", "to repay this loan!")
    elif year == 0 and month >= 1:
        print(f"It will take {month}", "months" if month != 1 else "month", "to repay this loan!")
    else:
        print(f"It will take {year}", "years" if year != 1 else "year", "to repay this loan!")


def overpayment(payment_, periods_, principal_):
    return payment_ * periods_ - principal_


def annuity_payment(principal_, payment_, periods_, interest_):
    i = interest_ / 1200
    if principal_ is None:
        principal_ = floor(payment_ / ((i * pow(1 + i, periods_)) / (pow(1 + i, periods_) - 1)))
        print(f"Your loan principal = {principal_}!\nOverpayment = {overpayment(payment_, periods_, principal_)}")
    elif periods_ is None:
        periods_ = ceil(log((payment_ / (payment_ - i * principal_)), 1 + i))
        month_to_years(periods_)
        print(f"Overpayment = {overpayment(payment_, periods_, principal_)}")
    else:
        payment_ = ceil(principal_ * (i * pow(1 + i, periods_)) / (pow(1 + i, periods_) - 1))
        print(f"Your annuity payment = {payment_}!\nOverpayment = {overpayment(payment_, periods_, principal_)}")


if check_type(type_of_calc) and check_pay_error(type_of_calc, payment) \
        and check_count_params() and check_negative(principal, payment, periods, interest) \
        and interest is not None:
    if type_of_calc == "diff":
        differentiated_payments(principal, periods, interest)
    else:
        annuity_payment(principal, payment, periods, interest)
else:
    print("Incorrect parameters")
    exit()
