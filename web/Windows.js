
// Exposing func to python
//eel.expose(my_javascript_function);
//function my_javascript_function(a, b, c, d) {
//  if (a < b) {
//    console.log(c * d);
//  }
//}

//document.getElementById('myButton').addEventListener('click', function() {
//    eel.my_python_function(); // Replace "my_python_function" with your actual Eel function name
//});

eel.expose(showMessage)
function showMessage(message) {
    var popup = document.getElementById('popup-div');
    var successClass = 'success';
    var errorClass = 'error';
    var messageText = '';
  
    // Remove existing classes
    popup.classList.remove(successClass, errorClass);
  
    // Determine the appropriate class and message text based on the message type
    if (message === 'success') {
      popup.classList.add(successClass);
      messageText = 'Operation successful!';
    } else if (message === 'error') {
      popup.classList.add(errorClass);
      messageText = 'An error occurred.';
    }
  
    // Delay displaying the message to ensure it appears after the infobox is shown
    setTimeout(function() {
      // Insert the message text into the popup
      popup.innerHTML = messageText;
  
      // Add the "active" class to display the popup
      popup.classList.add('active');
  
      // Remove the "active" class after 5 seconds
      setTimeout(function() {
        popup.classList.remove('active');
      }, 8000);
    }, 100); // Adjust the delay as needed
  }
  
  
  

// Data Collection Button
document.getElementById('data-collection-btn').addEventListener('click', function() {
    showMessage('success'); // Handle data collection button click
  });
  
  // Telemetry Button
  document.getElementById('telemetry-btn').addEventListener('click', function() {
    showMessage('error');
    eel.my_python_function(); // Handle telemetry button click
  });
  
  // Turn Off Sleep Button
  document.getElementById('turn-off-sleep-btn').addEventListener('click', async function() {
    try {
      const response = await eel.disable_sleep()();
      console.log("success: " + response);
      showMessage(response);
    } catch (error) {
      console.log("error: " + error);
      showMessage("error");
    }
  });
  

  
  // Disable Lid Sleep Button
  document.getElementById('disable-lid-sleep-btn').addEventListener('click', async function() {
    try {
      const response = await eel.disable_sleep_lid_close()();
      console.log("success: " + response);
      showMessage(response);
    } catch (error) {
      console.log("error: " + error);
      showMessage("error");
    }
  });
  
  // Disable Automatic Updates Button
  document.getElementById('disable-automatic-updates-btn').addEventListener('click', function() {
    // Handle disable automatic updates button click
  });
  
  // Disable Windows 11 Button
  document.getElementById('disable-win11-btn').addEventListener('click', function() {
    // Handle disable Windows 11 button click
  });
  
  // Crack Windows Button
  document.getElementById('crack-btn').addEventListener('click', function() {
    // Handle crack Windows button click
  });
  
  // Make Local Account Button
  document.getElementById('new-local-acc-btn').addEventListener('click', function() {
    // Handle make local account button click
  });
  
