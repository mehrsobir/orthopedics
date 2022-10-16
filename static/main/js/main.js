const headerDivMenu = document.querySelector('.header__div-menu');
const openmenu = document.querySelector('.header__div-openmenu');

headerDivMenu.onclick = function(){
    headerDivMenu.classList.toggle("active")
    openmenu.classList.toggle("active")
}

const showImgImg = document.querySelectorAll(".show-img__img");
const showImgControl = document.querySelectorAll(".show-img__control");

showImgControl.forEach(function(item){
    item.addEventListener('click', function(){
        const imgs = item.getAttribute("data-control");
        const img = document.querySelector(imgs);

        showImgControl.forEach(function(item){
            item.classList.remove("active");
        });
        showImgImg.forEach(function(item){
            item.classList.remove("active")
        })

        img.classList.add("active");
        item.classList.add("active");
    });
});
