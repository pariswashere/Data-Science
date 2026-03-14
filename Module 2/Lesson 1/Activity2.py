dict = {'Name' : "Tasmia" , 'Age' : "20" , 'Country' : "Bangladesh"}


print(dict['Name'])
print(dict.get('Name'))

dict['Age'] = 27
print(dict)

dict['City'] = "Chittagong"
print(dict)

dict.pop('Country')
print(dict)