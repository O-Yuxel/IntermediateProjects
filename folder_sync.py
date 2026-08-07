from pathlib import Path
import shutil

def target_dirs():
    while True:
        source = Path(input("Kaynak klasörün yolunu gir"))
        if not source.is_dir():
            answer = input("Geçerli bir klasör bulunmamaktadır. Yeniden deneyin. Çıkmak için (q) basın.")
            if answer.lower() == "q":
                break
            else:
                pass
        else:
            backup = Path(input("Hedef klasörün yolunu gir"))
            if not backup.is_dir():
                answer = input("Geçerli bir klasör bulunmamaktadır. Yeniden deneyin. Çıkmak için (q) basın.")
                if answer.lower() == "q":
                    break
                else:
                    pass
            else:
                return True, source,backup

    
def compare(source, backup):
    n = 0
    source_files = []
    backup_files = []
    source_dont_have = []
    backup_dont_have = []

    for i in Path.iterdir(source):
        source_files.append(i)
    for i in Path.iterdir(backup):
        backup_files.append(i)

    sorted_source_files = sorted(source_files)
    sorted_backup_files = sorted(backup_files)

    while n < len(source_files):
        k = 0
        number = 0
        while k < len(backup_files):
            if sorted_source_files[n].name != sorted_backup_files[k].name:
                number += 1
            k += 1
        if number == len(backup_files):
            backup_dont_have.append(sorted_source_files[n])
            n += 1
        else:
            n += 1

    print("Kaynak'ta olup Yedek'de olmayan: ", backup_dont_have)
    n = 0

    while n < len(backup_files):
        k = 0
        number = 0
        while k < len(source_files):
            if sorted_backup_files[n].name != sorted_source_files[k].name:
                number += 1
            k += 1
        if number == len(source_files):
            source_dont_have.append(sorted_backup_files[n])
            n += 1
        else:   
            n += 1   

    if len(backup_dont_have) == 0 and len(source_dont_have) == 0:
        print("Dosyalar arasında bir farklılık yoktur.")
        return True, source_dont_have, backup_dont_have

    else:
        print("Yedek'te olup Kaynak'ta olmayan: ", source_dont_have)
        return True, source_dont_have, backup_dont_have

def synchronize(source, source_dont_have, backup, backup_dont_have):
    if len(backup_dont_have) == 0 and len(source_dont_have) == 0:
        print("Dosyalar arasında bir farklılık yoktur.")

    else:
        if len(backup_dont_have) > 0:
            answer = input(f"Kaynakta olup yedekte olmayan {len(backup_dont_have)} adet dosya saptandı. Yedeğe aktarmak istermisiniz? (e/h)")
            if answer.lower() == "e":
                for i in backup_dont_have:
                    shutil.copy2(i, backup)
            else:
                return
        if len(source_dont_have) > 0:
            answer = input(f"Yedekte olup kaynakta olmayan {len(source_dont_have)} adet dosya saptandı. Kaynağa aktarmak istermisiniz? (e/h)")
            if answer.lower() == "e":
                for i in source_dont_have:
                    shutil.copy2(i, source)
            else:
                return      
    

def menu():
    can_press_2 = False
    can_press_3 = False
    while True:
        print("===== Folder Sync =====\n")
        answer = input("1) Yeni klasör seç\n2) Karşılaştır\n3) Senkronize et\n4) Çıkış\nSeçiminiz: ")

        if answer == "1":
            can_press_2, source, backup = target_dirs()
        elif answer == "2" and can_press_2 == True:
            can_press_3, source_dont_have, backup_dont_have = compare(source, backup)        
        elif answer == "3" and can_press_3 == True:
            synchronize(source, source_dont_have, backup, backup_dont_have)
        elif answer == "4":
            return       
        else:
            print("Geçerli bir numara giriniz veya dosyaları oluşturup karşılaştırınız!")
            pass

menu()