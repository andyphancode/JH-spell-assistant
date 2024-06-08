import os
from flask import Flask, jsonify, request
from spellchecker import SpellChecker
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi

from secret import to_ye_olde_english
from discord_interactions import verify_key_decorator

DISCORD_PUBLIC_KEY = 'fd9aee8eaf1001ca5b335654aaf52ba5f66903cd9844d79bd95764410a161ebe'

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)
handler = Mangum(asgi_app)
# Initialize SpellChecker instance
spell = SpellChecker()


@app.route("/", methods=["POST"])
async def interactions():
    print(f"👉 Request: {request.json}")
    raw_request = request.json
    return interact(raw_request)

@verify_key_decorator(DISCORD_PUBLIC_KEY)
def interact(raw_request):
    if raw_request["type"] == 1:  # PING
        response_data = {"type": 1}  # PONG
    else:
        data = raw_request["data"]
        command_name = data["name"]

        if command_name == "commands":
            # content including reply and old /secret
            # message_content = """This is JH bot at your service, ready to figure out whatever your friend typed.\nHere are my available commands:\n```!commands: Get a list of commands\n\n!fix: Use this command and follow it up with any text to autocorrect it. For example sending [!fix helol eveyrone] without the brackets would result in me sending a message with the autocorrected response: hello everyone\n\n!re: Reply to a message with this command to autocorrect the message you replied to. For example, replying to a message that says [helol eveyrone] with !re would result in me sending a message with the autocorrected response: hello everyone\n\n!secret: Reply to a message with this command and see what happens! ```"""
            message_content = """This is JH bot at your service, ready to figure out whatever your friend typed.\nHere are my available commands:\n```!commands: Get a list of commands\n\n!fix: Use this command and follow it up with any text to autocorrect it. For example sending [!fix helol eveyrone] without the brackets would result in me sending a message with the autocorrected response: hello everyone\n\n!secret: Input a message with this command and see what happens! ```"""        
        elif command_name == "fix":
            original_message = data["options"][0]["value"]
            words = original_message.split()

            # Correct words that can be corrected, leave the rest unchanged
            corrected_words = [spell.correction(word) if spell.correction(word) is not None else word for word in words]

            # Join the corrected words back into a sentence
            corrected_message = " ".join(corrected_words)
            if corrected_message is None:
                message_content = "The typos in this message are beyond salvation..."
            else:
                message_content = f"The message you are correcting is:\n ```{original_message}```\n This is what I think it is:\n```{corrected_message}```"
        # Made without realizing that slash commands cannot interact with a replied message, commented out for now but may have functionality in the future
        # elif command_name == "re":
        #     referenced_message = data.get("referenced_message")
        #     if referenced_message is None:
        #         print(f"👉 Data: {data}")
        #         message_content = "Please reply to a message you want to correct. This command only works with replies."
        #     else:
        #         original_message = raw_request["message"]["referenced_message"]["content"]
        #         words = original_message.split()
        #         corrected_words = [spell.correction(word) for word in words]
        #         corrected_message = " ".join(corrected_words)
        #         message_content = f"The user you are correcting sent:\n```{original_message}```\nThis is what I think it means:\n```{corrected_message}```"
        elif command_name == "secret":
            original_message = data["options"][0]["value"]
            words = original_message.split()

            # Correct words that can be corrected, leave the rest unchanged
            corrected_words = [spell.correction(word) if spell.correction(word) is not None else word for word in words]

            # Join the corrected words back into a sentence
            corrected_message = " ".join(corrected_words)   
            if corrected_message is None:
                message_content = "The typos in this message are beyond salvation..."
            else:
                giga_corrected_message = to_ye_olde_english(corrected_message)
                message_content = f"The message you are correcting is:\n ```{original_message}```\n This is what I think it is:\n```{giga_corrected_message}```"




        response_data = {
            "type": 4,
            "data": {"content": message_content},
        }

    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)