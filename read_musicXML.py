from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn
import pandas as pd
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def attraction(p1,p2,fifths):
    #メロディック・アトラクションの算出
    #要素：anchoring strength
    #配列番号：pith class
    #辞書は文字列
    p1=p1.lower()
    p2=p2.lower()
    pitch=pitch_class(fifths)
    pc1=int(pitch[p1])
    pc2=int(pitch[p2])
    ##pc1とpc2が同じ値のときの処理も書く
    n=abs(pc2-pc1)#絶対値abs
    #print(n)
    if n>6:
        n=12-n
    #ピッチクラス0～11に対するアトラクタ
    x = np.array([4,1,2,1,3,2,1,3,1,2,1,2])
    if n>0:
        attr=x[pc2]/x[pc1]/n/n
    else:
        attr=0

    return attr


def pitch_class(fifths):
    if fifths == "C":
        #Cメジャーのピッチクラス
        pitch={'c':'0','c#':'1','d':'2','d#':'3','e':'4','f':'5','f#':'6','g':'7','g#':'8','a':'9','a#':'10','b':'11'}
    elif fifths == "C-sharp" or fifths=="D-flat":
        #C#メジャーのピッチクラス
        pitch={'c':'11','c#':'0','d':'1','d#':'2','e':'3','f':'4','f#':'5','g':'6','g#':'7','a':'8','a#':'9','b':'10'}
    elif fifths == "D":
        #Dメジャーのピッチクラス
        pitch={'c':'10','c#':'11','d':'0','d#':'1','e':'2','f':'3','f#':'4','g':'5','g#':'6','a':'7','a#':'8','b':'9'}
    elif fifths == "E-flat" or fifths=="D-sharp":
        #D#メジャーのピッチクラス
        pitch={'c':'9','c#':'10','d':'11','d#':'0','e':'1','f':'2','f#':'3','g':'4','g#':'5','a':'6','a#':'7','b':'8'}
    elif fifths == "E":
        #Eメジャーのピッチクラス
        pitch={'c':'8','c#':'9','d':'10','d#':'11','e':'0','f':'1','f#':'2','g':'3','g#':'4','a':'5','a#':'6','b':'7'}
    elif fifths == "F":
        #Fメジャーのピッチクラス
        pitch={'c':'7','c#':'8','d':'9','d#':'10','e':'11','f':'0','f#':'1','g':'2','g#':'3','a':'4','a#':'5','b':'6'}
    elif fifths == "F-sharp" or fifths=="G-flat":
        #F#メジャーのピッチクラス
        pitch={'c':'6','c#':'7','d':'8','d#':'9','e':'10','f':'11','f#':'0','g':'1','g#':'2','a':'3','a#':'4','b':'5'}
    elif fifths == "G":
        #Gメジャーのピッチクラス
        pitch={'c':'5','c#':'6','d':'7','d#':'8','e':'9','f':'10','f#':'11','g':'0','g#':'1','a':'2','a#':'3','b':'4'}
    elif fifths == "A-flat" or fifths=="G-sharp":
        #G#メジャーのピッチクラス
        pitch={'c':'4','c#':'5','d':'6','d#':'7','e':'8','f':'9','f#':'10','g':'11','g#':'0','a':'1','a#':'2','b':'3'}
    elif fifths == "A":
        #Aメジャーのピッチクラス
        pitch={'c':'3','c#':'4','d':'5','d#':'6','e':'7','f':'8','f#':'9','g':'10','g#':'11','a':'0','a#':'1','b':'2'}
    elif fifths == "B-flat" or fifths=="A-sharp":
        #A#メジャーのピッチクラス
        pitch={'c':'2','c#':'3','d':'4','d#':'5','e':'6','f':'7','f#':'8','g':'9','g#':'10','a':'11','a#':'0','b':'1'}
    elif fifths == "B":
        #Bメジャーのピッチクラス
        pitch={'c':'1','c#':'2','d':'3','d#':'4','e':'5','f':'6','f#':'7','g':'8','g#':'9','a':'10','a#':'11','b':'0'}
    else:
        print("fifthsが渡されていません")

    return pitch

