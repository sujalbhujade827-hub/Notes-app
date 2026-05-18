from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Structured dictionary list to match your Figma layout properties
notes = [
    {
        "id": 0,
        "title": "Untitled Note",
        "content": "No content",
        "category": "personal",
        "time": "about 2 hours ago"
    }
]

@app.route('/')
def home():
    # Check if the user clicked "+ New Note" or is viewing a blank slate
    view = request.args.get('view', 'empty')
    return render_template('index.html', notes=notes, view=view)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form.get('title', 'Untitled Note')
    category = request.form.get('category', 'Personal')
    content = request.form.get('content', '')

    # Provide fallback values if input fields are empty
    if not title.strip():
        title = "Untitled Note"
    if not content.strip():
        content = "No content"

    new_note = {
        "id": len(notes),
        "title": title.strip(),
        "content": content.strip(),
        "category": category.lower(),
        "time": "Just now"
    }
    
    notes.append(new_note)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)