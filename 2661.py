#baekjoon 2661 좋은 수열 python3

def check_seq(seq):
  if len(seq) == 1:
    return True

  for j in range(1,len(seq)//2+1):
    if seq[-j:] == seq[-j*2:-j]:
      return False
  return True

def back_tracking(seq):
  new_num = int(seq[-1])+1
  if new_num == 4:
    return back_tracking(seq[:-1])
  seq = seq[:-1] + str(new_num)
  if check_seq(seq):
    return seq
  else:
    return back_tracking(seq)
  

n = int(input())

good_seq = ""

while True:
  already_seq = good_seq
  
  for i in range(1,4):
    tmp_seq = good_seq + str(i)
    length = len(tmp_seq)

    if check_seq(tmp_seq):
      good_seq = tmp_seq
      break
    else:
      continue

  if len(good_seq) == n:
    break
  elif already_seq == good_seq:
    good_seq = back_tracking(good_seq)
      
print(good_seq)

