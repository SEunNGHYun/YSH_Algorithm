def solution(s):
    num = {"zero" : "0" ,"one" : "1","two" : "2","three" : "3","four" : "4","five" : "5","six" : "6","seven" : "7","eight" : "8","nine" : "9"}
    i = 0
    result = ''
    num_val = num.values()
    while (i < len(s)):
        if (s[i] in num_val):
            result += s[i]
            i += 1
        else:
            if(s[i:i+2] == 'ze'):
                result += '0'
                i += 4
            elif(s[i:i+2] == 'on'):
                result += '1'
                i += 3
            elif(s[i:i+2] == 'tw'):
                result += '2'
                i += 3
            elif(s[i:i+2] == 'th'):
                result += '3'
                i += 5
            elif(s[i:i+2] == 'fo'):
                result += '4'
                i += 4
            elif(s[i:i+2] == 'fi'):
                result += '5'
                i += 4
            elif(s[i:i+2] == 'si'):
                result += '6'
                i += 3
            elif(s[i:i+2] == 'se'):
                result += '7'
                i += 5
            elif(s[i:i+2] == 'ei'):
                result += '8'
                i += 5
            elif(s[i:i+2] == 'ni'):
                result += '9'
                i += 4
    return int(result)
            
            
            
    