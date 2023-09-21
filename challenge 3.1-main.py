"""
write a function called linear_search_product that takes the list of products and target product
name as input. the function should perform a linear search to find the target product in the list and
return air list indices occurrence of the product if found, oran empty list if the product is not
found
"""


def linearsearchproduct (productlist, targetproduct):
  indices = []

  for index, product in           enumerate(productlist):
    if product                       ==targetproduct:
      indices.append(index)

  return indices

#example usages :
products=["shoes","boot","loafer","shoes","sandal","shoes"]
target1 = "shoes"
target2 = 'Apple'
result=linearsearchproduct(products, target1)
print(result)