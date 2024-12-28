"""
Module for dump in json
"""

import json


async def json_dump(name: str, info) ->bool:
    """
    async function for dump json
    :param name:
    :param info:
    :return:
    """
    try:
        with(name, "w") as file:
            json.dump(info, file)
    except Exception as e:
        print(f"[ERROR] Error as json_file with error: {e}")
