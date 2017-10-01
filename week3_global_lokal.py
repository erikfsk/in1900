#feil implementering av funksjonen
def gange_med_10(x):
    x_lokal = 2
    return x_lokal*10

gange_med_10(3) #dette burde bli 30, men blir 20

#også feil...
def gange_med_10(x):
    return x_global*10

x_global = 10
gange_med_10(x_global)


#rett implementering
def gange_med_10(x_global):
    x_lokal = x_global #x_lokal eksisterer bare i funksjonen. 
    return x_lokal*10

x_global = 3 #denne eksisterer i hele programmet.
gange_med_10(x_global) #dette blir 30