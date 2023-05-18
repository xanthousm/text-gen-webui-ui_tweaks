document.getElementById("extensions").style.setProperty("max-width", "500px");
document.getElementById("extensions").style.setProperty("right", "100%");

// Get references to the elements
let extensions2 = document.getElementById('extensions');//re-using 'extensions' as a var name caused errors
let ext_btn = document.getElementById('ext_toggle');

// Add an event listener to the main element
ext_btn.addEventListener('click', function(e) {
    // Check if the ext element is visible
    if (extensions2.style.right == '100%') {
        extensions2.style.setProperty("right", "5px");
    } else {
        extensions2.style.setProperty("right", "100%");
    }
});

