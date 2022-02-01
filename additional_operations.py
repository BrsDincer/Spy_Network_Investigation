import random,json,socket,requests
from bs4 import BeautifulSoup

class ADDITIONAL_GET:
    def READING_FILE(file_name=str):
        try:
            with open(file_name,"r",
                      errors="replace") as file_tar:
                x_file=[]
                for line_x in file_tar:
                    try:
                        ext_tar=line_x.strip()
                        x_file.append(ext_tar)
                    except:
                        pass
            return x_file
        except:
            pass
    def USER_AGENT():
        try:
            f_op=open("user_agent.json")
            j_op=json.loads(f_op.read())
            list_agent=[]
            for x_value in j_op["user_agents"]:
                for ix_values in j_op["user_agents"][x_value]:
                    for ixl_values in j_op["user_agents"][x_value][ix_values]:
                        for ixlp_values in j_op["user_agents"][x_value][ix_values][ixl_values]:
                            list_agent.append(ixlp_values)
            return list_agent
        except:
            pass
    def GET_HEADER_EXAMPLE():
        try:
            user_agent_all=random.choice(ADDITIONAL_GET.USER_AGENT())
            ref_ex_list=ADDITIONAL_GET.READING_FILE("referer_list.txt")
            ref_all=random.choice(ref_ex_list)
            date_day=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
            date_month=["Jan","Feb","Mar","Apr","Aug","Sep","Oct","Nov","Dec"]
            date_day_number=random.randint(1,30)
            date_year=random.randint(2000,2021)
            date_time_x=random.randint(10,23)
            date_time_y=random.randint(10,50)
            date_time_z=random.randint(10,55)
            main_header={"User-Agent":str(user_agent_all),
                         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                         "Connection":"Keep-Alive",
                         "Keep-Alive":"155",
                         "Content-Type":"text/html",
                         "Accept-Encoding":"gzip,deflate",
                         "Accept-Language":"en-us,en;q=0.5",
                         "Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.7",
                         "Referer":str(ref_all),
                         "Date":f"{random.choice(date_day)}, {date_day_number} {random.choice(date_month)} {date_year} {date_time_x}:{date_time_y}:{date_time_z} GMT"}
            return main_header
        except:
            pass
        
    def GET_TOP_500():
        LIST_ALL = []
        REQ_URL = BeautifulSoup(requests.get("https://moz.com/top500").text,
                                "html.parser").find_all("tr")
        for x_h in REQ_URL:
            ALL_A = x_h.find_all("a",class_="text-nowrap")
            for x_a in ALL_A:
                s_h = x_a.get("href").split("/")[-1]
                LIST_ALL.append(s_h)
        return LIST_ALL
        
    def GET_SITE_IP(target_site=str):
        try:
            n_s = target_site.replace(" ","")\
                .replace("https://","")\
                    .replace("http://","")\
                        .replace("www.","")
            ip_s = socket.gethostbyname(n_s)
            return ip_s,n_s
        except:
            pass