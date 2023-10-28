
window.addEventListener("load", function() {
    console.log(window.location.href.split("/")[3]);
    getjson("http://127.0.0.1:5000/api/wisches/" + window.location.href.split("/")[4])
    .then(jsonData => {
        add_all(jsonData);
    });
  });