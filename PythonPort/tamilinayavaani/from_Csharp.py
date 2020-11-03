#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
import os
import sys

sys.path.append("/home/tamil-sandhi-checker")
from tamilsandhi.sandhi_checker import check_sandhi
DEBUG=False

def get_data_dir(data_dir):
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return os.path.sep.join([dirname,data_dir])

peyar = "MLTYWNEIQOGDHVXBPSളവ"
speyar = "CAJ"
venai = "ஆலனசளணஇழஉஓடதदधபநमயரறवउपकतईटरलळएचज"
nonderi = "Z"
deri = peyar + speyar + venai + "FUKഡഗജദപ"

cacheword = []
cachesug = []


def refreshcache(nword):
    found = cacheword.index(nword)
    cachesug[found] = "correct"


with open(os.path.join(get_data_dir('json'),'db.lint.valid.json'), encoding='utf-8-sig') as json_file:
    db = json.load(json_file)

# print(db[0]['DB'][3])
Oword = db[0]["DB"][4]  # //Words
Eword = db[0]["DB"][3]
tranrule = db[0]["DB"][2]
tword = db[0]["DB"][1]  # substiture english words to tamil words
gword = db[0]["DB"][0]

#        // string[] sandhi = { "க", "ச", "த", "ப" };
vauyir_json = "{\"வா\":\"ஆ\",\"வி\":\"இ\",\"வீ\":\"ஈ\",\"வு\":\"உ\",\"வூ\":\"ஊ\",\"வெ\":\"எ\",\"வே\":\"ஏ\",\"வை\":\"ஐ\",\"வொ\":\"ஒ\",\"வோ\":\"ஓ\",\"வௌ\":\"ஒள\"}"  # //\"வ\":\"அ\",
yauyir_json = "{\"யா\":\"ஆ\",\"யி\":\"இ\",\"யீ\":\"ஈ\",\"யு\":\"உ\",\"யூ\":\"ஊ\",\"யெ\":\"எ\",\"யே\":\"ஏ\",\"யை\":\"ஐ\",\"யொ\":\"ஒ\",\"யோ\":\"ஓ\",\"யௌ\":\"ஒள\"}"  # );// \"ய\":\"அ\",
auyir_json = "{\"ா\":\"ஆ\",\"ி\":\"இ\",\"ீ\":\"ஈ\",\"ு\":\"உ\",\"ூ\":\"ஊ\",\"ெ\":\"எ\",\"ே\":\"ஏ\",\"ை\":\"ஐ\",\"ொ\":\"ஒ\",\"ோ\":\"ஓ\",\"ௌ\":\"ஒள\"}"

vauyir = json.loads(vauyir_json)
yauyir = json.loads(yauyir_json)
auyir = json.loads(auyir_json)


def getviku(v, c, sc):
    blocks = ""

    if sc == "15":
        blocks = "01234567"

    if sc == "25":
        blocks = "0123456"

    if sc == "07":
        blocks = "0123456"

    if sc == "10":
        blocks = "01235"

    if sc == "11":  # //except special
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

    if sc == "17":  # //special
        blocks = "0"

    if sc == "08":  # //Peyar speical extension அநவரத  venai present echam சுவைப்பட,நாள்பட
        blocks = "4"

    if sc == "18":  # //special  -> 08 also takes 4 segment
        blocks = "4"

    if sc == "19":  # //special
        blocks = "5"

    if sc == "20":  # //special
        blocks = "6"

    if sc == "21":  # //special
        blocks = "7"

    if sc == "24":  # //echam verb is using
        blocks = "34"

    for d in range(8):
        if (str(d) in blocks):
            for b in range(len(v), -1, -1):

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

    return False


# uncomplete
# region check the word with existing root words


