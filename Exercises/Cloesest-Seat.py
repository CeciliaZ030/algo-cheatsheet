class Solution(object):

    # 我丑陋的代码
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        L = len(seats)

        if L == 2 and seats[0] == 1:
            return 1
        if L == 2 and seats[0] == 0:
            return 1
        
        
        maxx = 0
        mark = -1
        count = 0
        
        leading_zeros = 0
        if seats[0] == 0:
            j = 0
            while(seats[j] == 0):
                j+=1
            leading_zeros = j
        
        tailing_zeros = 0
        if seats[-1] == 0:
            j = L-1
            while(seats[j] == 0):
                j-=1
            tailing_zeros = L-j-1
        
        for i in range(L):
            if seats[i] == 1:
                count = 0
            else:
                count += 1
                if count >= maxx:
                    maxx = count
                    mark = i

        
        if maxx % 2 == 0:
            print('even')
            middle_sec = maxx/2
        else:
            print('odd')
            middle_sec = maxx/2+1
        
        return(max(middle_sec, max(leading_zeros, tailing_zeros)))


    #人家简洁的代码
    def maxDistToClosest2(seats):

        L = len(seats)

        maxx = 0
        mark = -1

        for i in range(L):

            if seats[i] == 0:
                continue
                # continue 就是跳过这一轮的意思

            if mark == -1:
                maxx = i
            else:
                maxx = max(maxx, (i - mark)/ 2)

            mark = i

        return max(maxx, L-1-mark)






