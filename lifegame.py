# coding: Shift_JIS
import random
import time
import os

# ���C�t�Q�[���i���[���͈ȉ��j
#   �ߖ��F���͂�1��4�ȏ゠�鎞
#   �ߑa�F���͂�1��1�ȉ����鎞
#   �a���F���͂�1��3���鎞
#   �����F���͂�1��2��3���鎞
sedai = 100  # ���㐔
s = 10       # �X�e�[�W�̈�ӂ̒���
rate = 70    # �����l�ŁA����������䗦(��)
stage1 = [[0 for i in range(s)] for j in range(s)]  # ������p
stage2 = [[0 for i in range(s)] for j in range(s)]  # ������p

# ���ʕ\���p�̊֐�
def print_stage(x, ar):
  os.system('cls')
  print(str(x+1) + "�����")
  for x in range(s):
    print(ar[x])
  time.sleep(1)
  return

# �v�Z�������s��
def calc(sedai, s, stage1, stage2):
  for x in range(sedai):
    for i in range(s):     # 0�`s-1�͈̔�
      for j in range(s):
        cnt = 0
        # stage1[i][j]�̎���8�𒲂ׂ�
        if (i!=0) and (j!=0) and (stage1[i-1][j-1] == 1):
          cnt += 1
        if (i!=0) and (stage1[i-1][j] == 1):
          cnt += 1
        if (i!=0) and (j!=s-1) and (stage1[i-1][j+1] == 1):
          cnt += 1
        if (j!=0) and (stage1[i][j-1] == 1):
          cnt += 1
        if (j!=s-1) and (stage1[i][j+1] == 1):
          cnt += 1
        if (i!=s-1) and (j!=0) and (stage1[i+1][j-1] == 1):
          cnt += 1
        if (i!=s-1) and (stage1[i+1][j] == 1):
          cnt += 1
        if (i!=s-1) and (j!=s-1) and (stage1[i+1][j+1] == 1):
          cnt += 1
        # ������ɓ����
        stage2[i][j] = stage1[i][j]
        if cnt >= 4:      # �ߖ�
          stage2[i][j] = 0
        elif cnt <= 1:   # �ߑa
          stage2[i][j] = 0
        elif cnt==3:     # �a��
          stage2[i][j] = 1
    stage1 = stage2
    print_stage(x, stage1)
  return

# main����
for i in range(s):
  for j in range(s):
    if (random.randint(1, 100)<=rate):
      stage1[i][j] = 1  # ������stage1�ɏ����l������
calc(sedai, s, stage1, stage2)    # �������琢�㖈�̏���
