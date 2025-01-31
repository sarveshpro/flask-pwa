(function () {
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", () => {
      navigator.serviceWorker
        .register("/sw.js")
        .then(function (registration) {
          console.log("Service Worker Registered");
          return registration;
        })
        .catch(function (err) {
          console.error("Unable to register service worker.", err);
        });
      navigator.serviceWorker.ready.then(function (registration) {
        console.log("Service Worker Ready");
      });
    });
  }
})();

let deferredPrompt;
const btnAdd = document.querySelector("#btnAdd");

window.addEventListener("beforeinstallprompt", (e) => {
  console.log("beforeinstallprompt event fired");
  e.preventDefault();
  deferredPrompt = e;
  btnAdd.style.visibility = "visible";
});

btnAdd.addEventListener("click", (e) => {
  btnAdd.style.visibility = "hidden";
  deferredPrompt.prompt();
  deferredPrompt.userChoice.then((choiceResult) => {
    if (choiceResult.outcome === "accepted") {
      console.log("User accepted the A2HS prompt");
    } else {
      console.log("User dismissed the A2HS prompt");
    }
    deferredPrompt = null;
  });
});

window.addEventListener("appinstalled", (evt) => {
  app.logEvent("app", "installed");
});

// move forward
function moveForward() {
  var apiUrl = "/forward";
  fetch(apiUrl)
    .then((response) => {
      return response.text();
    })
    .then((data) => {
      // Work with JSON data here
      console.log(data);
      let botStatus = document.getElementById("botStatus");
      botStatus.innerHTML = data;
    })
    .catch((err) => {
      // Do something for an error here
      console.error("Error", err);
    });
}

// move backward
function moveBackward() {
  var apiUrl = "/backward";
  fetch(apiUrl)
    .then((response) => {
      return response.text();
    })
    .then((data) => {
      // Work with JSON data here
      console.log(data);
      let botStatus = document.getElementById("botStatus");
      botStatus.innerHTML = data;
    })
    .catch((err) => {
      // Do something for an error here
      console.error("Error", err);
    });
}

// stop moving
function moveStop() {
  var apiUrl = "/stop";
  fetch(apiUrl)
    .then((response) => {
      return response.text();
    })
    .then((data) => {
      // Work with JSON data here
      console.log(data);
      let botStatus = document.getElementById("botStatus");
      botStatus.innerHTML = data;
    })
    .catch((err) => {
      // Do something for an error here
      console.error("Error", err);
    });
}

// turn Left
function moveLeft() {
  var apiUrl = "/left";
  fetch(apiUrl)
    .then((response) => {
      return response.text();
    })
    .then((data) => {
      // Work with JSON data here
      console.log(data);
      let botStatus = document.getElementById("botStatus");
      botStatus.innerHTML = data;
    })
    .catch((err) => {
      // Do something for an error here
      console.error("Error", err);
    });
}

//turn Right
function moveRight() {
  var apiUrl = "/right";
  fetch(apiUrl)
    .then((response) => {
      return response.text();
    })
    .then((data) => {
      // Work with JSON data here
      console.log(data);
      let botStatus = document.getElementById("botStatus");
      botStatus.innerHTML = data;
    })
    .catch((err) => {
      // Do something for an error here
      console.error("Error", err);
    });
}

// start stream
function startStream() {
  let streamStatus = document.getElementById("streamStatus");
  streamStatus.innerHTML = "Streaming";
  var imageComponent = document.getElementById("stream");
  var placeHolder = document.getElementById("livePlaceholder");
  imageComponent.style.display = "block";
  placeHolder.style.display = "none";
}

// stop stream
function stopStream() {
  let streamStatus = document.getElementById("streamStatus");
  streamStatus.innerHTML = "Stopped";
  var imageComponent = document.getElementById("stream");
  var placeHolder = document.getElementById("livePlaceholder");
  imageComponent.style.display = "none";
  placeHolder.style.display = "block";
}
