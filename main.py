from sklearn.metrics.pairwise import manhattan_distances
from sklearn.metrics.pairwise import euclidean_distances


def man_dst():
    p_a = [5, 14]
    p_b = [7, 11]
    z = [p_a, p_b]
    dst = manhattan_distances(z)
    print('Manhattan distance: ', )
    print(dst)

def eucl_dst():
    x = [4, 8]
    y = [4, 9]
    z = [x, y]
    dst = euclidean_distances(z)


def main():
    a = man_dst()






RUN_MAIN = main()