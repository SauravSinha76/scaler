def solve(A):
    N = len(A)
    ans = []
    # a map to maintain the frequency of any element at any given time
    # 5 -> 1, 2, 3
    # 7 -> 1, 2
    # 4 -> 1
    freqMap = {}
    # a map to maintain the frequency and eligible elements with that frequency in a stacked way
    # 1 -> stack[5, 7, 4]
    # 2 -> stack[5, 7, 4]
    # 3 -> stack[5]
    eleFreqStack = {}
    maxFreq = 0
    for i in range(N):
        operation = A[i][0]
        value = A[i][1]
        if operation == 1:
            ans.append(-1)
        # update frequency of value
            if value not in freqMap:
                freqMap[value] = 1
            else:
                freqMap[value] += 1
            # push this element to top of the stack of this frequency
            if freqMap[value] in eleFreqStack:
                eleFreqStack[freqMap[value]].append(value)
            else:
                eleFreqStack[freqMap[value]] = [value]
            # check if this frequency is the maximum frequency
            maxFreq = max(maxFreq, freqMap[value])
        else:
            # remove the top element with max frequency
            ele = eleFreqStack[maxFreq].pop()
            # reduce the frequency of this element, as this is removed now.
            freqMap[ele] -= 1
            ans.append(ele)
            # if this was the only element, reduce the maxFrequency by 1
            if len(eleFreqStack[maxFreq]) == 0:
                maxFreq -= 1
    print(freqMap)
    print(eleFreqStack)
    return ans


A = [
            [1, 5],
            [1, 7],
            [1, 5],
            [1, 7],
            [1, 4],
            [1, 5],
            [2, 0],
            [2, 0],
            [2, 0],
            [2, 0]  ]
print(solve(A))