import sys
import subprocess
import ctypes
import json
import time


APPS = [

    # (package, name, evaluation)

    # Bing
    ("Microsoft.BingNews", "Microsoft 新聞", "垃圾"),
    ("Microsoft.MSNews", "Microsoft 新聞", "垃圾"),
    ("Microsoft.BingWeather", "Microsoft 天氣", "垃圾"),
    ("Microsoft.BingFinance", "Microsoft 財經", "垃圾"),
    ("Microsoft.BingSports", "Microsoft 運動", "垃圾"),
    ("Microsoft.BingFoodAndDrink", "Microsoft 美食", "垃圾"),
    ("Microsoft.BingTravel", "Microsoft 旅遊", "垃圾"),
    ("Microsoft.BingSearch", "Bing 搜尋", "留著好"),

    # 輔助工具
    ("Microsoft.GetHelp", "取得協助", "垃圾"),
    ("Microsoft.Getstarted", "開始使用", "垃圾"),
    ("Microsoft.WindowsFeedbackHub", "意見反應中樞", "垃圾"),
    ("Microsoft.DevHome", "Dev Home", "用不到"),
    ("Microsoft.Windows.DevHome", "Dev Home", "用不到"),
    ("Microsoft.Widgets", "小工具", "垃圾"),
    ("Microsoft.Copilot", "Copilot", "垃圾"),
    ("Microsoft.Windows.Copilot", "Copilot", "垃圾"),

    # Xbox
    ("Microsoft.Xbox", "Xbox", "留著好"),
    ("Microsoft.XboxApp", "Xbox", "留著好"),
    ("Microsoft.XboxGamingOverlay", "Xbox Game Bar", "留著好"),
    ("Microsoft.XboxGameOverlay", "Xbox 遊戲覆蓋", "留著好"),
    ("Microsoft.XboxIdentityProvider", "Xbox 身分識別提供者", "留著好"),
    ("Microsoft.XboxSpeechToTextOverlay", "Xbox 語音轉文字覆蓋", "垃圾"),
    ("Microsoft.Xbox.TCUI", "Xbox TCUI", "垃圾"),
    ("Microsoft.XboxGameCallableUI", "Xbox 遊戲介面", "留著好"),
    ("Microsoft.GamingApp", "Xbox / Gaming App", "留著好"),

    # 娛樂
    ("Microsoft.ZuneMusic", "媒體播放器", "留著好"),
    ("Microsoft.WindowsMediaPlayer", "媒體播放器", "留著好"),
    ("Microsoft.ZuneVideo", "電影與電視", "留著好"),
    ("Microsoft.MicrosoftSolitaireCollection", "Microsoft 接龍", "垃圾"),

    # 通訊
    ("Microsoft.SkypeApp", "Skype", "垃圾"),
    ("Microsoft.MicrosoftTeams", "Microsoft Teams", "我通常刪掉後自己裝"),
    ("Microsoft.Messaging", "訊息", "垃圾"),
    ("Microsoft.MicrosoftJournal", "Microsoft Journal", "垃圾"),
    ("Microsoft.Windows.Mail", "郵件與行事曆", "垃圾"),

    # Office
    ("Microsoft.MicrosoftOfficeHub", "Microsoft 365 (Office)", "垃圾"),
    ("Microsoft.Office.OneNote", "OneNote", "垃圾"),
    ("Microsoft.Office.Sway", "Sway", "垃圾"),
    ("Microsoft.Office.Lens", "Microsoft Lens", "垃圾"),
    ("Microsoft.OutlookForWindows", "新版 Outlook", "垃圾"),

    # 個人服務
    ("Microsoft.YourPhone", "手機連結", "垃圾"),
    ("Microsoft.CrossDevice", "跨裝置體驗 (Phone Link 延伸)", "垃圾"),
    ("MicrosoftWindows.CrossDevice", "跨裝置體驗 (Phone Link 延伸)", "垃圾"),
    ("Microsoft.Todos", "Microsoft To Do", "垃圾"),
    ("Microsoft.Whiteboard", "Microsoft Whiteboard", "垃圾"),
    ("Microsoft.PowerAutomateDesktop", "Power Automate", "垃圾"),
    ("MicrosoftCorporationII.MicrosoftFamily", "Microsoft Family", "垃圾"),
    ("MicrosoftCorporationII.QuickAssist", "快速協助", "垃圾"),
    ("Microsoft.549981C3F5F10", "Cortana", "垃圾"),

    # 工具
    ("Microsoft.WindowsMaps", "Windows 地圖", "垃圾"),
    ("Microsoft.People", "Microsoft 人脈", "垃圾"),
    ("Microsoft.WindowsAlarms", "鬧鐘與時鐘", "留著好"),
    ("Microsoft.WindowsSoundRecorder", "錄音機", "留著好"),
    ("Microsoft.Windows.SoundRecorder", "錄音機", "留著好"),
    ("Microsoft.WindowsCamera", "相機", "留著好"),
    ("Microsoft.MSPaint", "小畫家", "留著好"),
    ("Microsoft.Paint", "小畫家", "留著好"),
    ("Microsoft.ScreenSketch", "剪取工具", "留著好"),
    ("Microsoft.WindowsSnippingTool", "剪取工具", "留著好"),
    ("Microsoft.Photos", "相片", "留著好"),
    ("Microsoft.Windows.Photos", "相片", "留著好"),
    ("Microsoft.Recall", "Windows Recall", "垃圾"),
    ("Microsoft.MicrosoftStickyNotes", "自黏便箋", "用不到"),
    ("Microsoft.StickyNotes", "自黏便箋", "用不到"),
    ("Clipchamp.Clipchamp", "Clipchamp", "垃圾"),

    # 3D
    ("Microsoft.Microsoft3DViewer", "3D 檢視器", "垃圾"),
    ("Microsoft.Print3D", "3D 列印", "垃圾"),
    ("Microsoft.MSPaint3D", "Paint 3D", "垃圾"),
    ("Microsoft.MixedReality.Portal", "混合實境入口網站", "垃圾"),

    # OneDrive
    ("Microsoft.OneDriveSync", "OneDrive", "垃圾"),

    # 第三方 App
    ("CandyCrushSaga", "Candy Crush Saga", "垃圾"),
    ("King.com.CandyCrushSodaSaga", "Candy Crush Soda", "垃圾"),
    ("SpotifyAB.SpotifyMusic", "Spotify 預裝版", "垃圾"),
    ("SpotifyAB.SpotifyMusic-for-Windows", "Spotify 預裝版", "垃圾"),
    ("Disney.378537B5418F", "Disney+", "垃圾"),
    ("Disney", "Disney+", "垃圾"),
    ("Netflix", "Netflix", "垃圾"),
    ("TikTok", "TikTok", "垃圾"),
    ("LinkedInApp", "LinkedIn", "垃圾"),
    ("PrimeVideo", "Amazon Prime Video", "垃圾"),
    ("Instagram", "Instagram", "垃圾"),
    ("Facebook", "Facebook", "垃圾"),
    ("AdobeSystemsIncorporated.AdobePhotoshopExpress", "Adobe Photoshop Express", "垃圾"),

]


