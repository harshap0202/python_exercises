# Programming Challenge: Grocery Store Purchase
# A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:
# 1. Penne 16 oz Pack of 12 - $16.68
# 2. Arrabiata Pasta Sauce 24 oz - $6.98
# 3. Bag of 20 Organic Garlic Cloves - $16.78
# 4. Italian Seasoning 1.5 oz Bottle - $15.26
# 5. Artisan Baguettes Twin Pack - $3.00
# 6. 12 oz Bag of Meatballs - $4.39
# In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.  
# The subtotal is just the sum of all of their prices.
# Use print() to display the result of the expression.

penne = 16.68
pasta = 6.98
garlic = 16.78
seasoning = 15.26
baguettes = 3.00
meatballs = 4.39

subtotal = round(penne + pasta + garlic + seasoning + baguettes + meatballs, 2)
print(subtotal)