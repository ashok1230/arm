class armstrong:
    def __init__(self):
	sum=0
	number=int(raw_input("enter a number "))
	temp=number
	while temp>=1:
	    rem=temp%10
	    temp=temp/10
	    sum+=rem**3
	if sum==number:
	    print number,' is armstrong number'
	else:
	    print number, 'is not armstrong number'

a=armstrong()