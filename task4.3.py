print('Hello!')
name_city=input('Enter your city: ').lower()

file1=open('google_'+name_city+'.txt','a')
file1.write('New complaint:\n\t'+input('Enter your complaint: ')+'\n\n')

file1.close()
