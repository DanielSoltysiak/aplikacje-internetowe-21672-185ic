function startWorkerFib() {
    var wFib;
    var nFib = document.getElementById("nFib").value;
    if(typeof(Worker) !== "undefined") {
        wFib = new Worker("fibonacci.js");
        wFib.postMessage(nFib);
        wFib.onmessage = function(event) {
            document.getElementById("resultFib").innerHTML = event.data;
        };
    } 
}

function startWorkerFac() {
    var wFac;
    var nFac = document.getElementById("nFac").value;
    if (typeof(Worker) !== "undefined") {
        wFac = new Worker("factorial.js");
        wFac.postMessage(nFac);
        wFac.onmessage = function(event) {
            document.getElementById("resultFac").innerHTML = event.data;
        };
    } 
}