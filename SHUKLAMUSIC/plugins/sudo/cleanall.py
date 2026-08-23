from pyrogram import filters, enums
from pyrogram.errors import RPCError

from SHUKLAMUSIC import app
from config import OWNER_ID


# Add additional trusted sudo IDs here.
# Example:
# SUDO_USERS = {123456789, 987654321}
SUDO_USERS = set()

# Safety: admins/owners are NEVER banned by this command.
SKIP_ADMINISTRATORS = True


def is_authorized(user_id: int) -> bool:
    return user_id == OWNER_ID or user_id in SUDO_USERS


@app.on_message(filters.command(["cleanall", "banall"]))
async def clean_all_command(client, message):

    # Must be a private/group/supergroup message.
    if message.chat.type not in (
        enums.ChatType.GROUP,
        enums.ChatType.SUPERGROUP,
    ):
        return await message.reply_text(
            "❌ This command can only be used in a group."
        )

    # Only OWNER_ID / SUDO_USERS can execute it.
    # They do NOT need to be admins themselves.
    if not message.from_user or not is_authorized(message.from_user.id):
        return await message.reply_text(
            "❌ You are not authorized to use this command."
        )

    # The BOT itself must have ban/restrict permission.
    try:
        bot_member = await client.get_chat_member(
            message.chat.id,
            "me",
        )

        if bot_member.status not in (
            enums.ChatMemberStatus.ADMINISTRATOR,
            enums.ChatMemberStatus.OWNER,
        ):
            return await message.reply_text(
                "❌ Make me an administrator first."
            )

        if (
            bot_member.status == enums.ChatMemberStatus.ADMINISTRATOR
            and not bot_member.privileges.can_restrict_members
        ):
            return await message.reply_text(
                "❌ I need the **Ban Users** permission."
            )

    except RPCError as e:
        return await message.reply_text(
            f"❌ Couldn't check my permissions.\n`{e}`"
        )

    await message.reply_text(
        "⚠️ <b>Clean All Started</b>\n\n"
        "I will remove regular members from this group.\n"
        "Administrators and protected users will be skipped."
    )

    banned = 0
    skipped = 0
    failed = 0

    try:
        async for member in client.get_chat_members(message.chat.id):

            user = member.user

            if not user:
                skipped += 1
                continue

            # Never ban the bot itself.
            if user.is_self:
                skipped += 1
                continue

            # Never ban configured owner.
            if user.id == OWNER_ID:
                skipped += 1
                continue

            # Never ban sudo users.
            if user.id in SUDO_USERS:
                skipped += 1
                continue

            # Never ban administrators/creator.
            if SKIP_ADMINISTRATORS and member.status in (
                enums.ChatMemberStatus.ADMINISTRATOR,
                enums.ChatMemberStatus.OWNER,
            ):
                skipped += 1
                continue

            # Only process actual members.
            if member.status not in (
                enums.ChatMemberStatus.MEMBER,
                enums.ChatMemberStatus.RESTRICTED,
            ):
                skipped += 1
                continue

            try:
                await client.ban_chat_member(
                    message.chat.id,
                    user.id,
                )
                banned += 1

            except RPCError:
                failed += 1

    except RPCError as e:
        return await message.reply_text(
            "❌ <b>Clean All stopped.</b>\n\n"
            f"Error: `{e}`\n\n"
            f"✅ Banned: `{banned}`\n"
            f"⏭ Skipped: `{skipped}`\n"
            f"❌ Failed: `{failed}`"
        )

    await message.reply_text(
        "✅ <b>Clean All Finished</b>\n\n"
        f"👤 Banned: `{banned}`\n"
        f"🛡 Skipped: `{skipped}`\n"
        f"❌ Failed: `{failed}`"
    )
