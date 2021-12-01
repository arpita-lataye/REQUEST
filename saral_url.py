import requests
import json
import os



saral_url=("http://saral.navgurukul.org/api/courses")  
# response=requests.get(saral_url)

def request(url,f_write):

    response=requests.get(url)
    
    with open(f"{f_write}.json","wb") as file:

        file.write(response.content)

    return response.json()


# def read(file_read):
#     with open ("courses.json","r") as file:
#         data_read=file.read()
#         data_load=json.loads(data_read)
#     return (data_load)
    

#     available_courses=data_load['availableCourses']
#     for i in range(len(available_courses)):
#         course=available_courses[i]
#         course_name=course['name']
#         print(i+1,course_name)


def read_file(f_read):
    with open(f'{f_read}',"r") as file:
        data_read=file.read()
        data_load=json.loads(data_read)
    return (data_load)


courses_id_list=[]
def saral_courses():
    data_load=read_file("courses.json")
    available_courses=data_load['availableCourses']
    for i in range(len(available_courses)):
        courses=available_courses[i]
        course_name=courses['name']
        courses_id=courses['id']
        print(i+1,course_name,":",courses_id)
        courses_id_list.append(courses_id)

# user_input=int(input('which course in you want to Enroll:'))
# select_id=courses_id_list[user_input+1]
# print(select_id)
# print(saral_courses())
def select_course():
    user_input=int(input('which course in you want to Enroll:'))
    select_id=courses_id_list[user_input-1]
    return "the course you have selected {} is the ID {} of the course.".format(user_input,select_id)

if os.path.exists('./courses.json'):
    saral_courses()
    print(select_course())
    # user_input=int(input('which course in you want to Enroll:'))
    # select_id=courses_id_list[user_input+1]
    # print("the course you have selected {} is the ID {} of the course.".format(user_input,select_id))
    # print("yes")
else:
    request(saral_url,"courses")
    saral_courses()
    print(select_course())
    # user_input=int(input('which course in you want to Enroll:'))
    # select_id=courses_id_list[user_input+1]
    # print("the course you have selected {} is the ID {} of the course.".format(user_input,select_id))
    # # print("no")

