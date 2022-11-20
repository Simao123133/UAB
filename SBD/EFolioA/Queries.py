import sqlite3
con = sqlite3.connect("EfolioA.db")
cur = con.cursor()


cur.execute("""
            SELECT nome
            FROM Equipa, Jogo
            WHERE idEquipa == equipaCasa
                AND (jornada == 1)
                AND (golosCasa > golosFora)
            UNION
            SELECT nome
            FROM Equipa, Jogo
            WHERE idEquipa == equipaCasa
                AND (golosCasa > golosFora)
                AND (jornada == 17)
            """)

print("Union operator", cur.fetchall())


cur.execute("""
            SELECT nome
            FROM Equipa, Jogo
            WHERE idEquipa == equipaCasa
            AND (jornada == 1 OR jornada == 17)
            AND (golosCasa > golosFora)
            """)            

print("Without union operator", cur.fetchall())


cur.execute("""
            SELECT nome, Max(golos)
            FROM Jogador, Jogador_Jogo
            WHERE Jogador.idJogador == Jogador_jogo.idJogador
            GROUP BY nome
            ORDER BY max(golos) DESC
            """)            

print("Max goals of each player", cur.fetchall())


cur.execute("""
            SELECT nome, count(golos)
            FROM Jogador
            LEFT JOIN Jogador_Jogo
            ON Jogador.idJogador == Jogador_Jogo.idJogador 
            AND golos > (SELECT avg(golos)
                         FROM Jogador_Jogo)
            GROUP BY nome
            """)        

print("Number of times that a player scored more goals than the average goals per game", cur.fetchall())
   
cur.execute("""
            UPDATE Jogo
            SET golosCasa = golosFora + 1
            WHERE golosCasa < golosFora 
            AND equipaCasa == (SELECT idEquipa
                               FROM Equipa
                               WHERE nome == "SLB")
            """)        

con.commit()
con.close()