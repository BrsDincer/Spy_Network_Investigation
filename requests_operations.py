import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
from additional_operations import ADDITIONAL_GET as AG
from print_operations import PRINT_LAST as PL
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class REQUESTS_OPS():
    def GET_WEB_INFO(self,t_s=str):
        r_s = requests.Session()
        try:
            if "http://" in t_s or "https://" in t_s:
                if t_s.endswith("/"):
                    t_s[-1] = ""
                    r_o = r_s.get(t_s,
                                  headers=AG.GET_HEADER_EXAMPLE(),
                                  timeout=7,
                                  stream=True,
                                  verify=False)
                    return r_o.status_code,r_o.text,r_o.content,r_o.headers
                else:
                    r_o = r_s.get(t_s,
                                  headers=AG.GET_HEADER_EXAMPLE(),
                                  timeout=7,
                                  stream=True,
                                  verify=False)
                    return r_o.status_code,r_o.text,r_o.content,r_o.headers
            else:
                n_s = "http://"+t_s
                if n_s.endswith("/"):
                    n_s[-1] = ""
                    r_o = r_s.get(n_s,
                                  headers=AG.GET_HEADER_EXAMPLE(),
                                  timeout=7,
                                  stream=True,
                                  verify=False)
                    return r_o.status_code,r_o.text,r_o.content,r_o.headers
                else:
                    r_o = r_s.get(n_s,
                                  headers=AG.GET_HEADER_EXAMPLE(),
                                  timeout=7,
                                  stream=True,
                                  verify=False)
                    return r_o.status_code,r_o.text,r_o.content,r_o.headers
        except:
            PL.OUT().unk_error()
            
class RQ_OPS():
    def GET_RQ_INFO():
        r_i = type("REQUESTS OPERATIONS",
                   (REQUESTS_OPS,),
                   {})
        req_o = r_i()
        return req_o

            
                
        
        