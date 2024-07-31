from colorama import Fore, init
import time, os, webbrowser, urllib.parse, pyautogui
init(autoreset=True)

def openFileNumber(listNumber):
    lenNumProgress = 0
    realDataNum = []
    print(Fore.CYAN + f"Membuka Path {listNumber}...")
    with open(listNumber, 'r', encoding='utf-8') as f:
        dataNum = f.readlines()
        print("Membaca Nomor...")
        f.close()
    for i in dataNum:
        if i.startswith("+"):
            splitParsingNumber = i.split(',')[0].strip().strip('"').replace("+", "").replace(" ", "").replace("-", "")
            realDataNum.append(splitParsingNumber)
            lenNumProgress+=1
            print(lenNumProgress, realDataNum[len(realDataNum)-1])
        else:
            continue
    print("Selesai!")
    return realDataNum, lenNumProgress==0

def configuration():
    print(Fore.CYAN + "Membaca Files config-wa-sender.txt...")
    with open('config-wa-sender.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.close()
    
    Data = {}
    Pesan = []
    Parsing = True
    pesan_start = False
    
    print("Parsing Data...")
    for line in lines:
        
        if line.startswith("PathFileNumber"):
            path_file_number = line.split('=')[1].strip().strip('"')
            if Parsing:
                path_file_number0 = line.split('=')[0].strip().strip('"')
                Data[path_file_number0] = path_file_number
                
        elif line.startswith("Pesan"):
            pesan_start = True
            continue
            
        elif line.startswith("Jeda_Waktu"):
            jeda_waktu = line.split('=')[1].strip().strip('"')
            if Parsing:
                jeda_waktu0 = line.split('=')[0].strip().strip('"')
                Data[jeda_waktu0] = jeda_waktu
                break
            
        if pesan_start:
            if line.strip() == ")":
                continue
            Pesan.append(line.strip())
            
    print("Parsing Selesai!")
    return Data, Pesan

def pesanFull(pesan_list):
    with open('pesanFull.txt', 'w', encoding='utf-8') as file:
        for i in range(0, len(pesan_list)):
            if (len(pesan_list)-1) == i:
                file.write(pesan_list[i])
            else:
                file.write(pesan_list[i] + "\n")
        file.close()
    with open('pesanFull.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        textparse = urllib.parse.quote_plus(text)
        f.close()
    os.remove("pesanFull.txt")
    return textparse

def main():
    file_config, pesan_list = configuration()
    numberParsingConfig, Jeda_Waktu = file_config.get('PathFileNumber', 'Kosong'), file_config.get('Jeda_Waktu', 'Kosong')
    listNumber, lengthNumber = openFileNumber(numberParsingConfig)
    Jeda_Waktu = int(Jeda_Waktu) - 9
    if Jeda_Waktu < 5:
        print(Fore.LIGHTBLUE_EX + "Jeda Waktu Dibawah Batas Min.14 Detik, Otomatis Diubah Default Menjadi 14 Detik")
        Jeda_Waktu = 14 - 9
    Pesan = pesanFull(pesan_list)

    webbrowser.open("https://drive.google.com/file/d/1AODLFDje6OAg_D9J8eWhxhdO-nAkJSWj/view?usp=drivesdk", new=0, autoraise= False)
    print(Fore.LIGHTRED_EX + "Jika Sudah Masuk Ke Halaman Browser, Tekan ENTER")
    input()

    for i in listNumber:
        lengthNumber += 1
        print(Fore.CYAN + f"Mengirim Pesan Ke {i}|({lengthNumber}/{len(listNumber)})")    
        webbrowser.open("https://wa.me/" + i + "?text=" + Pesan, new=0, autoraise= False)
        time.sleep(5)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(1)
        webbrowser.open("https://wa.me/" + i + "?text=" + Pesan, new=0, autoraise= False)
        time.sleep(Jeda_Waktu-1)
        pyautogui.press('enter')
        print("Berhasil Mengirim!")
        time.sleep(1)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')
        print("Jeda Waktu...")
        time.sleep(1)
    print(Fore.LIGHTRED_EX + "Program Selesai!")
    
if __name__ == "__main__":
    main()