# -----------------------------------------
def diatonic(p):
    if p=="c":
        diatonic=[5,1,2,1,3,2,1,4,1,2,1,2]
    elif p=="c#":
        diatonic=[2,5,1,2,1,3,2,1,4,1,2,1]
    elif p=="d":
        diatonic=[1,2,5,1,2,1,3,2,1,4,1,2]
    elif p=="d#":
        diatonic=[2,1,2,5,1,2,1,3,2,1,4,1]
    elif p=="e":
        diatonic=[1,2,1,2,5,1,2,1,3,2,1,4]
    elif p=="f":
        diatonic=[4,1,2,1,2,5,1,2,1,3,2,1]
    elif p=="f#":
        diatonic=[1,4,1,2,1,2,5,1,2,1,3,2]
    elif p=="g":
        diatonic=[2,1,4,1,2,1,2,5,1,2,1,3]
    elif p=="g#":
        diatonic=[3,2,1,4,1,2,1,2,5,1,2,1]
    elif p=="a":
        diatonic=[1,3,2,1,4,1,2,1,2,5,1,2]
    elif p=="a#":
        diatonic=[2,1,3,2,1,4,1,2,1,2,5,1]
    elif p=="b":
        diatonic=[1,2,1,3,2,1,4,1,2,1,2,5]
    else:
        print("コードがありません")
    return diatonic



def calc_k(c1,c2):
    # ベーシックスペース上の建て増しの数 kを計算する関数
    dia1=diatonic(c1)
    dia2=diatonic(c2)
    k=0
    xx=0
    for x in range(12):
        xx=dia2[x]-dia1[x]
        if xx > 0:
            k += xx
    return k

def calc_j(c1,c2):
    #和音の五度圏の移動ステップ数 jを計算する関数
    cycle=["c","g","d","a","e","b","f"]
    j=abs(cycle.index(c2)-cycle.index(c1))
    if j>3:
        j=7-j
    return j

def chord(c_list):
    for c in range(0,len(c_list)-1):
        pass

    return c

def input_chord(count):
    c_list=[]#入力したコード進行を保存
    for p in range(count):
        print(p+1,"つ目のコード：")
        c_list.append(input())

    return c_list
# ---------------------------------------------


def find_key(mode, fifths):
    """ Find key from mode(major/minor) and fifths(-7 to +7). """
    keys = {}
    keys["major"] = ["C","G","D","A","E","B","F-sharp","D-flat","A-flat","E-flat","B-flat","F"]
    keys["minor"] = ["A","E","B","F-sharp","C-sharp","G-sharp","D-sharp","B-flat","F","C","G","D"]
    # check
    if (mode.lower() not in keys) or (fifths<-7 or fifths>7):
        print("mode: str of major or minor, fifth: -7 to +7.")
    return keys[mode.lower()][fifths] + " " +mode.lower()



