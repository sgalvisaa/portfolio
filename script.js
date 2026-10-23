// Project filter: show cards whose data-tags include the selected filter.
const chips = document.querySelectorAll('.chip');
const cards = document.querySelectorAll('#project-grid .card');

chips.forEach((chip) => {
  chip.addEventListener('click', () => {
    const filter = chip.dataset.filter;
    chips.forEach((c) => {
      const on = c === chip;
      c.classList.toggle('active', on);
      c.setAttribute('aria-pressed', String(on));
    });
    cards.forEach((card) => {
      const tags = card.dataset.tags.split(' ');
      card.hidden = !(filter === 'all' || tags.includes(filter));
    });
  });
});

// Email buttons: still open the mail app, and also copy the address so the
// click does something for visitors without a default mail app.
document.querySelectorAll('.email-link').forEach((link) => {
  const original = link.textContent;
  const address = link.getAttribute('href').replace('mailto:', '');
  link.addEventListener('click', () => {
    if (!navigator.clipboard) return;
    navigator.clipboard.writeText(address).then(() => {
      link.textContent = `Copied: ${address}`;
      setTimeout(() => { link.textContent = original; }, 2500);
    });
  });
});
