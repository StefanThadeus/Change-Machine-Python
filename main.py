print("This program returns back the inserted value as change in forms of 1, 2, 5 and 10 dollar bills.")

to_return = int(input("Please insert the amount of money to return: "))
bills_10, bills_5, bills_2, bills_1 = 0, 0, 0, 0

to_return_remain = to_return
if to_return_remain >= 10:
    bills_10 = to_return_remain // 10
    to_return_remain -= bills_10 * 10

if to_return_remain >= 5:
    bills_5 = to_return_remain // 5
    to_return_remain -= bills_5 * 5

if to_return_remain >= 2:
    bills_2 = to_return_remain // 2
    to_return_remain -= bills_2 * 2

if to_return_remain == 1:
    bills_1 = to_return_remain

print(f"\nThe amount to return: {to_return}")
print(f"-Total 10 dollar bills: {bills_10}")
print(f"-Total 5 dollar bills: {bills_5}")
print(f"-Total 2 dollar bills: {bills_2}")
print(f"-Total 1 dollar bills: {bills_1}")