def extract_music(soup):
    """ Extract music data from xml file. """
    """
    この関数はピッチの情報をreturnする
    pitch_listには、[cur_time,step,octave,accidental]

    """
    pitch_list = []
    cur_time = 0 # Current time
    tmp_duration = 0

    step=""
    octave=""
    accidental=""
    voice=""

    tempo_list=[]
    dynamics_list=[]
    tempo=""
    dynamics=""

    # parse
    for m in soup.find_all("measure"):
        for nb in m.find_all({"note", "backup","sound"}):
            if nb.name == "backup": # 巻き戻し
                cur_time -= int(nb.duration.string)
            if nb.name == "note":
                if not nb.chord: # 和音でなければ
                    cur_time += tmp_duration

                if nb.accidental:
                    accidental = nb.accidental.string

                if nb.rest: # 休符
                    pass
                if nb.duration: # 装飾音はdurationないので飛ばす
                    tmp_duration= int(nb.duration.string)

                if nb.voice: # パート
                    voice = nb.voice.string

                if nb.pitch: # 音符

                    step=nb.pitch.step.string
                    octave=int(nb.pitch.octave.string)
                    # パートを示すvoiceはリストの一番最後にすること。voice_part()の関数の都合上
                    pitch_list.append([cur_time,step,octave,accidental,tmp_duration,voice])
                    accidental=""

                    if tempo:
                        tempo_list.append([cur_time,tempo,voice])
                    if dynamics:
                        dynamics_list.append([cur_time,dynamics,voice])

            if nb.name == "sound":
                if has_tempo_but_no_dynamics(nb):
                    tempo = int(nb["tempo"])
                if has_dynamics_but_no_tempo(nb):
                    dynamics = int(nb["dynamics"])

    return pitch_list , tempo_list, dynamics_list


def voice_part(pitch_list):
    voice_1_list=[]
    voice_2_list=[]
    voice_3_list=[]
    for p in pitch_list:
        if p[-1]=="1":
            voice_1_list.append(p)
        if p[-1]=="2":
            voice_2_list.append(p)
        if p[-1]=="3":
            voice_3_list.append(p)

    return voice_1_list, voice_2_list, voice_3_list


def pitch_highest(part):
    before=part[0]
    pitch_highest_list=[]
    for p in part:
        if before[0] != p[0]:
            pitch_highest_list.append(before)
        before = p
    pitch_highest_list.append(before)

    return pitch_highest_list


# 音高リスト
def height(pitch):
    tonal=find_key(soup.attributes.key.mode.string,int(soup.attributes.key.fifths.string.encode("utf-8")))
    cde_list = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

    pitch_height_list=[]
    for p in pitch:
        c_pitch=accidental(tonal[0],p[1],p[3])
        h = int(p[2])*12
        h += cde_list.index(c_pitch)
        pitch_height_list.append([p[0],h])

    return pitch_height_list









# 関数フィルター（BeautifulSoupの参考サイトの関数より）
# soundの中からtempoだけ抜き出す.
# true falseを返す
def has_tempo_but_no_dynamics(sound):
    return sound.has_attr('tempo') and not sound.has_attr('dynamics')

def has_dynamics_but_no_tempo(sound):
    return sound.has_attr('dynamics') and not sound.has_attr('tempo')


def local_tempo(data,tempo_list):
    divisions=int(soup.attributes.divisions.string)
    local_tempo_list=[]
    c=0
    time=0 # 単位を秒に変更
    before=data[0][0]
    if data[0][0] != 0:
        # 曲の一番最初の音の発音時刻
        time=(data[0][0]/divisions)*(60/tempo_list[0][1])

    for d in data[1:]:
        ioi = ((d[0]-before)/divisions)*(60/tempo_list[c][1])
        local_tempo = 1/ioi
        local_tempo_list.append([time,local_tempo])
        c += 1
        before = d[0]
        time += ioi
    local_tempo_list.append([time,0])
    return local_tempo_list





