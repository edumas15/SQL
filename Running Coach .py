# your fastest mile should be 6.5% faster than your 5k race pace. this python script observes that relationship and suggests workouts

x = input('How many minutes to run 1 mile? ')
y= input('How many minutes to run a 5k? ')
if float(y) / 3.125 > float(x) + float(x) * .065:
    print('Your 5k pace is ' + str(float(y)/3.125) + ' minutes/mile')
    print(str(float(x) + float(x) *.065)+' minutes/mile should be your 5k pace based on mile personal best')
    print('Work on improving aerobic capacity. Incorporate more long, slow runs')
else:
    print('your 5k pace is ' + str(float(y) / 3.125) + " minutes/mile")
    print(str(float(y)/3.125 * .935) + ' minutes should be your mile personal best based on your 5k')
    print('Work on top end speed. Incorporate intervals in your training like 12x400')
