from models import Perfil, Perfil_VIP

path_name = 'files/perfis.csv'

perfis = Perfil.create_profile_from_csv(path_name)

for perfil in perfis:
    perfil.to_string()


path_name = 'files/perfis_vip.csv'

perfis_vip = Perfil_VIP.create_profile_from_csv(path_name)

for perfil_vip in perfis_vip:
    perfil_vip.to_string()