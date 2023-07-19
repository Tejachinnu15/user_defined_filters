from django import template

register=template.Library()
@register.filter()
def swap(data):
    return data.swapcase()
@register.filter()
def remove(data,arg):
    return data.replace(arg,' ')

@register.filter()
def count(data,arg):
    c=0
    for i in range(len(data)):
        if data[i:i+len(arg):]==arg:
            c+=1
    return c
@register.filter()
def change(value):
    s=value.split()
    l=[]
    for i in range(len(s)):
        if i==0 or i==len(s)-1:
            l.append(s[i])
        else:
            l.append(s[i].lower())
    return ' '.join(l)
     
