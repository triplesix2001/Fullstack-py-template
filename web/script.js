
// Exposing func to python
eel.expose(my_javascript_function);
function my_javascript_function(a, b, c, d) {
  if (a < b) {
    console.log(c * d);
  }
}

document.getElementById('myButton').addEventListener('click', function() {
    eel.my_python_function(); // Replace "my_python_function" with your actual Eel function name
});
