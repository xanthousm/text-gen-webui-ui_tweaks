// Get references to the elements
//extensions defined in main.js
let ext_btn = document.getElementById('ext_toggle');
//bar_w_str defined in script.py

// Add an event listener to the extensions toggle button
ext_btn.addEventListener('click', function(e) {
    // Toggle extensions offset to show/hide
    if (extensions.style.right != '5px') {
        extensions.style.setProperty("right", "5px");
    } else {
        extensions.style.setProperty("right", bar_w_str);
    }
});

