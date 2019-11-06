def snail(snail_map):
    return_array = []
    first_elements = []

    while snail_map:
        for i, array in enumerate(snail_map):
            # 0x0の場合
            if len(array) == 0:
                return []

            # リストの中身が1つの場合
            if len(array) == 1:
                return_array.append(snail_map[0])
                return_array = list(flatten(return_array))
                del snail_map[0]
                continue

            array_length = len(snail_map)

            # ↑以外の場合、最初の一行ではこの処理が行われる
            if i == 0:
                return_array.append(array)
                continue

            # 最後の一行ではこの処理が行われる
            if i == array_length - 1:
                array.reverse()
                return_array.append(array)

                # snakeの上に上がってくる部分。
                first_elements.reverse()
                return_array.append(first_elements)

                # 元リストの最後と最後の行を削除
                del snail_map[-1]
                del snail_map[0]

                return_array = list(flatten(return_array))
                first_elements.clear()
                continue

            # はさまれている行は以下処理が行われる
            # ↓snakeの上に上がってくる部分用に最初の要素をリストに入れる。
            first_int = array[0]
            first_elements.append(first_int)

            # リストの最後の要素を追加。
            return_array.append(array[-1])

            # その行の最初と最後の要素を削除
            del array[0]
            del array[-1]

    return return_array


# https://qiita.com/shiracamus/items/fb85943ed34d5ec09c4f
def flatten(data):
    for item in data:
        if hasattr(item, '__iter__'):
            for element in flatten(item):
                yield element
        else:
            yield item


import unittest


class TestSnail(unittest.TestCase):

    def test_function(self):
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(snail(array), expected)

        array = [[1, 2, 3, 2],
                 [8, 9, 4, 2],
                 [1, 2, 3, 5],
                 [7, 6, 5, 4]]
        expected = [1, 2, 3, 2, 2, 5, 4, 5, 6, 7, 1, 8, 9, 4, 3, 2]
        self.assertEqual(snail(array), expected)

        array = [[1]]
        expected = [1]
        self.assertEqual(snail(array), expected)

        array = [[]]
        expected = []
        self.assertEqual(snail(array), expected)


if __name__ == "__main__":
    unittest.main()
