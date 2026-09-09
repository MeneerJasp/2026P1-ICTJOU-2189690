workouts = [] 

  

aantal_workouts = int(input("Hoevaak wil je een workouttype toevoegen? ")) 

  

while len(workouts) < aantal_workouts: 

    workouttype = input("Welk type workout? ") 

    duur = int(input("Hoeveel minuten duurde de workout? ")) 

  

    workout = (workouttype, duur) 

    workouts.append(workout) 

  

for workouttype, duur in workouts: 

    print("type: {} | duur: {} minuten".format(workouttype, duur)) 