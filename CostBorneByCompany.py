# Company1 400
# Company2 500
# Company3 600
# Company2 150
# Company1 350
# Write a script command to find the total cost incurred by Company1.
# output: {'Company1': 750, 'Company2': 650, 'Company3': 600}
my_dict = {}
txt = open('CompanyCost')
print(txt)
for item in txt:
    #print(item.strip())
    each_item = item.strip().split(' ')
    #print(each_item)
    my_dict[each_item[0]] = int(my_dict.get(each_item[0], 0)) + int(each_item[1])
    # print(my_dict)

print(my_dict)