this is my bot!

a friend helped me get started on it, so thanks to Roan Elmos for building the initial proof of concept for me!

if you want to run it yourself, put a discord bot token in a text file named 'discord_token.txt' and have that in the root of the git clone (same directory as 'send.py')

## How it works
When the bot detects an unsanitized youtube link, it deletes the message and resends it with a sanitized version of the link.

It sends the original poster, along with the timestamp of the original message, too!




## Future
I am working on a variant of the bot that looks at a dictionary containing several different websites and what modifiers to their links are and aren't "safe", so that the bot can remove them automatically.

That project is being developed on the cross-platform-version branch, so look there if you are interested.