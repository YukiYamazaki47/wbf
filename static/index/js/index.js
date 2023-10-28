
function add_all(ids) {
    for (var i of ids) {
        console.log(i);
        getjson("http://127.0.0.1:5000/api/wisches/data/" + i)
        .then(jsonData => {
            console.log(jsonData);
            const jdals2 = document.createElement("span");
            const jdals1 = document.createElement("span");
            const jdal = document.createElement("li");
            const jda = document.createElement("a");
            const jd = document.createElement("div");
            jd.className="slisto"
            jdals2.innerHTML=jsonData.allcost;
            jdals2.className="slistiip2"
            jdals1.innerHTML=jsonData.name;
            jda.href="http://127.0.0.1:5000/wlist/" + jsonData.name;
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
