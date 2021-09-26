# def quick_sort(arr): # 퀵 정렬 함수 정의
#     if len(arr) <= 1: # 정렬할 원소의 개수가 1보다 적다면 그냥 그 값 자체를 리턴해준다.
#         return arr
#     pivot = arr[len(arr) // 2] # 피봇을 정하기 위해 원소의 가장 가운데 값을 정한다.
#     low, equal, high = [], [], [] # 피봇을 기준으로 3가지 리스트를 만든다. 
#     for num in arr: # 함수내 원소를 한번씩 순회하여 피봇보다 크거나 작은지 판단한다.
#         if num < pivot:
#             low.append(num) # 작으면 less 
#         elif num > pivot:
#             high.append(num) # 크면 bigger
#         else:
#             equal.append(num) # 피봇과 같으면 equal 
#     return quick_sort(low) + equal + quick_sort(high) # 정렬된 함수를 리턴해준다.


# arr = [1,3,5,7,9,2,4,6,8]
# arr = quick_sort(arr)

# print(arr)



# def quick_sort(arr):
#     if len(arr) <= 1: # 정렬할 원소의 개수가 1보다 적다면 그냥 그 값 자체를 리턴해준다.
#         return arr
    
#     pivot, tail = arr[0], arr[1:] # pivot을 첫번째 숫자로 설정해 주고, tail 값으로 나머지 리스트 값을 준다.
    
#     left = [x for x in tail if x <= pivot] # left 라는 리스트를 만들어서 tail리스트의 원소 값들을 pivot과 비교해 작으면 left에 넣어준다.
#     right = [x for x in tail if x > pivot] # right 라는 리스트를 만들어서 tail리스트의 원소 값들을 pivot과 비교해 크면 right에 넣어준다.
    
#     return quick_sort(left) + [pivot] + quick_sort(right) # 리턴 해준다.

# arr = [1,3,5,7,9,2,4,6,8]
# arr = quick_sort(arr)

# print(arr)


# 퀵 정렬 
def partition(arr, start, end):
    pivot = arr[start] # 정렬하고자 하는 집합의 첫번째 원소를 피봇으로 한다.
    i = start + 1
    j = end
    while i <= j:
        while i <= j and arr[i] <= pivot: i += 1 # i 는 pivot 값보다 작은수면 계속해서 오른쪽으로 이동한다.
        while i <= j and arr[j] >= pivot: j -= 1 # j 는 pivot 값보다 큰수면 계속해서 왼쪽으로 이동한다.
        if i < j: # i와 j 가 이동할 수 없다면 그 값을 바꿔준다. 이런 경우를 i 와 j가 같아지는 지점에 이를 때까지 반복한다. 
            arr[i], arr[j] = arr[j], arr[i]
    arr[start], arr[j] = arr[j], arr[start] 
    return j # j 는 새로운 pivot 값이 된다.

def quicksort(arr, start, end):
    pivot = partition(arr, start, end) # 새로운 피봇값을 가운데 설정해 준다.
    if start < pivot-1:
        quicksort(arr, start, pivot-1) # 피봇값을 기준으로 재귀함수를 실행 해 준다.
    if end > pivot:
        quicksort(arr, pivot+1, end)


a = [1,3,5,7,9,2,4,6,8]
quicksort(a, 0, len(a)-1)
print(a)
