from exercicios.models import Perfil, Data

perfil1 = Perfil('Fernando Seguim', '11982646822', 'Freela')
perfil2 = Perfil('Gabriela Orselli', '11953494000', 'Automatos')
perfil3 = Perfil(telefone='11999999999', nome='Silvia Orselli', empresa='Posto Melhado')

outro_perfil = perfil1
outro_perfil.nome = "Fernando H S Seguim"

perfil1.to_string()
perfil2.to_string()
perfil3.to_string()

print type(perfil1)
print perfil1.__class__

outro_perfil.to_string()

data = Data(03,03,2017)
data.format_data("/")
