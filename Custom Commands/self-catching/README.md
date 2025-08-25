To add this injection code, follow the steps:
1. Open the `countryball.py` file (`ballsdex/packages/countryballs/countryball.py`)
2. Copy the codes individually from `injection_code.py` and paste them to the defined lines in `countryball.py`:
 * `asyncio` import to the imports 
 * Class variable to under line 40 (super init)
 * Main function to `spawn` function (between line 236-260)
 * Trigger function between line 273-274
3. Save the file and restart the bot.
4. Copy the eval from `eval.py` and run it with your bot's prefix. (replace `BALL_NAME`, `INT_SECONDS` and `CHANNEL_ID`)

There you go! After seconds you defined in INT_SECONDS, bot itself will catch that ball! If you have any questions, feel free to ask to the creator in Discord! (angerrandom)
