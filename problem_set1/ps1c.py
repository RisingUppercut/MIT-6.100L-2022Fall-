## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_house = 800000
down_payment = 0.25 * cost_of_house
months = 3 * 12

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

low = 0
high = 1
r = (low + high) / 2
steps = 0
while abs(down_payment - initial_deposit * (1+r/12)**months) > 100:
    if (initial_deposit >= down_payment):
        r = 0
        break
    elif (initial_deposit * (1 + 1/12)**months < down_payment):
        r = None
        break
    
    if (down_payment < initial_deposit * (1+r/12)**months):
        high = r
    else:
        low = r
    r = (low + high) / 2
    steps += 1

print(f'Best savings rate: {r}')
print(f'Steps in bisection search: {steps}')

