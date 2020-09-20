import pandas as pd
import re

stop_chars=["@", "#", "&", "$"]

df1 = pd.read_csv('../UrIII_admin_translated.csv')

lines = list(df1.values[:, 0])
      
def savefile(filename,LIST):
    with open(filename, 'w') as f:
        for line in LIST:
            f.write("%s\n" % line)
            
def processing_1(text_line):
    #x = re.sub(r"\[\.+\]","unk",text_line)
    #x = re.sub(r"...","unk",x)
    x = re.sub(r'\#', '', text_line)
    x = re.sub(r"\_", "", x)
    x = re.sub(r"\[", "", x)
    x = re.sub(r"\]", "", x)
    x = re.sub(r"\<", "", x)
    x = re.sub(r"\>", "", x)
    x = re.sub(r"\!", "", x)
    x = re.sub(r"@c", "", x)
    x = re.sub(r"@t", "", x)
    #x=re.sub(r"(x)+","x",x)
    x = re.sub(r"\?", "", x)
    x = x.split()
    x = " ".join(x)
    k = re.search(r"[a-wyzA-Z]+",x)
    if k:
        return x
    else:
        return ""

def pretty_line_sum(text_line):
    #x = re.sub(r"\[\.+\]","unk",text_line)
    #x = re.sub(r"...","unk",x)
    x = re.sub(r'\#', '', text_line)
    x = re.sub(r"\_", "", x)
    x = re.sub(r"\[", "", x)
    x = re.sub(r"\]", "", x)
    x = re.sub(r"\<", "", x)
    x = re.sub(r"\>", "", x)
    x = re.sub(r"\!", "", x)
    x = re.sub(r"@c", "", x)
    x = re.sub(r"@t", "", x)
    #x=re.sub(r"(x)+","x",x)
    x = re.sub(r"\?", "", x)
    x = x.split()
    x = " ".join(x)
    k = re.search(r"[a-wyzA-Z]+",x)
    if k:
        return x
    else:
        return ""

def pretty_line_eng(text_line):
    x = re.findall("[ a-zA-Z1-9]+", text_line)
    return ''.join(x)

def parallel(lines_r):
    # pll_org = open("../sumerian_translated.atf", "r")
    sum_org = open("../dataset/original/UrIII_sum_pll.txt", "w")
    eng_org = open("../dataset/original/UrIII_eng_pll.txt", "w")
    sumerian_pll = open("../dataset/cleaned/UrIII_sum_pll.txt", "w")
    english_pll = open("../dataset/cleaned/UrIII_eng_pll.txt", "w")
    # lines = pll_org.readlines()
    # print(len(lines_r))
    for lines in lines_r:
        lines = lines.split('\n')
        # print(len(lines))
        sum_lines = []
        eng_lines = []
        org_sum_lines = []
        org_eng_lines = []
        count_words = 0
        for i in range(len(lines)):
            if lines[i] != "" and lines[i] != " " and lines[i][0] not in stop_chars:
                index=lines[i].find(".")
                sum_line = pretty_line_sum(lines[i][index+1:])
                count_words += len(sum_line.split())
                if(sum_line not in sum_lines):
                    sum_lines.append(sum_line)
                    org_sum_lines.append(lines[i][index+1:])
                while sum_line != "" and sum_line != " ":
                    try:
                        i += 1
                        if lines[i].find("#tr.en") != -1:
                            eng_line = pretty_line_eng(lines[i][8:])
                            org_eng_lines.append(lines[i][8:])
                            if eng_line != "" and eng_line != " ":
                                eng_lines.append(eng_line)
                                break
                    except:
                        break

            if count_words>5 or len(sum_lines) >= 3 or i == len(lines)-1 and count_words:
                sum_org.write(' '.join(org_sum_lines))
                eng_org.write(' '.join(org_eng_lines))
                sumerian_pll.write(' '.join(sum_lines))
                english_pll.write(' '.join(eng_lines))
                sumerian_pll.write('\n')
                english_pll.write('\n')
                sum_lines = []
                eng_lines = []
                org_sum_lines = []
                org_eng_lines = []
                count_words = 0
                    
parallel(lines)

# df1.apply(parallel)

# Original_sumerian_mono=[]

# for i in lines:
#     if len(i)>0 and i[0] not in stopping_chars:
#         index=i.find(".")
#         l=i[index+1:].strip()
#         Original_sumerian_mono.append(l)

# print('Data Loaded')

# processed_summerian=[] 
# for i in range(len(Original_sumerian_mono)):
#     text=processing_1(Original_sumerian_mono[i])
#     if(re.search("\d\d\d\d\d",text)):
#         continue
#     if(len(text)>2):
#         processed_summerian.append(text)

# print('Data Processed')
        
        
# savefile('../Dataset/Original_Data/supp_mono.txt', Original_sumerian_mono)
# savefile('../Dataset/Cleaned_Data/sumerian_mono.txt', processed_summerian)

# print('Files Saved')