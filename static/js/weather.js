const menuIcon = document.getElementById('menu-icon');
const checkBtn = document.getElementById('check-btn');

checkBtn.addEventListener('change', function() {
    if (this.checked) {
        menuIcon.src = "/static/imgs/close.svg";
    } else {
        menuIcon.src = "/static/imgs/menu.svg";
    }
});


const key = "0967acc753b95489a70ecccc162c64a8";
navigator.geolocation.getCurrentPosition((position) => {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    
    // OpenWeatherMap API 호출
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${key}&units=metric`;
    
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        const locationElement = document.getElementById('location');
        //const weatherElement = document.getElementById('weather');
        const temperatureElement = document.getElementById('temperature');
        
        locationElement.textContent = `${data.name}`;
        //weatherElement.textContent = `Weather: ${data.weather[0].description}`;
        temperatureElement.textContent = `${data.main.temp} °C`;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, (error) => {
    console.error('Error getting geolocation:', error);
  });