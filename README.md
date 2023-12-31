# **COM🎬**
###  'Crossroads Of Movies'의 약자로,
### 영화 선택의 갈림길에 서있는 "**MZ 세대**"를 위한 새로운 추천 시스템을 제공한다.

<img src="./readme_pic/crossroads.jpg" style="width: 500px ">

<blockquote>
수 없이 많이 쏟아지는 OTT컨텐츠 속에서 발견하는 보석!

"오늘 뭐 볼까?" 에 대한 답을 내려준다.

선택의 역설(The paradox of choice)에서 구해줄 단 하나의 선택지, **COM**
</blockquote>

<br><br>

# 가. 개발 기획

<br>

## 1) 개발 기간

📅 2023.05.17 ~ 2023.05.25 (9일)

<br>

## 2-1) 팀원 정보 및 업무 분담

👩‍💻**FrontEnd** 권소정 - 💃ESFP / 🦁사자자리(8월 21일) / 🩸AO(Rh+)

👨‍💻**BackEnd** 김준형 - 👨‍⚖️ENTJ / 🦀게자리(6월 28일) / 🩸O(Rh+)

<br>

## 2-2) 기술 스택

**FrontEnd**  Vue / Vuex / VueBootstrap

**BackEnd**  Python / Django

**DB**  Sqlite3

**UI tool**  Figma

<br>

## 2-3) 코드 스타일 가이드

**Python**  PEP8

**Java Script**  Airbnb

<br>

## 2-4) Git Commit Convention

📌**Commit Convention**
```
type: Subject - body
```

<br>

✏**Commit Type**

<img src="./readme_pic/commit_type.PNG" style="width: 300px ">

<br>

🐹**Subject Rule**

1. 제목은 최대 50글자
2. 마침표 및 특수기호 사용 X
3. 첫 글자 대문자, 명령문 사용
4. 개조식 구문으로 작성 (간결하게)

<br>

🐾**Body Rule**

1. 한 줄당 최대 72글자
2. 최대한 상세히 작성
3. 어떻게 보다는 `'무엇을'`, `'왜'` 변경했는지에 대해 작성

<br><br>

## 3-1) 목표 서비스
- 홈화면

<img src="./readme_pic/Home.png" style="width: 500px ">

<br>

- Movies 페이지

<img src="./readme_pic/Movies.png" style="width: 500px ">

<br>

- 영화 디테일 페이지

<img src="./readme_pic/Detail.png" style="width: 500px ">
    
<br>

- 날씨 기반 영화 추천

<img src="./readme_pic/Weather.png" style="width: 500px ">
    
<br>

- 영화 월드컵 페이지

<img src="./readme_pic/Movie_worldcup.png" style="width: 500px ">
    
<br>

- 영화 월드컵 우승 영화 기반 추천 페이지

<img src="./readme_pic/Movie_worldcup_1st.png" style="width: 500px ">

<br>

- 유저 프로필 페이지

<img src="./readme_pic/profile.png" style="width: 500px ">

<br>

- 유저 프로필 페이지 > 리뷰

<img src="./readme_pic/profile_content.png" style="width: 500px ">

<br><br>

## 3-2) 실제 구현 정도

- 회원가입

<img src="./readme_pic/Finish/Fin_Signup.png">

<br>

- 로그인

<img src="./readme_pic/Finish/Fin_Login.png">

<br>

- 홈

<img src="./readme_pic/Finish/Fin_Home.png">

<br>

- 영화 리스트

<img src="./readme_pic/Finish/Fin_Movies.png">

<br>

- 영화 상세

<img src="./readme_pic/Finish/Fin_Movie_Detail.png">

<br>

- 영화 리뷰 상세

<img src="./readme_pic/Finish/Fin_Review_Detail.png">

<br>

- 영화 추천

<img src="./readme_pic/Finish/Fin_Recommend.png">

<br>

- 프로필

<img src="./readme_pic/Finish/Fin_Profile.png">

<br><br>

## 4-1) 데이터베이스 모델링(ERD)
<img src="./readme_pic/Final_PJT_ERD.png" style="width: 500px ">

<br>

## 4-2) API 설계

