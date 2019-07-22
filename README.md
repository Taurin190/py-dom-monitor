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
