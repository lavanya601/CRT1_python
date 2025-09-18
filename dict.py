d1={'college':'nec','add':'narasaraopeta','class':'IT','branch':'ECE','students':1000}
d2={'state':'AP'}
print(d1)
print(d1['students'])
print(d1.get('students'))
print(d1.keys())
for x1 in d1.keys():
    print(x1,end='')
print(d1.values())
for x1 in d1.values():
    print(x1)
print(d1.values())
print(d1.popitem())
print(d1)
print(d1.pop('college'))
print(d1)
d1.update(d2)
print(d1)