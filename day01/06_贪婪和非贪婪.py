import re

html = '''
<div><p>九霄龙吟惊天变</p></div>
<div><p>风云际会潜水游</p></div>
'''
#贪婪模式
p = re.compile(r'<div><p>.*?</p></div>',re.S)
r_list = p.findall(html)
print(r_list)