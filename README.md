# read_musicXML

## 編集するところ
- xml_name に、xmlファイルの名前を記載する
- csv_writerに書き出す時の名前を記載する


## 参考サイト
- 名曲の楽譜データをMusicXML形式で入手し、プログラムで可視化する方法 http://roomba.hatenablog.com/entry/2016/02/03/150354

- Beautiful Soup 4.2.0 Doc. 日本語訳 (2013-11-19最終更新) http://kondou.com/BS4/


## BeautifulSoup

## extract_music()
- Extract music data from xml file.
- この関数はピッチの情報をreturnする.pitch_listには、[cur_time,step,octave,accidental]

## find_key()
- Find key from mode(major/minor) and fifths(-7 to +7).
- 楽曲の調をreturnする

## voice_part()
- パートリストを分ける


---
# 特徴量

## pitch_highest()
- 渡されたパートの最高音（メロディライン）を抜き出す？

## height()

## accidental()
- 臨時記号を考慮
## key_signatures()
- 調に元々付いているシャープやフラットを考慮

## attr()
- メロディ期待値のリストをreturnする
## attraction()
* メロディ期待値
  - 音p1, 音p2, 楽曲の調fifthsをattraction()に渡すとメロディ期待値を返す関数

## pitch_class()
- 楽曲の調fifthsのピッチクラスをreturnする

---
## has_tempo_but_no_dynamics(sound)
## has_dynamics_but_no_tempo(sound)
- 関数フィルター（BeautifulSoupの参考サイトの関数より）
- soundの中からtempoだけ抜き出す.
- true falseを返す

## local_tempo()
- ローカルテンポのリストをreturnする

---


## diatonic()
- ベーシックスペース（音の重要度）

## calc_k()
- c1,c2を受け取り、ベーシックスペース上の建て増しの数 kを計算する関数
## calc_j()
- c1,c2を受け取り、和音の五度圏の移動ステップ数 jを計算する関数
---
## chord()
- コードの入力回数？
## input_chord()
- 入力したコード進行を保存
---
## csv_make()
- csvにするデータをくっつける
## csv_writer()
- csvにデータを書き込む
