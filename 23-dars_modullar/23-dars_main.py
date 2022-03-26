# 23.12.2021
# 23-dars:    MODULLAR

# import avto_info_modul

# avto1 = avto_info_modul.avto_info('gm', 'malibu', 'qora', 'avtomat', 2019, 40000)
# avto_info_modul.info_print(avto1)



# import avto_info_modul as aim  # Nodul nomini qisqartirib chaqirish

# avto1 = aim.avto_info('gm', 'malibu', 'qora', 'avtomat', 2019, 40000)
# aim.info_print(avto1)



## Quyidagi usul bilan modul nomini yozib o'tirmasdan, funlsiyaning o'zini chaqirish kifoya

# from avto_info_modul import avto_info, info_print

# avto1 = avto_info('gm', 'malibu', 'qora', 'avtomat', 2019, 40000)
# info_print(avto1)



## Quyidagi usul yordamida chaqirilayotgan funksiyaga yangi nom berish mumkin

# from avto_info_modul import avto_info as ainfo, info_print as iprint

# avto1 = ainfo('gm', 'malibu', 'qora', 'avtomat', 2019, 40000)
# iprint(avto1)



## Quyidagi usul yordamida modul ichidagi barcha funksiyalarni bir vaqtda chaqirish imkoniyati bor

# from avto_info_modul import *         # не рекомендуется

# avto1 = avto_info('gm', 'malibu', 'qora', 'avtomat', 2019, 40000)
# info_print(avto1)



