""" esra sÃ¼mer 22210202044"""

class TelefonUygulamasi:
    def __init__(self):
        self.kontor_miktari = 0
        self.gorusme_suresi = 0

    def ana_menu(self):
        while True:
            print("\nAna MenÃ¼:")
            print("1- KontÃ¶r Al")
            print("2- GÃ¶rÃ¼Åme Yap")
            print("3- Bilgiler")
            print("9- ÃÄ±kÄ±Å")

            secim = input("SeÃ§iminiz: ")

            if secim == "1":
                self.kontor_al()
            elif secim == "2":
                self.gorusme_yap()
            elif secim == "3":
                self.bilgileri_goster()
            elif secim == "9":
                print("ÃÄ±kÄ±Å yaptÄ±nÄ±z.")
                break
            else:
                print("GeÃ§ersiz seÃ§im!")

    def kontor_al(self):
        miktar = int(input("Ne kadar kontÃ¶r alacaksÄ±nÄ±z: "))

        if miktar < 0 or miktar > 120:
            print("0âdan kÃ¼Ã§Ã¼k 120âden bÃ¼yÃ¼k deÄer giremezsiniz.")
        else:
            if self.kontor_miktari + miktar > 120:
                print("Telefona 120 liradan fazla kontÃ¶r alamazsÄ±nÄ±z.")
            else:
                self.kontor_miktari += miktar
                print(f"{miktar} liralÄ±k kontÃ¶r aldÄ±nÄ±z.")

    def gorusme_yap(self):
        sure = int(input("KaÃ§ dakika gÃ¶rÃ¼Åme yapacaksÄ±nÄ±z: "))

        if self.kontor_miktari == 0:
            print("Telefonda yeterli kontÃ¶r olmadÄ±ÄÄ± iÃ§in gÃ¶rÃ¼Åme yapamazsÄ±nÄ±z.")
        else:
            harcanacak_kontor = sure * 0.12
            if harcanacak_kontor > self.kontor_miktari:
                print("Telefonda yeterli kontÃ¶r olmadÄ±ÄÄ± iÃ§in gÃ¶rÃ¼Åme yapamazsÄ±nÄ±z.")
            else:
                self.kontor_miktari -= harcanacak_kontor
                self.gorusme_suresi += sure
                print(f"{sure} dakika gÃ¶rÃ¼Åme yaptÄ±nÄ±z.")

    def bilgileri_goster(self):
        while True:
            print("\nBilgiler:")
            print("1- Kontör Bilgisi")
            print("2- Görüşme Bilgisi")
            print("9- çıkış")

            secim = input("Seçiminiz: ")

            if secim == "1":
                print(f"Telefonda {self.kontor_miktari:.1f} liralık kontör vardÄ±r.")
            elif secim == "2":
                print(f"{self.gorusme_suresi} dakikalÄ±k gÃ¶rÃ¼Åme yaptÄ±nÄ±z.")
            elif secim == "9":
                break
            else:
                print("GeÃ§ersiz seÃ§im!")


if __name__ == "__main__":
    uygulama = TelefonUygulamasi()
    uygulama.ana_menu()
