
def get_days_of_power(R1, D1, R2, D2, R3, D3, K):
    loans = [(R1, D1), (R2, D2), (R3, D3)]

    loans.sort(key = lambda x: x[1])

    # Initialize total amount, current_rate and final value (days of power)
    current_amount = K # money

    current_rate = 0
    total_days_of_lighting = 0

     # Loop for the first n - 1 loans
    for i in range(len(loans) - 1):
        # Update current rate
        current_rate += loans[i][0]

        # Finding the number of days
        number_of_days = loans[i + 1][1] - loans[i][1]

        amount_used = number_of_days * current_rate

        current_amount -= amount_used

        # if remaining amount is less than current rate
        if current_amount < current_rate:
            #calculate current day of date 
            temp = amount_used - abs(current_amount)
            total_days_of_lighting += int(temp / current_rate)

            return total_days_of_lighting

        total_days_of_lighting += number_of_days

    # handle the third special/final case
    current_rate += loans[len(loans) - 1][0]

    total_days_of_lighting += int(current_amount  / current_rate)

    return total_days_of_lighting


if __name__ == "__main__":
    print(get_days_of_power(R1=1000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=3000))