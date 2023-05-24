// Get references to the elements
//main defined in main.js
//extensions defined in main.js
//bar_w_str defined in script.py

// Add an event listener to the main element
main_parent.addEventListener('click', function(e) {
    // Check if extensions bar open and was not the target (or the target's ancestor), hide
    if (extensions.style.right == '5px') {
        extensions.style.setProperty("right", bar_w_str);
    }
});