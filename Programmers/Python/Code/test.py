def solution(num):
    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(num)))

def solution(s):
    answer = []
    string = sorted(s[2:-2].split('},{'), key=len)
    print(string)
    for st in string:
        for srt_num in st.split(','):
            num = int(srt_num)
            if num not in answer:
                answer.append(num)

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))