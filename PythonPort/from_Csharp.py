#!/usr/bin/env python3

import json
import re
import os
import sys


peyar = "MLTYWNEIQOGDHVXBPSളവ"
speyar = "CAJ"
venai = "ஆலனசளணஇழஉஓடதदधபநमயரறवउपकतईटरलळएचज"
nonderi = "Z"


def Vaani():
    deri = peyar + speyar + venai + "FUKഡഗജദപ"


cacheword = []
cachesug = []

def refreshcache(nword):
    found = cacheword.find(nword)
    cachesug[found] = "correct"


with open('db.lint.valid.json',encoding='utf-8-sig') as json_file:
    db = json.load(json_file)


#print(db[0]['DB'][3])




def getviku(v,c,sc):
    blocks = ""

    if sc == "15":
        blocks = "01234567"

    if sc == "25":
        blocks = "0123456"


    if sc == "07":
        blocks = "0123456"


    if sc == "10":
        blocks = "01235"


    if sc == "11": #//except special
        blocks = "012356"


    if sc == "09":
        blocks = "02"


    if sc == "06":
        blocks = "023"


    if sc == "05":
        blocks = "013"


    if sc == "04":
        blocks = "03"


    if sc == "03":
        blocks = "13"


    if sc == "02":
        blocks = "2"


    if sc == "01":
        blocks = "1"


    if sc == "16":
        blocks = "3"


    if sc == "17": #//special
        blocks = "0"


    if sc == "08": #//Peyar speical extension அநவரத  venai present echam சுவைப்பட,நாள்பட
        blocks = "4"


    if sc == "18": #//special  -> 08 also takes 4 segment
        blocks = "4"


    if sc == "19": #//special
        blocks = "5"


    if sc == "20": #//special
        blocks = "6"


    if sc == "21": #//special
        blocks = "7"


    if sc == "24": #//echam verb is using
        blocks = "34"



    for d in range(8):

        for b in range(len(v),-1,-1):

            subpaku = v[0, b]
            subviku = v[b]

            part = Eword[c][d][subpaku]

            if part:
                if ("①" or "②" in part):

                    code1 = part[len(part) - 3, 1]
                    subcode1 = part[len(part) - 2]

                    vikuth = getviku(subviku, code1, subcode1)

                    if (vikuth != "false"):
                        return vikuth

                    elif (subviku == ""):
                        return part

    return false


#uncomplete
#region check the word with existing root words



def checkroot(word):

    outp = word.split(',')
    Oword = db[0]["DB"][4] #//Words

