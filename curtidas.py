from models import Perfil, Perfil_VIP

usuario = Perfil('Jhon Doe', '11999999999', 'ACME')

usuario.to_string()

usuario.set_like()
usuario.to_string()
usuario.set_like()
usuario.to_string()


usuario_vip = Perfil_VIP('Michael Jackson dos Anjos', '11998765432', 'Star of Pop', 'Mika')

usuario_vip.to_string()
print(usuario_vip.apelido)

usuario_vip.set_like()
usuario_vip.set_like()
usuario_vip.to_string()

print(usuario_vip.get_creditos())
