from django.http import HttpResponse
from django.shortcuts import render 
import operator
# import MySQLdb

# db_name = 'Contacts'
# table_name = 'Address'

def home(request):
	# context = {"name": "shashi"}
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')
	
def count(request):
	wordlist = request.GET['fulltext']
	wordlist = wordlist.split()
	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			worddictionary[word] += 1
		else:
			worddictionary[word] = 1

	sort = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)		
	context = {"fulltext": wordlist, "sort": sort}
	return render(request, 'count.html', context)


# class DBConnect:

# 	def __init__(self):
# 		'''
# 		Connect to the Database
# 		'''
# 		self.conn = MySQLdb.connect(host='192.168.33.11', user='root', passwd='data')
# 		self.cursor = self.conn.cursor()
# 		self.cursor.execute('DROP SCHEMA %s' % db_name)	
# 		self.conn.commit()


# 	def create_db(self):
# 		'''
# 		Create a Database and create Cursor object the execute the queries.
# 		'''
# 		self.cursor.execute('CREATE DATABASE %s' % db_name)		
# 		self.cursor.execute('USE %s' % db_name)		

# 	def create_table(self, first_name, last_name, age, location, mobile_number, email):
# 		'''
# 		Create Table 
# 		'''
# 		table = '''create table %s 
# 					(%s char(30) primary key,
# 					 %s char(50), 
# 					 %s int(5), 
# 					 %s char(30), 
# 					 %s VARCHAR(10), 
# 					 %s char(30))
# 				''' % ( table_name, first_name, last_name, age, location, mobile_number, email)   

# 		self.cursor.execute(table)
			
# 	def insert_values(self):	
# 		sql = '''INSERT INTO {}(first_name, 
# 								last_name, 
# 								age, 
# 								location, 
# 								mobile_number, 
# 								email) 
# 				 VALUES(%s, %s, %s, %s, %s, %s)'''.format(table_name)
# 		values = ('Shashidhar', 'Devraj', 29, 'Bangalore', 8951645124, 'shashidhardevraj@gmail.com')
# 		self.cursor.execute(sql, values)
# 		self.cursor.execute('''INSERT %s(first_name, last_name, age, location, mobile_number, email) 
# 							   VALUES ('Manjunath', 'Devraj', 31, 'Blr', 9739831038, 'manjudevraj@gmail.com')''' % table_name)
# 		self.conn.commit()




# db = DBConnect()
# db.create_db()
# db.create_table('first_name','last_name','age', 'location', 'mobile_number', 'email')
# db.insert_values()
# db.update_db()