#    print(Oword)
    Eword = db[0]["DB"][3] #//family

    #rule = JsonConvert.DeserializeObject("{\"M\":\"ம்\",\"L\":\"ு\",\"T\":\"ு\",\"Y\":\"\",\"W\":\"\",\"N\":\"\",\"E\":\"\",\"I\":\"ல்\",\"Q\":\"ள்\",\"ള\":\"ள்\",\"O\":\"்\",\"P\":\"்\",\"S\":\"்\",\"V\":\"ு\",\"വ\":\"ு\",\"ഗ\":\"\",\"ഡ\":\"\",\"ജ\":\"\",\"ദ\":\"\",\"പ\":\"\",\"B\":\"ை\",\"G\":\"ர்\",\"D\":\"ர்\",\"X\":\"ர்\",\"H\":\"ர்\",\"ஆ\":\"தல்\",\"ல\":\"ல்தல்\",\"ன\":\"ல்தல்\",\"ச\":\"்லுதல் \",\"ள\":\"ள்தல்\",\"ண\":\"ள்ளுதல்\",\"இ\":\"ுதல்\",\"ழ\":\"ுதல்\",\"உ\":\"தல்\",\"ஓ\":\"தல்\",\"ட\":\"ுதல்\",\"த\":\"த்தல்\",\"द\":\"த்தல்\",\"ध\":\"த்தல்\",\"ப\":\"்த்தல்\",\"ந\":\"த்தல்\",\"म\":\"த்தல்\",\"ய\":\"தல்\",\"ர\":\"்தல்\",\"ற\":\"ுதல்\",\"व\":\"ாதல்\",\"उ\":\"ணுதல்\",\"प\":\"்ணுதல்\",\"क\":\"ாண்ணுதல்\",\"त\":\"னுதல்\",\"ई\":\"்னுதல்\",\"ट\":\"ள்தல்\",\"र\":\"ல்தல்\",\"ल\":\"ல்தல்\",\"ळ\":\"ுதல்\",\"ए\":\"றுதல்\",\"च\":\"தல் \",\"ज\":\"ேகுதல்\"}");
    rule_json = "{\"M\":\"ம்\",\"L\":\"ு\",\"T\":\"ு\",\"Y\":\"\",\"W\":\"\",\"N\":\"\",\"E\":\"\",\"I\":\"ல்\",\"Q\":\"ள்\",\"ള\":\"ள்\",\"O\":\"்\",\"P\":\"்\",\"S\":\"்\",\"V\":\"ு\",\"വ\":\"ு\",\"ഗ\":\"\",\"ഡ\":\"\",\"ജ\":\"\",\"ദ\":\"\",\"പ\":\"\",\"B\":\"ை\",\"G\":\"ர்\",\"D\":\"ர்\",\"X\":\"ர்\",\"H\":\"ர்\",\"ஆ\":\"தல்\",\"ல\":\"ல்தல்\",\"ன\":\"ல்தல்\",\"ச\":\"்லுதல் \",\"ள\":\"ள்தல்\",\"ண\":\"ள்ளுதல்\",\"இ\":\"ுதல்\",\"ழ\":\"ுதல்\",\"உ\":\"தல்\",\"ஓ\":\"தல்\",\"ட\":\"ுதல்\",\"த\":\"த்தல்\",\"द\":\"த்தல்\",\"ध\":\"த்தல்\",\"ப\":\"்த்தல்\",\"ந\":\"த்தல்\",\"म\":\"த்தல்\",\"ய\":\"தல்\",\"ர\":\"்தல்\",\"ற\":\"ுதல்\",\"व\":\"ாதல்\",\"उ\":\"ணுதல்\",\"प\":\"்ணுதல்\",\"क\":\"ாண்ணுதல்\",\"त\":\"னுதல்\",\"ई\":\"்னுதல்\",\"ट\":\"ள்தல்\",\"र\":\"ல்தல்\",\"ल\":\"ல்தல்\",\"ळ\":\"ுதல்\",\"ए\":\"றுதல்\",\"च\":\"தல் \",\"ज\":\"ேகுதல்\"}"

    rule = json.loads(rule_json)
 #   print(rule)


    for a in range(len(word)-1,-1,-1):
        print(a)
        paku = word[0:a]
        print("paku = " + paku)
        viku = word[a]
        print("viku = " + viku)

#        print(Oword[paku])

        if paku in Oword:
            qcode = Oword[paku]

            if ( qcode ) and (len(qcode) >0):
                for b in qcode:
                    print("qcode = " + str(b))
                    code = b['t'][0:1]
                    print("code = " + code)
                    subcode = b['t'][1:]
                    print("subcode = " + subcode)
                    vikuthi = getviku(viku, code, subcode)

                    if vikuthi != "false":
                        outp[0] = paku + str(rule[code])
                        outp[1] = " " + tranlate(vikuthi)
                        return outp

                    print(outp)
#checkroot("நன்றிகள்")



#done
def tranlate(code):

    trans_json = "{\"㚱\":\"நான்காம் வேற்றுமை(கு)\", \
                  \"㚲\":\"இரண்டாம் வேற்றுமை(ஐ)\", \
                  \"㚳\":\"வேற்றுமை உருபு(இன்)\", \
                  \"㚵\":\"மூன்றாம் வேற்றுமை(உடன்)\", \
                  \"㚶\":\"மூன்றாம் வேற்றுமை(ஓடு)\", \
                  \"㚷\":\"மூன்றாம் வேற்றுமை(ஆல்)\", \
                  \"㚸\":\"வேற்றுமை உருபு(இல்)\", \
                  \"㚹\":\"ஏழாம் வேற்றுமை(இடம்)\", \
                  \"㚺\":\"ஆறாம் வேற்றுமை\"}"

    translation = json.loads(trans_json)

    if code in translation:
        return translation[code]
    else:
        return ""

print(tranlate("㚱"))





def gpathil11(mword, opt, mode):

        Oword = db[0]["DB"][4] #//Words
        Eword = db[0]["DB"][3]
        tranrule = db[0]["DB"][2]
        tword = db[0]["DB"][1]   # substiture english words to tamil words
        gword = db[0]["DB"][0]


        if os.path.exists("koppu/user.txt"):
            userfile = open("koppu/user.txt",'r').readlines()
            userOword = userfile[0].split(',')
            usergword = userfile[1].split(',')
        else:
            userOword = ""
            usergword = ""

        splitchar = ','

