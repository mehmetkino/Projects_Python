def is_invalid(mod_num):
       if mod_num != 100 and mod_num != 200 and mod_num != 300:
              status = True
              print(status)
       else:
              status = False
              print(status)
       return status

is_invalid(200)