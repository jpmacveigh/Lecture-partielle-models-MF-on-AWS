import pandas as pd
import subprocess
import pygrib
class modelsMFonAWS:
  def __init__(self,path):
    self.path=path
    self.path_inv=self.path+".inv"  # le path du fichier qui décrit le découpage du grib2 en morceaux
    inv= pd.read_csv(self.path_inv,delimiter=":",header=None,names=["num","octet","date","param","niv","ech"])
    print (inv)
    self.nb_grib=inv.shape[0]
    tab=[inv["num"][i] for i in range(1,len(inv["num"])+1)]
    self.liste_des_chargements=[(tab[i],tab[i+1]-1) for i in range(0,len(tab)-1)]
    self.liste_des_chargements.append((tab[-1],-1))
    assert inv.shape[0]==len (self.liste_des_chargements)
    print (self.path)
    print (self.path_inv)
    print (self.liste_des_chargements)
    self.inventaire=inv
    print (self.inventaire)
  def lire_grib_partiel(self,num):
    def lecture_partielle_grib (path,fic_sortie,ndeb,nfin):
      if nfin == -1:
        commande=f"curl -r {ndeb}-  -o {fic_sortie} {path}"
      else:
        commande=f"curl -r {ndeb}-{nfin} -o {fic_sortie} {path}"
      print (commande)
      subprocess.call(commande, shell=True)
      #!$commande  # lecture partielle du fichier grib2
      return
    file="grib_partiel.grib2"
    lecture_partielle_grib(self.path,file,self.liste_des_chargements[num-1][0],self.liste_des_chargements[num-1][1])
    rep=pygrib.open(file)  # analyse du fichier partiel téléchargé
    for grb in rep:
      print(grb)
    return rep