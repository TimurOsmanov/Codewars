# For this kata, we're given an image in which some object of interest (e.g. a face, or a license plate, or an aircraft)
# appears as a large block of contiguous pixels all of the same colour. (Probably some image-processing has already
# occurred to achieve this, but we needn't worry about that.) We want to find the centre of the object in the image.
#
# We'll do this by finding which pixels of the given colour have maximum depth. The depth of a pixel P
# is the minimum number of steps (up, down, left, or right) you have to take from P to reach either a
# pixel of a different colour or the edge of the image.
# In the picture, the red pixel marked "3" has a depth of 3: it takes at least 3 steps from there to reach
# something other than another red pixel. Note that the steps need not be all in the same direction.
# Only one red pixel has depth 3: the one right in the middle of the red region. Similarly,
# the blue pixel marked "2" has a depth of 2 (but it is not the only one with this depth).
# The green and purple pixels all have depth 1.
#
# The pixels of a given colour with the largest depth will be found at the centre of
# the biggest solid region(s) of that colour. Those are the ones we want.
#
# The function you'll write (central_pixels) belongs to the following data structure (class Image)
# The image data consists of a one-dimensional array pixels of unsigned integers (or just integers,
# in languages that don't have unsigned integers as such), which correspond to pixels in row-by-row order.
# (That is, the top row of pixels comes first, from left to right, then the second row, and so on,
# with the pixel in the bottom right corner last of all.) The values of the pixels array elements represent colours
# via some one-to-one mapping whose details need not concern us.
#
# The central_pixels function should find and return all the positions (pixels array indices) of the pixels having
# the greatest depth among all pixels of colour colour).
#
# Note 1. The final test in the suite (Big_Test) is a 16-megapixel image (1 megapixel in the Python version),
# so you will need to consider the time and space requirements of your solution for images up to that size.
#
# Note 2. The order of pixel positions in the returned array is not important; sort them however you like.
#
# Hint. It is possible to get this done in two passes through the pixel data.
import numpy as np
import time

arr = np.random.randint(15, size=(1000, 1000))
ans = [c for x in arr for c in x]

start = time.time()


# Version 1 - passed
class Image:
    def __init__(self, data, w, h):
        self.pixels = data
        self.width = w
        self.height = h


class Central_Pixels_Finder(Image):

    def central_pixels(self, color):
        depth_ascending = {}
        depth_descending = {}
        depth = {}
        pixels = self.pixels
        width = self.width

        def pixel_init(pixel_num):

            right = None if pixel_num + 1 > len(pixels) or (pixel_num + 1) % width == 0 or pixels[
                pixel_num + 1] != color else pixel_num + 1
            down = None if pixel_num + width >= len(pixels) or pixels[pixel_num + width] != color else pixel_num + width
            left = None if pixel_num - 1 < 0 or (pixel_num - 1) % width == width - 1 or pixels[
                pixel_num - 1] != color else pixel_num - 1
            up = None if pixel_num - width < 0 or pixels[pixel_num - width] != color else pixel_num - width
            trigger = 1 if all((right, down, left, up)) else 0

            return right, down, left, up, trigger

        def check_ascending(pixel_num, left, up, trigger, depth_ascending):
            if trigger:
                depth_ascending[pixel_num] = min(depth_ascending[left], depth_ascending[up]) + 1
            else:
                depth_ascending[pixel_num] = 1

        def check_descending(pixel_num, right, down, trigger, depth_descending):
            if trigger:
                depth_descending[pixel_num] = min(depth_descending[right], depth_descending[down]) + 1
            else:
                depth_descending[pixel_num] = 1

            depth_final = min(depth_ascending[pixel_num], depth_descending[pixel_num])
            if depth_final not in depth:
                depth[depth_final] = [pixel_num]
            else:
                depth[depth_final].append(pixel_num)

        for pixel_num, pixel in enumerate(self.pixels):
            if pixel == color:
                pixel_new = pixel_init(pixel_num)
                check_ascending(pixel_num, pixel_new[2], pixel_new[3], pixel_new[4], depth_ascending)
            else:
                depth_ascending[pixel_num] = 0

        length = len(self.pixels) - 1

        for pixel_num, pixel in enumerate(self.pixels[::-1]):
            pixel_num = abs(pixel_num - length)
            pixel_new = pixel_init(pixel_num)

            if pixel == color:
                check_descending(pixel_num, pixel_new[0], pixel_new[1], pixel_new[4], depth_descending)
            else:
                depth_ascending[pixel_num] = 0

        return depth[max([x for x in depth])] if max([x for x in depth]) else []


v1 = Central_Pixels_Finder(
    ans,
    1000,
    1000).central_pixels(5)
print(time.time() - start)

# Version 2 - not passed
start = time.time()


class Image:
    def __init__(self, data, w, h):
        self.pixels = data
        self.width = w
        self.height = h


