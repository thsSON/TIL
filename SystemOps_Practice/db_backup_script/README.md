# 🗂️ MySQL 자동 백업 스크립트

## 📌 프로젝트 목적
MySQL 데이터베이스를 주기적으로 백업하고, 일정 기간 이후 자동으로 삭제하는 스크립트를 작성하여 운영 자동화 기초를 실습합니다.

## 🧩 주요 기능
- DB 백업 파일 생성 (`.sql`)
- 날짜별 파일 저장
- 7일 이상 된 백업 파일 자동 삭제
- 로그 파일 기록
- crontab 등록으로 매일 자동 실행

## 🧪 실행 방법
```bash
bash backup.sh 또는 크론탭 등록