#        // string[] sandhi = { "க", "ச", "த", "ப" };
        vauyir_json = "{\"வா\":\"ஆ\",\"வி\":\"இ\",\"வீ\":\"ஈ\",\"வு\":\"உ\",\"வூ\":\"ஊ\",\"வெ\":\"எ\",\"வே\":\"ஏ\",\"வை\":\"ஐ\",\"வொ\":\"ஒ\",\"வோ\":\"ஓ\",\"வௌ\":\"ஒள\"}"  #//\"வ\":\"அ\",
        yauyir_json = "{\"யா\":\"ஆ\",\"யி\":\"இ\",\"யீ\":\"ஈ\",\"யு\":\"உ\",\"யூ\":\"ஊ\",\"யெ\":\"எ\",\"யே\":\"ஏ\",\"யை\":\"ஐ\",\"யொ\":\"ஒ\",\"யோ\":\"ஓ\",\"யௌ\":\"ஒள\"}" #);// \"ய\":\"அ\",
        auyir_json = "{\"ா\":\"ஆ\",\"ி\":\"இ\",\"ீ\":\"ஈ\",\"ு\":\"உ\",\"ூ\":\"ஊ\",\"ெ\":\"எ\",\"ே\":\"ஏ\",\"ை\":\"ஐ\",\"ொ\":\"ஒ\",\"ோ\":\"ஓ\",\"ௌ\":\"ஒள\"}"

        vauyir = json.loads(vauyir_json)
        yauyir = json.loads(yauyir_json)
        auyir = json.loads(auyir_json)

        parinthu = [[None,None] for i in range(len(mword))]
        ottran = [[None,None] for i in range(len(mword))]


        for i in range(len(mword)):
            parinthu[i][ 0] = 0 #;//count of suggestion
            parinthu[i][ 1] = "wrong" #;//suggestions
            ottran[i][ 0] = 0
            ottran[i][1] = 1

        for i in range(len(mword)):

            sandi = ""
            punarchi = False

#            //1 - if it is verified already
            if (ottran[i][ 0] == 1):
                continue

#            //2 - removing blank char
            if (len(mword[i]) < 1):
                parinthu[i, 0] = -1
                parinthu[i, 1] = ""
                continue

#           //3.ignoring single consonant letters


            if (len(mword[i]) == 2):

                rgx = "[ா-்]"
                if (re.match(rex,mword[i][-1])):
                    ottran[i][0] = 1
                    parinthu[i][1] = "correct"
                    parinthu[i][0] = 0
                    continue


#                //4.ignoring single vowel letters
            if (len(mword[i]) == 1):
                ottran[i][0] = 1
                parinthu[i][1] = "correct"
                parinthu[i][0] = 0
                continue

#                            //5- Typo Correction
                mword[i] = mword[i].replace("ொ", "ொ")
                mword[i] = mword[i].replace("ோ", "ோ")



#                //6 - Translation
            if (opt == true):
                if (ottran[i][ 0] == 0):
                    istrans = false

                    for key in tword.keys():
                        tname = key
                        if tname in mword[i]:
                            if (len(tword[tname]) > 0):
                                for k in tword[tname]:
#                                          {//k is array of suggestions
                                    a = str(k['t'])
                                    b = str(k['w'])

                                    for l in tranrule[a]:
                                        map = str(l['t']).split(',')

                                        if  (tname + map[0]) in mword[i]:

                                            nword = mword[i].replace(tname + map[0], b + map[1])

                                            if (checkword(nword, 0)):
                                                addparinthu(parinthu, i, nword)
                                                istrans = true

                    if (istrans == true):
                        ottran[i, 0] = 1



   #             //7.sandhi remover and sandi/punarchi memory
            if ((i + 2) < len(mword)):
                if (len(mword[i + 2]) > 0):
                    ottru = mword[i][(len(mword[i]) - 2):]
                    methi = mword[i][0:len(mword[i]) - 2]
                    muthal = mword[i + 2][0: 1]

                    rgx1 = "[கசதப]்"
                    rgx2 = "[கசதப]"

                    if re.match(rgx1,ottru):
                        if (muthal + "்" == ottru):
                            mword[i] = methi
                            sandi = ottru;

                    elif ottru == "ட்":
                        if re.match(rgx2,muthal):
                             mword[i] = methi + "ள்"
                             punarchi = true

                    elif ottru == "ற்":
                        if re.match(rgx2,muthal):
                             mword[i] = methi + "ல்"
                             punarchi = true

                    elif ottru == "ங்":
                        if muthal == "க":
                            mword[i] = methi + "ம்"
                            sandi = "ங்"
                            punarchi = true

                    elif ottru == "ஞ்":
                        if muthal == "ச":
                            mword[i] = methi + "ம்"
                            sandi = "ஞ்"
                            punarchi = true

                    elif ottru == "ந்":
                        if muthal == "த":
                            mword[i] = methi + "ம்"
                            sandi = "ந்"
                            punarchi = true


