> [!NOTE]  
> This custom command was made by [Ray Hsueh](https://github.com/Ray-Hsueh), I just made a easy to follow tutorial with markdown.

# How do I add this?

1. Copy the imports in `daily.py`. This file will contain everything you will need to add this command.

If you need a reminder on how to import or don't know how, click [here](https://github.com/ContestedWheel/EvalEvalEval-BD/wiki/Adding-custom-commands#importing)

2. Paste the imports in `cog.py`, located in `ballsdex/packages/balls`

It should look like this once you have pasted in the imports:

<img width="437" height="153" alt="image" src="https://github.com/user-attachments/assets/4853e800-3a75-422f-be97-b3eb0a75ccaf" />

3. Copy the second thing you see after the imports, which would be "Paste this on line 39". Do what the comment says, it should look like this when you paste it:

> [!NOTE]  
> I have added Before and After pictures for less confusion since some people may already have code in these lines.

Before:

<img width="558" height="140" alt="image" src="https://github.com/user-attachments/assets/efdd371a-23cf-45d1-9507-ef82ceb497d7" />

After:

<img width="900" height="136" alt="image" src="https://github.com/user-attachments/assets/3955cf3c-82cc-47f0-8b10-c306161a9989" />

---

4. Copy the third thing that says "Paste this on line 124". Do what the comment says again, it should look like this when you paste it:


Before:

<img width="687" height="155" alt="image" src="https://github.com/user-attachments/assets/b079b9ee-c614-4bbd-9a9a-828a83bd9c58" />

After:

<img width="818" height="762" alt="image" src="https://github.com/user-attachments/assets/d2730587-0f0a-4285-a50d-e269ed48bf80" />

---

5. Finally, copy the last thing that is in the file, which should be the actual command. Add the command into the file, no specific line required as the comment says.
If you need a reminder on how to add custom commands or don't know how, click [here](https://github.com/ContestedWheel/EvalEvalEval-BD/wiki/Adding-custom-commands#adding-a-command)

6. Save the file, and restart the bot using `docker compose restart`. Refresh your Discord if you don't see the command.

If there is any issue with this README, please let me know ASAP by pinging me in the Ballsdex Developers server (tag is ihailthenight1234).
