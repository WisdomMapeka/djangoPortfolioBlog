// alert('hellllo');

    let top_nav_menu = document.querySelector("#top-nav-menu-id");
    let menu_toogle_button = document.querySelector("#menu-toogle-button-id");

    let toggleSearchBar = function () {
       console.log("run");
       console.log(top_nav_menu.classList.contains("hide-menu"));

       if (top_nav_menu.classList.contains("hide-menu")) {
        top_nav_menu.classList.remove("hide-menu");
       } else {
        top_nav_menu.classList.add("hide-menu");
       }

    }

    toggleSearchBar();
    menu_toogle_button.addEventListener("click",toggleSearchBar);

    