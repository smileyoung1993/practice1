##q4
s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

import re

def remove_tag(s):
   clear =re.compile('<.*?>')
   cleantext = re.sub(clear, '', s)
   return cleantext

print(remove_tag(s))