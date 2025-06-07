# pypix

**Gerador de código "copia e cola" e QR Code de pagamentos via PIX em Python.**

---

## ✨ O que é isso?

O `pypix` é um módulo simples em Python que gera o código EMV do Pix (aquele "copia e cola" que você usa pra pagar no app do banco) e também o QR Code correspondente.

Ideal pra quem tá fazendo bots, sistemas de venda, automações ou qualquer integração com pagamento via Pix.

---

## 🧠 Como funciona?

Você informa os seguintes dados:
- A **chave Pix**
- O **nome do recebedor**
- A **cidade do recebedor**
- Um **valor opcional**
- E uma **descrição opcional**

O `pypix` gera o payload Pix conforme o padrão oficial do Banco Central do Brasil e exibe um QR Code pronto pra escanear!

---

## 📦 Instalação

Instalando as blibiotecas necessárias:

```bash
pip install qrcode[pil]
```

Depois, clone este repositório:

```bash
git clone https://github.com/zeus123-e/pypix.git
```

---

##👮🏿‍♂️Autor

Alexandre Amaral ==> blackalexandre222@gmail.com
