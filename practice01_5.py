##q5

s = '''We encourage everyone to contribute to Python If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process.'''

s = s.upper()
s = s.strip().replace('.','').replace(',','').replace(" ",'')
print("s:",s)
s = set(s)
print(s)

s_lst = list(s)

print("s_lst",s_lst)
'''
print(s_lst.find("ATFER"))
print(s_lst.find("AVAILABLE"))
print(s_lst.find("CONTRIBUTE"))
print(s_lst.find("CONTRIBUTORS"))

'''