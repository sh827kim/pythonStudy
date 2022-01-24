#### pickle ####

import pickle

# profile_file = open("profile.pickle", "wb")
# profile = {"Name":"Spark", "Age":30, "For fun":["Sing", "Watch Youtube", "Coding"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

## with 를 사용하면 cloas 처리가 필요없음.
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file: 
    study_file.write("I study hard Python")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


#### Quiz ####

for index in range(1, 51) :
    file_name = "week_"+ str(index) + ".txt"
    with open(file_name, "w", encoding="utf8") as report_file:
        report_file.write("- week {0} report -\n".format(index))
        report_file.write("team : \n")
        report_file.write("name : \n")
        report_file.write("summary : ")
