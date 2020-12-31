with open('answer.data', 'rb') as a:
         answer = a.read(8192)
         with open('cloud.data', 'ab') as c:
             while answer:
                 c.write(answer)
                 answer = a.read(8192)

