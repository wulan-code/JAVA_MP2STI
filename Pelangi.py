import sys
import time

def jalanin_lirik():
    lirik =[
    # BRIDGE
    ("Kau bagai kapal yang terus melaju",0.08 ),
    ("Di luasnya ombak samudera biru",0.08 ),
    ("Namun sayangnya kau tak pilih aku",0.08 ),
    ("Jadi Pelabuhanmu",0.10 ),

    # CHORUS
    ("Tetaplah engkau di sini",0.09 ),
    ("Jangan datang lalu kau pergi",0.09 ),
    ("Jangan anggap hatiku",0.08 ),
    ("Jadi tempat persinggahanmu",0.08 ),
    ]

    delay = [
        # TEKS, DELAY KARAKTER, DELAY SETELAH BARIS
        (1.0),
        (1.0),
        (1.5),
        (2.0),

        # CHORUS
        (1.0),
        (1.0),
        (1.0),
        (2.0),
    ]
    print("\n== PELANGI - HIVI")
    time.sleep(2)
    for i, (baris_lagu,delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter,end="")
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
        

jalanin_lirik()     
print("// code by KELOMPOK JAVA") 