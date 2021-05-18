def shiftArray(nums,indStart,indEnd):
    while indStart < indEnd:
        nums[indEnd] = nums[indEnd-1]
        indEnd -= 1
def insertionSort(nums):
    for i in range(1,len(nums)):
        predIndex = i-1
        while predIndex >= 0 and nums[i] < nums[predIndex]:
            predIndex -= 1
        temp = nums[i]
        shiftArray(nums,predIndex + 1, i)
        nums[predIndex+1] = temp

def testCases(input,output):
    insertionSort(input)
    myOutput = input
    if len(output) != len(myOutput):
        return False
    for i in range(len(output)):
        if output[i] != myOutput[i]:
            return False
    return True


arrays = [[1, -1,54, 6, 7, 12, 9, 0, 31],[1],[1,-1],[-1,1],[]]
outputs = [[-1,0,1,6,7,9,12,31,54], [1], [-1, 1], [-1, 1], []]
i = 0
for arr in arrays:
    print(testCases(arr,outputs[i]))
    i += 1
