import re

html = '''
<div class="animal">
    <p class="name">
        <a title="Tiger"></a>
    </p>
    <p class="content">
        Two Tigers two tigers run fast
    </p>
</div>
<div class="animal">
    <p class="name">
        <a title="Rabbit"></a>
    </p>
    <p class="content">
        Small white Rabbit white and white
    </p>
</div>
'''

p = re.compile(r'<div.*?title="(\w*?)">.*?class="content">(.*?)</p>\n</div>',re.S)
p_list = p.findall(html)
print(p_list)
r_list = []
for i in p_list:
    r_list = i[0]
    r_list += i[1].strip()
print(r_list)