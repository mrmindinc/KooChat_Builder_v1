from flask import request, jsonify
from flask_api import FlaskAPI, status

from model.chatbot.kogpt2 import chatbot as ch_kogpt2

app = FlaskAPI(__name__)

@app.route('/chatbot/g')
def reactChatbotV1():
    sentence = request.args.get("s")
    if sentence is None or len(sentence) == 0 or sentence == '\n':
        return jsonify({
            "answer": "듣고 있어요. 더 말씀해주세요~ "
        })

    answer = ch_kogpt2.predict(sentence)
    return jsonify({
        "answer": answer
    }), status.HTTP_200_OK

if __name__ == '__main__':
    default_host = "0.0.0.0"
    default_port = "10734"


    import os
    os.environ['FLASK_ENV'] = "development"

    import optparse
    parser = optparse.OptionParser()

    parser.add_option("-H", "--host",
                      help="Hostname of the Flask app " + \
                           "[default %s]" % default_host,
                      default=default_host)

    parser.add_option("-P", "--port",
                      help="Port for the Flask app " + \
                           "[default %s]" % default_port,
                      default=default_port)

    options, _ = parser.parse_args()

    app.run(
        debug=True,
        host=options.host,
        port=int(options.port)
    )