import pandas as pd
import io



def read_file(full_path_in):
    f_t = open(full_path_in, "r", encoding="UTF-8", errors = 'ignore')
    text_t = f_t.read() #reads entire file
    #text_t = clean_txt(text_t)
    f_t.close()
    return text_t

def file_crawler(path_in):
    import os
    import pandas as pd
    my_pd_t = pd.DataFrame()
    for root, dirs, files in os.walk(path_in, topdown=False):
       for name in files:
           try:
               txt_t = read_file(root + "/" + name)
               if len(txt_t) > 0:
                   the_lab = root.split("/")[-1]
                   tmp_pd = pd.DataFrame(
                       {"body": txt_t, "label": the_lab}, index=[0])
                   my_pd_t = pd.concat(
                       [my_pd_t, tmp_pd], ignore_index=True)
           except:
               print (root + "/" + name)
               pass
    return my_pd_t