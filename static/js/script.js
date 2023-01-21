const navbarToggle = navbar.querySelector("#navbar-toggle");
const navbarMenu = document.querySelector("#navbar-menu");
const navbarLinksContainer = navbarMenu.querySelector(".navbar-links");
let isNavbarExpanded = navbarToggle.getAttribute("aria-expanded") === "true";

const toggleNavbarVisibility = () => {
  isNavbarExpanded = !isNavbarExpanded;
  navbarToggle.setAttribute("aria-expanded", isNavbarExpanded);
};

navbarToggle.addEventListener("click", toggleNavbarVisibility);

navbarLinksContainer.addEventListener("click", (e) => e.stopPropagation());
navbarMenu.addEventListener("click", toggleNavbarVisibility);

// const para = document.createElement('hr');
// const element = document.getElementById("show-side-bar");
// const element_form = element.getElementsByTagName('')
//
// element.appendChild[1](para);


function show_side_bar() {
  document.getElementById("show-side-bar").classList.toggle("show-form");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn') && !event.target.closest('#show-side-bar')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show-form')) {
        openDropdown.classList.remove('show-form');
      }
    }
  }
}

