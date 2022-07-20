# Script command to print the sentence in reverse order.
# I/P - "You are in Amazon"
# O/P - "Amazon in are You"


text = "You are in Amazon"
text_arr = text.split(" ")
print(text_arr)
print(text_arr[::-1])
text_revers = text_arr[::-1]
for i in text_revers:
    print(i, end=" ")
