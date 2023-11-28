const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const dbPath = path.resolve(__dirname, 'chemicals.db');

// Initialize a new database object to store chemical data
const db = new sqlite3.Database(dbPath, sqlite3.OPEN_READWRITE | sqlite3.OPEN_CREATE, (err) => {
  if (err) {
    console.error(err.message);
  } else {
    console.log('Connected to the local SQLite database.');
    initializeDatabase(); // Create tables if they don't exist
  }
});

// Function to initialize the database with the required tables
function initializeDatabase() {
  db.run(`CREATE TABLE IF NOT EXISTS chemicals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    formula TEXT NOT NULL,
    properties TEXT,  // JSON string to store various properties
    graphData TEXT    // JSON string to store data for graphing
  )`, (err) => {
    if (err) {
      console.error('Error creating table', err.message);
    } else {
      console.log('Table "chemicals" ensured.');
    }
  });
}

// Function to insert a new chemical into the database
function insertChemical(name, formula, properties, graphData) {
  const propertiesStr = JSON.stringify(properties);
  const graphDataStr = JSON.stringify(graphData);

  db.run(`INSERT INTO chemicals (name, formula, properties, graphData) VALUES (?, ?, ?, ?)`, 
    [name, formula, propertiesStr, graphDataStr], 
    function(err) {
      if (err) {
        console.error('Error inserting chemical', err.message);
      } else {
        console.log(`A row has been inserted with rowid ${this.lastID}`);
      }
  });
}

// Function to retrieve chemical data by name
function getChemicalByName(name, callback) {
  db.get(`SELECT * FROM chemicals WHERE name = ?`, [name], (err, row) => {
    if (err) {
      callback(err, null);
    } else {
      callback(null, row);
    }
  });
}

// Function to regress data from the database for a given chemical
// This function would likely call another module to perform the regression analysis
function regressChemicalData(chemicalName, callback) {
  // Placeholder: Fetch the data and perform regression analysis
  console.log(`Performing regression analysis on data for chemical: ${chemicalName}`);
  // ... regression logic here
}

// Function to generate graph data points for a given chemical
// This would involve returning the data in a format that can be consumed by a graphing library
function getGraphDataForChemical(chemicalName, callback) {
  // Placeholder: Fetch the graph data and format it for the frontend
  console.log(`Fetching graph data for chemical: ${chemicalName}`);
  // ... fetch and format graph data logic here
}

// Example usage:
// insertChemical('Methane', 'CH4', { molecularWeight: 16.04 }, [{ temp: 100, cp: 54 }]);
// getChemicalByName('Methane', (err, chemical) => {
//   if (err) {
//     console.error(err);
//   } else {
//     console.log(chemical);
//   }
// });

// Export functions for use in other modules
module.exports = {
  insertChemical,
  getChemicalByName,
  regressChemicalData,
  getGraphDataForChemical
};

