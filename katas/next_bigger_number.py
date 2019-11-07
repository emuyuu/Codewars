# テストパスしていない
# Next bigger number with the same digits


def next_bigger(number):
    int_list = list(str(number))

    number_len = len(int_list)
    for i in range(2, number_len + 1):
        # 後ろからi個めの数字から、リストの最後まで
        compare_list = int_list[-i::]
        print(f'will compare: {compare_list}')
        if left_is_smaller(compare_list):
            # 数字の並び替え
            reordered = reorder_int(compare_list)
            print(f'reordered: {reordered}')

            del int_list[-len(reordered)::]
            print(int_list)
            int_list.extend(reordered)
            return int(''.join(int_list))
    return -1


def reorder_int(compare_list):
    new_order = []

    # 数字を重複なしの小さい順に並び替え。２番目に小さい数字を取り出すし、新しいリストの先頭に。
    sorted_list = list(set(compare_list))
    sorted_list.sort()
    if len(sorted_list) == 2:
        second_small = sorted_list[1]
        print(f'secondsmall: {second_small}')
    else:
        second_small = sorted_list[-2]
        print(f'secondsmall: {second_small}')
    compare_list.remove(second_small)
    new_order.append(second_small)

    # 残りの数字も新しいリストに追加する。
    compare_list.sort()
    new_order.extend(compare_list)
    return new_order


def left_is_smaller(compare_list):
    # 与えられたリストで、右と左の数字を比較していく
    for j in range(len(compare_list) - 1, 0, -1):
        print(f'start index: {len(compare_list) - 1}')
        if compare_list[j - 1] < compare_list[j]:
            print(f'right: {compare_list[j]}')
            print(f'left: {compare_list[j - 1]}')
            return True
    return False


import unittest


class TestBiggerNumber(unittest.TestCase):
    def test_function(self):
        self.assertEqual(next_bigger(12), 21)
        self.assertEqual(next_bigger(111), -1)
        self.assertEqual(next_bigger(513), 531)
        self.assertEqual(next_bigger(2017), 2071)
        self.assertEqual(next_bigger(414), 441)
        self.assertEqual(next_bigger(144), 414)
        self.assertEqual(next_bigger(441), -1)


if __name__ == "__main__":
    unittest.main()
