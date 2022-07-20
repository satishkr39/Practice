# Given a file containing some sample text, write a script command to count the number of occurrences of the word “Amazon”.
txt = 'lkjasf sagasjglk Amazon sgkasdgh Amazon sdgflasjkgd sadgsajkldg Amazon sdgasdg sdfjkolasj mlasdf Amazon'
count =0
for i in txt.split(' '):
    print(i)
    if i == 'Amazon':
        count+=1
print('Occurence of Amazon: ', count)

# Given a file containing some sample text, write a script command to change all occurrences of the word “Amazon” with “It” in the file.
new_txt = txt.replace('Amazon', 'It')
print(new_txt)
with open('new_replace.txt') as f:
    f.write(new_txt)