SERVICES = [

    # (service_name, display_name, evaluation)
    # startup_type: Manual / Disabled / Automatic

    ("DiagTrack", "Connected User Experiences and Telemetry (追蹤診斷)", "垃圾"),
    ("sysmain", "SysMain (Superfetch)", "留著好"),
    ("dmwappushservice", "WAP 撥號介面訊息轉接服務 (蒐集數據用)", "垃圾"),
    ("MapsBroker", "Downloaded Maps Manager (地圖服務)", "垃圾"),
    ("XblAuthManager", "Xbox Live 身份驗證服務", "垃圾"),
    ("XblGameSave", "Xbox Live 存檔存儲服務", "垃圾"),
    ("XboxNetApiSvc", "Xbox Live 網路服務", "垃圾"),
    ("RemoteRegistry", "遠端登錄", "用不到"),

    ("WerSvc", "Windows Error Reporting (錯誤報告)", "垃圾"),
    ("PcaSvc", "Program Compatibility Assistant (相容性助理)", "用不到"),
    ("lfsvc", "Geolocation Service (地理位置服務)", "留著好"),
    ("Wisvc", "Windows Insider Service (測試員服務)", "垃圾"),
    ("TouchKeyboardHandwriting", "Touch Keyboard and Handwriting Panel (觸控與手寫面板)", "桌機用不到"),
    ("SSDPSRV", "SSDP Discovery (UPnP 裝置搜尋)", "用不到"),
    ("lmhosts", "TCP/IP NetBIOS Helper (舊版網路名稱解析)", "用不到"),

]


