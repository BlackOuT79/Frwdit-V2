#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging
    
    API_ID = 15252966
    API_HASH = "89822193d394af2f140022f7edbac6f7"
    BOT_TOKEN = "5537023010:AAEsdyac_7F6zsj3oHFGuB47D5y-H5LGGNk"
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = "BlackOuT"
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "video")
    OWNER_ID = 1925020999
    SESSION = "BQCA1vEQ09_ANM_6wbpmuWHu3k7ePNOrtvG2vDrhMwx741wUGpoHUX358M6WwALeTNjC4xfaFPpgi8coMcb4XgrO_tnoUUQr7cajzqLBtQUmX0vncu8lfc_-0hQeFNxWtITrOcKCsm-S532EM34vC4TmQ9_Hkn3kvU4FjbaWGoQiHLSAhqh8je3pl0I7sxKlVPt8naU6rK4mFwPvLGj9hK1FnS9wua1UJrSoc2w1C_Z4Px4c4jd0xg3hNag3ablZpzJs6fWFVLe8x9OlZPWmuBR3hvZuPWVzt4JuoS8WPP7qcUVmZo2Ob8WitnKc9qZ2P86-ZBGdQyKENdCbSkxuEyIzcr19RwA"

class Config:
    
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", 12345)
    SESSION = os.environ.get("SESSION")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