#           o     //8. skip if it is repeated word
            found = cacheword.find(mword[i] + sandi)

            if found > -1:
                a = cacheword[found]
                if (a == mword[i] + sandi):
                    b = cachesug[found]
                    parinthu[i][1] = b

                    if not istamil(b):
                        parinthu[i][0] = 0
                    elif b.find(',') < 0:
                        parinthu[i][0] = 1
                    else:
                        parinthu[i][0] = len(b.split(','))
                    ottran[i][0] = 1




#            //9 - skip if was userpreferance
            if (ottran[i][0] == 0):
                for a in userOword:
                    if (a == str(mword[i])):
                        ottran[i][ 0] = 1
                        parinthu[i][1] = "correct"
                        parinthu[i][0] = 0

            if (ottran[i][0] == 0):
                for a in usergword:
                    nword = a.split('|')

                    if (nword[0] == str(mword[i])):
                        parinthu = addparinthu(parinthu, i, nword[1])


#                //10 - word match
            if (ottran[i][0] == 0):
                if (checkword(mword[i], 0)):
                    ottran[i][0] = 1
                    parinthu[i][1] = "correct"
                    parinthu[i][0] = 0



#                                    //11 - gword suggestion
            if (opt == true):
                if (ottran[i][0] == 0):
                    sample = getsuggestion(mword[i])
                    emp = {}
                    sample2 = getsuggestion2(mword[i])
                    sample = list(sample + sample2)
                    usample = set(sample)

                    for l in usample:
                        nword = 1
                        if (checkword(nword, 7)):
                            if (punarchi):
                                ottru = nword[len(nword) - 2]
                                methi = nword[0, len(nword) - 2]

                                if (ottru == "ள்"):
                                    addparinthu(parinthu, i, methi + "ட்")
                                elif (ottru == "ல்"):
                                    addparinthu(parinthu, i, methi + "ற்")
                                elif ottru == "ம்":
                                    addparinthu(parinthu, i, methi + sandi)

                            else:
                                parinthu = addparinthu(parinthu, i, nword + sandi)





#                //12 cache the search
            if (len(mword[i]) > 0):

                if not (mword[i] + sandi) in cacheword:

                    cacheword.append(mword[i] + sandi)
                    cachesug.append(parinthu[i][1])



            #//13 - Check sandhi need or not needed should not cache
            if (ottran[i],[0] == 1): #//if this word is correct
                if (len(mword) > i + 2):
                    if (len(mword[i + 2]) > 1):
                        chandi = mword[i + 2][0: 1] + "்"  #;//if user did give chandi
                        rgx1 = "[கசதப]்"

                        if re.match(rgx1,chandi) : # ) //if next word is kachathapa
                            if (checkword(mword[i + 2], 0)):
                                ottran[i + 2][0] = 1
                                parinthu[i + 2][1] = "correct"
                                parinthu[i + 2][0] = 0

                            if (ottran[i + 2][0] == 1): #//if next word is correct
                                combo = checkword(mword[i] + mword[i + 2], 0)
                                thibo = checkword(mword[i] + chandi + mword[i + 2], 0)
                                derive = checkword(mword[i], 5)  # ;//return true if it is valid perfect noun

                                if (sandi != ""):

                                    if combo:
                                        if not thibo:
                                            parinthu = addparinthu(parinthu, i, mword[i])
                                else:
                                    if thibo:
                                        if not combo:
                                            if not derive:
                                                parinthu = addparinthu(parinthu, i, mword[i] + chandi)

# 14 commented in source itself
#            //14 - for Developer Sheet research
#            if (ottran[i][0] == 0):
#                if (parinthu[i][0] > 0):
#                    //byproduct(mword[i], parinthu[i].join(","));


        if mode=="web":
            z = ":"
            Arr = ""
            for i in parinthu:  #//foreach can't be used, since dynamic(multi dimension) will return all units and no increments are not accepted
                Arr = Arr + str(i) + z
                if (z == ":"):
                    z = "|"
                else:
                    z = ":"
            return Arr[0: len(Arr) - 1]
        else:
            return parinthu


# def RemoveDuplicates(s):
#
#We can use set instead of this function. Hence skipping this.
#

def getsample(b,c,a,d):
    raise NotImplementedError() #TBD.

def getsuggestion(c):  #//c is  mword[i]
    sug = {}
    gword = db[0]["DB"][0]
    for j in gword.keys():
