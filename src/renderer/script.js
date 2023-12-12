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
    const massEnergyBalanceBtn = document.getElementById('massEnergyBalance');
    if (massEnergyBalanceBtn) {
      massEnergyBalanceBtn.addEventListener('click', () => {
        // Logic for Flowsheet Simulation
        console.log("Mass Energy Balance Clicked");
        // You might load new content, call a function, or send a message to the main process
      });
    }

    // Event listener for the Flowsheet Simulation button
    const bernoulliBalanceBtn = document.getElementById('equiptmentDesign');
    if (bernoulliBalanceBtn) {
      bernoulliBalanceBtn.addEventListener('click', () => {
        // Logic for Flowsheet Simulation
        console.log("Hydrualic Design Clicked");
      });
    }
    // Event listener for the Flowsheet Simulation button
    const processEconomicsBtn = document.getElementById('processEconomics');
    if (processEconomicsBtn) {
      processEconomicsBtn.addEventListener('click', () => {
        // Logic for Flowsheet Simulation
        console.log("Process Economics Button Clicked");
        // You might load new content, call a function, or send a message to the main process
      });
    }
    
      const processSafetyBtn = document.getElementById('processSafety');
      if (processSafetyBtn) {
        processSafetyBtn.addEventListener('click', () => {
          // Logic for Flowsheet Simulation
          console.log("Process Safety Button Clicked");
          // You might load new content, call a function, or send a message to the main process
        });

      }
      const addRemoveChemicalsBtn = document.getElementById('addRemoveChemicals');
      if (addRemoveChemicalsBtn) {
        addRemoveChemicalsBtn.addEventListener('click', () => {
          // Logic for Flowsheet Simulation
          console.log("Chemical Properties Button Clicked");
          // You might load new content, call a function, or send a message to the main process
        });
      }
      const thermodynamicPropertiesBtn = document.getElementById('thermodynamicProperties');
      if (thermodynamicPropertiesBtn) {
        thermodynamicPropertiesBtn.addEventListener('click', () => {
          // Logic for Flowsheet Simulation
          console.log("Thermodynamic Properties Button Clicked");
          // You might load new content, call a function, or send a message to the main process
        });
      }
      const pipingInstrumentationBtn = document.getElementById('pipingInstrumentation');
      if (pipingInstrumentationBtn) {
        pipingInstrumentationBtn.addEventListener('click', () => {
          // Logic for Flowsheet Simulation
          console.log("Piping and Instrumentation Button Clicked");
          // You might load new content, call a function, or send a message to the main process
        });
      }
    const processControlBtn = document.getElementById('processControl');
    if (processControlBtn) {
      processControlBtn.addEventListener('click', () => {
        // Logic for Flowsheet Simulation
        console.log("Process Control Button Clicked");
        // You might load new content, call a function, or send a message to the main process
      });
    }
    const processOptimizationBtn = document.getElementById('processOptimization');
    if (processOptimizationBtn) {
      processOptimizationBtn.addEventListener('click', () => {
        // Logic for Flowsheet Simulation
        console.log("Process Optimization Button Clicked");
        // You might load new content, call a function, or send a message to the main process
      });
    }
    
    const unitOpSimulationBtn = document.getElementById('unitOpSimulation');
    if (unitOpSimulationBtn) {
      unitOpSimulationBtn.addEventListener('click', () => {
        // Logic for Flowsheet Simulation
        console.log("Unit Op Simulation Button Clicked");
        // You might load new content, call a function, or send a message to the main process
      });
    }
    
    
    const equiptmentDesignBtn = document.getElementById('equiptmentDesign');
    if (equiptmentDesignBtn) {
      equiptmentDesignBtn.addEventListener('click', () => {
        // Logic for Flowsheet Simulation
        console.log("Process Synthesis Button Clicked");
        // You might load new content, call a function, or send a message to the main process
      });
    }
    const postProcessAnalysisBtn = document.getElementById('postProcessAnalysis');
    if (postProcessAnalysisBtn) {
      postProcessAnalysisBtn.addEventListener('click', () => {
        // Logic for Flowsheet Simulation
        console.log("Post Process Analysis Button Clicked");
        // You might load new content, call a function, or send a message to the main process
      });
    }
    const exportTechnicalReportBtn = document.getElementById('exportTechnicalDocument');
    if (exportTechnicalReportBtn) {
      exportTechnicalReportBtn.addEventListener('click', () => {
        // Logic for Flowsheet Simulation
        console.log("Export Technical Report Button Clicked");
        // You might load new content, call a function, or send a message to the main process
      });
    }
    const generalSettingsBtn = document.getElementById('generalSettings');
    if (generalSettingsBtn) {
      generalSettingsBtn.addEventListener('click', () => {
        // Logic for Flowsheet Simulation
        console.log("General Settings Button Clicked");
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
  