def checkroot(word):
    outp = word.split(',')

    # rule = JsonConvert.DeserializeObject("{\"M\":\"ம்\",\"L\":\"ு\",\"T\":\"ு\",\"Y\":\"\",\"W\":\"\",\"N\":\"\",\"E\":\"\",\"I\":\"ல்\",\"Q\":\"ள்\",\"ള\":\"ள்\",\"O\":\"்\",\"P\":\"்\",\"S\":\"்\",\"V\":\"ு\",\"വ\":\"ு\",\"ഗ\":\"\",\"ഡ\":\"\",\"ജ\":\"\",\"ദ\":\"\",\"പ\":\"\",\"B\":\"ை\",\"G\":\"ர்\",\"D\":\"ர்\",\"X\":\"ர்\",\"H\":\"ர்\",\"ஆ\":\"தல்\",\"ல\":\"ல்தல்\",\"ன\":\"ல்தல்\",\"ச\":\"்லுதல் \",\"ள\":\"ள்தல்\",\"ண\":\"ள்ளுதல்\",\"இ\":\"ுதல்\",\"ழ\":\"ுதல்\",\"உ\":\"தல்\",\"ஓ\":\"தல்\",\"ட\":\"ுதல்\",\"த\":\"த்தல்\",\"द\":\"த்தல்\",\"ध\":\"த்தல்\",\"ப\":\"்த்தல்\",\"ந\":\"த்தல்\",\"म\":\"த்தல்\",\"ய\":\"தல்\",\"ர\":\"்தல்\",\"ற\":\"ுதல்\",\"व\":\"ாதல்\",\"उ\":\"ணுதல்\",\"प\":\"்ணுதல்\",\"क\":\"ாண்ணுதல்\",\"त\":\"னுதல்\",\"ई\":\"்னுதல்\",\"ट\":\"ள்தல்\",\"र\":\"ல்தல்\",\"ल\":\"ல்தல்\",\"ळ\":\"ுதல்\",\"ए\":\"றுதல்\",\"च\":\"தல் \",\"ज\":\"ேகுதல்\"}");
    rule_json = "{\"M\":\"ம்\",\"L\":\"ு\",\"T\":\"ு\",\"Y\":\"\",\"W\":\"\",\"N\":\"\",\"E\":\"\",\"I\":\"ல்\",\"Q\":\"ள்\",\"ള\":\"ள்\",\"O\":\"்\",\"P\":\"்\",\"S\":\"்\",\"V\":\"ு\",\"വ\":\"ு\",\"ഗ\":\"\",\"ഡ\":\"\",\"ജ\":\"\",\"ദ\":\"\",\"പ\":\"\",\"B\":\"ை\",\"G\":\"ர்\",\"D\":\"ர்\",\"X\":\"ர்\",\"H\":\"ர்\",\"ஆ\":\"தல்\",\"ல\":\"ல்தல்\",\"ன\":\"ல்தல்\",\"ச\":\"்லுதல் \",\"ள\":\"ள்தல்\",\"ண\":\"ள்ளுதல்\",\"இ\":\"ுதல்\",\"ழ\":\"ுதல்\",\"உ\":\"தல்\",\"ஓ\":\"தல்\",\"ட\":\"ுதல்\",\"த\":\"த்தல்\",\"द\":\"த்தல்\",\"ध\":\"த்தல்\",\"ப\":\"்த்தல்\",\"ந\":\"த்தல்\",\"म\":\"த்தல்\",\"ய\":\"தல்\",\"ர\":\"்தல்\",\"ற\":\"ுதல்\",\"व\":\"ாதல்\",\"उ\":\"ணுதல்\",\"प\":\"்ணுதல்\",\"क\":\"ாண்ணுதல்\",\"त\":\"னுதல்\",\"ई\":\"்னுதல்\",\"ट\":\"ள்தல்\",\"र\":\"ல்தல்\",\"ल\":\"ல்தல்\",\"ळ\":\"ுதல்\",\"ए\":\"றுதல்\",\"च\":\"தல் \",\"ज\":\"ேகுதல்\"}"

    rule = json.loads(rule_json)
    #   print(rule)

    for a in range(len(word) - 1, -1, -1):
        #print(a)
        paku = word[0:a]
        #print("paku = " + paku)
        viku = word[a]
        #print("viku = " + viku)

        #        print(Oword[paku])

        if paku in Oword:
            qcode = Oword[paku]

            if (qcode) and (len(qcode) > 0):
                for b in qcode:
                    #print("qcode = " + str(b))
                    code = b['t'][0:1]
                    #print("code = " + code)
                    subcode = b['t'][1:]
                    #print("subcode = " + subcode)
                    vikuthi = getviku(viku, code, subcode)

                    if vikuthi != "false":
                        outp[0] = paku + str(rule[code])
                        outp[1] = " " + tranlate(vikuthi)
                        return outp

                    #print(outp)


