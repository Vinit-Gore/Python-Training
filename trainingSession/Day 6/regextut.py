import re
myMainString = "Hi, I am Vinit Gore, and my date of birth is Jun 09. I work as Project Trainee (Software Development ). I joined MKCL on Jul 01, 2019. My email is vinitg@mkcl.org. My emergency number is 9869486181."
print(re.compile('\d\d').findall(myMainString))
print(re.compile('[0-9]+').findall(myMainString))
print(re.compile('\S+@\S+').findall(myMainString))
print(re.compile('([\w.-]+)@([\w-]+)\.([\w]+)').findall(myMainString))
print(re.compile('09').split(myMainString))
print(dir(re.compile('09').match(myMainString)))
print(re.compile('09').search(myMainString))
print(re.split('x+', 'axbc'))