#                    {//j gives every miswords
        a = j
        if a in c:
            if (len(gword[a]) > 0):
                for k in gword[a]:
                    b = str(k['t'])
                    d = str(k['w'])

                    if (b == "9"):
                        supersug = c.replace(a, d)

                        if (checkword(supersug, 0)):
                            supersugg = { supersug }
                            return supersugg
                        else:
                            sug1 = {}
                            suggest = getsuggestion(c.replace(a, "s"))
                            sug1 = list(sug1 + suggest)

                            for l in range(len(sug1)):
                                sug1[l] = sug1[l].replace("s", d)
                                return sug1

                    else:
                        sug = list(sug + (getsample(b, c, a, d)))



    sug = list(sug + getsample("100", c, "", "்")) # //special logics for ்
    sug = list(sug + getsample("100", c, "", "ா")) # .ToArray();//special logics for ா
    sug = list(sug + getsample("100", c, "", "ி")) # .ToArray();//special logic ி
    sug = list(sug + getsample("100", c, "", "ை")) # .ToArray();//special logic ை
    sug = list(sug + getsample("101", c, "", "")) # .ToArray();//special logics for ர-ா
    sug = list(sug + getsample("102", c, "", "1")) #.ToArray();
    sug = list(sug + getsample("102", c, "", "2")) #.ToArray();
    sug = list(sug + getsample("102", c, "", "3")) #.ToArray();
    return sug



# #region get third level suggestions for given word
def getsuggestion3(c, supl, n):
    jObj = json.loads(supl)
    o = len(jObj)

    if o < 3:
        if n < 1:
            supgword_json = "{\"க\":[{\"t\":\"5\",\"w\":\"க்க\"}],\"க்க\":[{\"t\":\"0\",\"w\":\"க\"}],\"ச\":[{\"t\":\"5\",\"w\":\"ச்ச\"}],\"ச்ச\":[{\"t\":\"0\",\"w\":\"ச\"}],\"த\":[{\"t\":\"5\",\"w\":\"த்த\"}],\"த்த\":[{\"t\":\"0\",\"w\":\"த\"}],\"ப\":[{\"t\":\"5\",\"w\":\"ப்ப\"}],\"ப்ப\":[{\"t\":\"0\",\"w\":\"ப\"}],\"ர\":[{\"t\":\"0\",\"w\":\"ற\"}],\"ற\":[{\"t\":\"0\",\"w\":\"ர\"}],\"ல\":[{\"t\":\"0\",\"w\":\"ள\"},{\"t\":\"0\",\"w\":\"ழ\"}],\"ள\":[{\"t\":\"0\",\"w\":\"ல\"},{\"t\":\"0\",\"w\":\"ழ\"}],\"ழ\":[{\"t\":\"0\",\"w\":\"ல\"},{\"t\":\"0\",\"w\":\"ள\"}],\"ந\":[{\"t\":\"0\",\"w\":\"ன\"},{\"t\":\"0\",\"w\":\"ண\"}],\"ன\":[{\"t\":\"0\",\"w\":\"ந\"},{\"t\":\"0\",\"w\":\"ண\"}],\"ண\":[{\"t\":\"0\",\"w\":\"ன\"},{\"t\":\"0\",\"w\":\"ந\"}]}"
            supword = json.loads(supgword_json)

            jsonString = ""

            for j in supword.keys():
                a = j
                if a in c:
                    jsonString = jsonString + ",\"" + a + "\":" + json.dumps(supgword[a]) #//suplist[j]=supgword[j];

            jsonString = "{" + jsonString[1:] + "}" #;//placing comma at begginging

    else:
         jsonString = json.dumps(supl)
         suplist = json.loads(jsonString)

         sug2 = {}

         for j in suplist.keys(): #//list of required super suggestion list
             c2 = {}
             a = j
             for k in suplist[a]:
 #                //k is array of suggestions
                 b = k['t']
                 d = k['w']
                 p = "p" + str(n)

                 getsamplec2 = getsample(b, c, a, p)

                 c2 = list(c2 + getsamplec2)

                 suplist2 = json.loads(json.dumps(suplist)) #;//to avoid original json change

                 suplist2.remove(a) #YTD Have to find the relevant remove method for python

                 sug2 = list(sug2 + c2)

                 suplist2Obj = json.dumps(suplist2)

                 if (len(suplist2Obj) > 2):
                     for l in range(len(c2)):
                         getsuggestion2sug2 = getsuggestion3(c2[l], suplist2, n + 1)
                         sug2 = list(sug2 + getsuggestion2sug2)


                 for l in range(len(sug2)):
                     sug2[l] = sug2[l].replace(p, d)

         return sug2


gpathil11("நன்றி",'அஇஉ','ஈஈஊ')
getsuggestion("அன்றி")