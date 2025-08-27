> [!NOTE]  
> This snippet of code was made by Jovial Merryment, blame him not me.

# How do I add this?

1. Copy the contents in `code.py`

2. Open `cog.py` in `ballsdex/packages/balls`

3. Scroll down to line 276 in the file, and highlight all the code from lines 276 to 355 by click and holding down your left mouse button.

It should look like this after you have highlighted the code:

<img width="652" height="1060" alt="image" src="https://github.com/user-attachments/assets/db7d66be-577a-40ea-b4e6-1a17b50ff7fe" />

4. Press CTRL + V to paste the code from `code.py`. It should look like this after you paste:

<img width="575" height="1226" alt="image" src="https://github.com/user-attachments/assets/817a5852-3040-402e-bd76-ee303502a2ba" />

5. Replace ECONOMYID1 and ECONOMYID2 with the ID of the economies you want to show completion for. The economy ID is under "PK" in the admin panel.

<img width="101" height="160" alt="image" src="https://github.com/user-attachments/assets/c6ba6b38-c3cf-4185-a2e1-d52b5944267d" />

6. Replace ECONOMY_TITLE_1 and ECONOMY_TITLE_2 with the names of the economies.

> [!TIP]
> You can add more than two economies if you'd like, just keep the above in mind if you are going to do so.

7. Save your changes and restart the bot using `docker compose restart`. Once the bot is back up, test the completion command to see if it works.

This is what this snippet looks like in action:

<img width="599" height="513" alt="image" src="https://github.com/user-attachments/assets/05c7afd9-8491-4fef-8d28-22d49bef2a39" />
