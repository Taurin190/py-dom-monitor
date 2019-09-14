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
- [x] clientの作成
  - [x] requestsでhtmlを取得する
  - [x] seleniumでhtmlを取得する
- [x] databaseの作成
  - [x] 試行回数を取得する
  - [x] 前回取得したhtmlを取得する
  - [x] 試行回数を更新する
  - [x] 前回取得したhtmlを更新する
- [x] 差分を見つけるツール作成
  - [x] 比較して差分問題のあるDomの部分を特定する
  - [x] 差分をリストして返す
- [x] ドメインクラスの作成
  - [x] データベースに接続
  - [x] 今回で何回目のアクセスか取り出す
  - [x] データベースより前回の結果を取り出す
  - [x] 対象のURLからHTMLを取得する
  - [x] 前回のHTMLと今回のHTMLを比較する
  - [x] 今回出たdiffと同一のdiffがあるか探す
  - [x] 毎回成功しているのに失敗した場合はアラート結果に出力する
  - [x] 毎回Diffが出ているのに同じ結果が出る場合はアラート結果に出力する
- [x] アラートクラスを作成する
  - [x] アラート結果が空で無い場合通知する
- [ ] 動作確認
  - [x] 単体テストの境界値など足りないテスト追加する
  - [ ] 考えられる結合テストを作成して実施する
    - [x] Argument無しで実施した場合に、エラーとusageを表示する
    - [x] Argumentで無効なconfigファイルを指定した時にエラーを出す
    - [x] 正常に実行していつもと異なるdiffが見つからない
  - [ ] GCPのCloudFunctionで動作させてみる
- [ ] READMEを整える
  - [ ] 使い方を詳しく書く
  - [ ] DEMOをgifイメージで作る
  - [ ] 要件を分解したTODOリストを消す