# checkroot("நன்றிகள்")


# done
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


# print(tranlate("㚱"))

# lazy caching.
class _Cached:
    _g_userOword=None
    _g_usergword=None

def gpathil11(mword, opt=True, mode='exe'):
    """ entry point of the spell-checker. Default option is True, mode = 'exe'."""
    # print("gpathil11" + mword[0] )
    user_file = os.path.join(get_data_dir("koppu"),"user.txt")
    if os.path.exists(user_file):
        if (not _Cached._g_userOword) and (not _Cached._g_usergword):
            with open(user_file, 'r') as fp:
                userfile = fp.readlines()
            userOword = userfile[0].split(',')
            usergword = userfile[1].split(',')
            _Cached._g_userOword = userOword
            _Cached._g_usergword = usergword
        else:
            userOword = _Cached._g_userOword
            usergword = _Cached._g_usergword
    else:
        userOword = ""
        usergword = ""
    splitchar = ','

    parinthu = [[None, None] for i in range(len(mword))]
    ottran = [[None, None] for i in range(len(mword))]

    #    mword,result_stats = check_sandhi(mword)
    #    print(mword)
    #    print(result_stats)
    for i in range(len(mword)):
        parinthu[i][0] = 0  # ;//count of suggestion
        parinthu[i][1] = "wrong"  # ;//suggestions
        ottran[i][0] = 0
        ottran[i][1] = 1

    for i in range(len(mword)):
        sandi = ""
        punarchi = False

        #1 - if it is verified already
        if (ottran[i][0] == 1):
            continue

        #2 - removing blank char
        if (len(mword[i]) < 1):
            parinthu[i, 0] = -1
            parinthu[i, 1] = ""
            continue

        #3.ignoring single consonant letters
        if (len(mword[i]) == 2):

            rgx = "[ா-்]"
            if (re.match(rgx, mword[i][-1])):
                ottran[i][0] = 1
                parinthu[i][1] = "correct"
                parinthu[i][0] = 0
                continue

        #4.ignoring single vowel letters
        if (len(mword[i]) == 1):
            ottran[i][0] = 1
            parinthu[i][1] = "correct"
            parinthu[i][0] = 0
            continue

        #5- Typo Correction
        mword[i] = mword[i].replace("ொ", "ொ")
        mword[i] = mword[i].replace("ோ", "ோ")

        #6 - Translation
        if (opt == True):
            if (ottran[i][0] == 0):
                istrans = False

                for key in tword.keys():
                    tname = key
                    if tname in mword[i]:
                        if (len(tword[tname]) > 0):
                            for k in tword[tname]:
                                #k is array of suggestions
                                a = str(k['t'])
                                b = str(k['w'])
                                for l in tranrule[a]:
                                    map = str(l['t']).split(splitchar)
                                    if (tname + map[0]) in mword[i]:
                                        nword = mword[i].replace(tname + map[0], b + map[1])
                                        if (checkword(nword, 0)):
                                            addparinthu(parinthu, i, nword)
                                            istrans = True
                if (istrans == True):
                    ottran[i, 0] = 1

        #7.sandhi remover and sandi/punarchi memory
        if ((i + 2) < len(mword)):
            if (len(mword[i + 2]) > 0):
                muthal = mword[i + 2][0: 1]
                rgx1 = "[கசதப]்"
                rgx2 = "[கசதப]"
                # if the second word starts with any uyirmei of கசதப let us call sandhi checker

                if re.match(rgx2, muthal):
                    #                if re.match(rgx2,muthal) and  not (mword[i][(len(mword[i]) - 2):] == muthal + "்"):
                    sanlist = [mword[i], mword[i + 2]]
                    sanlist, result_stats = check_sandhi(sanlist)
                    #print(sanlist)
                    #print(result_stats)
                    if sanlist[0] != mword[i]:
                        mword[i] = sanlist[0]
                        parinthu[i][0] = 1
                        parinthu[i][1] = sanlist[0]

                ottru = mword[i][(len(mword[i]) - 2):]
                methi = mword[i][0:len(mword[i]) - 2]

                if re.match(rgx1, ottru):
                    if (muthal + "்" == ottru):
                        if (parinthu[i][0] == 0):
                            mword[i] = methi
                            sandi = ottru

                elif ottru == "ட்":
                    if re.match(rgx2, muthal):
                        mword[i] = methi + "ள்"
                        punarchi = True

                elif ottru == "ற்":
                    if re.match(rgx2, muthal):
                        mword[i] = methi + "ல்"
                        punarchi = True

                elif ottru == "ங்":
                    if muthal == "க":
                        mword[i] = methi + "ம்"
                        sandi = "ங்"
                        punarchi = True

                elif ottru == "ஞ்":
                    if muthal == "ச":
                        mword[i] = methi + "ம்"
                        sandi = "ஞ்"
                        punarchi = True

                elif ottru == "ந்":
                    if muthal == "த":
                        mword[i] = methi + "ம்"
                        sandi = "ந்"
                        punarchi = True

        #           o     //8. skip if it is repeated word
        if (mword[i] + sandi) in cacheword:
            found = cacheword.index(mword[i] + sandi)
        else:
            found = -1

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

        #9 - skip if was userpreferance
        if (ottran[i][0] == 0):
            for a in userOword:
                if (a == str(mword[i])):
                    ottran[i][0] = 1
                    parinthu[i][1] = "correct"
                    parinthu[i][0] = 0

        if (ottran[i][0] == 0):
            for a in usergword:
                nword = a.split('|')

                if (nword[0] == str(mword[i])):
                    parinthu = addparinthu(parinthu, i, nword[1])

        #10 - word match
        if (ottran[i][0] == 0):
            if (checkword(mword[i], 0)):
                ottran[i][0] = 1
                parinthu[i][1] = "correct"
                parinthu[i][0] = 0

        #11 - gword suggestion
        if (opt == True):
            if (ottran[i][0] == 0):
                sample = getsuggestion(mword[i])
                #emp = {}
                sample2 = getsuggestion2(mword[i])
                sample2.extend(sample)
                usample = set(sample2)
                #print(usample)

                for l in usample:
                    nword = l
                    if (checkword(nword, 7)):
                        # print('nword' + ' ' + nword)
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

        # 13 - Check sandhi need or not needed should not cache
        if (ottran[i], [0] == 1):  # //if this word is correct
            if (len(mword) > i + 2):
                if (len(mword[i + 2]) > 1):
                    chandi = mword[i + 2][0: 1] + "்"  # ;//if user did give chandi
                    rgx1 = "[கசதப]்"

                    if re.match(rgx1, chandi):  # ) //if next word is kachathapa
                        if (checkword(mword[i + 2], 0)):
                            ottran[i + 2][0] = 1
                            parinthu[i + 2][1] = "correct"
                            parinthu[i + 2][0] = 0

                        if (ottran[i + 2], [0] == 1):  # //if next word is correct
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
    #    print(parinthu)

    if mode == "web":
        z = ":"
        Arr = ""
        for i in parinthu:  # //foreach can't be used, since dynamic(multi dimension) will return all units and no increments are not accepted
            Arr = Arr + str(i) + z
            if (z == ":"):
                z = "|"
            else:
                z = ":"
        return Arr[0: len(Arr) - 1]
    if DEBUG: print(parinthu)
    return parinthu

