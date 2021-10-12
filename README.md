# Get_Mergeable_Lambda
AWS LambdaでAWS CodeCommitのブランチ間マージが可能かを取得するツールを作成する。

## デプロイ

### ソースデプロイ

1. ```create_zip.sh```を実行する。
2. 作成された```lambda_app.zip```をAWS Lambda関数にデプロイする。
  - Pythonでデプロイ可能な状態になっていることを想定して記載する。
    1. コード -> アップロード元 -> .zipファイル をクリックする。
    2. アップロードをクリックし、```lambda_app.zip```を選択する。
    3. 保存をクリックする。

### 権限

CodeCommitへのアクセス権限を設定する。

1. 設定 -> アクセス権限 -> 実行ロール -> ロール名をクリックする。
2. インラインポリシーの追加をクリックする。
3. サービスの選択をクリックし、検索欄に「CodeCommit」を入力し、出てきたリンクを押下。
4. リソースをクリックし、アクセス対象のCodeCommitリポジトリを入力する。
5. ポリシーの確認をクリックする。
6. ポリシーの作成をクリックする。

## イベント（起動引数）

``` json
{
  "repositoryName": "MergeEventDetectiton", # リポジトリ名
  "source": "develop01",                    # マージ元ブランチ
  "destination": "develop03"                # マージ先ブランチ
}
```

## 残課題

- 起動引数を渡す方法の調査
  - 環境変数に書いておけば結果は取得できるが、リポジトリが複数ある場合、AWS Lambda関数が複数必要になってしまうので、あまり上手くない。
  - 特定のイベントが発生したときに、特定の引数でAWS Lambdaを呼ぶ方法を構築したい。
- AWS Lambdaの実行結果の連携
  - 要件未確定。

## 参考

- [Use_Boto3:SampleUser0001:Github](https://github.com/SampleUser0001/Use_Boto3)
- [Use_GitPython_Lambda:SampleUser0001:Github](https://github.com/SampleUser0001/Use_GitPython_Lambda)