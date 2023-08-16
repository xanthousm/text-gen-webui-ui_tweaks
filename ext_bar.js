// Get references to the elements
//extensions defined in main.js
let ext_btn = document.getElementById('ext_toggle');
//bar_w_str defined in script.py

//visibility check for ext_button
main_parent.addEventListener('click', function(e) {
	let chat_visible = (chat_tab.offsetHeight > 0 && chat_tab.offsetWidth > 0);
    let notebook_visible = (notebook_tab.offsetHeight > 0 && notebook_tab.offsetWidth > 0);
    let default_visible = (default_tab.offsetHeight > 0 && default_tab.offsetWidth > 0);
	if (chat_visible || notebook_visible || default_visible) {
        ext_btn.style.display = 'block';
    } else {
        ext_btn.style.display = 'none';
    }
});

// Add an event listener to the extensions toggle button
ext_btn.addEventListener('click', function(e) {
    // Toggle extensions offset to show/hide
    if (extensions.style.right != '5px') {
        extensions.style.setProperty("right", "5px");
    } else {
        extensions.style.setProperty("right", bar_w_str);
    }
});

