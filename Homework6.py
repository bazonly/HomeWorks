
my_list = [i+5 for i in range(10)]
print(my_list)
print(len(my_list))

my_list2 = my_list[::2]
print(my_list2)
print(len(my_list2))

mul = 1
sum = 0
for i in my_list2:
    mul*=i
    sum+=i
print(mul)
print(sum)

my_list2.append(mul)
print(my_list2)
my_list2.append(sum)
print(my_list2)
my_list2.sort(reverse=True)
print(my_list2)

my_list3 = [str(i) for i in my_list2]
print(my_list3)

my_list3 = '='.join(my_list3)
print(my_list3)
print(type(my_list3))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 5, 9, -7, -10]
for i in a:
    if i<5:
        print(i)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 11]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 11, 12, 13]

if a>b:
    c = [i for i in a if i in b]
else:
    c = [i for i in b if i in a]

c = list(c)
c.sort()
print(c)



s = 'kafka python course stack flow dict list python stack course star product star product analytics flow star kafka stack flow ython list set ist fit predict dict list python ourse ython ourse star product ist fit predict analytics kafka stack flow product ist fit predict analytics star flow dict flow list python course stack flow dict list python stack course'

word_count = {}
for word in s.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
num_unique_words = len(word_count)

most_frequent_word = ""
max_count = 0
for word, count in word_count.items():
    if count > max_count:
        most_frequent_word = word
        max_count = count

print("The sentence contains", num_unique_words, "unique words.")
print("The most frequent word is:", most_frequent_word)

names = ['igor',
         'dasha',
         'martin',
         'vladimir',
         'rishat',
         'maria',
         'marat',
         'petr',
         'dima',
         'polina',
         'katya',
         'elena']

occupations = ['smm',
               'developer',
               'analyst',
               'president',
               'analyst',
               'ceo',
               'customer development',
               'founder',
               'developer',
               'ml engineer',
               'product manager',
               'cmo']

dict = {}

for i in range(len(names)):
    dict[names[i]] = occupations[i]
print(dict['maria'])

dict1={1:10, 2:20, 3901:11, 384:13, 8489:1, 48:10}

dict2={3:30, 4:40, 93:12, 91:41, 95:1, 841:11, 584:11}

dict3={5:50, 6:60, 9:90, 3:13, 7:11}

dict4 = {**dict1, **dict2, **dict3}
print(len(dict4))
print(dict4)


given_string = 'Python Star Course for beginners and experts for data science and analytics without sql with code'
f = list(given_string)
char_count = {}
for char in f:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

del char_count[' ']
print(char_count)
num_unique_words = len(char_count)


# most_frequent_word = ""
# max_count = 0
# for word, count in word_count.items():
#     if count > max_count:
#         most_frequent_word = word
#         max_count = count


