# How do I add this?

1. Copy the contents in the `rarity_button.py` file.

2. Open `countryball.py` in `ballsdex/packages/countryballs`.

3. Scroll down to line 167 and paste it like this:

<img width="865" height="264" alt="image" src="https://github.com/user-attachments/assets/0a33a12d-c4dd-4f9b-bc5c-08377e1a24e2" />

3.1. Optionally, you can replace "ball" with whatever you want. Example is below:

<img width="806" height="141" alt="image" src="https://github.com/user-attachments/assets/9e9711ec-9bcf-4dbe-9a73-ec199a29304b" />

> [!TIP]
> If you encounter indenting issues when pasting like this picture below, just press backspace until it lines up correctly.

<img width="938" height="258" alt="image" src="https://github.com/user-attachments/assets/78c1369d-f852-4d02-b5b1-e2ecc6fc95a5" />

# Can I make the button unusable after someone catches it?

Yes you can!

In the same file (`countryball.py`) go to line 158 and create a new line, Then, copy and paste what's below in the new line
```py
self.rar_btn.disabled = True
```

It should look like this. If it does, save the file and restart the bot to apply changes.

<img width="342" height="61" alt="image" src="https://github.com/user-attachments/assets/9e757e75-e143-402b-9f8e-678aa464b0dd" />
