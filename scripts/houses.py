import json
import os
import geocoder
import torch
import pathlib
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\dan08\\Documents\\HACK\HacKMSK_IPITik_web\\models\\best.pt', force_reload=True)

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
    address = data['address']
    del data['address']
    if address in houses.keys():
        return 'Already in the system', 0 # TODO: handle
    houses[address] = data
    with open('./Houses/houses.json', 'w') as f:
        json.dump(houses, f, indent=3)
        f.close()
    return

def cv2_f(path):
    vidcap = cv2.VideoCapture(path)
    success,image = vidcap.read()
    count = 0
    results = []
    while success:
        #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        if success:
            if count % 3 == 0:
                try:
                    m = model(image)         
                    print(m)       
                    crops = m.crop(save=False)
                    
                    name = crops[0]["label"]

                    results.append(name)
                except:
                    continue
                
        count += 1
    return results

def update_house(data, video): # TODO: API version
    houses = get_houses_dic()            
    address = data['address']
    del data['address']
    if not os.path.exists('./videos/raw/'+address):
        os.makedirs('./videos/raw/'+address)
    # data['video'] = '/videos/raw' # TODO: handle of video
    for room, data_r in houses[address]['data'].items():
        if data['floor'] == data_r['floor'] and data['flat'] == data_r['flat'] and data['room_type'] == data_r['room_type']:
            data['video'] = './videos/raw/'+address+"/"+str(room) + ".mp4"
            results = model(data['video'])
            results.print()
            houses[address]['data'][room] = data
            with open('./Houses/houses.json', 'w') as f:
                json.dump(houses, f, indent=3)
                f.close()
            video.save('./videos/raw/'+address+"/"+str(room) + ".mp4")
            datares =  cv2_f(data['video'])   
            return datares 

    path = "./videos/raw/" + address + "/" + str(len(houses[address]['data'])+1) + ".mp4"
    houses[address]['data'].update({len(houses[address]['data'])+1:data})
    houses[address]['data'][len(houses[address]['data'])]['video'] = path
    video.save(path)
    vid_path = pathlib.Path(path)
    datares = cv2_f(path)
    with open('./Houses/houses.json', 'w') as f:
        json.dump(houses, f, indent=3)
        f.close()
        
    return datares

def delete_house_room(address, floor, flat, room_type): # TODO: API version
    houses = get_houses_dic()
    try:
        for room, data_r in houses[address]['data'].items():
            if floor == data_r['floor'] and flat == data_r['flat'] and room_type == data_r['room_type']:
                del houses[address]['data'][room]
                with open('./Houses/houses.json', 'w') as f:
                    json.dump(houses, f, indent=3)
                    f.close()
                return True
    except:
        return False
    with open('./Houses/houses.json', 'w') as f:
        json.dump(houses, f, indent=3)
    return True

def delete_house(address): # TODO
    houses = get_houses_dic()
    try:
        del houses[address]
        with open('./Houses/houses.json', 'w') as f:
            json.dump(houses, f, indent=3)
            f.close()
        
    except:
        return False
    return True

d = {
    'address':[59.5546666666667, 33.5907516666667],
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
#print(update_house(d2))
#delete_house_room("Bolokhovo, Komsomol'skaya ulitsa, 3", '2', '2', 'kit')
#delete_house("Bolokhovo, Komsomol'skaya ulitsa, 3")
#print(get_houses_address())
#print(get_house("Bolokhovo, Komsomol'skaya ulitsa, 3"))