from print_operations import PRINT_LAST as PL
from loop_operations import LOOP_OPS as LO
import json

def MAIN_TRACKER(self):
    try:
        domain_main_list = []
        domain_sub_list = []
        entities_all_list = []
        entities_main_list = []
        main_entities = []
        open_doc = open("social_network.json",errors="replace")
        load_doc = json.loads(open_doc.read())
        trackers_all = load_doc["trackers"]
        entities_all = load_doc["entities"]
        LO.GET_LOOP().FOR_LOOP_ADD(trackers_all,domain_main_list)
        LO.GET_LOOP().FOR_LOOP_ADD(entities_all,entities_all_list)
        LO.GET_LOOP().CX_FOR_LOOP_ADD(domain_main_list,
                                        trackers_all,
                                        domain_sub_list,
                                        "domain")
        LO.GET_LOOP().CX_FOR_LOOP_ADD(entities_all_list,
                                        entities_all,
                                        entities_main_list,
                                        "domains")
        for x_in in entities_main_list:
            for x_sub in x_in:
                main_entities.append(x_sub)
        self.domain_sub = domain_sub_list
        self.main_entry = main_entities
    except:
        PL.OUT().red_out("[X] NOT FOUND - DOCUMENT")
        
def TRACKER_DOMAIN_JSON(self):
        try:
            domain_list = []
            categories_list = []
            name_list = []
            open_doc = open("tracker_huge.json",errors="replace")
            load_doc = json.loads(open_doc.read())
            domain_name = load_doc["trackers"]
            LO.GET_LOOP().FOR_LOOP_ADD(domain_name,domain_list)
            LO.GET_LOOP().RANGE_FOR_LOOP_ADD(range(len(domain_list)),
                                            domain_name,
                                            categories_list,
                                            domain_list,
                                            "categories")
            LO.GET_LOOP().TARGET_FOR_LOOP_ADD(range(len(domain_list)),
                                            domain_name,
                                            name_list,
                                            domain_list,
                                            "owner",
                                            "name")
            self.domain_list=domain_list
            self.cat_list=categories_list
            self.name_list=name_list
        except:
            pass
        
class TRANSFER_OUT():
    def GET_INFO():
        g_i = type("GET DOCUMENT",
                   (),
                   {"tracker_info":MAIN_TRACKER,
                    "huge_info":TRACKER_DOMAIN_JSON})
        get_i = g_i()
        get_i.tracker_info()
        get_i.huge_info()
        return get_i

        
        
        
        
        
        
        
        
        
        