import csv
field=['roll.no','name','age']
sdict=[{'roll.no':1,'name':"Archana",'age':22},
        {'roll.no':2,'name':"Anamika",'age':21}]
with open('dept.csv','w')as dfile:
 writer=csv.DictWriter(dfile,filenames=field)
 writer.writeheader()
 writer.writerows(sdict)
