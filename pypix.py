import qrcode

class Pix:
    @staticmethod
    def format_field(id, value): # FORMATAR CAMPOS
        length = str(len(value)).zfill(2)
        return f"{id}{length}{value}"
    
    @staticmethod
    def gerar_pix(chave_pix, nome_recebedor, cidade_recebedor, valor=0.0, descricao=""): # PAYLOAD PIX
        nome_recebedor = nome_recebedor.upper()
        cidade_recebedor = cidade_recebedor.upper()

        payload = ""

        payload += Pix.format_field("00", "01")
        payload += Pix.format_field("26",
            Pix.format_field("00", "BR.GOV.BCB.PIX") +
            Pix.format_field("01", chave_pix) +
            (Pix.format_field("02", descricao) if descricao else "")
        )
        payload += Pix.format_field("52", "0000")
        payload += Pix.format_field("53", "986")
        if valor > 0:
            payload += Pix.format_field("54", f"{valor:.2f}")
        payload += Pix.format_field("58", "BR")
        payload += Pix.format_field("59", nome_recebedor[:25])
        payload += Pix.format_field("60", cidade_recebedor[:15])
        payload += Pix.format_field("62", Pix.format_field("05", "***"))

        payload_com_crc = payload + "6304"
        crc = Pix.crc16(payload_com_crc.encode("utf-8"))
        payload += "6304" + crc

        return payload

    @staticmethod
    def crc16(data: bytes) -> str: # CALCULAR CRC
        crc = 0xFFFF
        polinomio = 0x1021
        for byte in data:
            crc ^= byte << 8
            for _ in range(8):
                if (crc & 0x8000):
                    crc = (crc << 1) ^ polinomio
                else:
                    crc <<= 1
                crc &= 0xFFFF
        return format(crc, '04X')

    @staticmethod
    def gerar_qrcode(codigo): # GERAR QR CODE
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
        qr.add_data(codigo)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.show()
    
    @staticmethod
    def main(chave, nome, cidade, valor, descricao): # MAIN
        codigo = Pix.gerar_pix(chave, nome, cidade, valor, descricao)
        print("Código Pix: ")
        print(codigo)
        Pix.gerar_qrcode(codigo)
