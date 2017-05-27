string_test = 'ppffccmmssnnhhbbmmggxxaaooeeqqeennffzzaaeeyyaaggggeessvvssggbbccnnrrjjxxuuzzbbjjrruuaaccaaoommkkkkxx'
#string_test = 'aaabccddd'  # abd


# Expected Output = Empty String

def check_dup_complete(check_string):
    for i in range(0,len(check_string)-1):
        if check_string[i] == check_string[i+1]:
            return True
        else:
            return False


def check_dup(string_test_check, i):
    while i < len(string_test_check) - 1:
        print(string_test_check, i, "check_dup_in_while")
        if string_test_check[i] == string_test_check[i + 1]:
            string_test_check, i = remove_dup(string_test_check, i)
        else:
            '''# i = i+1'''
            # pass
            # else:
            # return string_test_check
            # if len(string_test_check) == 2:
        i = i + 1


def remove_dup(string_test_remove, i):
    string_test_remove = string_test_remove[0:i] + string_test_remove[i + 2:]
    print(string_test_remove, i, 'rem_dup')
    return string_test_remove, 0

check_dup(string_test, 0)
'''final_string =
if len(final_string) == 2 and final_string[0] == final_string[-1]:
    print('Empty String')
else:
    print(final_string)
'''