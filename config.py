"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re
import heroku3
from dotenv import load_dotenv
from helpers.log import LOGGER

load_dotenv()

YSTREAM=False
STREAM=os.environ.get("STARTUP_STREAM", "https://www.youtube.com/live/zw2flSYNebw?feature=share")
regex = r"^(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?"
match = re.match(regex,STREAM)
if match:
    YSTREAM=True
    finalurl=STREAM
    LOGGER.warning("Starting Startup Stream From YouTube!")
else:
    finalurl=STREAM
    LOGGER.warning("Starting Startup Stream From Link!")

class Config:

    # Mendatory Variables

    ADMIN = os.environ.get("AUTH_USERS", "2046359138")
    ADMINS = [int(admin) for admin in (ADMIN).split(2046359138)]
    API_ID = int(os.environ.get("API_ID", "18679215"))
    API_HASH = os.environ.get("API_HASH", "09849f9f1481edfb639ed45b80a01991")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5827200200:AAH5tdYzhD4JIPyce-xtjCf6PuqIvmpb0ZA")     
    SESSION = os.environ.get("SESSION_STRING", "BQEdBa8ARD7SGKdG1BzKHP6pfP-4P6RgwT3gYpywgzElYoAwaODyo-WhqnPWV2UfqVPhSTduZV-RW_DIOTS_FUnyuY5dLBGPePsFuY5l0QAccILiemg8isSVdfei9v_hbmi7HlhFSh-M_vJZh7VBM2fEeFNbE_cE1yr5At3vm_Wg86txyUFVcH7Wtoi3p_FrL8L8qUY_s-S210GUigHh5CYmTSe3YAEHg9_laBT3_DVB8YYM9nZreyHJiSUmtVDfjf002lRN0oeJw03QASaLU29OczAk-o62zPzW8Nj2_OoJFbCXBzVlq6mmRW9GmsykTnyUmTx3hEk7V0XSxU7bL4B0Uw-j_wAAAAB5-PZiAA")
    CHAT_ID = int(os.environ.get("CHAT_ID", "-1001620112060"))

    # Optional Variables

    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001805579621")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    BOT_USERNAME=None
    STREAM_URL=finalurl
    YSTREAM=YSTREAM
    SHUFFLE=bool(os.environ.get("SHUFFLE", True))
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "False")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
        LOGGER.warning("Reply Message Found, Enabled PM Guard ! 🔗 @www_SL_Cricket_com

🔗 @SL_cricket_news

🔥 Join Now 🔥")
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE=os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE=="False":
        EDIT_TITLE=None
        LOGGER.warning("VC Title Editing Turned OFF !")
    IS_NONSTOP_STREAM=os.environ.get("IS_NONSTOP_STREAM", True)
    if IS_NONSTOP_STREAM=="False":
        IS_NONSTOP_STREAM=None
        LOGGER.warning("Nonstop Live Stream Feature Disabled !")
    THUMB_LINK=os.environ.get("THUMB_LINK", "https://telegra.ph/file/8ef4c550bfeb2579b8cd3.jpg")

    # Extra Variables ( For Heroku )

    API_KEY = os.environ.get("HEROKU_API_KEY", None)
    APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    if not API_KEY or \
       not APP_NAME:
       HEROKU_APP=None
    else:
       HEROKU_APP=heroku3.from_key(API_KEY).apps()[APP_NAME]

    # Temp DB Variables ( Don't Touch )

    msg = {}
    playlist=[]
    DUR={}
    DATA={}
    GET_FILE={}
    STREAM_END={}
    FFMPEG_PROCESSES={}
    PAUSE=False
    MUTED=False
    STREAM_LINK=False
    ADMIN_CACHE=False
    CALL_STATUS=False
