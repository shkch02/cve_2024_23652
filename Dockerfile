# Dockerfile.buildkit_cve_test
# 마커 파일을 삭제하려는 의도적 BuildKit RUN --mount 테스트

# base image (아무거나 간단한 것)
FROM alpine

# BuildKit RUN --mount를 사용하여 의도적으로 마운트한 경로의 파일을 삭제 시도
RUN --mount=type=bind,target=/mnt,source=${MARKER_PATH} \
    rm -f /mnt/marker.txt

# 실제로는 이 Dockerfile은 빌드용이므로 컨테이너는 실행되지 않음
