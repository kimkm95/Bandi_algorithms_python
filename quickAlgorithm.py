# 샘플데이터

# 21, 10, 34, 75, 41, 30, 12, 19, 56, 50, 7, 43, 28, 91, 83, 81

# 중에서 45와 10번째로 값이 근접한 숫자를 찾아 결과값 출력하도록 작성하시면 됩니다.

# 설명: 풀이과정 중간과정 출력등 자유롭게 작성하여 제출하시기 바랍니다.




ori_arr = [21, 10, 34, 75, 41, 30, 12, 19, 56, 50, 7, 43, 28, 91, 81] # 주어진 샘플데이터
print(f'주어진 원본 배열 {ori_arr}')

arr = []
def quick_sort(arr):
    if len(arr) <= 1: # 정렬할 원소의 개수가 1보다 적다면 그냥 그 값 자체를 리턴해준다.
        return arr
    
    pivot, tail = arr[0], arr[1:] # pivot을 첫번째 숫자로 설정해 주고, tail 값으로 나머지 리스트 값을 준다.
    
    left = [x for x in tail if x <= pivot] # left 라는 리스트를 만들어서 tail리스트의 원소 값들을 pivot과 비교해 작으면 left에 넣어준다.
    right = [x for x in tail if x > pivot] # right 라는 리스트를 만들어서 tail리스트의 원소 값들을 pivot과 비교해 크면 right에 넣어준다.
    
    return quick_sort(left) + [pivot] + quick_sort(right) # 리턴 해준다.


for i in range(0, len(ori_arr)):
    arr.append(abs(ori_arr[i] - 45))    # 주어진 샘플데이터에 기준 값인 45를 뺀 값을 절대값화하여 새로운 배열에 넣어주었다.
arr = quick_sort(arr) # 새로운 배열을 정렬하였다.

print(f'원본 배열에서 얼마나 45에 가까운지 척도를 나타내는 새로운 배열 {arr}')

potential_ans = [arr[9] + 45, 45 - arr[9]] # 새로운 배열에서 원래 값을 찾을 수 있는 두가지 경우를 생각해주었다.

flag = 0 # 가능한 답이 들어있는 배열값이 실제 원본 배열에 있는 값인지 확인하는 절차를 가진다. 만약 진짜 있다면 그 값이 10번째로 근사한 값이다.
for i in range(0, len(ori_arr)):
    if(ori_arr[i] == potential_ans[0]):
        flag += 1

print(f'절대값을 벗겨서 나올 수 있는 10번째로 45와 가까운 값의 경우 2가지 {potential_ans}')

if(flag != 0): 
    print(f'45와 가장 근사한 수는 {potential_ans[0]} 입니다.')
else:
    print(f'45와 가장 근사한 수는 {potential_ans[1]} 입니다.')