# def RemoveDuplicates(s):
#
# We can use set instead of this function. Hence skipping this.
#

def getsuggestion(c):  # //c is  mword[i]
    # print("getsuggestion" + " " + c)
    #    sug = {}
    sug = []
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
                            supersugg = {supersug}
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
                        sug.extend(getsample(b, c, a, d))

    sug = list(sug + getsample("100", c, "", "்"))  # //special logics for ்
    sug = list(sug + getsample("100", c, "", "ா"))  # .ToArray();//special logics for ா
    sug = list(sug + getsample("100", c, "", "ி"))  # .ToArray();//special logic ி
    sug = list(sug + getsample("100", c, "", "ை"))  # .ToArray();//special logic ை
    sug = list(sug + getsample("101", c, "", ""))  # .ToArray();//special logics for ர-ா
    sug = list(sug + getsample("102", c, "", "1"))  # .ToArray();
    sug = list(sug + getsample("102", c, "", "2"))  # .ToArray();
    sug = list(sug + getsample("102", c, "", "3"))  # .ToArray();
    # print(sug)
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
                    jsonString = jsonString + ",\"" + a + "\":" + json.dumps(supword[a])  # //suplist[j]=supgword[j];

            jsonString = "{" + jsonString[1:] + "}"  # ;//placing comma at begginging

    else:
        jsonString = json.dumps(supl)
        suplist = json.loads(jsonString)

        sug2 = {}

        for j in suplist.keys():  # //list of required super suggestion list
            c2 = {}
            a = j
            for k in suplist[a]:
                #                //k is array of suggestions
                b = k['t']
                d = k['w']
                p = "p" + str(n)

                getsamplec2 = getsample(b, c, a, p)

                c2 = list(c2 + getsamplec2)
                #                 c2 = list(c2)
                suplist2 = json.loads(json.dumps(suplist))  # ;//to avoid original json change

                suplist2.remove(a)  # YTD Have to find the relevant remove method for python

                sug2 = list(sug2 + c2)

                suplist2Obj = json.dumps(suplist2)

                if (len(suplist2Obj) > 2):
                    for l in range(len(c2)):
                        getsuggestion2sug2 = getsuggestion3(c2[l], suplist2, n + 1)
                        sug2 = list(sug2 + getsuggestion2sug2)

                for l in range(len(sug2)):
                    sug2[l] = sug2[l].replace(p, d)

        return sug2

    # get second level suggestion for given word


