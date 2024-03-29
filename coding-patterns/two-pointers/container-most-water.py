def container_with_most_water(height):
    
    length = len(height)
    maxArea = 0

    start, end = 0, length-1
    while start < end:
        x = end - start
        y = min(height[start], height[end])
        maxArea = max(maxArea, x * y)

        if (height[start] <= height[end]):
            start += 1
        else:
            end -= 1

    # Brute force O(n^2)
    # for i in range(length):
    #     for j in range(i+1, length):
    #         x = j - i
    #         y = min(height[i], height[j])
    #         maxArea = max(maxArea, x * y)

    return maxArea

def main():
    heights = [
                [1, 8, 6, 2, 5, 4, 8, 3, 7], 
                [20, 30, 9, 69],
                [13, 18, 12, 8],
                [45, 32, 56, 99], [23, 20]
                ]
    index = 1
    for i in heights:
        print(str(index)+".\tHeights: "+str(i))
        print("\n\tMaximum Area: " + str(container_with_most_water(i)))
        index += 1
        print("-" * 100)


if __name__ == "__main__":
    main()
