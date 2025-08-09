"""
Within a list of tasks represented by integers in an array called "nums," pinpoint a consecutive sequence of tasks. Rearranging these tasks in ascending order of complexity would ensure that the entire list is arranged in ascending order of complexity. Provide the indices denoting the start and end of this task sequence.

Example 1:
Input:
nums = [2, 6, 4, 8, 10, 9, 15]
Output:
[1, 5]
Explanation:
To ensure that all events proceed in chronological order, you need to rearrange the events starting from the second event [6] to the sixth event [9]. This subarray [6, 4, 8, 10, 9] represents the shortest sequence of events that need to be rescheduled, allowing all events to progress seamlessly.

Example 2:
Input:
nums = [1, 3, 2, 4, 5]
Output:
[1, 2]
Explanation:
To ensure that tasks are tackled in the order of their priority levels, you need
to rearrange the tasks starting from the second task [3] to the third task [2].
This subarray [3, 2] represents the shortest sequence of tasks that need to be
reassigned, ensuring that tasks are addressed according to their priorities.

Constraints:
Array is not given sorted.
"""

nums = [1, 3, 2, 6, 5]
last_index = 0
have_first_index = False
output_list = []

for i in range(len(nums) - 1):

    if nums[i] > nums[i + 1]:
        temp = nums[i]
        nums[i] = nums[i + 1]
        nums[i + 1] = temp

        if have_first_index == False:
            output_list.append(i)
            have_first_index = True
        
        last_index = i + 1

output_list.append(last_index)
print(output_list)