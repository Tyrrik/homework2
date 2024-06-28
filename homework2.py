Exercise=int(input())
Time=float(input())
Cours=input()
Time_on_one=str((Exercise/Time)/60)
print("Курс: ",Cours,', '+"Всего задач: ", Exercise, ', ' + "Всего затрачено часов: ", Time, ', '
      + "Среднее время выполнения 1 Задания:", Time_on_one[:5], "часа"+'.')