def is_admin() -> bool:
    """
    檢查目前是否系統管理員權限
    """

    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

    except Exception:
        return False


def ask_yes_no(name: str, evaluation: str="", action_text="") -> bool:
    """
    詢問是否刪除
    """

    evaluation_text = f" ({evaluation})" if evaluation else ""

    print()
    value = input(
        f"{action_text}: {name}{evaluation_text} ( y / N )\n"
        " > "
    ).strip().lower()

    return value == "y"


def get_installed_packages() -> set[str]:
    """
    取得所有套件小寫名稱
    """

    result = subprocess.run(
        [
            "powershell",
            "-NoProfile",
            "-Command",
            "Get-AppxPackage | Select-Object -ExpandProperty Name",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return set()

    return {line.strip().lower() for line in result.stdout.splitlines() if line.strip()}


def remove_app(package: str, all_users: bool=False):
    """
    移除套件
    """

    user = " -AllUsers" if all_users else ""

    powershell_cmd = f"Get-AppxPackage{user} '{package}' | Remove-AppxPackage{user}"

    return subprocess.run(
        [
            "powershell", "-NoProfile", "-Command",
            powershell_cmd
        ],
        capture_output=True,
        text=True,
    )


def remove_app_from_pre_installed_packages(package: str):
    """
    從系統預裝套件移除
    """

    powershell_cmd = (
        f"Get-AppxProvisionedPackage -Online | "
        f"Where-Object {{ $_.DisplayName -eq '{package}' -or $_.PackageName -like '*{package}*' }} | "
        "Remove-AppxProvisionedPackage -Online"
    )

    return subprocess.run(
        [
            "powershell", "-NoProfile", "-Command",
            powershell_cmd
        ],
        capture_output=True,
        text=True,
    )


def get_services() -> dict:
    """
    取得所有 Windows 服務資訊

    Return:
        Name: Name, DisplayName, State, StartMode
    """

    powershell_cmd = (
        "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; "
        "Get-CimInstance Win32_Service | Select-Object Name, DisplayName, State, StartMode | ConvertTo-Json -Compress"
    )

    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", powershell_cmd],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    if result.returncode != 0 or not result.stdout.strip():
        return {}

    try:
        data = json.loads(result.stdout)
        # 若系統只有 1 個服務, ConvertTo-Json 會回傳 dict, 需轉為 list
        if isinstance(data, dict):
            data = [data]

        return {d["Name"].lower(): d for d in data if "Name" in d}

    except json.JSONDecodeError:
        return {}


def set_service_startup(service_name: str, startup_type: str):
    """
    修改服務啟動類型 (Manual / Disabled / Automatic)
    """

    powershell_cmd = (
        "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; "
        f"Set-Service -Name '{service_name}' -StartupType {startup_type} -ErrorAction Stop"
    )

    return subprocess.run(
        [
            "powershell", "-NoProfile", "-Command",
            powershell_cmd
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


if __name__ == "__main__":

    mode = "0"

    if is_admin():

        print()
        print("輸入 (1) 移除套件")
        print("輸入 (2) 為所有使用者移除套件")
        print("輸入 (3) 移除套件, 且從系統預裝套件移除")
        print("輸入 (4) 為所有使用者移除套件, 且從系統預裝套件移除")
        print("輸入 (5) 跳至下一步, 取消自動Windows服務")

        while True:
            mode = input(" > ").strip()
            if mode in {"1", "2", "3", "4", "5"}:
                break

            print("無效的輸入")

    else:

        print()
        print("目前非系統管理員權限, 僅可為目前使用者移除套件")
        print("以系統管理員權限以解鎖以下功能:")
        print(" - 為所有使用者移除套件")
        print(" - 從系統預裝套件移除")
        print(" - 取消自動Windows服務")
        print()

        time.sleep(3)


    if mode != "5":

        print("掃描系統已安裝的 Appx 套件...")

        installed_packages = get_installed_packages()

        if not installed_packages:

            print("無法取得已安裝套件清單")
            print("結束")
            sys.exit()

        print(f"掃描完成, 共找到 {len(installed_packages)} 個套件")
        print()


        # 為了把未安裝全放前面
        for package, name, evaluation in APPS:

            if package.lower() not in installed_packages:
                print(f"未安裝: {name}")


        for package, name, evaluation in APPS:

            if package.lower() not in installed_packages:
                continue


            if not ask_yes_no(name, evaluation, "移除"):
                continue


            if mode in {"0", "1", "3"}:
                result = remove_app(package, False)

            else:
                result = remove_app(package, True)


            if result.returncode == 0:
                print(f"已移除: {name}")

            else:
                print(f"移除失敗: {name}")
                if result.stderr.strip():
                    print(f" > {result.stderr.strip()}")


            if mode in {"3", "4"}:

                result = remove_app_from_pre_installed_packages(package)

                if result.returncode == 0:
                    print(f"已從預裝清單移除: {name}")

                else:
                    print(f"從預裝清單移除失敗: {name}")
                    if result.stderr.strip():
                        print(f" > {result.stderr.strip()}")


        print()
        print("刪除階段結束")


    if mode != "0":
        print()
        print("取消自動Windows服務")


        services_now = get_services()


        for service_name, display_name, evaluation in SERVICES:

            if service_name.lower() not in services_now:
                print(f"未發現服務: {display_name}")
                continue

            if services_now[service_name.lower()]["StartMode"] == "Manual":
                print(f"已經為手動: {display_name}")

            if services_now[service_name.lower()]["StartMode"] == "Disabled":
                print(f"已經為停用: {display_name}")


        for service_name, display_name, evaluation in SERVICES:

            if service_name.lower() not in services_now:
                continue


            if services_now[service_name.lower()]["StartMode"] != "Auto":
                continue


            if not ask_yes_no(display_name, evaluation, "設為手動"):
                continue


            result = set_service_startup(service_name, "Manual")


            if result.returncode == 0:
                print(f"已取消自動: {service_name}")

            else:
                print(f"取消自動失敗: {service_name}")
                if result.stderr.strip():
                    print(f" > {result.stderr.strip()}")


    print()
    print("結束")
    input("Enter..")


# 取得所有套件名稱
# powershell_cmd = "Get-AppxPackage | Select-Object -ExpandProperty Name"

# # 移除
# powershell_cmd = f"Get-AppxPackage '{package}' | Remove-AppxPackage"

# # 為所有使用者移除 (系統管理員)
# powershell_cmd = f"Get-AppxPackage -AllUsers '{package}' | Remove-AppxPackage -AllUsers"

# # 從系統預裝套件清單移除 (系統管理員)
# powershell_cmd = f"Get-AppxProvisionedPackage -Online | Where-Object {{ $_.DisplayName -eq '{package}' }} | Remove-AppxProvisionedPackage -Online"

# 取得 Windows 服務資訊
# powershell_cmd = "Get-CimInstance Win32_Service | Select-Object Name, DisplayName, State, StartMode | ConvertTo-Json -Compress"

# 修改服務啟動類型 (Manual / Disabled / Automatic)
# powershell_cmd = f"Set-Service -Name '{service_name}' -StartupType {startup_type} -ErrorAction Stop"