# sweets_list = ['chocolate', 'lollipop', 'cookie', 'candy']
#
# with open('save.txt', 'w') as f:
#     for i in sweets_list:
#         f.write(i + '\n')


sweets_list = ['chocolate', 'lollipop', 'cookie', 'candy']
sweets_str = '\n'.join(sweets_list)
with open('save.txt', 'w') as f:
    f.write(sweets_str)
