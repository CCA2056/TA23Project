// Nav Link Pairs
const navLinkPairs = [
    {id: "logo", link: "/home"},
    {id: "main-nav-list-scenarios", link: "/scenario-role-play-list"},
    {id: "get-started-button", link: "/home"}
]

// Relocate to ref function
const relocateToHref = (id) => {
    for (let i = 0; i < navLinkPairs.length; i++) {
        if (id === navLinkPairs[i].id) window.location.href = navLinkPairs[i].link
    }
}