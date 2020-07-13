class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = arr.count(0)
        length = len(arr)
        # append the elements = no of zeroes to be appended
        for i in range(count):
            arr.append(0)
        for j in range(length-1,-1,-1):
            if arr[j] == 0:
                # duplicating zero if arr[i] = 0
                arr[j+count] = 0
                arr[j+count-1] = 0
                count -= 1
            else:
                arr[j+count] = arr[j]
        print(arr)
        #delete the elements which fall out of the size of the original array
        del arr[length:]
        
        
