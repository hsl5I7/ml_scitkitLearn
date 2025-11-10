from pathlib import Path # 파일 경로를 다루기 위한 모듈
import pandas as pd
import tarfile # .tar, .tar.gz, .tgz 파일 압축 해제를 위한 모듈
import urllib.request # URL에서 파일 요청 및 다운로드를 위한 모듈

def load_housing_data():
    tarball_path = Path("datasets/housing.tgz") # 해당 파일 찾음
    if not tarball_path.is_file(): # 해당 파일이 없으면
        Path("datasets").mkdir(parents=True, exist_ok=True) # datasets 디렉토리 생성
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path) # URL에서 파일 다운로드
        with tarfile.open(tarball_path) as housing_tarball: # tarball 파일 압축 해제
            housing_tarball.extractall(path="datasets", filter="data") # 데이터 파일만 추출
    return pd.read_csv(Path("datasets/housing/housing.csv")) # 파일을 읽어서 DataFrame으로 변환 후 반환
housing_full = load_housing_data()

# print(housing_full.head()) # 데이터프레임의 처음 5행 출력
# print(housing_full.info()) # 데이터프레임의 요약 정보 출력
# print(housing_full["ocean_proximity"].value_counts()) # ocean_proximity 열의 고유값과 그 개수 출력
# print(housing_full.describe()) # 수치형 열들의 통계 요약 정보 출력

# import matplotlib.pyplot as plt
# housing_full.hist(bins=50, figsize=(12,8)) # 각 수치형 열에 대한 히스토그램 생성
# plt.show() # 히스토그램 출력

# creating test set
import numpy as np
def shuffle_and_split_data(data, test_ratio, rng):
    shuffled_indices = rng.permutation(len(data)) # 데이터의 인덱스를 무작위로 섞음/셔플
    test_set_size = int(len(data) * test_ratio) # 테스트 세트의 크기 계산
    test_indices = shuffled_indices[:test_set_size] # 테스트 세트의 인덱스 선택
    train_indices = shuffled_indices[test_set_size:] # 훈련 세트의 인덱스 선택, iloc: short for integer location
    return data.iloc[train_indices], data.iloc[test_indices] # 훈련 세트와 테스트 세트 반환

