class LOOP_FUNCTION():
    def FOR_LOOP_ADD(self,
                     x_e,
                     list_app=list):
        for x_s in x_e:
            try:
                list_app.append(x_s)
            except:
                pass
    def CX_FOR_LOOP_ADD(self,
                        x_e,
                        main_e,
                        list_app=list,
                        params=str):
        for x_s in x_e:
            try:
                list_app.append(main_e[x_s][params])
            except:
                pass
    def RANGE_FOR_LOOP_ADD(self,
                           x_e,
                           x_loop,
                           list_app=list,
                           x_list=list,
                           params=str):
        for x_s in x_e:
            try:
                list_app.append(x_loop[x_list[x_s]][params])
            except:
                pass
    def TARGET_FOR_LOOP_ADD(self,
                            x_e,
                            x_loop,
                            list_app=list,
                            x_list=list,
                            params=str,
                            target=str):
        for x_s in x_e:
            try:
                list_app.append(x_loop[x_list[x_s]][params][target])
            except:
                pass


class LOOP_OPS():
    def GET_LOOP():
        l_p = type("LOOP FUNCTIONS",
                   (LOOP_FUNCTION,),
                   {})
        loop_f = l_p()
        return loop_f