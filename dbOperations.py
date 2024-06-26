import psycopg2
class DbOperations:
    def __init__(self):
        pass
    def createTable():
        f"""
        CREATE TABLE IF NOT EXISTS android_authencity_cleaned_data(
         'App TEXT',
         'Package TEXT',
         'Category TEXT',
         'Rating DECIMAL(2,1)',
         'Number of ratings NUMBER(12,0)',
         'Price DECIMAL(8,2)',
         'Dangerous permissions count INT',
         'Default : Access DRM content. (S) INT',
         'Default : Access Email provider data (S) INT',
         'Default : Access download manager. (S) INT',
         'Default : Advanced download manager functions. (S) INT',
         'Default : Audio File Access (S) INT',
         'Default : Install DRM content. (S) INT',
         'Default : Modify Google settings (S) INT',
         'Default : Move application resources (S) INT',
         'Default : Read Google settings (S) INT',
         'Default : Send download notifications. (S) INT',
         'Default : Voice Search Shortcuts (S) INT',
         'Default : access SurfaceFlinger (S) INT',
         'Default : access checkin properties (S) INT',
         'Default : access the cache filesystem (S) INT',
         'Default : bind to a wallpaper (S) INT',
         'Default : bind to an input method (S) INT',
         'Default : change screen orientation (S) INT',
         'Default : control location update notifications (S) INT',
         'Default : control system backup and restore (S) INT',
         'Default : delete applications (S) INT',
         "Default : delete other applications' caches (S) INT",
         "Default : delete other applications' data (S) INT",
         'Default : directly call any phone numbers (S) INT',
         'Default : directly install applications (S) INT',
         'Default : disable or modify status bar (S) INT',
         'Default : display unauthorized windows (S) INT',
         'Default : enable or disable application components (S) INT',
         'Default : force application to close (S) INT',
         'Default : force device reboot (S) INT',
         'Default : interact with a device admin (S) INT',
         'Default : manage application tokens (S) INT',
         'Default : modify battery statistics (S) INT',
         'Default : modify secure system settings (S) INT',
         'Default : modify the Google services map (S) INT',
         'Default : monitor and control all application launching (S) INT',
         'Default : partial shutdown (S) INT',
         'Default : permission to install a location provider (S) INT',
         'Default : power device on or off (S) INT',
         'Default : press keys and control buttons (S) INT',
         'Default : prevent app switches (S) INT',
         'Default : read frame buffer (S) INT',
         'Default : read phone state and identity (S) INT',
         'Default : record what you type and actions you take (S) INT',
         'Default : set time (S) INT',
         'Default : update component usage statistics (S) INT',
         'Development tools : enable application debugging (D) INT',
         'Development tools : limit number of running processes (D) INT',
         'Development tools : make all background applications close (D) INT',
         'Development tools : send Linux signals to applications (D) INT',
         'Hardware controls : change your audio settings (D) INT',
         'Hardware controls : control flashlight (S) INT',
         'Hardware controls : control vibrator (S) INT',
         'Hardware controls : record audio (D) INT',
         'Hardware controls : take pictures and videos (D) INT',
         'Hardware controls : test hardware (S) INT',
         'Network communication : Broadcast data messages to applications. (S) INT',
         'Network communication : control Near Field Communication (D) INT',
         'Network communication : create Bluetooth connections (D) INT',
         'Network communication : full Internet access (D) INT',
         'Network communication : make/receive Internet calls (D) INT',
         'Network communication : receive data from Internet (S) INT',
         'Network communication : view Wi-Fi state (S) INT',
         'Network communication : view network state (S) INT',
         'Phone calls : intercept outgoing calls (D) INT',
         'Phone calls : modify phone state (S) INT',
         'Phone calls : read phone state and identity (D) INT',
         'Services that cost you money : directly call phone numbers (D) INT',
         'Services that cost you money : send SMS messages (D) INT',
         'Storage : modify/delete USB storage contents modify/delete SD card contents (D) INT',
         'System tools : allow Wi-Fi Multicast reception (D) INT',
         'System tools : automatically start at boot (S) INT',
         'System tools : bluetooth administration (D) INT',
         'System tools : change Wi-Fi state (D) INT',
         'System tools : change network connectivity (D) INT',
         'System tools : change your UI settings (D) INT',
         'System tools : delete all application cache data (D) INT',
         'System tools : disable keylock (D) INT',
         'System tools : display system-level alerts (D) INT',
         'System tools : expand/collapse status bar (S) INT',
         'System tools : force stop other applications (S) INT',
         'System tools : format external storage (D) INT',
         'System tools : kill background processes (S) INT',
         'System tools : make application always run (D) INT',
         'System tools : measure application storage space (S) INT',
         'System tools : modify global animation speed (D) INT',
         'System tools : modify global system settings (D) INT',
         'System tools : mount and unmount filesystems (D) INT',
         'System tools : prevent device from sleeping (D) INT',
         'System tools : read subscribed feeds (S) INT',
         'System tools : read sync settings (S) INT',
         'System tools : read sync statistics (S) INT',
         'System tools : read/write to resources owned by diag (S) INT',
         'System tools : reorder running applications (D) INT',
         'System tools : retrieve running applications (D) INT',
         'System tools : send package removed broadcast (S) INT',
         'System tools : send sticky broadcast (S) INT',
         'System tools : set preferred applications (S) INT',
         'System tools : set time zone (D) INT',
         'System tools : set wallpaper (S) INT',
         'System tools : set wallpaper size hints (S) INT',
         'System tools : write Access Point Name settings (D) INT',
         'System tools : write subscribed feeds (D) INT',
         'System tools : write sync settings (D) INT',
         'Your accounts : Google App Engine (D) INT',
         'Your accounts : Google Docs (D) INT',
         'Your accounts : Google Finance (D) INT',
         'Your accounts : Google Maps (D) INT',
         'Your accounts : Google Spreadsheets (D) INT',
         'Your accounts : Google Voice (D) INT',
         'Your accounts : Google mail (D) INT',
         'Your accounts : Picasa Web Albums (D) INT',
         'Your accounts : YouTube (D) INT',
         'Your accounts : YouTube usernames (D) INT',
         'Your accounts : access all Google services (S) INT',
         'Your accounts : access other Google services (D) INT',
         'Your accounts : act as an account authenticator (D) INT',
         'Your accounts : act as the AccountManagerService (S) INT',
         'Your accounts : contacts data in Google accounts (D) INT',
         'Your accounts : discover known accounts (S) INT',
         'Your accounts : manage the accounts list (D) INT',
         'Your accounts : read Google service configuration (S) INT',
         'Your accounts : use the authentication credentials of an account (D) INT',
         'Your accounts : view configured accounts (S) INT',
         'Your location : access extra location provider commands (S) INT',
         'Your location : coarse (network-based) location (D) INT',
         'Your location : fine (GPS) location (D) INT',
         'Your location : mock location sources for testing (D) INT',
         'Your messages : Read Email attachments (D) INT',
         'Your messages : Send Gmail (S) INT',
         'Your messages : edit SMS or MMS (D) INT',
         'Your messages : modify Gmail (D) INT',
         'Your messages : read Gmail (D) INT',
         'Your messages : read SMS or MMS (D) INT',
         'Your messages : read instant messages (D) INT',
         'Your messages : receive MMS (D) INT',
         'Your messages : receive SMS (D) INT',
         'Your messages : receive WAP (D) INT',
         'Your messages : send SMS-received broadcast (S) INT',
         'Your messages : send WAP-PUSH-received broadcast (S) INT',
         'Your personal information : add or modify calendar events and send email to guests (D) INT',
         'Your personal information : choose widgets (S) INT',
         "Your personal information : read Browser's history and bookmarks (D) INT",
         'Your personal information : read calendar events (D) INT',
         'Your personal information : read contact data (D) INT',
         'Your personal information : read sensitive log data (D) INT',
         'Your personal information : read user defined dictionary (D) INT',
         'Your personal information : retrieve system internal state (S) INT',
         'Your personal information : set alarm in alarm clock (S) INT',
         "Your personal information : write Browser's history and bookmarks (D) INT",
         'Your personal information : write contact data (D) INT',
         'Your personal information : write to user defined dictionary (S) INT',
         'Class INT'
         )""".replace('\n','')