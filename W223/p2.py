class Solution:
    def __init__(self):
        self.result = []

    def longestSquareStreak(self, nums: List[int]) -> int:
        # Stores the current
        # subsequence
        curr_set = []

        # Sort the vector
        nums.sort()

        # Backtrack function to
        # generate subsequences
        self.backtrack(nums, 0, curr_set)
        self.prints()
        return 0

    # Function to generate all distinct
    # subsequences of the array
    # using backtracking

    def backtrack(self,nums, start, curr_set):

        # Global result
        self.result.append(list(curr_set))

        for i in range(start, len(nums)):

            # If the current element is repeating
            if (i > start and nums[i] == nums[i - 1]):
                continue

            # Include current element
            # into the subsequence
            curr_set.append(nums[i])

            # Proceed to the remaining array
            # to generate subsequences
            # including current array element
            self.backtrack(nums, i + 1, curr_set)

            # Remove current element
            # from the subsequence
            curr_set.pop()

    # Function to sort the array and generate
    # subsequences using Backtracking

    # Function to prints all subsequences
    def prints(self):

        for i in range(len(self.result)):
            print('{', end='')

            for j in range(len(self.result[i])):
                print(result[i][j], end='')

                if (j < len(self.result[i]) - 1):
                    print(',', end=' ')

            print('} ', end='')