def array_centered(arr):
    if len(arr) == 1:
        return [1]
    centered = [x + 1 for x in range(len(arr) // 2)]
    mid = [centered[-1] + 1] if len(arr) % 2 == 1 else []
    centered = centered + mid + centered[::-1]
    return centered


def check_row(row_pixels, color, result, index, height):
    temp = []
    row_pixels.append(color + 1)
    for num_pixel, pixel in enumerate(row_pixels[:-1]):
        if pixel == color:
            if row_pixels[num_pixel + 1] == pixel:
                temp.append(1)
            else:
                temp.append(1)
                if index in (0, height - 1):
                    result.extend(temp)
                else:
                    result.extend(array_centered(temp))
                temp = []
        else:
            result.append(0)


def check_pixels_near(pixel_index, width, result_rows):
    if result_rows[pixel_index] > 2:
        right, down, left, up = pixel_index + 1, pixel_index + width, pixel_index - 1, pixel_index - width

        def find1(right_, down_, left_, up_, i):
            coord1 = [result_rows[right_], result_rows[down_], result_rows[left_], result_rows[up_]]
            if any([x == 1 for x in coord1]):
                result_rows[pixel_index] = min(result_rows[pixel_index], (i + 1))
            else:
                find1(right_ + 1, down_ + width, left_ - 1, up_ - width, i + 1)

        find1(right, down, left, up, 1)


def check_col(col_pixels, col_pixels_indexes, color, result, width, result_rows, res_dict):
    temp = []
    col_pixels.append(color + 1)
    for num_pixel, pixel in enumerate(col_pixels[:-1]):
        if pixel == color:
            if col_pixels[num_pixel + 1] == pixel:
                temp.append(1)
            else:
                temp.append(1)
                if col_pixels_indexes[0] in (0, width - 1):
                    result.extend([x for x in temp])
                else:
                    result.extend([x for x in array_centered(temp)])
                temp = []
        else:
            result.append(0)

    for pixel_index, pixel in enumerate(result):
        result_rows[col_pixels_indexes[pixel_index]] = min(pixel, result_rows[col_pixels_indexes[pixel_index]])


class Central_Pixels_Finder(Image):
    def central_pixels(self, color):
        result_rows = []
        res_dict = {}
        for num_row, row in enumerate(range(self.width - 1, self.height * self.width, self.width)):
            row_pixels = self.pixels[row // self.width * self.width:row + 1]
            check_row(row_pixels, color, result_rows, num_row, self.height)

        for col in range(self.width):
            col_pixels_indexes = [x for x in range(col, self.height * self.width, self.width)]
            col_pixels = [self.pixels[x] for x in range(col, self.height * self.width, self.width)]
            check_col(col_pixels, col_pixels_indexes, color, [], self.width, result_rows, res_dict)

        for num_pixel, pixel in enumerate(result_rows):
            check_pixels_near(num_pixel, self.width, result_rows)
            if result_rows[num_pixel] not in res_dict:
                res_dict[result_rows[num_pixel]] = [num_pixel]
            else:
                res_dict[result_rows[num_pixel]].append(num_pixel)

        # for num_row, row in enumerate(range(self.width - 1, self.height * self.width, self.width)):
        #     print(f'{num_row * self.width:_>3}', result_rows[row // self.width * self.width:row + 1])
        #
        # print([x for x in res_dict], res_dict)

        return res_dict[max([x for x in res_dict])] if max([x for x in res_dict]) else []


v2 = Central_Pixels_Finder(
    ans,
    1000,
    1000).central_pixels(5)
print(time.time() - start)

# Version 3 - not passed
start = time.time()


class Image:
    def __init__(self, data, w, h):
        self.pixels = data
        self.width = w
        self.height = h


class Pixel:
    def __init__(self, pixel_num, value, pixels, width, color):
        self.right = None if pixel_num + 1 > len(pixels) or (pixel_num + 1) % width == 0 \
                             or pixels[pixel_num + 1] != color else pixel_num + 1
        self.down = None if pixel_num + width >= len(pixels) \
                            or pixels[pixel_num + width] != color else pixel_num + width
        self.left = None if pixel_num - 1 < 0 or (pixel_num - 1) % width == width - 1 \
                            or pixels[pixel_num - 1] != color else pixel_num - 1
        self.up = None if pixel_num - width < 0 \
                          or pixels[pixel_num - width] != color else pixel_num - width
        self.pixel_num = pixel_num
        self.value = value
        self.counter = 1
        self.trigger = 1 if all((self.right, self.down, self.left, self.up)) else 0

    def __str__(self):
        return f"pixel: {self.pixel_num}, color: {self.value}, near: {self.right}, {self.down}, {self.left}, {self.up}"

    def __repr__(self):
        return f"pixel: {self.pixel_num}, color: {self.value}, near: {self.right}, {self.down}, {self.left}, {self.up}"


def check(pixel_num, visited, counter, pixels, width, color, depth_dict):
    near = [pixel.trigger == 1 for pixel in visited]

    if not all(near):
        if counter not in depth_dict:
            depth_dict[counter] = [pixel_num]
        else:
            depth_dict[counter].append(pixel_num)
        return counter

    new_near = []
    for pixel in visited:
        new_near.append(Pixel(pixel.right, pixels[pixel.right], pixels, width, color))
        new_near.append(Pixel(pixel.down, pixels[pixel.down], pixels, width, color))
        new_near.append(Pixel(pixel.left, pixels[pixel.left], pixels, width, color))
        new_near.append(Pixel(pixel.up, pixels[pixel.up], pixels, width, color))
    visited = new_near
    check(pixel_num, visited, counter + 1, pixels, width, color, depth_dict)


class Central_Pixels_Finder(Image):

    def central_pixels(self, color):
        depth_dict = {}

        for pixel_num, pixel in enumerate(self.pixels):
            if pixel == color:
                pixel_new = Pixel(pixel_num, pixel, self.pixels, self.width, color)
                check(pixel_num, [pixel_new], 1, self.pixels, self.width, color, depth_dict)
        if depth_dict:
            return depth_dict[max(depth_dict)]
        else:
            return []


v3 = Central_Pixels_Finder(
    ans,
    1000,
    1000).central_pixels(5)
print(time.time() - start)


# Version 4 - not passed
start = time.time()


class Image:
    def __init__(self, data, w, h):
        self.pixels = data
        self.width = w
        self.height = h


def pixel_init(pixel_num, pixels, width, color):
    right = None if pixel_num + 1 > len(pixels) or (pixel_num + 1) % width == 0 or pixels[
        pixel_num + 1] != color else pixel_num + 1
    down = None if pixel_num + width >= len(pixels) or pixels[pixel_num + width] != color else pixel_num + width
    left = None if pixel_num - 1 < 0 or (pixel_num - 1) % width == width - 1 or pixels[
        pixel_num - 1] != color else pixel_num - 1
    up = None if pixel_num - width < 0 or pixels[pixel_num - width] != color else pixel_num - width
    counter = 1
    trigger = 1 if all((right, down, left, up)) else 0
    return right, down, left, up, trigger, counter


def check(pixel_num, visited, counter, pixels, width, color, depth_dict):
    near = [pixel[-2] == 1 for pixel in visited]

    if not all(near):
        if counter not in depth_dict:
            depth_dict[counter] = [pixel_num]
        else:
            depth_dict[counter].append(pixel_num)
        return counter

    new_near = []
    for pixel in visited:
        new_near.append(pixel_init(pixel[0], pixels, width, color))
        new_near.append(pixel_init(pixel[1], pixels, width, color))
        new_near.append(pixel_init(pixel[2], pixels, width, color))
        new_near.append(pixel_init(pixel[3], pixels, width, color))
    visited = new_near
    check(pixel_num, visited, counter + 1, pixels, width, color, depth_dict)


class Central_Pixels_Finder(Image):

    def central_pixels(self, color):
        depth_dict = {}

        for pixel_num, pixel in enumerate(self.pixels):
            if pixel == color:
                pixel_new = pixel_init(pixel_num, self.pixels, self.width, color)
                check(pixel_num, [pixel_new], 1, self.pixels, self.width, color, depth_dict)
        if depth_dict:
            return depth_dict[max(depth_dict)]
        else:
            return []


v4 = Central_Pixels_Finder(
    ans,
    1000,
    1000).central_pixels(5)
print(time.time() - start)


########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
start = time.time()


class Image:
    def __init__(self, data, w, h):
        self.pixels = data
        self.width = w
        self.height = h


class Central_Pixels_Finder(Image):

    def central_pixels(self, colour):
        size      = self.width * self.height
        depths    = [0] * size
        internal  = [ ]
        for position, pcolour in enumerate(self.pixels):
            if pcolour == colour:
                depths[position] = 1
                if ( position >        self.width  and
                     position < size - self.width  and
                     position       %  self.width  and
                    (position + 1)  %  self.width):
                        internal.append(position)
                        depths[position] += min(depths[position - 1         ],
                                                depths[position - self.width])
        max_depth = 1
        for position in internal[::-1]:
            depths[position] = min(depths[position             ]    ,
                                   depths[position + 1         ] + 1,
                                   depths[position + self.width] + 1)
            max_depth        = max(depths[position], max_depth)
        return [position for position, depth in enumerate(depths) if depth == max_depth]


v5 = Central_Pixels_Finder(
    ans,
    1000,
    1000).central_pixels(5)
print(time.time() - start)
print(sorted(v1) == sorted(v2) == sorted(v3) == sorted(v4) == sorted(v5))
