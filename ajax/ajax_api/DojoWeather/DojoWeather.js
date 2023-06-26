function removeCookies(element) {
    element.parentElement.parentElement.remove();
}

async function cityAlert(location) {
    
    const imperialURL = `http://api.openweathermap.org/data/2.5/weather?q=${location}&cnt=4&APPID=4311fdac3ff190c26fe7016c3cbf638b&units=imperial`;
    
    const metricURL = `http://api.openweathermap.org/data/2.5/weather?q=${location}&cnt=4&APPID=4311fdac3ff190c26fe7016c3cbf638b&units=metric`;
    
    const imperialResponse = await fetch(imperialURL);
       
    const imperialApiData = await imperialResponse.json();
    
    console.log(`\n\napiData:\n${JSON.stringify(imperialApiData["main"]["feels_like"])}\n\n`);
    
    const metricResponse = await fetch(metricURL);
       
    const metricApiData = await metricResponse.json();
    
    alert(`Current temp in ${location} is ${JSON.stringify(imperialApiData["main"]["feels_like"])} degrees F and ${JSON.stringify(metricApiData["main"]["feels_like"])} degrees C`);
    
}

function tempConversion() {

    if (document.querySelector("#dropdown").value === "F") {

        for (let i = 0; i < document.querySelectorAll(".hi").length; ++i) {

            document.querySelectorAll(".lo")[i].innerText = JSON.stringify(Math.round(parseInt(document.querySelectorAll(".lo")[i].innerText) * (9 / 5) + 32));
            document.querySelectorAll(".hi")[i].innerText = JSON.stringify(Math.round(parseInt(document.querySelectorAll(".hi")[i].innerText) * (9 / 5) + 32));

        }

    }

    else {

        for (let i = 0; i < document.querySelectorAll(".hi").length; ++i) {

            document.querySelectorAll(".lo")[i].innerText = JSON.stringify(Math.round((parseInt(document.querySelectorAll(".lo")[i].innerText) - 32) * (5 / 9)));
            document.querySelectorAll(".hi")[i].innerText = JSON.stringify(Math.round((parseInt(document.querySelectorAll(".hi")[i].innerText) - 32) * (5 / 9)));
        }
    }

}