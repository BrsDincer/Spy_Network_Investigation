from requests_operations import RQ_OPS as RQ 
from additional_operations import ADDITIONAL_GET as AG
from print_operations import PRINT_LAST as PL
from document_operations import TRANSFER_OUT as TO
import pandas as pd

################################################
########### SITE INFORMATION PROCESS ###########  # STEP I
################################################
# ip_list = []
# host_list = []
# for x_site in AG.GET_TOP_500():
#     try:
#         x_ip,x_host = AG.GET_SITE_IP(str(x_site))
#         ip_list.append(x_ip)
#         host_list.append(x_host)
#     except:
#         pass
    
# series_ip = pd.Series(ip_list,name="IP")
# series_host = pd.Series(host_list,name="HOST")
# main_concat = pd.concat([series_ip,series_host],axis=1)
# main_concat.to_csv("TOP_500_SITE.csv")



#########################################################
########### SITE INV WITH TRACKER LIST I ################  # STEP II
#########################################################

# new_frame = {}
# for x_site in AG.GET_TOP_500():
#     try:
#         r_s,r_t,r_c,r_h = RQ.GET_RQ_INFO().GET_WEB_INFO(str(x_site))
#         if r_s == 200:
#             new_frame[str(x_site)] = []
#             for x_tracker in TO.GET_INFO().main_entry:
#                 try:
#                     if x_tracker in r_t or x_tracker in r_c:
#                         new_frame[str(x_site)].append(x_tracker)
#                 except:
#                     pass
#     except:
#         pass
#     try:
#         if len(new_frame[str(x_site)]) > 2 and new_frame[str(x_site)] != None:
#             series_spec = pd.Series(new_frame[str(x_site)])
#             series_spec.to_csv(f"...\\P_{str(x_site)}.csv")
#         else:
#             pass
#     except:
#         pass
    


##########################################################
########### SITE INV WITH TRACKER LIST II ################  # STEP III
##########################################################  
# new_frame = {}

# for x_site in AG.GET_TOP_500():
#     try:
#         r_s,r_t,r_c,r_h = RQ.GET_RQ_INFO().GET_WEB_INFO(str(x_site))
#         if r_s == 200:
#             new_frame[str(x_site)] = []
#             for x_tracker in TO.GET_INFO().domain_list:
#                 try:
#                     if x_tracker in r_t or x_tracker in r_c:
#                         new_frame[str(x_site)].append(x_tracker)
#                 except:
#                     pass
#     except:
#         pass
#     try:
#         if len(new_frame[str(x_site)]) > 2 and new_frame[str(x_site)] != None:
#             series_spec = pd.Series(new_frame[str(x_site)])
#             series_spec.to_csv(f"...\\P_{str(x_site)}.csv")
#         else:
#             pass
#     except:
#         pass


##################################################################
########### SITE INV -header WITH TRACKER LIST I ################  # STEP IV
########################################################## ######## 
# new_frame = {}

# for x_site in AG.GET_TOP_500():
#     try:
#         r_s,r_t,r_c,r_h = RQ.GET_RQ_INFO().GET_WEB_INFO(str(x_site))
#         if r_s == 200:
#             new_frame[str(x_site)] = []
#             for x_tracker in TO.GET_INFO().main_entry:
#                 try:
#                     if x_tracker in r_t or x_tracker in r_h:
#                         new_frame[str(x_site)].append(x_tracker)
#                 except:
#                     pass
#     except:
#         pass
#     try:
#         if len(new_frame[str(x_site)]) > 2 and new_frame[str(x_site)] != None:
#             series_spec = pd.Series(new_frame[str(x_site)])
#             series_spec.to_csv(f"...\\P_{str(x_site)}.csv")
#         else:
#             pass
#     except:
#         pass



##################################################################
########### SITE INV -header WITH TRACKER LIST II ################  # STEP V
########################################################## ######## 
# new_frame = {}

# for x_site in AG.GET_TOP_500():
#     try:
#         r_s,r_t,r_c,r_h = RQ.GET_RQ_INFO().GET_WEB_INFO(str(x_site))
#         if r_s == 200:
#             new_frame[str(x_site)] = []
#             for x_tracker in TO.GET_INFO().domain_list:
#                 try:
#                     if x_tracker in r_t or x_tracker in r_h:
#                         new_frame[str(x_site)].append(x_tracker)
#                 except:
#                     pass
#     except:
#         pass
#     try:
#         if len(new_frame[str(x_site)]) > 2 and new_frame[str(x_site)] != None:
#             series_spec = pd.Series(new_frame[str(x_site)])
#             series_spec.to_csv(f"...\\P_{str(x_site)}.csv")
#         else:
#             pass
#     except:
#         pass



    