def getsuggestion2(word):
    # print("getsuggestion2" + " " + word)
    sugword = ["க்க,க", "ச்ச,ச", "த்த,த", "ப்ப,ப", "ற,ர", "ல,ள,ழ", "ந,ன,ண"]
    sug = []
    limit = len(word)
    for h in range(0, limit):
        sug1 = []
        flag = False
        for i in range(0, len(sugword)):
            poss = sugword[i].split(',')
            if (flag == False):
                for j in range(0, len(poss)):
                    if (flag == False):
                        if (len(word) >= len(poss[j])):
                            if (word[0: len(poss[j])] == poss[j]):
                                word = word[len(poss[j]):]
                                sug1 = sug1 + combination(sug, poss)
                                flag = True
                                break

        if (len(sug1) < 1):
            if (len(word) > 0):
                sug = combination(sug, [word[0:1]])
                word = word[1:]
        else:
            sug = sug1.copy()
            if (len(sug) > 1000):
                return []
    # print(sug)
    return sug


def combination(word, sug):
    if (len(word) == 0):
        return sug

    sug1 = []

    for i in sug:
        for j in word:
            sug1.append(j + i)

    return sug1


def getsample(code, word, fstr, tstr):
    sample = []
    if code == "0":
        sample.append(word.replace(fstr, tstr))  # all replace
        for j in range(word.count(fstr)):
            sample.append(nth_replace(word, fstr, tstr, j))  # eachone replace
    elif code == "1":  # ச->ச்   should not be starting letter.should be end with perfect mei
        cmatch1 = re.finditer(fstr + "([ா-்]|)", word)
        incre = 0
        a = word
        for mat in cmatch1:
            c1 = mat.group(0)
            count = mat.start()
            c2 = mat.group(1)
            if (ismat(c2, count)):
                a = a[0:count + incre] + tstr + a[count + len(c1) + incre:]
                incre += len(tstr) - len(c1)
                sample.append(word[:count] + tstr + word[count + len(c1):])
    elif code == "2":  # should not be starting letter
        cmatch2 = re.finditer(fstr, word)
        incre = 0
        a = word
        for mat in cmatch2:
            c1 = mat.group(0)
            count = mat.start()
            #            c2 = mat.group(1)
            if count > 0:  # eachone replace?
                a = a[:count + incre] + tstr + a[count + len(c1) + incre:]  # all replace?
                incre += len(tstr) - len(c1)
                sample.append(word[:count] + tstr + word[count + len(c1):])
    elif code == "3":  # should only be last letter
        thala = word[:len(word) - len(fstr)]
        if word == thala + fstr:
            sample.append(thala + tstr)
    elif code == "9":
        pass  # since it is dual check, handled before income?
    elif code == "4":  # should only be first letter
        mcase4 = re.search(fstr, word)
        if mcase4.group(0) == 0:
            sample.append(tstr + word[:len(fstr)])  # when it match with first character
    elif code == "5":  # replace each one
        cmatch5 = re.finditer(fstr, word)
        incre = 0
        for mat in cmatch5:
            c1 = mat.group(0)
            count = mat.start()
            if (count > 0 and count < len(word) - 1):
                incre += len(tstr) - len(c1)
                sample.append(word[:count] + tstr + word[count + len(c1):])
    elif code == "101":  # நரர்கள் -> நார்கள்
        matches0 = re.finditer("[க-ஹ]ர([^ா-்]|)", word)
        a = word
        for mat in matches0:
            count = mat.start()
            a = a[:count - 1] + "ா" + a[count:]  # all replace
            sample.append(word[:count - 1] + "ா" + word[count:])
        sample.append(a)
    elif code == "102":  # for repeated sequence
        diff = int(tstr)
        for i in range(len(word) - (diff * 2)):
            if (word[i:i + diff] == word[i + diff:i + diff + diff]):
                sample.append(word[:i] + word[i + diff:])
    elif code == "100":
        #       ச->ச்
        matches2 = re.finditer("[க-ஹ]([ா-்]|)", word)
        incre = 0
        a = word
        for mat in matches2:
            c1 = mat.group(0)
            count = mat.start()
            c2 = mat.group(1)
            if (ismat(c2, count)):
                a = a[:count + incre] + c1 + tstr + a[count + len(c1) + incre:]  # all replace
                incre += len(tstr) - len(fstr)
                sample.append(word[:count] + c1 + tstr + word[count + len(c1):])
        sample.append(a)

        #       க்ச->கச் ottru post shifter
        matches4 = re.finditer("[க-ஹ]" + tstr + "[க-ஹ]([ா-்]|)", word)
        incre = 0
        a = word
        for mat in matches4:
            c1 = mat.group(0)
            count = mat.start()
            c2 = mat.group(1)
            if (ismat(c2, count)):
                a = word[:count] + c1[:1] + c1[2:3] + tstr + word[count + len(c1):]
                sample.append(a)

        #       கச்->க்ச ottru pre shifter படிபப்டியாக
        matches5 = re.finditer("[க-ஹ]" + tstr + "[க-ஹ]([ா-்]|)", word)
        incre = 0
        a = word
        for mat in matches5:
            c1 = mat.group(0)
            count = mat.start()
            c2 = mat.group(1)
            if (ismat(c2, count)):
                a = word[:count] + c1[:1] + tstr + c1[1:2] + word[count + len(c1):]
                sample.append(a)

        #       ப்ட்ட->ப்டட் doubleottru post shifter
        matches6 = re.finditer("[க-ஹ]" + tstr + "[க-ஹ]([ா-்]|)", word)
        incre = 0
        a = word
        for mat in matches6:
            c1 = mat.group(0)
            count = mat.start()
            c2 = mat.group(1)
            if (ismat(c2, count)):
                a = word[:count] + c1[:3] + c1[4:5] + tstr + word[count + len(c1):]
                sample.append(a)

    #       பட்ட்->ப்டட் doubleottru pre shifter-unused since pratically ottru pre shifter do this
    #       word.replace(RegExp("[க-ஹ]([ா-்]|)[க-ஹ]"+tstr+"[க-ஹ]"+tstr, "gi"), function (c1,c2,count,word) {if(ismat(c2,count)){var a =word.substr(0,count)+c1.substr(0,1)+tstr+c1.substr(1,1)+c1.substr(3,2)+word.substr(count+c1.length);sample.push(a);}return ;});

    return sample


