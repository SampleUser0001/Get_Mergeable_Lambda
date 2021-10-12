# -*- coding: utf-8 -*-
import os
import sys
import boto3

def lambda_handler(event, context):

  print("event:{}".format(event))
  
  # ローカルで動かす場合はアクセス権の指定として、access key idや、secret access keyが必要だが、
  # AWS Lambdaで動かす場合は、設定 - アクセス権限 - リソースの概要で参照できる権限を使用するため、
  # インスタンス生成時に指定する必要はない。
  codecommit_clinent = boto3.client('codecommit')

  # TODO : eventを起動引数
  response = codecommit_clinent.get_merge_conflicts(
    repositoryName = event['repositoryName'],
    sourceCommitSpecifier = event['source'],
    destinationCommitSpecifier = event['destination'],
    mergeOption = 'FAST_FORWARD_MERGE'
  )

  print("response:{}".format(response))

  # 戻り値は別途考える
  return response
