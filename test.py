import subprocess

# 파이썬 실행 파일의 경로
python_path = "C:/Users/hackc/AppData/Local/Programs/Python/Python39/python.exe"

# pip를 사용하여 mysql 모듈 설치
subprocess.run([python_path, "-m", "pip", "install", "selenium"])
