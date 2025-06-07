# Definir um dicionário com 3 elementos

def definindo_elemento():
    album = {'Nome':'A Night at the Opera','Artista':'Blind Guardian','Lançamento':2002}
    print(album) 

# Adicionar um elemento (chave/valor)

def adicionando_elemento():
    album = {'Nome':'A Night at the Opera','Artista':'Blind Guardian','Lançamento':2002}
    album['Plataforma'] = 'Spotify'
    print(album)

# Alterar um valor de uma chave especifica 

def alterar_valor():
    album = {'Nome':'A Night at the Opera','Artista':'Blind Guardian','Lançamento':2002}
    album.update({'Plataforma':'Apple Music'})
    print(album)

# Remover um elemento (chave/valor)

def remover_elemento():
    album = {'Nome':'A Night at the Opera','Artista':'Blind Guardian','Lançamento':2002}
    del album['lançamento']
    print(album)

if __name__ == "__main__":
    definindo_elemento()
    adicionando_elemento()
    alterar_valor()
    remover_elemento()