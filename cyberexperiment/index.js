const menu =document.querySelector("#mobile_menu");
const navLinks = document.querySelector(".nav_menu");
const navLogo = document.querySelector("#navbar_logo");

//display mobile menu


const mobileMenu =()=>{
    menu.classList.toggle("is-active");
    navLinks.classList.toggle("active");
}
menu.addEventListener("click", mobileMenu);


//Animation

gsap.registerPlugin(ScrollTrigger);

gsap.from(".hero_animation", {
    duration:0.8 ,
    opacity:0,
    y:-150,
    stagger:0.3
});

gsap.from(".header_animation", {
    scrollTrigger:".header_animation",
    duration:2 ,
    opacity:0,
    y:-150,
    stagger:0.3,
    delay:0.5
});

gsap.from(".card_animation", {
    scrollTrigger: ".card_animation",
    duration:1,
    opacity:0,
    x:-150,
    stagger:0.1,
    delay:0.2
});
gsap.from(".card_animation2", {
    scrollTrigger: ".card_animation2",
    duration:1,
    opacity:0,
    x:-150,
    stagger:0.1,
    delay:0.2
});
gsap.from(".card_animation3", {
    scrollTrigger: ".card_animation3",
    duration:1.5,
    opacity:0,
    y:150,
    stagger:0.1,
    delay:0.2
});
gsap.from(".card_animation4", {
    scrollTrigger: ".card_animation4",
    duration:1,
    opacity:0,
    y:150,
    stagger:0.1,
    delay:0.2
});
gsap.from(".card_animation5", {
    scrollTrigger: ".card_animation5",
    duration:1,
    opacity:0,
    x:-150,
    stagger:0.1,
    delay:0.2
});
gsap.from(".card_animation6", {
    scrollTrigger: ".card_animation6",
    duration:1,
    opacity:0,
    x:-150,
    stagger:0.1,
    delay:0.2
});