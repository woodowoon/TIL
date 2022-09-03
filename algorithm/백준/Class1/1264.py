# 브론즈4 문제
# 모음의 개수

while True :
  input_data = input()
  if input_data == "#" :
    break
  value =  'aeiouAEIOU'
  result = 0
  for i in range(len(input_data)) :
    if input_data[i] in value :
      result += 1

  print(result)

  # 처음에 sen 배열에 입력된 문장들을 담고 for문을 2번 돌리려고했다.
  # 하지만, 시간초과에 걸릴 것 같아서 다른 방법을 찾아보다가 모르겠어서 다른 코드를 보았는데,
  # 그냥 문제 자체를 이해하지 못하고 있었던 것이었다...
  # 모든 문장을 저장하고 나서 그 뒤에 모음 수를 차례로 출력하는줄알았는데 문장을 칠때마다 모음 수를 출력하는 것이었다.
    