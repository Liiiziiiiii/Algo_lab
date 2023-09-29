def peak_length(array):
    n = len(array)
    peaks = []
    max_len_peak = 0
    max_peak = []
    peak = 0

    i = 0
    while i < n:
        left_peak = []
        while i < n - 1 and array[i] < array[i + 1]:
            left_peak.append(array[i])
            i += 1

        right_peak = []

        while i < n - 1 and array[i] > array[i + 1]:
            right_peak.append(array[i])
            i += 1
            right_peak.append(array[i])

        if left_peak and right_peak:
            all_side_peak = left_peak + right_peak
            peaks.append(all_side_peak)
            if len(all_side_peak) > max_len_peak:
                max_len_peak = len(all_side_peak)
                max_peak = all_side_peak

        i += 1

        # peak = max(max_peak)

        return max_len_peak

    # return max_len_peak, # return peaks, "    ", peak, "    ", max_len_peak, "   ", max_peak


print(peak_length([2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0]))
# print(peak_length([1, 3, 5, 4, 2, 0, 8, 3, 7]))

# print(peak_length([-4, -3, -2, -1, -8, 8]))

# [1, 3, 8, 9, 0]
# [1, 4, 8, 11, 12, 1]
# [2, 8, 9, 0]
# 6
