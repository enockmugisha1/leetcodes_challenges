class Solution:
    #my task is to complete this function where i have to return false if length is even else return true
    def isLengthEven(self, head):
        current = head
        count =0
        while current:
            count += 1
            current =current.next

        return count % 2 == 0
