def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
	#########################################################################
	portion_down_payment = 0.25
	monthly_salary = yearly_salary / 12
	amount_saved = 0
	r = 0.05
	months = 0
	semi_cnt = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	
	while amount_saved < cost_of_dream_home * portion_down_payment:
	    if semi_cnt == 6:
	        monthly_salary *= 1 + semi_annual_raise
	        semi_cnt = 0
	        
	    # if (semi_cnt % 6 == 0 and semi_cnt != 0): //another solution 
	    #     monthly_salary *= 1 + semi_annual_raise
	    
	    amount_saved = amount_saved * (1 + r / 12) + monthly_salary * portion_saved
	    
	    months += 1
	    semi_cnt += 1
	
	print(f"Number of months: {months}")
	return months