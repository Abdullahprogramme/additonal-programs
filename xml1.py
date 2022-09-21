import xml.etree.ElementTree as Et

input='''
<Stuff>
    <Users>
        <User X="2">
            <ID>001</ID>
            <Name>Abdullah</Name>
        </User>
        <User X="7">
            <ID>012</ID>
            <Name>Player</Name>
        </User>
    </Users>
</Stuff>'''

stuff=Et.fromstring(input)
list=stuff.findall('Users/User')
print("User Count is " ,len(list))

for item in list:
    print("Name: ",item.find('Name').text)
    print("ID: ",item.find('ID').text)
    print("Attribute: ",item.get("X"))