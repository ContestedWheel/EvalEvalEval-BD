# hai jovial :33

        # Economy definitions
        ECONOMY_NAMES = {
            ECONOMYID1: "ECONOMY_TITLE_1",
            ECONOMYID2: "ECONOMY_TITLE_2",
       }

        # Group enabled balls by economy
        economy_balls = defaultdict(dict)
        for ball_id, ball in balls.items():
            if not ball.enabled:
                continue
            economy_id = getattr(ball, "economy_id", None)
            if economy_id in ECONOMY_NAMES:
                economy_balls[economy_id][ball_id] = ball.emoji_id

        # Apply filters
        filters = {"player__discord_id": user_obj.id, "ball__enabled": True}
        if special:
            filters["special"] = special
            # filter balls for specials
            economy_balls = {
                eid: {
                    bid: emoji_id
                    for bid, emoji_id in group.items()
                    if (special.end_date is None or balls[bid].created_at < special.end_date)
                }
                for eid, group in economy_balls.items()
            }

        if self_caught is not None:
            filters["trade_player_id__isnull"] = self_caught

        owned_countryballs = set(
            x[0]
            for x in await BallInstance.filter(**filters)
            .distinct()
            .values_list("ball_id")
        )

        entries = []

        def fill_fields(title: str, emoji_ids: set[int]):
            first_field_added = False
            buffer = ""

            for emoji_id in emoji_ids:
                emoji = self.bot.get_emoji(emoji_id)
                if not emoji:
                    continue

                text = f"{emoji} "
                if len(buffer) + len(text) > 1024:
                    if first_field_added:
                        entries.append(("\u200b", buffer))
                    else:
                        entries.append((f"__**{title}**__", buffer))
                        first_field_added = True
                    buffer = ""
                buffer += text

            if buffer:
                if first_field_added:
                    entries.append(("\u200b", buffer))
                else:
                    entries.append((f"__**{title}**__", buffer))

        # Description tracks % per economy
        source_description = ""

        for econ_id, econ_balls in economy_balls.items():
            econ_name = ECONOMY_NAMES.get(econ_id, f"Economy {econ_id}")
            all_ids = set(econ_balls.keys())
            owned = all_ids & owned_countryballs
            missing = all_ids - owned

            percent = round((len(owned) / len(all_ids)) * 100, 1) if all_ids else 0
            source_description += f"\n{econ_name} Progression: **{percent}%**"

            if owned:
                fill_fields(f"{econ_name} Owned", {econ_balls[i] for i in owned})
            else:
                entries.append((f"__**{econ_name} Owned__**", "Nothing yet."))

            if missing:
                fill_fields(f"{econ_name} Missing", {econ_balls[i] for i in missing})
            else:
                entries.append(
                    (
                        f"__**:tada: No missing {econ_name}, congratulations! ❤️**__",
                        "\u200b",
                    )
                )
