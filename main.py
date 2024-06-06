import os
from flask import Flask, jsonify, request
import jamspell
from secret import to_ye_olde_english



app = Flask(__name__)
# Initialize jamspell
corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel('en.bin')



@app.route("/", methods=["POST"])
async def interactions():
    print(f"👉 Request: {request.json}")
    raw_request = request.json
    return interact(raw_request)


def interact(raw_request):
    if raw_request["type"] == 1:  # PING
        response_data = {"type": 1}  # PONG
    else:
        data = raw_request["data"]
        command_name = data["name"]

        if command_name == "commands":
            message_content = """This is JH bot at your service, ready to figure out whatever your friend typed.\nHere are my available commands:\n```!commands: Get a list of commands\n\n!fix: Use this command and follow it up with any text to autocorrect it. For example sending [!fix helol eveyrone] without the brackets would result in me sending a message with the autocorrected response: hello everyone\n\n!re: Reply to a message with this command to autocorrect the message you replied to. For example, replying to a message that says [helol eveyrone] with !re would result in me sending a message with the autocorrected response: hello everyone\n\n!secret: Reply to a message with this command and see what happens! ```"""
        elif command_name == "fix":
            original_message = data["options"][0]["value"]
            corrected_message = corrector.FixFragment(original_message)
            message_content = f"The message you are correcting is:\n ```{original_message}```\n This is what I think it is:\n```{corrected_message}```"
        elif command_name == "re":
            if "referenced_message" not in raw_request["message"] or raw_request["message"]["referenced_message"] is None:
                message_content = "Please reply to a message you want to correct. This command only works with replies."
            else:
                original_message = raw_request["message"]["referenced_message"]["content"]
                corrected_message = corrector.FixFragment(original_message)
                message_content = f"The user you are correcting sent:\n```{original_message}```\nThis is what I think it means:\n```{corrected_message}```"
        elif command_name == "secret":
            if "referenced_message" not in raw_request["message"] or raw_request["message"]["referenced_message"] is None:
                message_content = "Please reply to a message you want to correct. This command only works with replies."
            else:
                original_message = raw_request["message"]["referenced_message"]["content"]
                corrected_message = corrector.FixFragment(original_message)
                giga_corrected_message = to_ye_olde_english(corrected_message)
                message_content = f"The user you are correcting sent:\n```{original_message}```\nThis is what I think it means:\n```{giga_corrected_message}```"



        response_data = {
            "type": 4,
            "data": {"content": message_content},
        }

    return jsonify(response_data)
