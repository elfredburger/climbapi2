import requests
a = ['1', 'I', '5', '3a', '2', 'II', '5.1/5.2', '3b', '11', '3', 'III', '5.3/5.4', '3c', '12', '4a', 'IV',
                 '5.5',
                 '4a', 'VD', '13', '4b', 'IV+', '5.6', '4b', 'S', '14', '4c', 'V', '5.7', '4c', 'HS', '15', '5a', 'V+',
                 '5.8',
                 'VS', '16', '5b', 'VI-', '5.9', '5a', 'HVS', '17', '5c', 'VI', '5.10a', 'E1', '18', '6a', 'VI+',
                 '5.10b', '5b',
                 '19', '6a+', 'VII-', '5.10c', 'E2', '20', '6b', 'VII', '5.10d', '5c', '21', '6b+', 'VII+', '5.11a',
                 'E3', '22',
                 '6c', 'VIII-', '5.11b', '23', '6c+', 'VIII', '5.11c', '6a', 'E4', '24', '7a', 'VIII+', '5.11d', '',
                 '25',
                 '7a+', 'IX-', '5.12a', 'E5', '26', '7b', 'IX- IX', '5.12b', '6b', '7b+', 'IX', '5.12c', 'E6', '27',
                 '7c',
                 'IX IX+', '5.12d', '6c', '28', '7c+', 'IX+', '5.13a', 'E7', '29', '8a', 'IX+ X-', '5.13b', '8a+', 'X-',
                 '5.13c', '7a', '30', '8b', 'X', '5.13d', 'E8', '31', '8b+', 'X+', '5.14a', '', '32', '8c', 'X+ XI-',
                 '5.14b',
                 '7b', '33', '8c+', 'XI-', '5.14c', 'E9', '34', '9a', 'XI', '5.14d', '7c', '35', '9a+', 'XI+', '5.15a',
                 '36',
                 '9b', 'XII-', '5.15b', '37', '9b+', 'XII', '5.15c', '38', '9c', 'XII+', '5.15d', '39']
endpoint='http://localhost:8000/api/v1/grades'

for i in a:
    get_response=requests.post(endpoint,json={'boulder_grade':i})
    print({'boulder_grade':i})