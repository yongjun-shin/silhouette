const menuIcon = document.getElementById('menu-icon');
const checkBtn = document.getElementById('check-btn');

checkBtn.addEventListener('change', function() {
    if (this.checked) {
        menuIcon.src = "/static/imgs/close_closet.svg";
    } else {
        menuIcon.src = "/static/imgs/menu_closet.svg";
    }
});

const modal = document.getElementById('modal');
const addBtn = document.getElementById('add');
const closeBtn = modal.querySelector('.modal_close');

addBtn.addEventListener('click', ()=> {
    modal.style.display = 'block';
});
closeBtn.addEventListener("click", e => {
    modal.style.display = "none"
});

const upload = document.getElementById('upload');
const file = document.getElementById('file');

file.addEventListener('change', function(event) {
    var input = file.value;
    upload.value = input;
});

document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('#del');

    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const itemId = this.dataset.itemId;

            fetch(`/closet/del_clothes/${itemId}/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': window.csrfToken,
                },
            })
            .then(response => {
                if (response.ok) {
                    location.reload();
                }
            });
        });
    });

    const P = document.querySelectorAll('#clothes_name');
    const modalImg = modalClothes.querySelector('.modal_img');
    P.forEach(function(p) {
        p.addEventListener('click', function() {
            const itemId = this.dataset.itemId;
            console.log(itemId);
            modalImg.style.backgroundImage = `url(${itemId})`;
            modalClothes.style.display = 'block';
        });
    });
});

const modalClothes = document.getElementById('modal_clothes');
const clothesName = document.getElementById('clothes_name');
const clothesBtn = modalClothes.querySelector('.modal_clothes_close');

clothesName.addEventListener('click', ()=> {
    modalClothes.style.display = 'block';
});
clothesBtn.addEventListener("click", e => {
    modalClothes.style.display = "none"
});