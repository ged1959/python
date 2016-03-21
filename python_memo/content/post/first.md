+++
date = "2016-03-21T15:14:20+09:00"
draft = false
slug = "first_memo"
tags = ["hugo", "how-to"]
title = "このメモの作成方法"

+++

READMEに書いた通り、pythonの勉強用のメモ。忘れっぽいので。

## このサイトの作成法も

やっぱり忘れるだろうから、以下に。

### localにサイトを作る
まず、サイトの基本を作成。

```
hugo new site python_memo
```
テーマフォルダを作る。
```
mkdir themes
```
テーマをクローンする。（作者に感謝！！）

```
git clone https://github.com/tanksuzuki/angels-ladder
```
archetypesフォルダにdefault.mdを作る。内容は以下。
```
+++
date = "now()"
draft = true
slug = ""
tags = ["", ""]
title = ""
+++
```
config.tomlを編集する。内容は以下。
```
baseurl = "http://ged1959.github.io/python/"
languageCode = "ja-jp"
title = "My Memo"
canonifyurls = true
```
postを一つ作る。
```
hugo new post/first.md
```
上に、何かを書き込んで、以下で動作テスト。
```
hugo server -t angels-ladder -D
```

### Githubにアップする

アップロード用のデータを作成する。記事中の```draft = true```は```draft = false```とする。コマンドでもいいらしい。
```
hugo undraft content\post\first.md
```
で、作成。
```
hugo -t angels-ladder
```
publicのフォルダができる。中のindex.htmlをクリックすると、サイトが見える、という訳ではない。たぶん、上で```path```を決めたから。で、publicへ。
```
cd public/
```
gitにする。
```
git init
```
リモートリポジトリを指定する。
```
git remote add origin https://github.com/ged1959/python.git
```
gh-pagesのbranchを作成し、branchを移動する。
```
git checkout -b gh-pages
```
続いて、お決まりの手順。
```
git add .
git commit -m "1st commit"
git push -u origin gh-pages
```

以上。