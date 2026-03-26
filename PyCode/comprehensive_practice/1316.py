N = int(input())

result = 0 

for i in range(N):
    word = input()
    word_list = set()
    cnt_word = ""
    is_group_word = True

    for char in word:
        if char != cnt_word:
            if char in word_list:
                is_group_word = False
                break
            word_list.add(char)
        cnt_word = char
    
    if is_group_word:
        result += 1
        
print(result)

