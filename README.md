# ETL

> Python으로 의료 CSV 데이터를 이관하고, 필요한 정보를 추출한 저장소입니다.

## 개발 환경

* OS
  * Windows 10: 주요 코드 개발
  * Ubuntu 24.04​: AWS에서 코드 테스트
* Language: Python 3.12
* Tools: Jupyter Lab

## 프로젝트 특징

### 구현

* 파일 경로를 미리 설정하고, 반복문을 활용하여 CSV 파일을 유연하게 처리할 수 있다.
* 추출한 데이터를 각각 혈압, 심박수, 심장음 데이터로 저장해 DB에 저장한다.
* 각각의 데이터는 필요한 데이터만 추출해 하나의 데이터로 DB에 저장한다.
* Ubuntu Crontab을 사용하여 일정 간격마다 필요한 데이터를 추출해 처리하고 로그 파일을 생성한다.

## 실행결과

### 추출한 데이터
![image](https://github.com/user-attachments/assets/a8108259-cc1c-4bed-826b-c59d7a03d61c)

### Crontab 자동화
![image](https://github.com/user-attachments/assets/829d69f7-2c81-403e-81a2-5928b5de072c)
![image](https://github.com/user-attachments/assets/84176df8-72b6-402f-88cd-d8a386585ffa)
