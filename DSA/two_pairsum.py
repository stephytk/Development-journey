def two_pair_sum(numbers, target):

    result =False

    numbers.sort()   # Step 1: sort the list

    left = 0
    right = len(numbers) - 1

   

    while left < right:

        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return True

        elif current_sum < target:
            left = left + 1

        else:
            right = right - 1


    

    return result


numbers = [2, 7, 11, 15]
target = 9

print(two_pair_sum(numbers, target))


#method2 with sort and append

def two_pair_sum(numbers, target):

    numbers.sort()   # sort the list

    left = 0
    right = len(numbers) - 1

    pairs = []   # list to store pairs

    while left < right:

        current_sum = numbers[left] + numbers[right]

        if current_sum == target:

            pairs.append((numbers[left], numbers[right]))  # append pair

            left = left + 1
            right = right - 1

        elif current_sum < target:
            left = left + 1

        else:
            right = right - 1

    return pairs





numbers = [1,2,3,4,5,6]
target = 7

result = two_pair_sum(numbers, target)

print(result)