def key_signatures(key,pitch):
    # print("調：",key)
    # print("音：",pitch)

    # sharp flat
    correct_pitch=pitch
    if key=="G":
        if pitch=="F":
            correct_pitch="F#"
    if key=="D":
        if pitch=="F":
            correct_pitch="F#"
        elif pitch=="C":
            correct_pitch="C#"
    if key=="A":
        if pitch=="F":
            correct_pitch="F#"
        elif pitch=="C":
            correct_pitch="C#"
        elif pitch=="G":
            correct_pitch="G#"
    if key=="E":
        if pitch=="F":
            correct_pitch="F#"
        elif pitch=="C":
            correct_pitch="C#"
        elif pitch=="G":
            correct_pitch="G#"
        elif pitch=="D":
            correct_pitch="D#"
    if key=="B":
        if pitch=="F":
            correct_pitch="F#"
        elif pitch=="C":
            correct_pitch="C#"
        elif pitch=="G":
            correct_pitch="G#"
        elif pitch=="D":
            correct_pitch="D#"
        elif pitch=="A":
            correct_pitch="A#"
    if key=="F-sharp" or key=="G-flat":
        if pitch=="F":
            correct_pitch="F#"
        elif pitch=="C":
            correct_pitch="C#"
        elif pitch=="G":
            correct_pitch="G#"
        elif pitch=="D":
            correct_pitch="D#"
        elif pitch=="A":
            correct_pitch="A#"
        elif pitch=="E":
            correct_pitch="E#"
    ###
    if key=="F":
        if pitch=="B":
            correct_pitch="A#"
    if key=="B-flat" or key=="A-sharp":
        if pitch=="B":
            correct_pitch="A#"
        elif pitch=="E":
            correct_pitch="D#"
    if key=="E-flat" or key=="D-sharp":
        if pitch=="B":
            correct_pitch="A#"
        elif pitch=="E":
            correct_pitch="D#"
        elif pitch=="A":
            correct_pitch="G#"
    if key=="A-flat" or key=="G-sharp":
        if pitch=="B":
            correct_pitch="A#"
        elif pitch=="E":
            correct_pitch="D#"
        elif pitch=="A":
            correct_pitch="G#"
        elif pitch=="D":
            correct_pitch="C#"
    if key=="D-flat" or key=="C-sharp":
        if pitch=="B":
            correct_pitch="A#"
        elif pitch=="E":
            correct_pitch="D#"
        elif pitch=="A":
            correct_pitch="G#"
        elif pitch=="D":
            correct_pitch="C#"
        elif pitch=="G":
            correct_pitch="F#"

    return correct_pitch


# 臨時記号
def accidental(key,pitch_1,acci):
    pitch=key_signatures(key,pitch_1)
    correct_pitch=pitch
    # print("ダイアトニックスケールの音：",pitch)
    # print("元々の臨時記号なしの音：",pitch_1)

    if acci=="sharp":
        if pitch=="C":
            correct_pitch="C#"
        elif pitch=="C#":
            correct_pitch="D"
        elif pitch=="D":
            correct_pitch="D#"
        elif pitch=="D#":
            correct_pitch="E"
        elif pitch=="E":
            correct_pitch="F"
        elif pitch=="F":
            correct_pitch="F#"
        elif pitch=="F#":
            correct_pitch="G"
        elif pitch=="G":
            correct_pitch="G#"
        elif pitch=="G#":
            correct_pitch="A"
        elif pitch=="A":
            correct_pitch="A#"
        elif pitch=="A#":
            correct_pitch="B"
        elif pitch=="B":
            correct_pitch="C"
    elif acci=="flat":
        if pitch=="C":
            correct_pitch="B"
        elif pitch=="B":
            correct_pitch="A#"
        elif pitch=="A#":
            correct_pitch="A"
        elif pitch=="A":
            correct_pitch="G#"
        elif pitch=="G#":
            correct_pitch="G"
        elif pitch=="G":
            correct_pitch="F#"
        elif pitch=="F#":
            correct_pitch="F"
        elif pitch=="F":
            correct_pitch="E"
        elif pitch=="E":
            correct_pitch="D#"
        elif pitch=="D#":
            correct_pitch="D"
        elif pitch=="D":
            correct_pitch="C#"
        elif pitch=="C#":
            correct_pitch="C"
    elif acci=="natural":
        correct_pitch=pitch_1

    return correct_pitch

def attr(data,key):
    attr_list=[]
    for i in range(0,len(data)-1):
        p1=accidental(key,data[i][1],data[i][3])
        p2=accidental(key,data[i+1][1],data[i+1][3])
        attr_list.append([data[i][0],attraction(p1,p2,key)])
    attr_list.append([data[-1][0],0]) #一番最後のアトラクションは0

    return attr_list








