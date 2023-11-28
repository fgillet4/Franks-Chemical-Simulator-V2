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
  
    // Event listener for the Flowsheet Simulation button
    const flowsheetSimulationBtn = document.getElementById('flowsheetSimulation');
    if (flowsheetSimulationBtn) {
      flowsheetSimulationBtn.addEventListener('click', () => {
        // Logic for Flowsheet Simulation
        console.log("Flowsheet Simulation Clicked");
        // You might load new content, call a function, or send a message to the main process
      });
    }
  
    // More event listeners and logic can be added here as needed
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
  
  // Uncomment the below line to change the header text (can be triggered by some event)
  // changeHeaderText();
  