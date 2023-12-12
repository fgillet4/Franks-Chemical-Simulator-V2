const { app, BrowserWindow, screen } = require('electron');

function createWindow() {
  // Get the primary display's dimensions.
  const primaryDisplay = screen.getPrimaryDisplay();
  const { width, height } = primaryDisplay.workAreaSize;


  // Create the browser window with a dynamic size.
  let win = new BrowserWindow({
    width: width * 0.8, // 80% of the screen width
    height: height * 0.8, // 80% of the screen height
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false, // for Electron 12 or later, you might need to set this to false to use nodeIntegration
    }
  });

  // Load the index.html of the app.
  win.loadFile('src/renderer/index.html');

  // Open the DevTools.
  win.webContents.openDevTools();
}

app.whenReady().then(createWindow);

// Quit when all windows are closed, except on macOS.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
