document.addEventListener("DOMContentLoaded", () => {
    const html = document.documentElement;
    const icon = document.getElementById("theme-icon");

    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        html.classList.add("dark");
        icon.textContent = "☀️";
    }
});

function toggleDark() {
    const html = document.documentElement;
    const icon = document.getElementById("theme-icon");

    html.classList.toggle("dark");

    const isDark = html.classList.contains("dark");

    localStorage.setItem("theme", isDark ? "dark" : "light");

    icon.classList.add("rotate");

    setTimeout(() => {
        icon.textContent = isDark ? "☀️" : "🌙";
        icon.classList.remove("rotate");
    }, 300);
}
