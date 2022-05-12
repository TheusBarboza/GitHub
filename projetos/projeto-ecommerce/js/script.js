$('.banner').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
  });

const btnMobile = document.getElementById('btnMobile');

function toggleMenu(){
  const nav = document.getElementById('nav');
  nav.classList.toggle('active');
}

btnMobile.addEventListener('click', toggleMenu);