#import os
#os.system("pip3 uninstall numpy")  # remove previously installed version
#os.system("pip3 install numpy")
from modelsMFonAWS import modelsMFonAWS
path="https://mf-nwp-models.s3.amazonaws.com/arome-france/v1/2022-02-08/12/HP1/00H06H.grib2"
print(path)
fic=modelsMFonAWS(path)
#fic.make_inventaire()
#print(fic.nb_grib)
#rep= fic.lire_grib_partiel(random.randint(1,fic.nb_grib))
rep= fic.lire_grib_partiel(1)