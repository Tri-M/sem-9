# def count_substrings_with_k_distinct(s, k):
#     from collections import defaultdict

#     def count_at_most_k_distinct(s, k):
#         left = 0
#         count = 0
#         freq = defaultdict(int)

#         for right in range(len(s)):
#             freq[s[right]] += 1

#             while len(freq) > k:
#                 freq[s[left]] -= 1
#                 if freq[s[left]] == 0:
#                     del freq[s[left]]
#                 left += 1

#             count += right - left + 1

#         return count

#     # Count substrings with exactly k distinct characters
#     return count_at_most_k_distinct(s, k) - count_at_most_k_distinct(s, k - 1)

# # Example usage
# s = "pqpqs"
# k = 2
# print(count_substrings_with_k_distinct(s, k))  # Output: 7

# def maxpathsum(grid):
#     m=len(grid)
#     n=len(grid[0])
#     for i in range(m):
#         grid[0][i]+=grid[0][i-1]
#     for i in range(n):
#         grid[i][0]+=grid[i-1][0]
#     for i in range(m):
#         for j in range(n):
#             grid[i][j]+=max(grid[i-1][j],grid[i][j-1])
#     return grid[-1][-1]

# Question – : There are two banks – Bank A and Bank B. Their interest rates vary. You have received offers from both banks in terms of the annual rate of interest, tenure, and variations of the rate of interest over the entire tenure.You have to choose the offer which costs you least interest and reject the other. Do the computation and make a wise choice.

# The loan repayment happens at a monthly frequency and Equated Monthly Installment (EMI) is calculated using the formula given below :

# EMI = loanAmount * monthlyInterestRate / ( 1 – 1 / (1 + monthlyInterestRate)^(numberOfYears * 12))

# Constraints:

# 1 <= P <= 1000000
# 1 <=T <= 50
# 1<= N1 <= 30
# 1<= N2 <= 30
 

# Input Format:

# First line: P principal (Loan Amount)
# Second line: T Total Tenure (in years).
# Third Line: N1 is the number of slabs of interest rates for a given period by Bank A. First slab starts from the first year and the second slab starts from the end of the first slab and so on.
# Next N1 line will contain the interest rate and their period.
# After N1 lines we will receive N2 viz. the number of slabs offered by the second bank.
# Next N2 lines are the number of slabs of interest rates for a given period by Bank B. The first slab starts from the first year and the second slab starts from the end of the first slab and so on.
# The period and rate will be delimited by single white space.
# Output Format: Your decision either Bank A or Bank B.

# Explanation:

# Example 1
# Input
# 10000
# 20
# 3
# 5 9.5
# 10 9.6
# 5 8.5
# 3
# 10 6.9
# 5 8.5
# 5 7.9
# Output: Bank B
# Example 2
# Input
# 500000
# 26
# 3
# 13  9.5
# 3  6.9
# 10  5.6
# 3
# 14  8.5
# 6  7.4
# 6  9.6
# Output: Bank A
def calculate_emi(loan_amount, monthly_rate, months):
    if monthly_rate == 0:
        return loan_amount / months
    emi = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    return emi

def calculate_total_interest(loan_amount, slabs):
    total_interest = 0.0
    remaining_principal = loan_amount
    
    for slab in slabs:
        years, annual_rate = slab
        monthly_rate = annual_rate / 12 / 100  # Convert annual rate to monthly rate
        months = years * 12
        
        emi = calculate_emi(remaining_principal, monthly_rate, months)
        total_payment = emi * months
        total_interest += total_payment - remaining_principal
        
        # Update the remaining principal (the entire principal is used in EMI calculation each time)
        remaining_principal = total_payment - emi * months

    return total_interest

# Input
P = int(input())
T = int(input())

# Bank A
N1 = int(input())
bank_a_slabs = []
for _ in range(N1):
    period, rate = map(float, input().split())
    bank_a_slabs.append((period, rate))

# Bank B
N2 = int(input())
bank_b_slabs = []
for _ in range(N2):
    period, rate = map(float, input().split())
    bank_b_slabs.append((period, rate))

# Calculate total interest for Bank A
total_interest_a = calculate_total_interest(P, bank_a_slabs)

# Calculate total interest for Bank B
total_interest_b = calculate_total_interest(P, bank_b_slabs)

# Compare and choose the better offer
if total_interest_a < total_interest_b:
    print("Bank A")
else:
    print("Bank B")
