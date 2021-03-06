from random import randrange


def shuffle(arr: list[int], i: int = None):
    if i is None:
        i = len(arr)

    if i == 0:
        return

    idx = randrange(0, i)
    tmp = arr[idx]
    arr[idx] = arr[i - 1]
    arr[i - 1] = tmp

    shuffle(arr, i - 1)


if __name__ == '__main__':
    def main():
        arr = [1, 2, 3, 4]
        shuffle(arr)
        print(arr)

        # probability of being the last card: 0.75*0.66*0.5*1
        # probability of being the card before the last: 0.75*0.66*0.5*1


    main()
