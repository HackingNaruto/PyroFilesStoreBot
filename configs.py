# (c) @JAsuran2p0

import os


class Config(object):
	API_ID = 2817222
	API_HASH = "aed9f2af23e0df07d7f34011e8a3c86f"
	BOT_TOKEN = "6554076031:AAGhIAVOkAfLhwwvovRjVlv6_rcs9cAPkMg"
	BOT_USERNAME = "FilesStoresOfficialBot"
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001869909600"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1994781564"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://video:video@rishi.fzpls33.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "TamilLinksOfficial")
	LOG_CHANNEL = -1001707804911
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Render](https://render.com)

🧑🏻‍💻 **Developer:** @TamilLinksOfficial

👥 **Support Group:** [Channel TLO](https://t.me/TamilLinksOfficial)

📢 **Updates Channel:** [TamilLinksOfficial](https://t.me/TamilLinksOfficial)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @TamilLinksOfficial

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://t.me/TamilDonationBot) (Donation Bot)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.# (c) @TamilLinksOfficial 

import os

class Config(object):

	API_ID = 2817222

	API_HASH = "aed9f2af23e0df07d7f34011e8a3c86f"

	BOT_TOKEN = "6064443781:AAF2bSDg_XEperrhs5SUEQZDcrXf8V2uAIc"

	BOT_USERNAME = "FilesStoreOfficialBot"

	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001707804911"))

	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1994781564"))

	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://video:video@rishi.fzpls33.mongodb.net/?retryWrites=true&w=majority")

	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "TamilLinksOfficial")

UPDATES_CHANNELL = os.environ.get("UPDATES_CHANNEL", "TamilLinksOfficialTeam")

	LOG_CHANNEL = -1001707804911

	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())

	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))

	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))

	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))

	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))

	ABOUT_BOT_TEXT = f"""

This is Permanent Files Store Bot!

Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Render](https://render.com)

🧑🏻‍💻 **Developer:** @TamilLinksOfficial

👥 **Support Group:** [Channel TLO](https://t.me/TamilLinksOfficial)

📢 **Updates Channel:** [TamilLinksOfficial](https://t.me/TamilLinksOfficial)

"""

	ABOUT_DEV_TEXT = f"""

🧑🏻‍💻 **Developer:** @TamilLinksOfficial

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://t.me/TamilDonationBot) (Donation Bot)

"""

	HOME_TEXT = """

Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.

"""
"""
