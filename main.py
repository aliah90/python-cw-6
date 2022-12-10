# write your code here
person = {'name':'aliah' , 'age':'32' ,'hobbies':['music','read','games']}
print(person['name'])
print(person['age'])
person['age']=33
person['country']= 'kuwait'
print(person)
print(len(person))
person['hobbies'].append('dance')

def check_hobbies() :

    if len(person['hobbies']) > 3:
        print("WOW YOU ARE AMAZING") 
check_hobbies()
