
def solution(A, K):
    N = len(A)
    if N == 0 or K % N == 0:
        return A
    
    shift = K % N
    return A[-shift:] + A[:-shift]