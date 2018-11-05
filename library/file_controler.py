import os

file_name = "filehash.db"


def writer(file, data, place, hash1):
    with open(file, 'w') as f:
        for line in data:
            f.write(line)


# Returns index of x in data if present, else -1
def binarySearch(data, l, r, x):

    mid = int()
    # Check base case
    mid = int(l + (r - l) / 2)
    if r >= l:

        try:
            # If element is present at the middle itself
            if data[mid] == x:
                matched = "matched"
                return matched
            # If element is smaller than mid, then it
            # can only be present in left subarray
            elif data[mid] > x:
                return binarySearch(data, l, mid - 1, x)
            # Else the element can only be present
            # in right subarray
            else:
                return binarySearch(data, mid + 1, r, x)
        except TypeError:
            # print("There is a Un")
            return TypeError

    else:
        # Element is not present in the dataay
        # print("mid: ", mid)
        return mid


def binsert(data, hash1):
    high = len(data) - 1
    try:
        if high < 1:
            if data == []:
                mid = 0
                return mid
            elif data[high] < hash1:
                mid = 1
                return mid
            elif data[high] > hash1:
                mid = 0
                return mid
            elif data[high] == hash1:
                matched = "matched"
                return matched
    except TypeError:
        return TypeError


    # print("high: ", high)
    low = 0
    mid = binarySearch(data, low, high, hash1)
    # print("return of def: ", mid)
    return mid


def main_file_strike(xxhash):
    file = os.path.join(os.getcwd(), file_name)
    # print("File Opening: {}".format(file))
    try:
        with open(file, "r+") as fp:
            data = fp.readlines()

    except FileNotFoundError:
        print("{0} File Not Found !!!".format(file))
        with open(file, "w") as fp:
            print("File Created.......")

    finally:
        with open(file, "r+") as fp:
            data = fp.readlines()
        try:
            xxhash = xxhash + "\n"
        except TypeError:
            return -1

        mid = binsert(data, xxhash)
        if mid == "matched":
            # print("xxhash is already present!!!")
            return "FILE_NOT_MODIFIED"
        else:
            mid = mid + 1
            data.insert(mid, xxhash)
            writer(file, data, mid, xxhash)
        # print(type(data))
        # print(data)



# xxhash = "ba918c89"
# xxhash = "dae03bab"
# xxhash = "4cc82932"
# # xxhash = "24284847"

# main_file_strike(xxhash)
