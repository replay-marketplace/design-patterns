fetch('http://api.openweathermap.org/data/2.5/weather?q=CityName&appid=YourAPIKey')
.then(response => response.json())
.then(data => {
  document.getElementById('weather').innerHTML = `Temperature: ${data.main.temp}°C, Humidity: ${data.main.humidity}%`;
})