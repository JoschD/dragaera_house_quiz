from pyscript import document, when

# Chart data
chart_data = {
    'January': 12,
    'February': 19,
    'March': 3,
    'April': 5,
    'May': 2,
    'June': 15
}

# Counter state
counter = 0

def create_chart():
    """Create a bar chart using pure Python and HTML manipulation"""
    chart_div = document.querySelector("#chart")
    chart_div.innerHTML = ""
    
    # Find max value for scaling
    max_value = max(chart_data.values())
    
    # Create bars
    for month, value in chart_data.items():
        # Calculate width percentage
        width_percent = (value / max_value) * 100
        
        # Create bar HTML
        bar_html = f'''
        <div class="bar">
            <div class="bar-label">{month}</div>
            <div class="bar-visual" style="width: {width_percent}%">
                {value}
            </div>
        </div>
        '''
        chart_div.innerHTML += bar_html

def update_counter_display():
    """Update the counter display"""
    counter_display = document.querySelector("#counter-display")
    counter_display.innerText = str(counter)

@when("click", "#increment")
def increment_counter(event):
    """Increment button click handler"""
    global counter
    counter += 1
    update_counter_display()

@when("click", "#decrement")
def decrement_counter(event):
    """Decrement button click handler"""
    global counter
    counter -= 1
    update_counter_display()

@when("click", "#reset")
def reset_counter(event):
    """Reset button click handler"""
    global counter
    counter = 0
    update_counter_display()

# Initialize the page
def init():
    # Hide loading message
    loading = document.querySelector("#loading")
    loading.style.display = "none"
    
    # Show chart
    chart_container = document.querySelector("#chart-container")
    chart_container.style.display = "block"
    create_chart()
    
    # Show counter
    counter_section = document.querySelector("#counter-section")
    counter_section.style.display = "block"
    update_counter_display()
    
    print("PyScript initialized! Python is running in your browser! 🎉")

# Run initialization
init()
