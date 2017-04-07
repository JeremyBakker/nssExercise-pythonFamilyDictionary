my_family = {
	'brother': {
	'name':'Trevor',
	'age':42
	},
	'mother':{
	'name':'Joan',
	'age':71
	},
	'father':{
	'name':'Jerry',
	'age':71
	}
}

for key, value in my_family.items():
	print(value['name'] + ' is my ' + key + ' and is ' + str(value['age']) + ' years old.')