#list slicing(should create new cart)
amazon_Cart=[
'notebooks', 
 'milk',
 'toys'
 ,'sunglasses']
amazon_Cart[0] ='laptop'
new_Cart = amazon_Cart[:]
new_Cart[0]='gum'
print(new_Cart)
print(amazon_Cart)

