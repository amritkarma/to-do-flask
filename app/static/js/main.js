document.addEventListener("DOMContentLoaded", () => {
  const hamburger = document.getElementById("hamburgerBtn");
const mobileMenu = document.getElementById("mobileMenu");
const iconMenu = hamburger?.querySelector('.icon-menu');
const iconClose = hamburger?.querySelector('.icon-close');

if (hamburger) {
  hamburger.addEventListener("click", () => {
    mobileMenu.classList.toggle("show");
    const isOpen = mobileMenu.classList.contains("show");
    iconMenu.style.display = isOpen ? 'none' : 'block';
    iconClose.style.display = isOpen ? 'block' : 'none';
  });
}

  // Toggle light/dark theme
  function toggleTheme() {
    const isDark = document.body.classList.toggle('dark-mode');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    updateThemeIcon();
  }

  // Update icon display based on current theme
  function updateThemeIcon() {
    const isDark = document.body.classList.contains('dark-mode');
    const sunIcon = document.querySelector('.icon-sun');
    const moonIcon = document.querySelector('.icon-moon');
    if (sunIcon && moonIcon) {
      sunIcon.style.display = isDark ? 'block' : 'none';
      moonIcon.style.display = isDark ? 'none' : 'block';
    }
  }

  // Load theme preference from localStorage
  const saved = localStorage.getItem('theme');
  if (saved === 'dark') {
    document.body.classList.add('dark-mode');
  }
  updateThemeIcon();

  // Bind theme toggle button
  const themeToggleBtn = document.querySelector('.toggle-theme');
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', toggleTheme);
  }

  // Auto-dismiss flash messages
  setTimeout(() => {
    document.querySelectorAll('.flash').forEach(el => el.remove());
  }, 5000);
});
