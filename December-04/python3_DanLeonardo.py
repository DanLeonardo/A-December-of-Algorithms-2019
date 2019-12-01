# Return the highest h-index for the given papers
# N: the number of papers
# papers: the count of citations for each paper
def h_index(N, papers):
    # Copy and sort the list in descending order
    sorted = papers.copy()
    sorted.sort(reverse=True)

    # By sorting our list in reverse we can simply check if the first h values
    #   have a value of at least h.
    # Because we are looking for the maximum h-value we can start with our
    #   highest count and go down until we reach a valid h-value. If we don't
    #   find one then our default value of 0 still holds up.
    # E.G. [4,3,0,1,5] becomes [5,4,3,1,0]
    #   sorted[0] == 5 and sorted[5-1] <  5 so h-index 5 is not possible
    #   sorted[1] == 4 and sorted[4-1] <  4 so h-index 4 is not possible
    #   sorted[2] == 3 and sorted[3-1] >= 3 so h-index 3 is possible and any
    #   other h-indices would either be 3 or lower so we can stop.
    # This process goes through each item in papers once giving us a time
    #   complexity of O(n). With the addition of sorting the list at the
    #   beginning we are looking at O(n log n) + O(n) or simply O(n log n).

    max_h = 0

    # for count in sorted:
    #     if count <= len(sorted) and sorted[count-1] >= count:
    #         max_h = count
    #         break

    # This version is improved in cases where there are a lot of duplicate
    #   values in papers. This will not reduce the worst-case run time but
    #   should slightly improve average cases.
    for count in range(sorted[0], 0, -1):
        if count <= len(sorted) and sorted[count-1] >= count:
            max_h = count
            break

    print(max_h)
    return max_h

if __name__ == '__main__':
    h_index(5, [4,3,0,1,5])
    h_index(6, [4,5,2,0,6,4])
