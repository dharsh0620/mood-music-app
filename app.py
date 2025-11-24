from flask import Flask, request, render_template
import random

app = Flask(__name__)

mood_songs = {
    "energetic": [
        {
            "title": "monica",
            "youtube": "https://www.youtube.com/watch?v=2qCpY38ompo&list=RD2qCpY38ompo&start_radio=1",
            "reason": "High-energy track that boosts motivation."
        },
        {
            "title": "kaavalaya",
            "youtube": "https://www.youtube.com/watch?v=RVLNBVK8auM&list=RDRVLNBVK8auM&start_radio=1",
            "reason": "Catchy beats that hype your energy."
        },
        {
            "title": "Kaattu Payale",
            "youtube": "https://www.youtube.com/watch?v=JwvM4Fiha7E&list=RDJwvM4Fiha7E&start_radio=1",
            "reason": "Fast-paced track perfect for high energy mood."
        }
    ],
    "calm": [
        {
            "title": "kannukulla",
            "youtube": "https://www.youtube.com/watch?v=qC-X5MogTI0&list=RDqC-X5MogTI0&start_radio=1",
            "reason": "Soft and soothing voice that relaxes instantly."
        },
        {
            "title": "manasellam",
            "youtube": "https://www.youtube.com/watch?v=w6hZOvnUcJY&list=RDw6hZOvnUcJY&start_radio=1",
            "reason": "Peaceful melody that calms your emotions."
        },
        {
            "title": "oxygen",
            "youtube": "https://www.youtube.com/watch?v=gUXFiuBkPb8&list=RDgUXFiuBkPb8&start_radio=1",
            "reason": "Soulful tune that melts your stress."
        }
    ],
    "happy": [
        {
            "title": "hey nijamey",
            "youtube": "https://www.youtube.com/watch?v=w98ykYu6d0Y&list=RDw98ykYu6d0Y&start_radio=1",
            "reason": "Feel-good vibe that lifts your mood instantly."
        },
        {
            "title": "mundhinam",
            "youtube": "https://www.youtube.com/watch?v=Nomh_DiLye4&list=RDNomh_DiLye4&start_radio=1",
            "reason": "Cheerful, lively beats perfect for happy moments."
        },
        {
            "title": "ondra renda",
            "youtube": "https://www.youtube.com/watch?v=KL0G0asLNMU&list=RDKL0G0asLNMU&start_radio=1",
            "reason": "Romantic & cheerful tune for a bright mood."
        }
    ],
    "sad": [
        {
            "title": "Pirai Thedum",
            "youtube": "https://www.youtube.com/watch?v=QmHX0whk6Rg&list=RDQmHX0whk6Rg&start_radio=1",
            "reason": "Emotional depth and soulful music."
        },
        {
            "title": "Maruvaarthai",
            "youtube": "https://www.youtube.com/watch?v=rpIlP6pI8fo&list=RDrpIlP6pI8fo&start_radio=1",
            "reason": "A soulful melody that brings emotional clarity."
        },
        {
            "title": "yen ennai pirindhai",
            "youtube": "https://www.youtube.com/watch?v=Dfy5S93chgM&list=RDDfy5S93chgM&start_radio=1",
            "reason": "Heart-touching music for emotional moments."
        }
    ]
}


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        mood = request.form.get("mood").lower()

        if mood in mood_songs:
            chosen = random.choice(mood_songs[mood])
            chosen["mood"] = mood
            result = chosen

        else:
            result = "not_found"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
