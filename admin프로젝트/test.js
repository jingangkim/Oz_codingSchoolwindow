function isis() {
    var button = document.getElementById("myButton");
  
    if (button.innerText === "Hello") {
      button.innerText = "World";
    } else {
      button.innerText = "Hello";
    }
  }