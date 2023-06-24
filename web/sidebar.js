// Get references to the buttons
const windowsButton = document.getElementById('WindowsButton');
const softwareButton = document.getElementById('SoftwareButton');
const networkButton = document.getElementById('NetworkButton');
const extraButton = document.getElementById('ExtraButton');

// Function to set active class on button
function setActiveButton(button) {
  // Remove active class from all buttons
  const sidebarButtons = document.getElementsByClassName('SidebarButton');
  for (let i = 0; i < sidebarButtons.length; i++) {
    sidebarButtons[i].classList.remove('active');
  }

  // Add active class to the specified button
  button.classList.add('active');

  // Store the active button ID in local storage
  localStorage.setItem('activeButton', button.id);
}

// Event listeners for button clicks
windowsButton.addEventListener('click', function() {
  setActiveButton(windowsButton);
  console.log("test");
  window.location.href = '/Windows/WindowsStuff.html';
  // Perform actions for the Windows button click
});

softwareButton.addEventListener('click', function() {
  setActiveButton(softwareButton);
  window.location.href = '/Software/software.html';
  // Perform actions for the Software button click
});

networkButton.addEventListener('click', function() {
  setActiveButton(networkButton);
  // Perform actions for the Network button click
});

extraButton.addEventListener('click', function() {
  setActiveButton(extraButton);
  // Perform actions for the Extra button click
});

// Retrieve the active button ID from local storage when the page loads
document.addEventListener('DOMContentLoaded', function() {
  const activeButtonId = localStorage.getItem('activeButton');
  if (activeButtonId) {
    const activeButton = document.getElementById(activeButtonId);
    setActiveButton(activeButton);
  }
});
