# How do I add this?

1. Drag the `cardgenerator.py` folder to `ballsdex/packages/balls`

It should look like this:

<img width="615" height="196" alt="image" src="https://github.com/user-attachments/assets/f83e1aa3-991f-4fd8-9b1b-e37edc93715d" />

2. Open `cog.py` in the same folder and import the following:
- from ballsdex.packages.balls.cardgenerator import CardGenerator
- import io
- from ballsdex.core.utils.transformers import BallTransform
- ballsdex.core.utils.transformers import SpecialTransform

If you need a reminder on how to import or don't know how, click [here](https://github.com/ContestedWheel/EvalEvalEval-BD/wiki/Adding-custom-commands#importing)

3. Open `command.py` and copy it's contents.

4. Add the command like normal. If you need a reminder on how to add them or don't know how, click [here](https://github.com/ContestedWheel/EvalEvalEval-BD/wiki/Adding-custom-commands#adding-a-command)

4.1. Optionally, uncomment the 4th app_commands if you want the command to be an admin command.

5. Save the file, and restart the bot using `docker compose restart`. Refresh your Discord if you don't see the command.

If there is any issue with this README, please let me know ASAP by pinging me in the Ballsdex Developers server (tag is ihailthenight1234).
