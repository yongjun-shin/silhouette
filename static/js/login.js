const menuIcon = document.getElementById('menu-icon');
const checkBtn = document.getElementById('check-btn');

checkBtn.addEventListener('change', function() {
    if (this.checked) {
        menuIcon.src = "/static/imgs/close.svg";
    } else {
        menuIcon.src = "/static/imgs/menu.svg";
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const joinForm = document.getElementById('loginForm');
    joinForm.addEventListener('submit', function(event) {
        event.preventDefault();

        // 필수 입력값 가져오기
        var email = document.getElementById('email').value;
        var password = document.getElementById('pw').value;

        // 필수 입력값이 비어있는 경우 경고 표시
        if (!email || !password) {
            alert('All fields must be filled.');
            event.preventDefault(); // 폼 제출 막기
        } else {
            this.submit();
        }
    });
});