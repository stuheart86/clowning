from flask import Flask, request, render_template
import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def generate_story():
    openai.api_key = "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"

    genre = request.form.get('genre')
    story_teller = request.form.get('story_teller')
    story_telling_style = request.form.get('story_telling_style')
    creativity = request.form.get('creativity')

    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt='generate a {} story, told by a {} {} story teller, with {} creativity.'.format(genre, story_teller, story_telling_style, creativity),
      max_tokens=1000,
      n=1,
      stop=None,
      temperature=0.5,
    )

    story = response['choices'][0]['text']

    return render_template('story.html', story=story)

if __name__ == '__main__':
    app.run(debug=True)