**final_pjt url**
|HTTP verb|URL 패턴|설명|
|---|---|---|
||`admin`|admin.site.urls|
||`movies/`|include('movies.urls')|
||`accounts/`|include('dj_rest_auth.urls')|
||`profile/`|include('accounts.urls)|
||`accounts/signup/`|include('dj_rest_auth.registration.urls')|
||`api/token/`|TokenObtainPairView.as_view()|

**movies url**
|HTTP verb|URL 패턴|설명|
|---|---|---|
|GET|`movies/`|영화 페이지|
|GET|`movies/recommend/<int:movie_id>/`|좋아요한 영화 기반 추천 페이지|
|GET POST|`movies/<int:movie_pk>/reviews/`|단일 영화 조회 및 리뷰 작성 페이지|
|GET PUT DELETE|`movies/<int:movie_pk>/<int:review_pk>/`|리뷰 상세 및 댓글 작성 페이지|
|GET POST|`movies/<int:movie_pk>/<int:review_pk>/comment/`|댓글 상세 및 작성 페이지|
|DELETE|`movies/<int:movie_pk>/<int:review_pk>/comment/<int:comment_pk>/`|댓글 삭제|
|POST|`movies/<int:movie_pk>/likes/`|영화 좋아요|

**accounts url**
|HTTP verb|URL 패턴|설명|
|---|---|---|
|GET|`profile/<username>/`|회원 프로필 페이지|
|POST|`profile/follow/`|팔로우|

<br><br>


## 5) 배포 서버

준비중입니다..🙏

<br><br>

# 나. 일지 & 느낀점

📒 **5月 17日**

git 생성

- 기초 파일 생성 (django, vue)

목업 만들기 완료

ERD 작성 완료

README.md 초안 작성

- Commit 규칙 정하기
- 요구사항에 따라 틀 생성
- 코드 스타일 가이드 작성

**느낀점**

프로젝트 시작 전 계획 및 기획을 오늘까지 무사히 완료해서 만족스럽다.

막막했던 부분들을 잘게 쪼게니까 할만하다고 느껴졌다.

다른 팀들과 속도차이가 발생했는데, 우리팀만의 페이스로 진행하는게 중요하다고 생각한다.

여태껏 하지 않았던 커밋 규칙이나 ERD를 작성해 보아서 좀 더 체계적으로 프로젝트를 진행하는 기분이었다.

<br>

📒 **5月 18日**

Django 세팅

- models, serializers, urls

Vue 기본 작업

- App.vue
- Views 파일 생성
- router 설정

**느낀점**

이전 관통 프로젝트는 명세서를 기반으로 진행해서 쉬웠다면, 현재 프로젝트는 직접 명세서를 작성해서 진행하다보니 전보다 어려움

처음에 계획했던 내용은 진행하는 과정에서 많이 바꿔야한다는 사실을 알았다. > 처음에 계획을 확실히 세우자!

프로젝트를 진행하면서 serializers를 작성하려했는데, models로 빠지는 등 삼천포로 빠지는 일이 자주 있다..

<br>

📒 **5月 19日**

기존 파일의 문제를 인식하고, 해결하기 위해 새로 시작.

Vue - 기본파일 구성

Django - models, serializers, urls, views를 세팅

API를 Django에서 가져와서 불러오기 성공! (DB저장 완료)

**느낀점**

기본에 충실하자!

안배운게 나와도 검색으로 해결해야한다.

잘 갈아 엎었다.

DB에 대해서 더 공부하자.

주말과 야근은 필수

<br>

📒 **5月 21日**

Django models, views, serializers를 이용해 데이터베이스에 api를 사용해 얻은 데이터를 저장하고 Vue에 띄우는데 성공했다.

Home 이미지를 동적으로 움직이도록 CSS를 설정했다.

**느낀점**

처음 설계한대로 진행되지 않아서 힘들었다. 데이터를 만들어놓아야 Vue에서 가져와서 사용하기 편하다는 것을 다시 한 번 깨달았다.

DB에 대해서 약간(?)의 깨달음을 얻었다. 하지만 아직 갈 길이 멀다. (M:N은 도저히 모르겠다.)

생각보다 컴퓨터(노트북)의 설정이 중요하다. admin(관리자)계정은 반드시 이름을 영어로 설정하자..

Vue에서 데이터를 다루는 것보다 Django에서 다루는 것이 더 편하다는 사실을 알았다.

<br>

📒 **5月 22日**

리셋을 한 번 더 했다...

하지만 포기하지 않고 movies, auth(jwt token), review 와 comment 의 CR(U)D, profile 페이지 만들기 를 모두 했다.

커밋을 무려 43개 (READM 작성 전 기준) 했다 !

**느낀점**

리셋을 또 하지 않으려면 차근차근 하나하나 설계를 해나가야 한다..

체크리스트를 자세하게 작성하는 것이 중요하다는 것을 알았다.

교수님께 제출한 오늘의 체크리스트를 다 완수해서 우리 자신이 기특하다.

<br>

📒 **5月 23日**

필수 기능 완료

- 팔로우 / 언팔로우 기능 추가 (팔로우한 사람의 수 확인 가능)
- 영화 좋아요 기능 추가 (사용자 프로필에서 좋아요한 영화 리스트 확인 가능)
- Home 화면에 추천 영화 추가 (시간적 여유가 있다면 추후 변경 예정)

Home CSS 95% 작성

- Youtube trailer css 변경 예정

**느낀점**

2번의 reset을 이겨내고 드디어 필수 기능 구현을 완료했다.

체크리스트를 세분화하여 하나씩 완성해나가는 것이 큰 도움이 됐다.

프로젝트의 완성도를 위해서 후순위로 밀어놨던 자잘한 버그 / 기능들을 구현할 필요가 있다는 것을 깨달았다.

<br>

📒 **5月 24日**

Home, Movies 홈페이지 CSS 작성

영화 좋아요, 팔로우/언팔로우 버그 수정

**느낀점**

드디어 CSS 작성에 돌입! 시간이 많이 남진 않았지만 그래도 시간 내 끝낼 수 있을듯 하다.

기능적인 부분은 전체적으로 완성했으나, 디테일이 떨어지는 버그들이 종종 발생한다. 빠른 시일 내 해결 요망!

<br>

📒 **5月 25日**

마참내! css까지 다 완성했다 (아마도)

발표 자료를 만들고, 배포서버 만들기 시도

**느낀점**

내가 원하는 만큼은 구현하지 못했지만 9일이라는 짧은 시간 동안 그래도 최선은 다 한거 같아서 만족스럽다.