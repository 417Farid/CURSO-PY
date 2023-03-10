def count_substring(string, sub_string):
    matches = 0
    for i, char in enumerate(string):
        if char == sub_string[0]:
            if sub_string in string[i:i + len(sub_string):]:
                matches += 1
    return matches


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
