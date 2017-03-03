from models import Perfil

perfil1 = Perfil('Fernando Seguim', '11982646822', 'Freela')
perfil2 = Perfil('Gabriela Orselli', '11953494000', 'Automatos')
perfil3 = Perfil(telefone='11999999999', nome='Silvia Orselli', empresa='Posto Melhado')


print perfil1.to_string()
print perfil2.to_string()
print perfil3.to_string()

print type(perfil1)
print perfil1.__class__