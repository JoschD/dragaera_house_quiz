from pyscript import document, when
from js import console
from questions import Question, Questions, get_questions
from results import calculate_results, DESCRIPTIONS, COLOR_THEMES

# Quiz state
QUESTIONS: Questions = get_questions()
user_answers: dict[str, int] | None = None  # Will store index for each question
user_weights: dict[str, float] | None = None  # Will store 0.5, 1, or 2 for importance


def init_user_state():
    """Initialize user state"""
    global user_answers, user_weights

    QUESTIONS.reset()
    user_answers = {}
    user_weights = {}


def show_screen(screen_id):
    """Show a specific screen and hide others"""
    screens = ['welcome-screen', 'question-screen', 'results-screen', 'loading']
    for screen in screens:
        element = document.querySelector(f'#{screen}')
        if screen == screen_id:
            element.classList.remove('hidden')
        else:
            element.classList.add('hidden')


def set_theme(colors):
    """Apply a color theme to the page"""
    root = document.documentElement
    for key, value in colors.items():
        root.style.setProperty(f'--{key.replace("_", "-")}', value)


def display_question(question: Question, index: int):
    """Display the current question"""
    # Update progress
    progress = document.querySelector('#progress')
    progress.innerText = f"Question {index} of {len(QUESTIONS)}"

    # Update question text
    title = document.querySelector('#question-title')
    title.innerText = question.title

    text = document.querySelector('#question-text')
    text.innerText = question.text

    # Create choice buttons
    choices_div = document.querySelector('#choices')
    choices_div.innerHTML = ''

    for i, choice_text in enumerate(question.choices):
        choice_html = f'''
        <div class="choice" data-value="{i}">
            <input type="radio" name="choice" id="choice-{i}" value="{i}">
            <label for="choice-{i}">{choice_text}</label>
        </div>
        '''
        choices_div.innerHTML += choice_html

    # Reset importance to normal
    importance_normal = document.querySelector('#importance-normal')
    importance_normal.checked = True

    # Disable next button
    next_btn = document.querySelector('#next-btn')
    next_btn.disabled = True

    # Update back button state
    back_btn = document.querySelector('#back-btn')
    back_btn.disabled = not bool(index)


def display_results():
    """Display the results on the results screen"""
    # Sort by percentage (descending)
    results = calculate_results(user_answers, user_weights)
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    # Display results
    chart_div = document.querySelector('#results-chart')
    chart_div.innerHTML = ''

    for house_name, percentage in sorted_results:
        bar_html = f'''
        <div class="result-bar">
            <div class="result-label">
                <span>{house_name}</span>
                <span>{percentage:.1f}%</span>
            </div>
            <div class="result-bar-container">
                <div class="result-bar-fill" style="width: {percentage}%">
                </div>
            </div>
        </div>
        '''
        chart_div.innerHTML += bar_html

    # Display house description for winner
    winner = sorted_results[0][0]
    house = DESCRIPTIONS[winner]

    desc_div = document.querySelector('#house-description')
    desc_div.innerHTML = (
        f'<h2>{house["name"]}</h2>'
        f'<h3>{house["motto"]}.</h3><br>'
        f'<p>{house["description"]}</p>'
    )

    # Apply winner's color scheme
    set_theme(COLOR_THEMES[winner])


@when("click", "#start-quiz")
def start_quiz(event):
    """Start the quiz"""
    QUESTIONS.reset()
    console.log("Starting quiz... 🚀")
    show_screen('question-screen')
    display_question(QUESTIONS.next_question(), index=0)


@when("click", selector="#choices")
def select_choice(event):
    """Delegate choice selection"""
    target = event.target
    if not target:
        return

    # Find the .choice div (in case they clicked the label or input)
    while not target.classList.contains('choice'):
        target = target.parentElement
        if not target:
            return
        if target.id == 'choices':  # Reached parent without finding .choice
            return

    # safety check
    if not target or not target.classList.contains('choice'):
        return

    # Remove 'selected' class from all choices
    choices = document.querySelectorAll('.choice')
    for choice in choices:
        choice.classList.remove('selected')

    # Add 'selected' class to clicked choice
    target.classList.add('selected')

    # Get the value
    selected_choice = int(target.getAttribute('data-value'))
    user_answers[QUESTIONS.current_key] = selected_choice

    # Check the radio button
    radio = target.querySelector('input[type="radio"]')
    radio.checked = True

    # Enable next button
    next_btn = document.querySelector('#next-btn')
    next_btn.disabled = False


@when("click", "#next-btn")
def next_question(event):
    """Move to next question or show results"""

    # Check that an answer was selected
    if user_answers[QUESTIONS.current_key] is None:
        return

    # Save importance weight
    importance_radios = document.querySelectorAll('input[name="importance"]')
    for radio in importance_radios:
        if radio.checked:
            user_weights[QUESTIONS.current_key] = {0: 0.5, 1:1, 2:2}[int(radio.value)]
            break

    console.log(
        f"{QUESTIONS.current_key}: "
        f"User chose {user_answers[QUESTIONS.current_key]} with weight {user_weights[QUESTIONS.current_key]}."
    )

    # Move to next question or results
    question = QUESTIONS.next_question()
    if question is not None:
        display_question(question, QUESTIONS.current_index)
        return

    display_results()
    show_screen('results-screen')


@when("click", "#back-btn")
def previous_question(event):
    """Go back to previous question"""
    question = QUESTIONS.previous_question()
    if question is not None:
        display_question(question, QUESTIONS.current_index)


@when("click", "#restart-btn")
def restart_quiz(event):
    """Restart the quiz"""
    init_user_state()

    # Reset to default theme
    # set_theme(COLOR_THEMES['default'])

    show_screen('welcome-screen')


# Initialize
def init():
    """Initialize the quiz"""
    # Make sure DOM is ready
    if document.readyState == "loading":
        # DOM not ready yet, wait for it
        def on_ready(event):
            init()
        document.addEventListener("DOMContentLoaded", on_ready)
        return

    console.log("Quiz initialized! 🎉")
    init_user_state()
    show_screen('welcome-screen')

init()