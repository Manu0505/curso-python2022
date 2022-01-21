#1 - Crie um programa que receba o dia, mês e ano de 
# nascimento de uma pessoa. Use a biblioteca datatime 
# pra verificar o dia da semana que a pessoa nasceu. 
import locale
locale.setlocale(locale.LC_ALL, "pt_br")
import datetime


ano_nasc = int(input('digite em qual ano você nasceu:  \n'))
mes_nasc = int(input('digite em qual mês você nasceu:  \n'))
dia_nasc = int(input('digite em qual dia você nasceu:  \n'))
data_setada = datetime.datetime (ano_nasc, mes_nasc, dia_nasc)


print(data_setada.strftime(" %A -  %d - %B - %Y"))

