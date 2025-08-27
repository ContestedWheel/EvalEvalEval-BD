> [!NOTE]  
> This custom command was made by [AngerRandom](https://github.com/AngerRandom). He also made a draft of the tutorial which I have edited to make it more readable and with visual examples.

# How do I add this?

1. Copy the import in `injection_code.py`. This file will contain everything you will need to add this command.

If you need a reminder on how to import or don't know how, click [here](https://github.com/ContestedWheel/EvalEvalEval-BD/wiki/Adding-custom-commands#importing)

2. Paste the import in `countryball.py`, located in `ballsdex/packages/countryballs`

It should look like this once you have pasted in the import:

<img width="673" height="288" alt="image" src="https://github.com/user-attachments/assets/d6d07983-770d-4b2b-bcab-c58f62ac586d" />

3. Copy the second thing you see after the import, which would be the class variable. Paste it under line 151, it should look like this when you paste it:

> [!NOTE]  
> I have added Before and After pictures for less confusion since some people may already have code in these lines.

Before:

<img width="460" height="235" alt="image" src="https://github.com/user-attachments/assets/0920b11a-e5a2-4396-90dd-bd68657891a9" />

After:

<img width="550" height="270" alt="image" src="https://github.com/user-attachments/assets/c20d368d-c029-43a0-9114-89342c394560" />

---

4. Copy the third thing that says "main function". Paste this on line 250, it should look like this when you paste it:

Before:

<img width="835" height="397" alt="image" src="https://github.com/user-attachments/assets/5c932aed-4490-4e52-914c-a19cfef41b20" />

After:

<img width="769" height="662" alt="image" src="https://github.com/user-attachments/assets/7c7ad03f-4662-40c9-ada5-098d56d5c0da" />

---

5. Finally, copy the last thing that is in the file, which should be labeled "trigger function". Paste this between lines 273 and 274, it should look like this when you paste it.

Before:

<img width="687" height="119" alt="image" src="https://github.com/user-attachments/assets/3b47b38a-620e-4c92-9cd4-3cb8b04a2e82" />

After:

<img width="669" height="192" alt="image" src="https://github.com/user-attachments/assets/55203097-bea2-417f-9655-16c0c19f53c6" />

---

6. Save the file, and restart the bot using `docker compose restart`.

7. Copy the eval from `eval.py` and make sure to replace these 3 things:

- `BALL_NAME`: Replace it with the name of the ball you want the bot to catch.

- `INT_SECONDS`: Replace this with how much seconds you want till the bot catches the ball.

- `CHANNEL_ID`: Replace this with the channel ID of your choice.

Once you have done that, run the eval in the server of choice and you should see the bot itself will catch the ball.

If you have any questions or issues with this custom command, feel free to contact the creator on Discord. (tag is angerrandom)

<img width="412" height="232" alt="image" src="https://github.com/user-attachments/assets/f457740c-aea3-46db-9fc1-71c2683a6552" />





If you have any questions or issues with this, feel free to ask to the creator on Discord. (tag is angerrandom)
