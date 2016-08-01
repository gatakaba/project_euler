# coding:utf-8
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

letter_dic = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5:
              "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
letter_dic .update({11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"})

letter_dic.update({20: "twenty", 30: "thirty", 40: "forty", 50:
                   "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"})

letter_dic.update({100: "hundred", 1000: "one thousand"})

for i in range(20, 1000):
    if i in letter_dic.keys():
        continue
    elif i < 100:
        letter_dic[i] = letter_dic[int(i / 10) * 10] + " " + letter_dic[i % 10]
    elif i % 100 == 0:
        letter_dic[i] = letter_dic[int(i / 100)] + " " + letter_dic[100]
    else:
        letter_dic[i] = letter_dic[
            int(i / 100)] + " " + letter_dic[100] + " and " + letter_dic[i % 100]

letter_dic[100] = "one hundred"
for i in letter_dic.values():
    print i
l = map(lambda x: len(x.replace(" ", "")), letter_dic.values())
print sum(l)
print letter_dic[99]
