function toggleTheme() {
  const isDark = document.body.classList.toggle('dark-mode');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
  updateThemeIcon();
}

function updateThemeIcon() {
  const isDark = document.body.classList.contains('dark-mode');
  document.querySelector('.icon-sun').style.display = isDark ? 'block' : 'none';
  document.querySelector('.icon-moon').style.display = isDark ? 'none' : 'block';
}

document.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('theme');
  if (saved === 'dark') {
    document.body.classList.add('dark-mode');
  }
  updateThemeIcon();
});


setTimeout(() => {
  document.querySelectorAll('.flash').forEach(el => el.remove());
}, 5000); // Auto-dismiss after 5 seconds