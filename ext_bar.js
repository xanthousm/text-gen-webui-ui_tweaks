// Get references to the elements
//extensions defined in main.js
let ext_btn = document.getElementById('ext_toggle');

// Add an event listener to the main element
ext_btn.addEventListener('click', function(e) {
    // Check if the ext element is visible
    if (extensions.style.right != '5px') {
        extensions.style.setProperty("right", "5px");
    } else {
        extensions.style.setProperty("right", "-2000px");
    }
});

