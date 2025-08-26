> [!NOTE]  
> This custom command was made by [AngerRandom](https://github.com/AngerRandom). He also made a draft of the tutorial which I have edited to make it more readable and with visual examples.

# How do I add this?

1. Copy the import in `injection_code.py`. This file will contain everything you will need to add this command.

If you need a reminder on how to import or don't know how, click [here](https://github.com/ContestedWheel/EvalEvalEval-BD/wiki/Adding-custom-commands#importing)

2. Paste the import in `countryball.py`, located in `ballsdex/packages/countryballs`

It should look like this once you have pasted in the import:

<img width="673" height="288" alt="image" src="https://github.com/user-attachments/assets/d6d07983-770d-4b2b-bcab-c58f62ac586d" />

3. Copy the second thing you see after the import, which would be the class variable. Paste it under line 40, it should look like this when you paste it:

> [!NOTE]  
> I have added Before and After pictures for less confusion since some people may already have code in these lines.

Before:

<img width="444" height="67" alt="image" src="https://github.com/user-attachments/assets/abde0c0f-850e-4e95-b81a-adcf3f2ac292" />

After:

<img width="376" height="88" alt="image" src="https://github.com/user-attachments/assets/57333a6a-cf90-4e94-84ad-b39f0ce0aa1e" />

---

4. Copy the third thing that says "main function". Paste this on line 250, it should look like this when you paste it:

Before:

<img width="905" height="627" alt="image" src="https://github.com/user-attachments/assets/79a5da56-6d06-409f-8dee-db1ceabcaa0e" />

After:

<img width="822" height="860" alt="image" src="https://github.com/user-attachments/assets/ac6b3ea4-6790-47b8-9b35-93736a42be4a" />

---

5. Finally, copy the last thing that is in the file, which should be labeled "trigger function". Paste this between lines 273 and 274, it should look like this when you paste it.

Before:

<img width="739" height="260" alt="image" src="https://github.com/user-attachments/assets/3d969bba-929a-4584-8755-eb23bac0721e" />

After:

<img width="738" height="341" alt="image" src="https://github.com/user-attachments/assets/94ff6654-4f5a-43af-8256-16b440548a7e" />

---

6. Save the file, and restart the bot using `docker compose restart`.

7. Copy the eval from `eval.py` and make sure to replace these 3 things:

- `BALL_NAME`: Replace it with the name of the ball you want the bot to catch.

- `INT_SECONDS`: Replace this with how much seconds you want till the bot catches the ball.

- `CHANNEL_ID`: Replace this with the channel ID of your choice.

Once you have done that, run the eval in the server of choice and you should see the bot itself will catch the ball.

If you have any questions or issues with this, feel free to ask to the creator on Discord. (tag is angerrandom)
