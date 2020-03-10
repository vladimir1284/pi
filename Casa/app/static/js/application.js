function ge(s) { return document.getElementById(s) }

function initPage() {
    resetIndicators()
    get_indicators_data()
    var intervalID = setInterval(get_indicators_data, 2000);
}


function resetIndicators() {
    for (let i = 0; i < indicators.length; i++) {
        indicators[i].drawTemplate()
    }
}
// Script to open and close sidebar
function w3_open() {
    ge("mySidebar").style.display = "block"
    ge("myOverlay").style.display = "block"
}

function w3_close() {
    ge("mySidebar").style.display = "none"
    ge("myOverlay").style.display = "none"
}

window.onresize = resetIndicators

function get_indicators_data() {
    fetch("/get_indicators_data", {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(room),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(function (response) {
        let contentType = response.headers.get("content-type");
        if (contentType && contentType.indexOf("application/json") !== -1) {
            return response.json().then(function (json) {
                for (let i = 0; i < json.data.length; i++) {
                    indicators_dict[json.data[i].indicator].updateValue(json.data[i].value) 
                }
            });
        } else {
            console.log("Oops, we haven't got JSON!");
        }
    });
}
