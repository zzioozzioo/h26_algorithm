A = [5, 7, 23, 14]

def partition(A, left, right):
    # 피벗을 가장 오른쪽 원소로 설정
    pivot = A[right]
    i = left - 1  # 피벗보다 작은 원소들이 들어갈 위치의 경계
    
    for j in range(left, right):
        # 현재 원소가 피벗보다 작거나 같으면 위치를 교환
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            
    # 마지막으로 피벗을 자기 자리(i+1)로 이동
    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1

def quick_sort(A, left, right):
    if left < right:
        # 피벗의 위치를 결정 (파티션)
        pivot_index = partition(A, left, right)
        
        # 피벗을 기준으로 왼쪽과 오른쪽을 각각 다시 정렬
        quick_sort(A, left, pivot_index - 1)
        quick_sort(A, pivot_index + 1, right)

# 실행
quick_sort(A, 0, len(A) - 1)
print(A) # [5, 7, 14, 23]