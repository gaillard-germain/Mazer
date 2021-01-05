function showPath() {
  var button = document.getElementById("show")
  var path = document.getElementsByClassName("path");

  if (button.innerHTML === 'Cacher solution') {
    button.innerHTML = 'Voir solution';
    for (element of path) {
      element.style.fill = "white";
    }
  } else {
    button.innerHTML = 'Cacher solution';
    for (element of path) {
      element.style.fill = "#78b9ec";
    }
  }
}
