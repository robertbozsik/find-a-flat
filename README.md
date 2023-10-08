# find-a-flat

Help me find a flat in Berlin.

## Create and activate virtual environment
create: `python3 -m venv find-a-flat-venv`
activate: `source find-a-flat-venv/bin/activate`

## Create a Telegram bot
1. Download and set the Telegram application on your mobile
2. Search for the `@BotFather` username in your Telegram application
3. Click `Start` to begin a conversation with `@BotFather`
4. Send the message `/newbot` to `@BotFather`, follow the instructions and receive a **token**
   1. add a name to your bot
   2. add a username to your bot
   3. receive the token for your bot
5. Begin a conversation with your bot
   1. Click on the `t.me/<bot-username>` link in `@BotFather`'s response and click `Start`

### Check your bot in the browser
- https://api.telegram.org/bot<token>/getMe

### Get your Telegram chat ID in the browser
1. Paste the following link into your browser https://api.telegram.org/bot<token>/getUpdates?offset=0
2. Send a message to your bot in the Telegram application on your mobile
3. Refresh your browser
4. Identify the numerical chat ID by finding the `id` inside the `chat` JSON object, e.g. `123456789`

## Useful links
- https://core.telegram.org/bots
- https://docs.influxdata.com/kapacitor/v1/reference/event_handlers/telegram/
