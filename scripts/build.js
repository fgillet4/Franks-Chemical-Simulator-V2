const builder = require('electron-builder');

// 'Platform' and 'Arch' are imported from electron-builder to specify the target platform and architecture.
const Platform = builder.Platform;
const Arch = builder.Arch;

async function buildApp() {
  try {
    // Configuration for the build process
    const config = {
      appId: 'com.frankschemicalsimulator.v2',
      productName: "Frank's Chemical Simulator V2",
      directories: {
        output: 'dist/packaged', // Output directory for the packaged app
        buildResources: 'assets' // Directory for resources like icons
      },
      files: [
        'src/**/*', // Include all files from the src directory
        'package.json', // Don't forget to include package.json!
        'node_modules/**/*', // Include all node_modules required for the app
      ],
      win: {
        target: 'nsis', // Windows installer
        icon: 'assets/icons/app-icon.ico', // Application icon for Windows
      },
      mac: {
        target: 'dmg', // macOS disk image
        icon: 'assets/icons/app-icon.icns', // Application icon for macOS
      },
      linux: {
        target: 'AppImage', // Linux AppImage
        icon: 'assets/icons/app-icon.png', // Application icon for Linux
      },
      // Any additional electron-builder configuration options go here...
    };

    // Building for all platforms and arches
    await builder.build({
      targets: Platform.MAC.createTarget().concat(
        Platform.WINDOWS.createTarget(),
        Platform.LINUX.createTarget()
      ),
      config,
    });

    console.log('Build complete!');
  } catch (error) {
    console.error('Error during build!', error);
  }
}

// Run the build function
buildApp();
