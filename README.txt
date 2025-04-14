1.해당 하위디렉토리에 마커파일 작성
/tmp/buildkit_cve_marker/marker.txt

2.컨테이너 이미지 실행시 
RUN --mount=type=bind,source=/tmp/buildkit_cve_marker,target=/mnt/test
로 마운트

3.
python3 cve_2024_23652.py
으로 빌드타임 호스트 컨테이너 공격시도