def nth_replace(str, search, repl, index):
    split = str.split(search, index + 1)
    if len(split) <= index + 1:
        return str
    return search.join(split[:-1]) + repl + split[-1]


def ismat(v1, v2):
    # v1 needs to be blank since reg needs no ா-் nearby
    # v2 needs to be integer and not first letter
    if ((v2 > 0) and (v1 == "")):
        return True
    else:
        return False


# concating the suggestion alltogether to the suggestion of the wrong word
# public dynamic addparinthu(dynamic parinthu, int i, string w)
def addparinthu(parinthu, i, w):
    # does it check value in string with comma
    if (parinthu[i][1].find(w) < 0):  # to avoid duplicate suggestion
        # since unable to increase the array size
        if (int(parinthu[i][0]) > 0):
            parinthu[i][0] = int(parinthu[i][0]) + 1
            parinthu[i][1] = parinthu[i][1] + "," + w
        else:
            parinthu[i][0] = 1
            parinthu[i][1] = w

    return parinthu


def byproduct(varthai, suggest):
    pass


def checkword(sol, typ):
    # print("checkword" + " " + sol)
    #  return true;
    # output true or false

    # type = 0 -> any code
    # type = 1 -> only peyar
    # type = 2 -> only venai
    # type = 3 -> peyar or venai
    # type = 4 -> non deri(Z,Adjective,adverb,conjuction,int)
    # type = 5 -> perfect noun without viku
    # ty4 -> non deri(Z,Adjective,adverb,conjuction,int)
    # type = 5 -> perfect noun without viku
    # type = 6 ->
    # type = 7 -> special used for suggestion check to avoid extensive derivatives

    sugges = 0  # zero = it is not suggestion word

    if (typ == 7):
        sugges = 1

    for a in range(len(sol), 0, -1):
        # It cuts from end. end is best since small word has many derivation like ഊ
        paku = sol[0:a]
        viku = sol[a:]  # ,sol.length
        #        qcode = Oword.get(paku)
        if paku in Oword:
            qcode = Oword[paku]

            #        if (qcode is not None) :
            if (len(qcode) > 0):
                # foreach (dynamic b in qcode)
                for b in qcode:
                    if (b.get("s") != None):
                        #                    if (b["s"] != None) :
                        return True  # to save time for foreign words and misspelled words

                    code = b["t"][0:1]
                    subcode = b["t"][1:]

                    if (typ == 0):
                        #                        break
                        continue
                    elif (typ == 1):
                        if ((peyar.find(code) == -1 or subcode != "15") and speyar.find(code) == -1):
                            continue
                    elif (typ == 2):
                        if (venai.find(code) == -1 or subcode != "15"):
                            continue
                    elif (typ == 3):
                        if (venai.find(code) == -1 and peyar.find(code) == -1):
                            continue
                    elif (typ == 4):
                        if (nonderi.find(code) == -1):
                            continue
                    elif (typ == 5):
                        if (peyar.find(code) != -1 and paku == sol and speyar.find(code) != -1 and code != "M"):
                            return True
                        else:
                            return False
                    elif (typ == 6):
                        if (subcode != "15"):
                            continue

                if (checkviku(paku, viku, "", code, subcode, sugges)):
                    return True

    return False


