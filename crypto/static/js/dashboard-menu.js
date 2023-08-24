function toggleSidebar() {
    sideBar.classList.toggle('disappear');
    menuBar2.classList.toggle('disappear');
    menuBar1.classList.toggle('rotate45');
    menuBar3.classList.toggle('rotateneg45');
    toggleMenu.classList.toggle('vertical-stack');
    toggleMenu.classList.toggle('center-stack');
}
const sideBar = document.querySelector('.dashboard-sidebar');
const menuBar1 = document.querySelector('.bar1');
const menuBar2 = document.querySelector('.bar2');
const menuBar3 = document.querySelector('.bar3');
const toggleMenu = document.querySelector('.toggle-menu');