
window.addEventListener("load", function() {
    getjson("http://127.0.0.1:5000/api/wlists")
    .then(jsonData => {
        add_all(jsonData);
    });
  });