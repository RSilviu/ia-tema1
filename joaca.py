import json

# un interlocutor este de fapt un dictionar
iloc_1 = dict(nume='Ana', varsta=10, ocupatie='elev')
iloc_2 = dict(nume='Matei', varsta=20, ocupatie='student')
iloc_3 = dict(nume='Iulia', varsta=30, ocupatie='casnica')

# punem interlocutorii intr-o lista pentru a-i putea serializa json
iloc_list = [iloc_1,iloc_2,iloc_3]

# scriem interlocutorii in fisier
with open('interlocutori.json','w') as f:
    json.dump(iloc_list, f, indent=4)

# prin decodarea jsonului se reface lista de mai sus, apoi afisam info despre matei
with open('interlocutori.json', 'r') as f:
    iloc_list = json.load(f)
    print('matei')
    print(iloc_list[1]['varsta'],iloc_list[1]['ocupatie'])
