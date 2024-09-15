def first_non_repeating_letter(string):
    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i
    return ''


first_non_repeating_letter('a')  # 'a'
print(first_non_repeating_letter('stress') ) # 't'
print(first_non_repeating_letter('moonmen') ) # 'e'

first_non_repeating_letter('')  # ''

print(first_non_repeating_letter('abba'))  # ''
first_non_repeating_letter('aa')  # ''
