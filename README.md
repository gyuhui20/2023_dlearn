# 2023_dlearn
show the relativity between weather variances

사용할 딥러닝 모델 : 우선 5 layer DNN(후에 RNN 변경 가능)

x1, x2를 입력 데이터로 넣고, y1의 경향성 학습 및 예측(1차)

이렇게 찾아낸 경향성 기반, 입력 데이터에 x3를 추가하여 y1 학습(2차)

최종적으로 x1,x2,x3에 대해 y1의 경향성 예측(3차)

