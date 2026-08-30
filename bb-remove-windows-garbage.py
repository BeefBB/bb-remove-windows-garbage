import sys
import subprocess
import ctypes


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
    ("Microsoft.XboxIdentityProvider", "Xbox 身分識別提供者", "垃圾"),
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


def is_admin() -> bool:
    """
    檢查目前是否系統管理員權限
    """

    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    except Exception:
        return False


def ask_yes_no(name: str, evaluation: str="", default: bool=False) -> bool:
    """
    詢問是否刪除
    """

    evaluation_text = f" ({evaluation})" if evaluation else ""
    default_text = "Y / n" if default else "y / N"

    value = input(
        f"移除: {name}{evaluation_text} ( {default_text} )\n"
        " > "
    ).strip().lower()

    if not value:
        return default

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


if __name__ == "__main__":

    mode = "1"

    if is_admin():

        print()
        print("輸入 (1) 移除套件")
        print("輸入 (2) 為所有使用者移除套件")
        print("輸入 (3) 移除套件, 且從系統預裝套件移除")
        print("輸入 (4) 為所有使用者移除套件, 且從系統預裝套件移除")

        while True:
            mode = input(" > ").strip()
            if mode in {"1", "2", "3", "4"}:
                break

            print("無效的輸入")


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


        print()

        if not ask_yes_no(name, evaluation):
            continue

        if mode in {"1", "3"}:
            powershell_cmd = f"Get-AppxPackage '{package}' | Remove-AppxPackage"

        else:
            powershell_cmd = f"Get-AppxPackage -AllUsers '{package}' | Remove-AppxPackage -AllUsers"

        result = subprocess.run(
            [
                "powershell", "-NoProfile", "-Command",
                powershell_cmd,
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print(f"已移除: {name}")

        else:
            print(f"移除失敗: {name}")
            if result.stderr.strip():
                print(f" > {result.stderr.strip()}")


        if mode in {"3", "4"}:

            powershell_cmd = f"Get-AppxProvisionedPackage -Online | Where-Object {{ $_.DisplayName -eq '{package}' -or $_.PackageName -like '*{package}*' }} | Remove-AppxProvisionedPackage -Online"

            result = subprocess.run(
                [
                    "powershell", "-NoProfile", "-Command",
                    powershell_cmd,
                ],
                capture_output=True,
                text=True,
            )

            if result.returncode == 0:
                print(f"已從預裝清單移除: {name}")

            else:
                print(f"從預裝清單移除失敗: {name}")
                if result.stderr.strip():
                    print(f" > {result.stderr.strip()}")


    print()
    print("結束")
    input("Enter..")


# # 移除
# powershell_cmd = f"Get-AppxPackage '{package}' | Remove-AppxPackage"

# # 為所有使用者移除 (系統管理員)
# powershell_cmd = f"Get-AppxPackage -AllUsers '{package}' | Remove-AppxPackage -AllUsers"

# # 從系統預裝套件清單移除 (系統管理員)
# powershell_cmd = f"Get-AppxProvisionedPackage -Online | Where-Object {{ $_.DisplayName -eq '{package}' }} | Remove-AppxProvisionedPackage -Online"