# csvにするデータをくっつける
def csv_make(pitch_height,tempo_list,dynamics_list,local_tempo,attraction):
    c=0
    f_list=[["time","soprano","tempo","dynamics","local_tempo","attraction"]]
    # f_list=[["time","soprano","local_tempo","attraction"]]
    for p in pitch_height:
        # f_list.append([local_tempo_list[c][0],p[1],local_tempo[c][1],attraction[c][1]])
        f_list.append([local_tempo[c][0],p[1],tempo_list[c][1],dynamics_list[c][1],local_tempo[c][1],attraction[c][1]])

        c += 1
    return f_list


"""
# 特徴量３つ
def csv_make(pitch_height,local_tempo,attraction):
    c=0
    # f_list=[["time","soprano","tempo","local_tempo","attraction"]]
    f_list=[["time","soprano","local_tempo","attraction"]]
    for p in pitch_height:
        f_list.append([local_tempo[c][0],p[1],local_tempo[c][1],attraction[c][1]])
        # f_list.append([local_tempo[c][0],p[1],tempo[c][1],local_tempo[c][1],attraction[c][1]])

        # f_list.append([p[0],p[1],tempo[c][1],dynamics[c][1],local_tempo[c][1],attraction[c][1]])
        c += 1
    return f_list
"""



def csv_writer(xml_name,name,data):
# 内容
    # data = [[0, 'YUI'],[1, 'UI'],[2, 'MIO']]
    with open(xml_name + '_' + name + '.csv', 'w', newline='') as f:    #newline=''を追加した
        writer = csv.writer(f)
        writer.writerows(data)

    f.close()

if __name__ == "__main__":

    xml_name = "music/youkoso_full.xml"# Your MusicXML file
    soup = BeautifulSoup(open(xml_name,'r',encoding='utf-8').read(), "lxml")
    tonal=find_key(soup.attributes.key.mode.string,int(soup.attributes.key.fifths.string.encode("utf-8")))
    print("楽曲の調",tonal)

    music_data = extract_music(soup)
    part_list = music_data[0] #音に関するリスト
    tempo = music_data[1]
    dynamics = music_data[2]
    # print(part_list)
    # voiceわけ
    tempo_part = voice_part(tempo)
    dynamics_part = voice_part(dynamics)
    voice_list = voice_part(part_list) #パート分け
    voice_1_list = voice_list[0] # 1番目のパート
    voice_2_list = voice_list[1] # 1番目のパート

    tempo_list=pitch_highest(tempo_part[0])
    dynamics_list=pitch_highest(dynamics_part[0])
    pitch_height = height(pitch_highest(voice_1_list))
    # print(pitch_height[:50])
    # アトラクションの計算
    attraction = attr(pitch_highest(voice_1_list),tonal[0])
    local_tempo = local_tempo(pitch_highest(voice_1_list),tempo)
    # print(local_tempo)



    Feature_value = csv_make(pitch_height,tempo_list,dynamics_list,local_tempo,attraction)
    # Feature_value = csv_make(pitch_height,local_tempo,attraction)

    df = pd.DataFrame(Feature_value[1:], columns=Feature_value[0])

    print(df)
    """
    #{}"time","soprano","tempo","local_tempo","attraction"
    plt.plot(df["time"], df["soprano"],"r-",label="soprano")
    plt.plot(df["time"], df["tempo"],"g-",label="tempo")
    plt.plot(df["time"], df["local_tempo"],"b-",label="local_tempo")
    plt.plot(df["time"], df["attraction"],"k-",label="attraction")

    plt.xlabel("time (s)")
    plt.ylabel("tension value")
    plt.legend(loc=2)               # 凡例の位置
    # plt.axvline(x=100)     # x=1に沿ってx軸垂直に引く
    plt.show()
    """
    csv_writer(xml_name,"Feature_value",Feature_value)
