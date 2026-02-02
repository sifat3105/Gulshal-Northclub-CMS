document.addEventListener("DOMContentLoaded", () => {
    const sidebarSearch = document.querySelector("#nav-sidebar input[type='search']");
    if (sidebarSearch && !sidebarSearch.placeholder) {
        sidebarSearch.placeholder = "Search section";
    }

    const pageLinks = document.querySelectorAll("#nav-sidebar-apps a");
    for (const link of pageLinks) {
        if (link.textContent.includes(":")) {
            link.classList.add("font-medium");
        }
    }
});
