print('Enter some numbers in one line')
raw_input = input()
splitted_input = raw_input.split()
parsed_input = list()
for raw in splitted_input:
    parsed_input.append(int(raw))
parsed_input.sort()
print(f' your result: {parsed_input}')