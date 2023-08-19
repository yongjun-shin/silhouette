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
    console.log(latitude);
    console.log(longitude);

    // OpenWeatherMap API 호출
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${key}&units=metric`;
    // 내 위치, key 반영한 경로 https://api.openweathermap.org/data/2.5/weather?lat=37.4084367&lon=127.1580072&appid=0967acc753b95489a70ecccc162c64a8&units=metric

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        const locationElement = document.getElementById('location');
        const temperatureElement = document.getElementById('temperature');
        const weatherIcon = document.getElementById('weather_icon');
        const icon_url = `https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`;
        const temper = Number(data.main.temp).toFixed(1);
        const clothes1 = document.getElementById('clothes_icon1');
        const clothes2 = document.getElementById('clothes_icon2');
        const recommend = document.getElementById('recommend');

        if (temper >= 28){ // 반팔, 원피스 o
          recommend.textContent = '오늘 Silhouette에서는 민소매, 반팔, 반바지, 원피스를 추천드립니다.';
            clothes1.src = "static/imgs/t_shirt.svg";
            clothes2.src = "static/imgs/onepiece.svg";
        } else if (temper >= 23) { // 반팔, 반바지 o
            recommend.textContent = '오늘 Silhouette에서는 반팔, 얇은 셔츠, 반바지, 면바지를 추천드립니다.';
            clothes1.src = "static/imgs/t_shirt.svg";
            clothes2.src = "static/imgs/shorts.svg";
        } else if (temper >= 20) { // 긴팔, 츄리닝 o
            recommend.textContent = '오늘 Silhouette에서는 얇은 가디건, 긴팔, 면바지, 청바지를 추천드립니다.';
            clothes1.src = "static/imgs/longsleeve.svg";
            clothes2.src = "static/imgs/training_pants.svg";
        } else if (temper >= 17) { // 후드티, 청바지 o
            recommend.textContent = '오늘 Silhouette에서는 얇은 니트, 맨투맨, 가디건, 청바지를 추천드립니다.';
            clothes1.src = "static/imgs/hoody.svg";
            clothes2.src = "static/imgs/denim_jeans.svg";  
        } else if (temper >= 12) { // 자켓, 츄리닝 o
            recommend.textContent = '오늘 Silhouette에서는 자켓, 가디건, 야상, 스타킹, 청바지, 면바지를 추천드립니다.';
            clothes1.src = "static/imgs/jacket.svg";
            clothes2.src = "static/imgs/training_pants.svg";
        } else if (temper >= 9) { // 트렌치 코트, 청바지 o
            recommend.textContent = '오늘 Silhouette에서는 자켓, 트렌치 코트, 야상, 니트, 스타킹, 청바지를 추천드립니다.';
            clothes1.src = "static/imgs/trench.svg";
            clothes2.src = "static/imgs/denim_pants.svg";
        } else if (temper >= 5) { // 코트, 니트 o
            recommend.textContent = '오늘 Silhouette에서는 코트, 가죽자켓, 히트텍, 니트, 레깅스를 추천드립니다.';
            clothes1.src = "static/imgs/coat.svg";
            clothes2.src = "static/imgs/knit.svg";
        } else if (temper < 4) { // 패딩, 목도리 o
            recommend.textContent = '오늘 Silhouette에서는 패딩, 두꺼운 코트, 목도리, 기모제품을 추천드립니다.';
            clothes1.src = "static/imgs/down_jacket.svg";
            clothes2.src = "static/imgs/scarf.svg";
        }

        locationElement.textContent = `${data.name}`;
        weatherIcon.src = icon_url;
        temperatureElement.textContent = `${temper} °C`;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, (error) => {
    console.error('Error getting geolocation:', error);
  });