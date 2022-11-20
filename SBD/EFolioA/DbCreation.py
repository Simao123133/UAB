import sqlite3
con = sqlite3.connect("EfolioA.db")
cur = con.cursor()


""" Create Db """


cur.execute("""CREATE TABLE IF NOT EXISTS Equipa (
            idEquipa integer PRIMARY KEY,
            nome text,
            estádio text
            )""")

cur.execute("""CREATE TABLE IF NOT EXISTS Jogo (
            idJogo integer PRIMARY KEY,
            jornada integer,
            equipaCasa integer,
            equipaFora integer,
            golosCasa integer,
            golosFora integer,
            FOREIGN KEY(equipaCasa) REFERENCES Equipa(idEquipa),
            FOREIGN KEY(equipaFora) REFERENCES Equipa(idEquipa)
            )""")

cur.execute("""CREATE TABLE IF NOT EXISTS Jogador (
            idJogador integer PRIMARY KEY,
            nome text,
            número integer,
            equipa integer,
            posição text,
            FOREIGN KEY(equipa) REFERENCES Equipa(idEquipa)
            )""")

cur.execute("""CREATE TABLE IF NOT EXISTS Jogador_Jogo (
            idJogo integer,
            idJogador integer,
            minutos integer,
            assistências integer,
            golos integer,
            PRIMARY KEY (idJogo, idJogador),
            FOREIGN KEY(idJogo) REFERENCES Jogo(idJogo),
            FOREIGN KEY(idJogador) REFERENCES Jogador(idJogador)
            )""")


""" Equipas """


cur.execute("""INSERT OR IGNORE INTO Equipa 
            (idEquipa, nome, estádio) 
            VALUES 
            (0, 'FCP', 'Dragão')""")

cur.execute("""INSERT OR IGNORE INTO Equipa 
            (idEquipa, nome, estádio) 
            VALUES 
            (1, 'SLB', 'Luz')""")

cur.execute("""INSERT OR IGNORE INTO Equipa 
            (idEquipa, nome, estádio) 
            VALUES 
            (2, 'SCP', 'CampoGrande')""")

cur.execute("""INSERT OR IGNORE INTO Equipa 
            (idEquipa, nome, estádio) 
            VALUES 
            (3, 'SCB', 'Pedreira')""")


""" Jogos """


cur.execute("""INSERT OR IGNORE INTO Jogo 
(idJogo, jornada, equipaCasa, equipaFora, golosCasa, golosFora) 
VALUES 
(1, 1, 0, 1, 5, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogo 
(idJogo, jornada, equipaCasa, equipaFora, golosCasa, golosFora) 
VALUES 
(2, 1, 2, 3, 2, 1)""")

cur.execute("""INSERT OR IGNORE INTO Jogo 
(idJogo, jornada, equipaCasa, equipaFora, golosCasa, golosFora) 
VALUES 
(3, 2, 1, 0, 0, 5)""")

cur.execute("""INSERT OR IGNORE INTO Jogo 
(idJogo, jornada, equipaCasa, equipaFora, golosCasa, golosFora) 
VALUES 
(4, 2, 3, 2, 3, 2)""")

cur.execute("""INSERT OR IGNORE INTO Jogo 
(idJogo, jornada, equipaCasa, equipaFora, golosCasa, golosFora) 
VALUES 
(5, 3, 0, 2, 5, 4)""")

cur.execute("""INSERT OR IGNORE INTO Jogo 
(idJogo, jornada, equipaCasa, equipaFora, golosCasa, golosFora) 
VALUES 
(6, 3, 1, 3, 3, 1)""")

cur.execute("""INSERT OR IGNORE INTO Jogo 
(idJogo, jornada, equipaCasa, equipaFora, golosCasa, golosFora) 
VALUES 
(7, 4, 2, 0, 2, 6)""")

cur.execute("""INSERT OR IGNORE INTO Jogo 
(idJogo, jornada, equipaCasa, equipaFora, golosCasa, golosFora) 
VALUES 
(8, 4, 3, 1, 4, 2)""")

cur.execute("""INSERT OR IGNORE INTO Jogo 
(idJogo, jornada, equipaCasa, equipaFora, golosCasa, golosFora) 
VALUES 
(9, 5, 0, 3, 7, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogo 
(idJogo, jornada, equipaCasa, equipaFora, golosCasa, golosFora) 
VALUES 
(10, 5, 1, 2, 2, 5)""")

cur.execute("""INSERT OR IGNORE INTO Jogo 
(idJogo, jornada, equipaCasa, equipaFora, golosCasa, golosFora) 
VALUES 
(11, 17, 3, 0, 0, 8)""")

cur.execute("""INSERT OR IGNORE INTO Jogo 
(idJogo, jornada, equipaCasa, equipaFora, golosCasa, golosFora) 
VALUES 
(12, 17, 2, 1, 2, 5)""")


""" Jogadores """


""" FCP """
cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(1, 'Abel', 1, 0, 'GuardaRedes')""")

cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(2, 'Bruno', 3, 0, 'Defesa')""")

cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(3, 'Carlos', 8, 0, 'Médio')""")

cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(4, 'Daniel', 9, 0, 'Avançado')""")

""" SLB """
cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(5, 'Edgar', 99, 1, 'GuardaRedes')""")

cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(6, 'Francisco', 4, 1, 'Defesa')""")

cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(7, 'Gabriel', 6, 1, 'Médio')""")

cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(8, 'Hélio', 11, 1, 'Avançado')""")

""" SCP """
cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(9, 'Ígor', 1, 2, 'GuardaRedes')""")

cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(10, 'João', 3, 2, 'Defesa')""")

cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(11, 'Kelvin', 8, 2, 'Médio')""")

cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(12, 'Luís', 9, 2, 'Avançado')""")

""" SCB """
cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(13, 'Manuel', 1, 3, 'GuardaRedes')""")

cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(14, 'Nuno', 3, 3, 'Defesa')""")

cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(15, 'Óscar', 8, 3, 'Médio')""")

cur.execute("""INSERT OR IGNORE INTO Jogador 
(idJogador, nome, número, equipa, posição) 
VALUES 
(16, 'Pedro', 9, 3, 'Avançado')""")


""" Jogador_Jogo """

"""Jogo 1"""

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(1, 1, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(1, 2, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(1, 3, 67, 5, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(1, 4, 90, 0, 5)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(1, 5, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(1, 6, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(1, 7, 85, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(1, 8, 60, 0, 0)""")

"""Jogo 2"""

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(2, 9, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(2, 10, 80, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(2, 11, 90, 1, 1)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(2, 12, 90, 1, 1)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(2, 13, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(2, 14, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(2, 15, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(2, 16, 90, 0, 0)""")

"""Jogo 3"""

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(3, 1, 75, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(3, 2, 90, 2, 3)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(3, 3, 90, 3, 2)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(3, 4, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(3, 5, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(3, 6, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(3, 7, 85, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(3, 8, 60, 0, 0)""")

"""Jogo 4"""

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(4, 9, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(4, 10, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(4, 11, 50, 2, 1)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(4, 12, 70, 1, 2)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(4, 13, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(4, 14, 90, 0, 0)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(4, 15, 80, 0, 2)""")

cur.execute("""INSERT OR IGNORE INTO Jogador_Jogo 
(idJogo, idJogador, minutos, assistências, golos) 
VALUES 
(4, 16, 70, 2, 0)""")


con.commit()
con.close()