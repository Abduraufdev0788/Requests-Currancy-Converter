from utils import print_to
from manager import Money
import sys

while True:
    print_to()
    choise = input(" > ")
    if choise == "1" :
        summa = float(input("Dollar qilmoqchi bolgan summanigizni kiriting: "))
        Money.UZS(summa)
    elif choise == "2" :
        dollar = float(input("summa qilmoqchi bolgan dollarni kiriting: "))
        Money.from_Usd(dollar)
    elif choise == "3" :
        sys.exit(0)
    else:
        sys.exit(1)
