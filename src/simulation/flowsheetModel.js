// Defines a class to represent a component within a flowsheet
class Component {
    // Constructor initializes a new instance of the Component class
    constructor(id, type, parameters) {
      this.id = id; // Unique identifier for the component
      this.type = type; // Type of the component (e.g., 'pump', 'valve')
      this.parameters = parameters; // Object containing various parameters of the component
    }
  
    // Method to convert the component instance into a JSON object
    toJSON() {
      return {
        id: this.id, // Include the id in the JSON object
        type: this.type, // Include the type in the JSON object
        parameters: this.parameters // Include the parameters in the JSON object
      };
    }
  
    // Static method to create a new Component instance from a JSON object
    static fromJSON(json) {
      return new Component(json.id, json.type, json.parameters);
    }
  }
  
  // Defines a class to represent the entire flowsheet model
  class FlowsheetModel {
    // Constructor initializes a new instance of the FlowsheetModel class
    constructor(components = []) {
      this.components = components; // An array to store multiple Component instances
    }
  
    // Method to add a new Component instance to the flowsheet
    addComponent(component) {
      this.components.push(component); // Adds the component to the components array
    }
  
    // Method to remove a Component instance from the flowsheet based on its id
    removeComponent(componentId) {
      this.components = this.components.filter(c => c.id !== componentId); // Creates a new array without the component to remove
    }
  
    // Method to find a Component instance in the flowsheet by its id
    getComponentById(componentId) {
      return this.components.find(c => c.id === componentId); // Returns the found component or undefined
    }
  
    // Method to convert the flowsheet instance into a JSON object
    toJSON() {
      return {
        components: this.components.map(component => component.toJSON()) // Converts each component to JSON
      };
    }
  
    // Static method to create a new FlowsheetModel instance from a JSON object
    static fromJSON(json) {
      const components = json.components.map(Component.fromJSON); // Transforms each JSON object into a Component instance
      return new FlowsheetModel(components); // Creates a new FlowsheetModel instance with the array of Components
    }
  }
  
  // Example usage of the FlowsheetModel and Component classes
  const flowsheet = new FlowsheetModel(); // Creates a new FlowsheetModel instance with no components
  const pump = new Component('pump1', 'pump', { flowRate: 100, pressure: 10 }); // Creates a new Component instance representing a pump
  flowsheet.addComponent(pump); // Adds the pump component to the flowsheet
  
  // Serializes the flowsheet model to a JSON string
  const json = JSON.stringify(flowsheet.toJSON(), null, 2);
  console.log(json); // Logs the JSON string to the console
  
  // Parses the JSON string back into a FlowsheetModel instance
  const loadedFlowsheet = FlowsheetModel.fromJSON(JSON.parse(json));
  console.log(loadedFlowsheet); // Logs the re-created FlowsheetModel instance
  
  // Defines a class to represent a generic block in the flowsheet
  class Block {
    constructor(name) {
      this.name = name; // The name of the block
      this.inputs = []; // An array to store input streams
      this.outputs = []; // An array to store output streams
    }
  
    // Method to add an input stream to the block
    addInput(inputStream) {
      this.inputs.push(inputStream); // Adds the input stream to the inputs array
    }
  
    // Method to add an output stream to the block
    addOutput(outputStream) {
      this.outputs.push(outputStream); // Adds the output stream to the outputs array
    }
  }
  
  // Defines a class to represent a tank, extending from the Block class
  class Tank extends Block {
    constructor(name, position) {
      super(name); // Calls the constructor of the parent Block class
      this.position = position; // Position of the tank within the flowsheet
    }
  }
  
  // Defines a class to represent a centrifugal pump, extending from the Block class
  class CentrifugalPump extends Block {
    constructor(name, position) {
      super(name); // Calls the constructor of the parent Block class
      this.position = position; // Position of the pump within the flowsheet
    }
  }
  
  // ... more subclasses like HandValve, ReliefValve, etc.
  
  // Usage example of Tank and CentrifugalPump classes
  const tank = new Tank('Tank1', { x: 0, y: 0 }); // Creates a new Tank instance
  const pump = new CentrifugalPump('Pump1', { x: 1, y: 1 }); // Creates a new CentrifugalPump instance
  