let hidden = true;
let button = document.getElementById("show");
let path = document.getElementsByClassName("path");

button.addEventListener('click', function() {
  if (hidden) {
    hidden = false;
    button.value = 'Cacher solution';
    for (element of path) {
      element.style.fill = "#78b9ec";
    }
  } else {
    hidden = true;
    button.value = 'Voir solution';
    for (element of path) {
      element.style.fill = "white";
    }
  }
});
