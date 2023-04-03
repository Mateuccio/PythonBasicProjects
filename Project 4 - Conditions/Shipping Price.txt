weight = 1.5

#Ground Shipping

flat_charge = 20
if weight <= 2:
  cost = 1.5
elif weight <= 6:
  cost = 3
elif weight <= 10:
  cost = 4
else:
  cost = 4.75

print("Cost of ground Shipping is", (cost*weight+flat_charge),'$')

#Ground Shipping Premium

premium_flat_charge = 125
print("Cost of premium ground shipping is", premium_flat_charge, '$')

#Drone Shipping

if weight <= 2:
  cost = 4.5
elif weight <= 6:
  cost = 9
elif weight <= 10:
  cost = 12
else:
  cost = 14.25

print("Cost of drone shipping is", (cost*weight),'$')


