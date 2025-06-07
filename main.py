from pypix import Pix

if __name__ == "__main__":
    chave = "CHAVE PIX"
    nome = "NOME"
    cidade = "CIDADE"
    valor = float(input("Digite o valor: "))
    descricao = "DESCRICAO"
    Pix.main(chave, nome, cidade, valor, descricao)
