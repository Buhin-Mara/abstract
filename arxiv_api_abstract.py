#参考サイト
#https://pypi.org/project/arxiv/
#https://arxiv.org/help/api/user-manual#subject_classifications
#https://imagisi.com/python-arxiv-line/
import arxiv
import csv
import pandas as pd

#論文情報を取得する。対象カテゴリは超伝導。期間は過去5年間程度(一ヶ月200本くらいだから)
search = arxiv.Search(
  query = "cond-mat.supr-con", #AND submittedDate:[20180101 TO 20201231] #期間指定もできるらしいが、今回は未指定
  #query = "cond-mat.str-el", #クエリを一括で実行出来ないため、カテゴリ別に実行して後でファイル結合。
  max_results=10000,#APIの仕様上30万件まで可能らしい。
  sort_by = arxiv.SortCriterion.SubmittedDate #提出日付順に並び替え。デフォルトは最新のものから。
)

#読み込んだデータをPdデータフレーム化。
df = pd.DataFrame(index=[])
for result in search.get():
    abst = result.summary
    update = result.updated
    abst = abst.replace("\n"," ") #改行はスペースに置換
    abst = pd.Series([update,abst]) #日付とアブストをdfに格納
    df = df.append(abst, ignore_index=True)

df.to_csv("arxiv_abstract.csv",header=False, index=False)
print("str-el is finished")

