document.addEventListener('DOMContentLoaded', init);
document.addEventListener('DOMContentLoaded', () => {
  const saveBtn = document.getElementById('saveUnitConfigButton');
  saveBtn.addEventListener('click', saveUnitConfig);
});
function init() {
  setupTooltips();
  setupSidebarButtons();
  console.log('The DOM is fully loaded');
}

function setupTooltips() {
  const globalTooltip = document.getElementById('globalTooltip');
  document.querySelectorAll('.sidebar .tooltip-trigger').forEach(button => {
    button.addEventListener('mouseover', showTooltip.bind(null, globalTooltip));
    button.addEventListener('mouseout', hideTooltip.bind(null, globalTooltip));
  });
}

function showTooltip(globalTooltip, event) {
  const button = event.currentTarget;
  const rect = button.getBoundingClientRect();
  const tooltipText = button.getAttribute('data-tooltip');
  globalTooltip.textContent = tooltipText;
  globalTooltip.style.top = `${rect.top + window.scrollY + 12}px`;
  globalTooltip.style.left = `${rect.right + 10}px`;
  globalTooltip.style.visibility = 'visible';
  globalTooltip.style.opacity = '1';
}

function hideTooltip(globalTooltip) {
  globalTooltip.style.visibility = 'hidden';
  globalTooltip.style.opacity = '0';
}

function setupSidebarButtons() {
  document.querySelectorAll('.sidebar button').forEach(button => {
    button.addEventListener('click', function() {
      toggleActiveClass(this);
      displayOverlay(this.id + 'Overlay');
    });
  });
}

function toggleActiveClass(clickedButton) {
  document.querySelectorAll('.sidebar button').forEach(btn => btn.classList.remove('active'));
  clickedButton.classList.add('active');
}

function displayOverlay(overlayId) {
  document.querySelectorAll('.overlay-panel').forEach(panel => panel.style.display = 'none');
  const overlay = document.getElementById(overlayId);
  if (overlay) {
    overlay.style.display = 'block';
    if (overlayId === 'massEnergyBalanceOverlay') {
      initializeFlowsheet();
      initializePalette();
    }
  } else {
    console.error(`Overlay with ID ${overlayId} not found.`);
  }
}

function initializeFlowsheet() {
  const flowsheetContainer = document.getElementById('flowsheetContainer');
  flowsheetContainer.innerHTML = ''; // Clear existing content

  jsPlumb.ready(function() {
    var instance = jsPlumb.getInstance({
      // default drag options
      DragOptions: { cursor: 'pointer', zIndex: 2000 },
      // the overlays to decorate each connection with
      ConnectionOverlays: [
        [ "Arrow", {
          location: 1,
          visible:true,
          width:11,
          length:11,
          id:"ARROW",
          events:{
            click:function() { alert("you clicked on the arrow overlay")}
          }
        } ],
        [ "Label", {
          location: 0.5,
          id: "label",
          cssClass: "aLabel",
          events:{
            tap:function() { alert("hey"); }
          }
        }]
      ],
      Container: "flowsheetContainer"
    });
    // Initialize your flowsheet with jsPlumb here
  });
}

function initializePalette() {
  const paletteContainer = document.getElementById('paletteContainer');
  paletteContainer.innerHTML = ''; // Clear existing content

  // Add draggable unit operations to the palette
  const unitOps = ['UnitOp1', 'UnitOp2', 'UnitOp3']; // Example unit operations
  unitOps.forEach(function(op) {
    var el = document.createElement('div');
    el.innerHTML = op;
    el.className = 'palette-item';
    paletteContainer.appendChild(el);
  });

  // Make the palette items draggable
  new Sortable(paletteContainer, {
    group: { name: 'palette', pull: 'clone', put: false },
    sort: false, // Sorting inside list is not allowed
    animation: 150
  });

  // Make the flowsheet a drop zone
  var flowsheet = document.getElementById('flowsheetContainer');
  new Sortable(flowsheet, {
    group: { name: 'flowsheet', pull: false, put: true },
    onAdd: function (evt) {
      var itemEl = evt.item; // the current dragged HTMLElement
      // TODO: You might need to transform the dropped item into a jsPlumb endpoint or similar
    }
  });
}
document.addEventListener('DOMContentLoaded', function() {
  const flowsheet = document.getElementById('flowsheetContainer');
  let isPanning = false;
  let startX, startY;

  flowsheet.addEventListener('mousedown', function(e) {
    isPanning = true;
    startX = e.clientX - flowsheet.offsetLeft;
    startY = e.clientY - flowsheet.offsetTop;
    flowsheet.style.cursor = 'grabbing';
  });

  flowsheet.addEventListener('mousemove', function(e) {
    if (!isPanning) return;
    const x = e.clientX - startX;
    const y = e.clientY - startY;
    flowsheet.scrollTo(x, y);
  });

  flowsheet.addEventListener('mouseup', function() {
    isPanning = false;
    flowsheet.style.cursor = 'grab';
  });

  flowsheet.addEventListener('mouseleave', function() {
    isPanning = false;
  });
});
function setupSidebarButtons() {
  document.querySelectorAll('.sidebar button').forEach(button => {
    button.addEventListener('click', function() {
      toggleActiveClass(this);
      displayOverlay(this.id + 'Overlay');
      // Initialize the correct palette and flowsheet based on the button clicked
      switch (this.id) {
        case 'massEnergyBalance':
          initializeFlowsheet('massEnergyFlowsheetContainer');
          initializePalette('massEnergyPaletteContainer');
          break;
        case 'bernoulliBalance':
          initializeFlowsheet('bernoulliFlowsheetContainer');
          initializePalette('bernoulliPaletteContainer');
          break;
        case 'processEconomics':
          initializeFlowsheet('economicsFlowsheetContainer');
          initializePalette('economicsPaletteContainer');
          break;
        case 'processSafety':
          initializeFlowsheet('safetyFlowsheetContainer');
          initializePalette('safetyPaletteContainer');
          break;
        case 'pipingInstrumentation':
          initializeFlowsheet('pipingFlowsheetContainer');
          initializePalette('pipingPaletteContainer');
          break;
        case 'processControl':
          initializeFlowsheet('processControlFlowsheetContainer');
          initializePalette('processControlPaletteContainer');
          break;

      }
    });
  });
}