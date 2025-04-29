async function loadPage(page) {
    const res = await fetch(`/partials/${page}`);
    const html = await res.text();
    document.getElementById("app").innerHTML = html;
}

document.addEventListener("DOMContentLoaded", () => {
    loadPage("title");
});
