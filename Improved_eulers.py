def f(y,t):
     return -2*y

def eulers(y_in,t_in,t_final,dt):
    y = [y_in]
    t=[t_in]

    i = 0

    while t[i] <= t_final:
        y.append( (f(y[i],t[i]))*dt+y[i] )
        t.append(t[i]+dt)
        i+=1
    return y[-1]


def imp_eulers(y_in,t_in,t_final,dt):
    
  
    y_ie = [y_in]
    t = [t_in]

    i = 0

    while t[i] <= t_final :
        t.append(t[i]+dt)

        y_e = f(y_ie[i],t[i])*dt + y_ie[i] 

        f_pred = (f(y_ie[i],t[i])+f(y_e,t[i+1]))/2


        y_ie.append(f_pred*dt + y_ie[i])

       

        i+=1
    
    return y_ie[-1]



    


print(eulers(1,0,0.3,0.1))

print(imp_eulers(1,0,0.3,0.1))

