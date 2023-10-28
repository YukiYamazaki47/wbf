
function add_all(ids) {
    for (var i of ids) {
        console.log(i);
        getjson("http://127.0.0.1:5000/api/wisch/" + i)
        .then(jsonData => {
            console.log(jsonData);
            console.log(i);
            var jdals2 = document.createElement("span");
            var jdals1 = document.createElement("span");
            var jdal = document.createElement("li");
            var jda = document.createElement("a");
            var jd = document.createElement("div");
            jd.className="slisto"
            jdals2.innerHTML=jsonData.price;
            jdals2.className="slistiip2"
            jdals1.innerHTML=jsonData.name;
            jda.href="http://127.0.0.1:5000/wisch/" + jsonData.id;
            //jda.target="_blank"
            jda.className = "slisti"
            jdal.className = "slistiip1" 
            jd.appendChild(jda);
            jda.appendChild(jdal);
            jdal.appendChild(jdals1);
            jdal.appendChild(jdals2);
            document.getElementById("slist").appendChild(jd);
        });
    }
}
