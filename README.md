# doc-pipeline-api

- 금융 문서(CSV, 엑셀, PDF)를 받아 비동기로 데이터를 추출하는 백엔드 서비스
- 검증에 실패한 항목은 사람 검토로 넘기고, 완료되면 웹훅으로 알림
- FastAPI, PostgreSQL, Redis, LLM 추출과 정확도 평가, AWS 배포까지 단계적으로 구축
