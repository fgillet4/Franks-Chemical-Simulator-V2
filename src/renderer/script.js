// script.js

document.addEventListener('DOMContentLoaded', () => {
    // This code will run after the document is fully loaded
    console.log('The DOM is fully loaded');
  
    // Example: Update the header text when clicked
    const header = document.querySelector('h1');
    if (header) {
      header.addEventListener('click', () => {
        header.textContent = 'Header Clicked!';
        header.style.color = 'blue'; // Changing the color of the header on click
      });
    }
  
    // Add more event listeners as needed
    // ...
  });
  
  // Function to update the content of an element
  function updateContent(selector, content) {
    const element = document.querySelector(selector);
    if (element) {
      element.textContent = content;
    }
  }
  
  // Example usage of the updateContent function
  function changeHeaderText() {
    updateContent('h1', 'New Header Text');
  }
  
  // Call the function to update the header text (can be triggered by some event)
  // changeHeaderText();
  
  // You can include more helper functions, event handlers, and other code as needed
  // ...
  