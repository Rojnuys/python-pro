import random
import matplotlib.pyplot as plt


def get_max_mountain_deep(heights: list) -> int:
    if not len(heights):
        return 0

    max_deep = 0
    max_height = heights[0]
    min_height = heights[0]

    for height in heights:
        if height >= max_height:
            lake_deep = min(max_height, height) - min_height
            if lake_deep > max_deep:
                max_deep = lake_deep
            max_height = height
            min_height = height

        if height < min_height:
            min_height = height

        lake_deep = height - min_height
        if lake_deep > max_deep:
            max_deep = lake_deep

    return max_deep


print(get_max_mountain_deep([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]))

for i in range(3):
    heights = [random.randint(0, 20) for _ in range(random.randint(0, 30))]
    plt.plot(heights)
    plt.show()
    print(f"{i + 1}) {get_max_mountain_deep(heights)}")
    print(heights)
