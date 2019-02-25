# django-diary

### 開発時にはLocal にてdockerのDynamoDBを利用
```
$ docker run -it -p 8000:8000 amazon/dynamodb-local
```

### DynamoDBとPortが競合しないよう、runserverを実行
```
$ python manage.py runserver 8080
```
