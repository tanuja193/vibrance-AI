var inputvalue = document.querySelector('#cityinput');
var btn = document.querySelector('#add');
var city = document.querySelector('#cityoutput');
var descrip = document.querySelector('#description');
var temp = document.querySelector('#temp');
var wind = document.querySelector('#wind');
var apik = "0d17f079ed2c5d52507d1e6ab3536e9b";

function convertion(val) {
    return (val - 273.15).toFixed(2); // Correct conversion from Kelvin to Celsius
}

btn.addEventListener('click', function() {
    fetch('https://api.openweathermap.org/data/2.5/weather?q=' + inputvalue.value + '&appid=' + apik)
        .then(res => res.json())
        .then(data => {
            var nameval = data['name'];
            var descrip = data['weather'][0]['description']; // Corrected the index usage
            var tempature = data['main']['temp'];
            var wndspeed = data['wind']['speed'];

            city.innerHTML = `Weather of <span>${nameval}</span>`;
            temp.innerHTML = `Temperature: <span>${convertion(tempature)} °C</span>`;
            description.innerHTML = `Sky conditions: <span>${descrip}</span>`;
            wind.innerHTML = `Wind speed: <span>${wndspeed} km/h</span>`; // Corrected the variable name and closing tag
        })
        .catch(err => alert('You entered a wrong city name'));
});
