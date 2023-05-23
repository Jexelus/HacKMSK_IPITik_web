import json
import geocoder

def get_houses_dic():
    with open('./Houses/houses.json', 'r') as f:
        try:
            houses = json.load(f)
        except:
            return dict()
        f.close()
    if len(houses) == 0:
        return dict()
    else:
        return dict(houses)

def get_house(address):
    houses = get_houses_dic()
    if houses != None:
        if address in houses.keys():
            return houses[address]
    else:
        return None

def get_houses_address():
    houses = get_houses_dic()
    if houses != None:
        return list(houses.keys())
    else:
        return None

def add_house(data): # WEB version
    houses = get_houses_dic()
    address_encodet = geocoder.bing(data['address'], method='reverse', key="AgcMEj_11MYB6Epe-VDXd9IP-LbzfMqVCQR0M6_AgUqKQ59O8fba4q51i4MjYD6R")
    for res in address_encodet:
        address = str(res.city) + ','+' '+str(res.street)
    del data['address']
    if address in houses.keys():
        return 'Already in the system', 0 # TODO: handle
    houses[str(res.city) + ','+' '+str(res.street)] = data
    with open('./Houses/houses.json', 'w') as f:
        json.dump(houses, f, indent=3)
        f.close()
    return

def update_house(data): # TODO: API version
    houses = get_houses_dic()
    address_encodet = geocoder.bing(data['address'], method='reverse', key="AgcMEj_11MYB6Epe-VDXd9IP-LbzfMqVCQR0M6_AgUqKQ59O8fba4q51i4MjYD6R")
    for res in address_encodet:
        address = str(res.city) + ','+' '+str(res.street)
    del data['address']
    data['video'] = 'fp' # TODO: handle of video
    for room, data_r in houses[address]['data'].items():
        if data['floor'] == data_r['floor'] and data['flat'] == data_r['flat'] and data['room_type'] == data_r['room_type']:
            houses[address]['data'][room] = data
            with open('./Houses/houses.json', 'w') as f:
                json.dump(houses, f, indent=3)
                f.close()
            return        
    houses[address]['data'].update({len(houses[address]['data'])+1:data})
    with open('./Houses/houses.json', 'w') as f:
        json.dump(houses, f, indent=3)
        f.close()
    return 

def delete_house_room(address, floor, flat, room_type): # TODO: API version
    houses = get_houses_dic()
    try:
        for room, data_r in houses[address]['data'].items():
            if floor == data_r['floor'] and flat == data_r['flat'] and room_type == data_r['room_type']:
                del houses[address]['data'][room]
                with open('./Houses/houses.json', 'w') as f:
                    json.dump(houses, f, indent=3)
                    f.close()
                return
    except:
        return False
    with open('./Houses/houses.json', 'w') as f:
        json.dump(houses, f, indent=3)
    return  

def delete_house(address): # TODO
    houses = get_houses_dic()
    try:
        del houses[address]
        with open('./Houses/houses.json', 'w') as f:
            json.dump(houses, f, indent=3)
            f.close()
        
    except:
        return False
    return

d = {
    'address':[54.085676118550104, 37.832003036313964],
    'floors':'5',
    'flats':'30',
    'data':{}
} 

d2 = {
    'address':[54.085676118550104, 37.832003036313964],
    'floor':'2',
    'flat':'2',
    'room_type':'kit',
    'progress':'2%'
}
#add_house(d)
#pdate_house(d2)
#delete_house_room("Bolokhovo, Komsomol'skaya ulitsa, 3", '2', '2', 'kit')
#delete_house("Bolokhovo, Komsomol'skaya ulitsa, 3")
#print(get_houses_address())
#print(get_house("Bolokhovo, Komsomol'skaya ulitsa, 3"))