// // Basic example script to demonstrate dynamic behavior
// document.addEventListener('DOMContentLoaded', function() {
//     console.log('Blog page loaded');
// });

document.addEventListener('DOMContentLoaded', function() {
    console.log('Blog page loaded');
    
    // Example: Toggle dark mode
    const toggleButton = document.getElementById('toggle-dark-mode');
    toggleButton.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
    });
});
