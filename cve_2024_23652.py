# cve_2024_23652.py
import os
import time
import subprocess
from pathlib import Path

MARKER_DIR = str(Path("tmp").resolve())
MARKER_FILE = os.path.join(MARKER_DIR, "marker.txt")
DOCKERFILE_PATH = "Dockerfile.buildkit_cve_test"


def prepare_marker():
    os.makedirs(MARKER_DIR, exist_ok=True)
    with open(MARKER_FILE, "w") as f:
        f.write("This is a marker file for CVE-2024-23652 test.\n")
    print(f"[*] 마커 파일 생성됨: {MARKER_FILE}")


def run_buildkit_deletion_test():
    print("[*] BuildKit를 이용해 마커 파일 삭제 시도 중...")
    cmd = [
        "docker", "build", ".",
        "-f", DOCKERFILE_PATH,
        "--no-cache",
        "--progress=plain",
        "--build-arg", f"MARKER_PATH={MARKER_DIR}"
    ]
    subprocess.run(cmd)


def check_marker_deleted():
    time.sleep(2)
    if not Path(MARKER_FILE).exists():
        print("[!] 탐지됨: 마커 파일이 삭제되었습니다. -> CVE-2024-23652 활성 가능성 있음")
    else:
        print("[*] 정상: 마커 파일이 삭제되지 않음 -> BuildKit 패치 적용된 것으로 보임")


if __name__ == "__main__":
    prepare_marker()
    run_buildkit_deletion_test()
    check_marker_deleted()
