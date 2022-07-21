## Mariadb  사용자 생성 & Database 생성

``` Maridb 가 설치되어있다는 가정 하에 세팅. ```

1. 환경변수 path
2. C:\Program Files\MariaDB 10.8\bin  MariaDB 가 설치된 경로를 알아내주고 path에 추가

root  사용자로 접속

```sql 
cmd > mysql -u root -p
``` 

root 계정에서 작업을 한다면 굉장히 위험하기 때문에 계정을 생성해주고 이 계정에 권한을 부여해준다. 

첫번째는 외부 접속도 허용 두번째는 로컬 접속만 허용

그리고 새로고침

```sql 
cmd > create database test;

cmd > create user '계정명'@'%' identified by '비밀번호';

cmd > GRANT ALL PRIVILEGES ON test.* TO '계정명'@'%';

cmd > flush privileges;

cmd > exit
``` 
해당 계정은 test 라는 데이터베이스 내에서의 모든 권한을 부여받는다. <br>
test 가 아닌 * 을 해주면 모든 데이터베이스 내에서의 권한을 부여받게 된다.


계정에 접속해준다

```sql 
cmd > mysql -u 계정명 -p
``` 

데이터 베이스를 확인해주고 생성해준다 <br>
그리고 사용

```sql 
cmd > show databases;

cmd > create database db_name;

cmd > use db_name;
``` 
<br>

---

### 오류
``` 
Access denied for user 'dowoon'@'%' to database 'db_name'
```

과정을 진행하는데 이런 오류가 떳다. 

검색을 해봤다.

1. 외부 권한을 설정 안했을 경우
2. 비밀번호가 설정되어있지 않을 경우
3. 비밀번호가 영어 대문자 소문자, 특수문자를 포함되어있지 않은 경우

나 같은 경우에는 3번의 경우였다. 

비밀번호가 영어로만 이루어져있었기 때문이다.

그래서 사용자의 비밀번호를 바꿔주었다.

```sql 
cmd > mysql -u root -p

cmd > ALTER USER 'user-name'@'%' IDENTIFIED BY 'NEW_USER_PASSWORD';
``` 






