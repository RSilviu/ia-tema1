import json

iloc_1 = dict(nume='Ana', varsta=10, ocupatie='elev')
iloc_2 = dict(nume='Matei', varsta=20, ocupatie='student')
iloc_3 = dict(nume='Iulia', varsta=30, ocupatie='casnica')

iloc_list = [iloc_1,iloc_2,iloc_3]

with open('interlocutori.json','w') as f:
    json.dump(iloc_list, f, indent=4)

with open('interlocutori.json', 'r') as f:
    iloc_list = json.load(f)
    print('matei')
    print(iloc_list[1]['varsta'],iloc_list[1]['ocupatie'])
