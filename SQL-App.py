import mysql.connector as msc

prim_key=['n']
data_type_dict={'int':'int(15)','var':'varchar(30)','flp':'float(14,2)','date':'date'}


def connect():

	host_name=input('Enter Hostname*:')
	if host_name=='-/exit':return 0

	user_name=input('Enter Username*:')
	if user_name=='-/exit':return 0

	password=input('Enter Password*:')
	if password=='-/exit':return 0

	data_name=input('Enter database name*:')
	if data_name=='-/exit':return 0

	factor=0

	try:connection_object=msc.connect(host=host_name,user=user_name,passwd=password,database=data_name);factor=1
	except msc.errors.ProgrammingError:factor=-1;print('ERROR due to wrong data.')

	if factor==-1:print('Please fill correct data.To exit type "-/exit" instead of data.');return connect()
	else:print('Connection Successful ☻');return connection_object


def Display_Table(table):
	describe_table = 'describe ' + table
	du.execute(describe_table)
	a = du.fetchall()
	d = {}

	for i in a:
		if i[3]=='PRI':d[i[0]+'*']=i[1][0:3]
		else:d[i[0]]=i[1][0:3]

	display_table = 'select * from ' + table
	keys = tuple(d.keys())
	du.execute(display_table)
	records = du.fetchall() + [keys]

	ll = []
	for i in range(len(d)):
		length = max(list(len(str(j[i])) for j in records))
		ll.append(length)

	for i in range(len(keys)):print('||', ' ' * (ll[i] - len(keys[i])) + keys[i], end=' ')
	print('||')

	for i in records[:-1]:
		for j in range(len(i)): print('||', ' ' * (ll[j] - len(str(i[j]))) + str(i[j]), end=' ')
		print('||')


def field_input(key_list=prim_key):
	field_name,type=input('Enter field name:').split()
	if key_list==['n']:key=input('key(y/n):')
	x=''
	if ' 'in field_name:print('Rewrite field name replacing space with underscores(_)');return field_input()
	if type not in list(data_type_dict.keys()):print('Write symbol of data type as given in INSTRUCTIONS FOR TABLE CREATION .');return field_input()
	else:
		if key.lower() == 'y': key_list = ['y'];x='primary key'
		else:x=''
		return field_name,type,x


print('* necessary fields.')

dbu=connect()
if dbu==0:print('Exiting...');exit()

du=dbu.cursor()

# menus
menu='''░░░░░░░░
░ MENU ░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░ 1     -> Show Tables.        ░░
░░ 2     -> Create a Table.     ░░
░░ 3     -> Manipulate a Table. ░░
░░ 4     -> Delete a Table.     ░░
░░ 6     -> Exit.               ░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''

table_creation_instructions='''
* INSTRUCTIONS FOR TABLE CREATION *
One field must have a unique value for each record.Such a field is called primary key.
type y to make a desired field primary key.One table can have only 1 primary key.
type n to not to make it a primary key.
eg->Adm_no.,employee_id etc
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░ Each field of a table takes input of a specific type of data type.                                                                               ░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░ DataTypes     Symbol       Use                                                                                                                   ░░
░░ integer        int         data can only be a integer.eg->age,class                                                                              ░░
░░ varchar        var         data may contain anything letters,symbols(all symbols on the keyboard) and/or numbers.eg->name,Blood Grp,Admission No ░░
░░ decimal        flp         data can be decimal (floating point) numbers.eg->speed,salary                                                         ░░
░░ date           date        data should be date in yyyy-mm-dd format.eg->Date_Of_Birth                                                            ░░
░░                                                                                                                                                  ░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
While providing field name write its datatype symbol after a space.
eg.->Name var
eg.->Age int
eg.->dob date
eg.->salary flp
for primary key fields
eg->
adm_no. int  ---->giving the field name and type input separated ny a space
y            ---->typing y to make it primary key

emp_id var
y
*NOTE:field names must not contain black space character.Use underscore(_) instead of blank space
		eg.:   date of birth->date_of_birth
*NOTE:program will crash if you try to make 2 primary keys
'''

print(menu)

while 1:
	print('\n\n')
	print('░░░░░░░░░░░░░░░░░░░░░░░')
	print('░░ 5 -> Display menu ░░')
	print('░░░░░░░░░░░░░░░░░░░░░░░')
	prim_key=['n']
	choice=input('Enter choice (1-6):')

	if int(choice)==1:
		du.execute('show tables')
		tables=du.fetchall()
		print('List of all tables present in current database:')
		for i in tables:print(*i)
		print()
		print('TO Manipulate a table and to view its contents select 3 in the upcoming choice.')

	elif int(choice)==2:
		table=input('table name:')
		print(table_creation_instructions)
		field_list=[]
		for i in range(int(input('enter number of field for this table:'))):
			field_name,type,primary_key=field_input()
			a=field_name+' '+data_type_dict[type]+' '+primary_key
			field_list.append(a)
		create_table='create table'+table+' ('
		for i in field_list[0:-1]:create_table+=i+','
		create_table+=field_list[-1]+')'
		try:du.execute(create_table);dbu.commit();print('table created successfully...')
		except msc.errors.ProgrammingError:print('table already exists...\n\n');print(table);Display_Table(table)

	elif int(choice)==3:
		table=input('Enter table name:')
		print(table)
		Display_Table(table)

	elif int(choice)==4:
		table=input('Enter the table name you want to delete:')
		drop_table='drop table '+table
		confirm=input('Are you sure you want to delete '+table+' (y/n)')
		if confirm.lower()=='y':
			du.execute(drop_table)
			dbu.commit()
			print(table,'deleted successfully...')
		else:print('please try again if you want to delete '+table+'.')

	elif int(choice)==5:print(menu)

	elif int(choice)==6:print('Thanks for using this utility.');print('Exiting...');quit();break
