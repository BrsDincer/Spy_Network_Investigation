class PRINTING_OUTPUT():
    def cr():
        cr = type("COLOR",
                  (),
                  {"end":"\x1b[0m",
                   "red":"\033[1;31m",
                   "green":"\033[1;32m",
                   "yellow":"\033[1;33m",
                   "info":"\033[1;36m"})
        return cr
    
class ERROR_TYPE:
    def sys_error(self):
        print(PRINTING_OUTPUT.cr().red+"[X] SYSTEM ERROR, PLEASE TRY AGAIN"+PRINTING_OUTPUT.cr().end)
    def doc_error(self):
        print(PRINTING_OUTPUT.cr().red+"[X] FILE IS NOT VALID, PLEASE CHECK DIRECTORIES"+PRINTING_OUTPUT.cr().end)  
    def unk_error(self):
        print(PRINTING_OUTPUT.cr().red+"[X] SOMETHING IS WRONG, PLEASE TRY AGAIN"+PRINTING_OUTPUT.cr().end)

class PORT_INFO:
    def open_info(self,port_type=str):
        print(PRINTING_OUTPUT.cr().green+f"[>] PORT IS OPEN - PORT: {str(port_type)}"+PRINTING_OUTPUT.cr().end)
    def closed_info(self,port_type=str):
        print(PRINTING_OUTPUT.cr().yellow+f"[>] PORT MAY BE CLOSED OR FILTERED - PORT: {str(port_type)}"+PRINTING_OUTPUT.cr().end)
    def timeout_info(self,port_type=str):
        print(PRINTING_OUTPUT.cr().red+f"[>] TIMEOUT - PORT: {str(port_type)}"+PRINTING_OUTPUT.cr().end)
        
class GENERAL_INFO():
    def good_response(self,output_type=str):
        print(PRINTING_OUTPUT.cr().green+f"[+] LIVE - {str(output_type)}"+PRINTING_OUTPUT.cr().end)
    def bad_response(self,output_type=str):
        print(PRINTING_OUTPUT.cr().yellow+f"[!] RESPONSE DENIED - {str(output_type)}"+PRINTING_OUTPUT.cr().end)
        
class OUTPUT_TYPE():
    def green_out(self,output_st=str):
        print(PRINTING_OUTPUT.cr().green+f"{str(output_st)}"+PRINTING_OUTPUT.cr().end)
    def yellow_out(self,output_st=str):
        print(PRINTING_OUTPUT.cr().yellow+f"{str(output_st)}"+PRINTING_OUTPUT.cr().end)
    def info_out(self,output_st=str):
        print(PRINTING_OUTPUT.cr().info+f"{str(output_st)}"+PRINTING_OUTPUT.cr().end)
    def red_out(self,output_st=str):
        print(PRINTING_OUTPUT.cr().red+f"{str(output_st)}"+PRINTING_OUTPUT.cr().end)
        
        
class PRINT_LAST:
    def OUT():
        t_n = type("ERROR TYPES",(ERROR_TYPE,
                                  PORT_INFO,
                                  GENERAL_INFO,
                                  OUTPUT_TYPE),{})
        t_t = t_n()
        return t_t
