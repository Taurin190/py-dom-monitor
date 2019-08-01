# py-dom-monitor
前回作った[py-diffdom](https://github.com/Taurin190/py-diffdom)というツールでは、
２つのURLリストを比較するツールを作った。

ただ、同じURLで時間が経った後に変化しているかどうかを比較できるツールも有効であると考えて、
そのようなツールを作った。

## Description
このツールは、対象のURLを定期的に見てDOMに変更が加えられたかを監視するツールである。
以下のようなロジックで変更を監視する
- 毎回変わらない場合は問題なしとする
- 毎回変わる部分は問題なしとする
- 10回に1回変わるような特異な変更は通知を行う

## 要件の分解
- [x] Configから対象のURLを取得する
  - [x] staticmethodでhtmlを取得するclientを取得する
  - [x] staticmethodでdatabaseクラスを取得する
  - [x] staticmethodで通知クラスを取得する
  - [x] client,database,通知クラスを引数にドメインクラス取得する
  - [x] 対象のURLを取得する
- [ ] clientの作成
  - [ ] requestsでhtmlを取得する
  - [ ] seleniumでhtmlを取得する
- [ ] databaseの作成
  - [ ] 試行回数を取得する
  - [ ] 前回取得したhtmlを取得する
  - [ ] 試行回数を更新する
  - [ ] 前回取得したhtmlを更新する
- ドメインクラスの作成
  - データベースに接続
  - 今回で何回目のアクセスか取り出す
  - データベースより前回の結果を取り出す
  - 対象のURLからHTMLを取得する
  - 前回のHTMLと今回のHTMLを比較する
  - 今回出たdiffと同一のdiffがあるか探す
  - 毎回成功しているのに失敗した場合はアラート結果に出力する
  - 毎回Diffが出ているのに同じ結果が出る場合はアラート結果に出力する
  - アラート結果が空で無い場合通知する