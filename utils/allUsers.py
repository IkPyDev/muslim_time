
import json
allUser = set()
id_user = 251575174

def regions_kiritish(id_user,region_code):
    # jami = {}
    with open("regions_user.json", "a+") as file:

        jami = f'"{id_user}":["{id_user}":{region_code}];',
        # full = f' {id_user}:{region_code},'
        json.dump(jami,file)



# def region_return(id_uers):
    # with open("regions_user", "r") as file:
    #     jami = file.read()
    #     # jami = dict(jami)
    #     for key in jami:
    #         if key[0] == id_uers:
#     #             return key[1]
# with open("regions_user.txt", "r") as file:
#     jami = dict(file.read())
#     print(jami)
#     # for key in jami:
    #     # print(key)
    #     if key[0] == id_user:
    #         print(key[1])
    #     else:
    #         print(jami,"sefserf")




#
if __name__ == '__main__':
    # pprint(get_surah_id())
    regions_kiritish("251575174",85)
    regions_kiritish("251575175",57)
    regions_kiritish("251575178", 47)
    regions_kiritish("251575179", 54)
# #     # print(region_return(251575174))
#



