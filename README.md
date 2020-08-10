# IT 최신 RSS 메일링 서비스 

개발환경
- flask
- sqlite -> mongodb
- Google Cloud


완료 사항
- email 입력 db input 
- rss 리스트 show

추가 개발 사항
- 최신 rss 자료
- 메일링 리스트 제거
- 메일 등록 시 등록확인 메세지 
- 메일 중복 시 중복 메세지
- rss smtp 메일 스크립트
- 디자인

사용 RSS 리스트
- 한달내 활동 기록이 있는 기업블로그
- IT 뉴스 사이트 추가 예정

| author | address|
|-------|-------|
|카카오|https://tech.kakao.com/feed/|
|네이버|http://d2.naver.com/d2.atom|
|라인|https://engineering.linecorp.com/ko/feed/|
|우아한형제들|https://woowabros.github.io/feed.xml|
|당근마켓|https://medium.com/feed/daangn|
|멋쟁이 사자처럼|https://brunch.co.kr/rss/@@2YH6|
|레진 기술 블로그|http://tech.lezhin.com|
|Airbnb Engineering & Data Science - Medium|https://medium.com/feed/airbnb-engineering|
|Netflix TechBlog - Medium|https://netflixtechblog.com/feed|
|Riot Games Tech Blog News Feed|https://technology.riotgames.com/news/feed|
|Grab Tech|https://engineering.grab.com/feed.xml|

향후 추가 사항
- 개별 rss 구독
- 메일링 등록 시 확인 메일
