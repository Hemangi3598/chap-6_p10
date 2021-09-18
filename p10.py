# dp ===> default parameter

def show(a, b, c=30, d=40):
	print(a, b, c, d)

show(10, 20, 30, 40)
show(1, 0, 9)

# ek baar c=30 likha to uske right m sbko default krna pdega 
# show(a, b, c=90, d) likha to error ayega