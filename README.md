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

## install & Usage

    git clone https://github.com/Taurin190/py-dom-monitor.git
    cd py-dom-monitor
    pip install -e .
    
    dommonitor {config_file_path}

### Databaseの準備
dockerでdatabaseを用意することを推奨します。

    docker-compose up -d
    

### Configファイルの書き方
以下、"config.app.conf"ファイルサンプルです。

    [app]
    url = https://yahoo.co.jp
    client = request
    db_type = mongo
    slack_config = /config/slack.conf
    [database]
    hostname = localhost
    port = 27017
    username = python
    password = python
    database = monitor
    collection = monitor

監視の対象としてDOMを取得するURL

    url = https://yahoo.co.jp

使用するClientで、(request, selenium)が選択可能です。

    client = request

diffや試行回数を保存するストレージ。(mongo, file)が選択可能です。

    db_type = mongo

Slackの設定を保持するディレクトリの相対パスです。※

    slack_config = /config/slack.conf

MongoDBを使用した際の接続情報です。

    [database]
    hostname = localhost
    port = 27017
    username = python
    password = python
    database = monitor
    collection = monitor


※Slackのconfigファイルは以下のフォーマットで作成してください。

    [slack]
    url = https://hooks.slack.com/services/XXXXXXX/XXXXXXXXXXXXXX
