def set_invite_name(convite):
    p_final = len(convite)
    p_inicial = p_final - 4
    nome_convite = [convite[0:4], convite[p_inicial:p_final]]
    return nome_convite

def send_invite(convites):

    for convite in convites:
        nome_convite = set_invite_name(convite)
        print 'Enviando convite para %s %s' % (nome_convite[0], nome_convite[1])

def main():
    convites = ['Fernando Seguim', 'Gabriela Orselli']
    send_invite(convites)

main()
