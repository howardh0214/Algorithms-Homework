case = 1  
while True:
    try:  
        casenumber = input() 
        while casenumber == '':  
            casenumber = input()
        else:  
            casenumber = int(casenumber)  

        cool = 0  

        while casenumber > 0:  
            casenumber -= 1

            string = input()  
            count = set()  
            last_count = 0 

            while len(string) > 0:  

                if string.count(string[0]) == len(string) and len(count) == 0:
                    break  
                count.add(string.count(string[0]))  
                if last_count == len(count):  
                    break
                else:  
                    last_count = len(count)

                string = string.replace(string[0], '')  
            else:  
                cool += 1

        print('Case {}: {}'.format(case,cool)) 
        case += 1

    except:  
        break