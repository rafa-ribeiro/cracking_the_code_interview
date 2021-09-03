from exercise import locate_all_permutations


def test_locate_all_permutations():
    s = 'abbc'
    b = 'cbabadcbbabbcbabaabccbabc'

    permutations = ["cbab", "cbba", "abbc", "bcba", "cbab", "cbab", "babc"]
    expected_locations = [(0, 3), (6, 9), (9, 12),
                          (11, 14), (12, 15), (20, 23), (21, 24)]
    locations = locate_all_permutations(s=s, b=b)
    assert len(locations) == len(permutations)
    assert locations == expected_locations


# c = 8
# cb = 12
# cba = 14
# cbab = 18 -> IGUAL SUM_S -> GUARDA LOCATION sum_b = 10
# cbaba = 12
# cbabad = 12 + 999 -> ZERA sum_b = 0
# cbabadc = 8
# cbabadcb = 12
# cbabadcbb = 16
# cbabadcbba = 18 -> IGUAL SUM_S -> GUARDA_LOCATION sum_b = 10
# cbabadcbbab = 14
# cbabadcbbabb = 18 -> IGUAL SUM_S
