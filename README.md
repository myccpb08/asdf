# <span style="color:orange">딱정이</span>

#### - 당신에게 딱 맞는 정책은 이거다!



### <span style="color:blue">개요</span>

* 다양한 카테고리 (나이, 가구형태, 관심주제  등) 를 기준으로 정책을 분류해주는 사이트가 필요
* 개인이 각 정책에 대하여 지원자격이 되는지 직관적인 진단이 되는 사이트가 필요



### 미리보기

![](https://i.postimg.cc/90Fw8zzj/Kakao-Talk-20191104-175502365.png)





### Install

##### *  backend 폴더 내

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py shell < create_admin.txt
pip install django-rest-swagger
python manage.py runserver
```



##### * frontend 폴더 내

```bash
npm install
npm install --save @mdi/js
npm install --save vue-apexcharts
npm install --save firebase
npm run serve
```



##### * backend/backend 폴더 내

```bash
pip install beautifulsoup
pip install openpyxl
python db_policy.py
python crawling1.py
```



