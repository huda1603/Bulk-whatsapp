from colorama import Fore, init
import time, os, webbrowser, urllib.parse, pyautogui, platform
init(autoreset=True)

def userPlatform():
    platforms = platform.system()
    if platforms == "Windows" or platforms == "Linux":
        shortcut = ["ctrl", "alt"]
    elif platforms == "Darwin":
        shortcut = ["cmd", "cmd"]
    else:
        print(Fore.LIGHTBLUE_EX + "Program Hanya dapat dijalankan di platform Windows, Linux dan MacOS")
        exit()
    return shortcut    

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

def onceSender(Jeda_Waktu, oneAuthenticationP):
    if oneAuthenticationP.upper() == "YA":
        JedaChangeTab = 2
        JedaAfterOpenWA = int(Jeda_Waktu / JedaChangeTab)
        JedaAfterENTER = Jeda_Waktu - (JedaAfterOpenWA + (JedaChangeTab**2))
        return JedaChangeTab, JedaAfterOpenWA, JedaAfterENTER
    else:
        JedaChangeTab = 1
        JedaAfterOpenWA = 5
        return JedaChangeTab, JedaAfterOpenWA

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

        elif line.startswith("One_Sender"):
            oneAuthentication = line.split('=')[1].strip().strip('"')
            if Parsing:
                oneAuthentication0 = line.split('=')[0].strip().strip('"')
                Data[oneAuthentication0] = oneAuthentication
                break
            
        if pesan_start:
            if line.strip() == '")':
                pesan_start = False
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
    platforms = userPlatform()
    file_config, pesan_list = configuration()
    numberParsingConfig, Jeda_Waktu, oneAuthenticationP = file_config.get('PathFileNumber', 'Kosong'), file_config.get('Jeda_Waktu', 'Kosong'), file_config.get('One_Sender', 'Kosong')
    listNumber, lengthNumber = openFileNumber(numberParsingConfig)
    Jeda_Waktu = int(Jeda_Waktu)
    if oneAuthenticationP.upper() == "YA":
        JedaChangeTab, JedaAfterOpenWA, JedaAfterENTER = onceSender(Jeda_Waktu, oneAuthenticationP)
    else:
        JedaChangeTab, JedaAfterOpenWA = onceSender(Jeda_Waktu, oneAuthenticationP)
    if Jeda_Waktu < 15:
        print(Fore.LIGHTBLUE_EX + "Jeda Waktu Dibawah Batas Min.15 Detik, Otomatis Diubah Default Menjadi 15 Detik")
        Jeda_Waktu = 15 - 9    
    Pesan = pesanFull(pesan_list)

    webbrowser.open("https://drive.google.com/file/d/1AODLFDje6OAg_D9J8eWhxhdO-nAkJSWj/view?usp=drivesdk", new=0, autoraise= False)
    print(Fore.LIGHTRED_EX + "Jika Sudah Masuk Ke Halaman Browser, Tekan ENTER")
    input()

    for i in listNumber:
        lengthNumber += 1
        print(Fore.CYAN + f"Mengirim Pesan Ke {i}|({lengthNumber}/{len(listNumber)})")    
        webbrowser.open("https://wa.me/" + i + "?text=" + Pesan, new=0, autoraise= False)
        time.sleep(JedaAfterOpenWA)
        if oneAuthenticationP.upper() == "YA":
            pyautogui.press('enter')
            print("Berhasil Mengirim!")
            time.sleep(JedaAfterENTER)
            print("Jeda Waktu...")
        pyautogui.hotkey(platforms[1], 'tab')
        time.sleep(JedaChangeTab)
        pyautogui.hotkey(platforms[0], 'w')
        time.sleep(JedaChangeTab)
        if oneAuthenticationP.upper() == "YA":
            if i == listNumber[len(listNumber)-1]:
                break
            continue
        webbrowser.open("https://wa.me/" + i + "?text=" + Pesan, new=0, autoraise= False)
        time.sleep(Jeda_Waktu-1)
        pyautogui.press('enter')
        print("Berhasil Mengirim!")
        time.sleep(1)
        pyautogui.hotkey(platforms[1], 'tab')
        time.sleep(1)
        pyautogui.hotkey(platforms[0], 'w')
        print("Jeda Waktu...")
        time.sleep(1)
    print(Fore.LIGHTRED_EX + "Program Selesai!")
    
if __name__ == "__main__":
    main()