# third level suffix alanysis
def splitviku(viku, cod, scod, sugges):
    # used in verb and nouns with subcode 15
    # input  கிறவர்கள், ஆ
    # input   ர்கள், H

    # Logger.log(viku +", "+cod);
    # if(viku=="0")viku="";
    # for (int c = 1; c < viku.Length; c++) #starts from 1, zero given as last priority
    for c in range(1, len(viku)):
        subpaku = viku[0:c]
        subviku = viku[c:]
        if (checkviku("", subpaku, subviku, cod, scod, sugges)):
            return True

    if (checkviku("", "", viku, cod, scod, sugges)):  # similar effect of c=0 as it is needed to உலக-றிய
        return True

    return False


def codeuyir(part):
    # part -> ெழுதினார்
    # //் is that okay?
    if (len(part) < 1):
        return part  # To avoid empty string

    elu = ord(part[0:1])

    if (len(part) > 1):
        for key in auyir:
            c = key
            if (chr(elu) == c):
                return part.replace(c, chr(auyir[c]))

        if ((ord(elu) > 2965) and (ord(elu) < 2997)):
            return "அ" + part

    return part


# second level suffix analysis
def checkviku(p, v, sv, c, sc, sugges):  # paku,viku,subviku,code,subcode
    # input  "கொடு","க்கப்படுதல்","","த","15" ->looped again
    # input  "","க்கப்பட","ுதல்","த","15" ->looped again
    # input  "க்கப்பட","ுதல்","","இ","15"  ->passed
    # output    true   or false

    # நிகழ, ்ந்தமையால், , ர, 15
    # /்ந்த, மையால், , ഉ, 15

    # to adjust null part as zero
    # if(v==""){v="0";}//v needs to be blank in C#
    # if(sv==""){sv="0";}
    # don't adjust sv as 0

    # for வ family noun prefix starts
    if (c == "അ"):
        if (sv != ""):
            return False  # this special should act as prefix, so no sv
        secondword = p[-1] + v
        sw = ""

        if (len(secondword) > 2):
            sw = secondword
            for key, e in vauyir:
                d = key
                # if (sw.Substring(0, 2) == d) {
                if (sw[0: 2] == d):
                    sw = sw.replace(d, e)
                    break

                if (sw[0:1] == "வ"):
                    sw = "அ" + sw[1:]

        if (checkword(sw, 1)):
            return True
        elif (sw != secondword):
            secondword = p[-1] + v
            if (checkword(secondword, 1)):
                return True  # check the noun word
        return False
    # for வ noun prefix end

    # for ய family noun prefix starts
    if (c == "ആ"):
        if (sv != ""):
            return False
        secondword = p[-1] + v
        sw = ""
        if (len(secondword) > 2):
            sw = secondword
            for key, e in yauyir:
                d = key
                if (sw[0:2] == d):
                    sw = sw.replace(d, e)
                    break

            if (sw[0:1] == "ய"):
                sw = "அ" + sw[1:]

        if (checkword(sw, 1)):
            return True
        elif (sw != secondword):
            secondword = p[-1] + v
            if (checkword(secondword, 1)):
                return True

        return False
        # for ய family noun prefix end

    # for consonant family noun prefix
    if (c == "ഇ"):
        if (sv != ""):
            return False

        secondword = p[-1] + v

        if (checkword(secondword, 1)):
            return True

        return False

    # for vowel family verb prefix starts
    if (c == "ഉ"):
        if (sv != ""):
            return False
        secondword = codeuyir(v)
        if (checkword(secondword, 2)):
            return True

        return False

        # check verb word
    # for consonant family verb prefix starts
    if (c == "ഊ"):
        if (sv != ""):
            return False

        secondword = p[-1] + v
        if (checkword(secondword, 2)):
            return False

        return False

    # check verb word
    # for noun & verb
    if (c == "എ"):
        if (sv != ""):
            return False

        secondword = p[-1] + v
        if (checkword(secondword, 6)):
            return True

        return False

    # special code should not move further as Eword[ഊ] is not available
    # For nonderivatives Z family
    if ((v == "") and (nonderi.find(c) != -1)):
        return True

    blocks = ""

    sc_values = {
        "15": "01234567",
        "25": "0123456",
        "07": "012345",
        "10": "01235",
        "11": "012356",
        "09": "02",
        "06": "023",
        "05": "013",
        "04": "03",
        "03": "13",
        "02": "2",
        "01": "1",
        "16": "3",
        "17": "0",
        "08": "4",
        "18": "4",
        "19": "5",
        "20": "6",
        "21": "7",
        "24": "34"
    }

    #    blocks = sc_values[sc]
    blocks = sc_values.get(sc)
    for d in range(8):
        if str(d) not in blocks:
            #        if (blocks.find(d) == -1):
            continue

        if (Eword.get(c) is not None):
            if (Eword.get(c)[d].get(v) is not None):
                try:
                    if (derivative(Eword[c][d][v], v, sv, sugges)):
                        return True
                except:
                    pass

                    # C# need v as blank
    if (sv == ""):
        if (v != ""):
            if (deri.find(c) != -1):
                # to avoid adverb,adjective..
                if (splitviku(v, c, sc, sugges)):
                    return True

    return False


# check wheather derivatives are possible for given root words
def derivative(part, v, sv, sugges):
    # ① for extensive derivatives
    # ② for extensive derivatives excluded for suggestion
    if (part is not None):
        if ((part.find("①") != -1) or ((part.find("②") != -1) and (sugges == 0))):  # for extensive derivative

            # kudu = part.Substring(part.Length - 3, 1);//part.Length - 2
            startIndex = len(part) - 3
            endEndIndex = startIndex + 1
            kudu = part[startIndex:endEndIndex]

            # string elai = part.Substring(part.Length - 2);//part.Length
            elai = part[-2:]

            if (checkviku(v, sv, "", kudu, elai, sugges) == True):
                return True

            if (splitviku(sv, kudu, elai, sugges)):
                return True  # "க்கப்பட":"1இ" டுதலும் needs another split
        else:
            if (sv == ""):
                return True  # to return sucess if last part is blank
    return False

# validate and return true if given word is tamil
def istamil(aword):
    for a in aword:
        if (ord(a) >= 2944 and ord(a) <= 3071):
            return True
    return False
