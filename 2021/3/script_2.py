import time


def swap_rows_and_collumns(input) -> list:
    column_swapped = []
    for i in range(12):
        column_swapped.append('')
        for j in range(len(input)):
            column_swapped[-1] += input[j][i]

    return column_swapped


with open('input.txt') as f:
    lines = f.read().splitlines()
    ogr_bin = lines.copy()
    ogr_swapped = swap_rows_and_collumns(lines).copy()

    csr_bin = lines.copy()
    csr_swapped = swap_rows_and_collumns(lines).copy()

    for i in range(12):
        ones = 0
        zeros = 0
        ogr_str = ''
        csr_str = ''

        counter = 0
        while len(ogr_bin) != 1:
            if ogr_swapped[counter].count('1') >= len(ogr_swapped[counter]) / 2:
                ogr_str += '1'
            else:
                ogr_str += '0'

            for ogr in ogr_bin.copy():
                if not ogr.startswith(ogr_str):
                    ogr_bin.remove(ogr)
            ogr_swapped = swap_rows_and_collumns(ogr_bin)

            counter += 1

        counter = 0
        while len(csr_bin) != 1:
            if csr_swapped[counter].count('1') >= len(csr_swapped[counter]) / 2:
                csr_str += '0'
            else:
                csr_str += '1'

            for csr in csr_bin.copy():
                if not csr.startswith(csr_str):
                    csr_bin.remove(csr)
            csr_swapped = swap_rows_and_collumns(csr_bin)

            counter += 1


print(int(ogr_bin[0], 2) * int(csr_bin[0], 2))
