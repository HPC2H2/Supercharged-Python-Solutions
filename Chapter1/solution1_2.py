"""
Author: HPC2H2
Date: 2025-02-20
Description: Solution to exercise 1.2
"""
#  Write a function that efficiently strips the first two
#  characters of a string andthe last two characters
#  of a string. Returning an empty string should be
#  anacceptable return value. Test this function with
#  a series of different inputs.
# 编写一个程序，获取球体的半径，计算它的体积，然后打印出答案。
# 如有必要可以在网上查找体积计算公式。


def get_sphere_radius_calculate_volume(radius):
    """
    计算球体的体积。

    参数:
    radius (float): 球体的半径，必须大于0。

    返回:
    float: 球体的体积。

    异常:
    ValueError: 如果半径小于或等于0，则引发此异常。
    """
    if radius <= 0:
        exception = ValueError("The radius must be greater than 0.")
        raise exception
    volume = (4 / 3) * 3.14 * radius ** 3
    return format(volume, '.2f')

if __name__ == "__main__":
    inputted_radius = float(input("Enter the radius of the sphere:"))
    print("The volume of the sphere is:", \
        str(get_sphere_radius_calculate_volume(inputted_radius))+".")
