import bottle


@bottle.route("/")
def hello():
    return "Hello world"


@bottle.route("/holidays")
def holidays():
    data = {
        "Japan": [
            "Mon 23rd Nov \t Labor Thanksgiving Day",
            "Thu 31st Dec \t December 31 Bank Holiday"
        ],
        "India": [
            "Fri 20th Nov \t Chhat Puja (Pratihar Sashthi/Surya Sashthi)",
            "Tue 24th Nov \t Guru Tegh Bahadur's Martyrdom Day",
            "Mon 30th Nov \t Guru Nanak Jayanti",
            "Thu 24th Dec \t Christmas Eve",
            "Fri 25th Dec \t Christmas"
        ]

    }
    result = "<h1>Holidays</h1>"

    for k in data.keys():
        result += f"<b>{k}</b><br><br>"
        for idx, r in enumerate(data[k]):
            result += f"{data[k][idx]}<br>"
        result += "<br><br><br>"

    return result


if __name__ == "__main__":
    bottle.run(host='localhost', port=8080, debug=True)
