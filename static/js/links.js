// Nav Bar 
document.getElementById('logo').addEventListener('click', () => { relocateToHref('/home') })

// Landing page
if (window.location.pathname === "/") {
    document.getElementById('get-started-button').addEventListener('click', () => { relocateToHref('/home') })
}

// Relocate to ref function
const relocateToHref = href => window.location.href = href