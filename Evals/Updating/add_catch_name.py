ball = await Ball.get(country="test")
ball.catch_names = f"{ball.catch_names or ''}catchname1;catchname2;catchname3"
await ball.save()

# Replace catchname1, catchname2, and catchname3 with your own catch names
# If you want only one catch name, just remove the last 2 catch names so that only catchname1 is left.
# You can add more than 3 catch names by adding a semicolon (;) at the end then typing the new catch name you want.
